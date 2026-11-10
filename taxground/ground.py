"""Constrained grounding: de-duplicate candidates, choose parent / definitions / reports from closed sets,
apply SME decisions read back from the release store, and resolve siblings."""
import json
import subprocess

import numpy as np

from . import text as T

DEFAULT_SETTINGS = {
    "units": "report",             # report (one vector per report) | chunks (section-aware: summary, findings, ~1,100-char narrative pieces)
    "lexical": "fts",              # fts (PostgreSQL full text, trial) | bm25 (Okapi BM25, k1=1.2 b=0.75)
    "retrieval": "linear",         # linear (trial blend) | rrf (RRF fusion + coverage/phrase rerank, RAG deck s.8)
    "context_header": False,
    "merged_cap_scale": False,      # a merged bucket may hold max_reports per absorbed twin
    "cutoff_scope": "source",      # global (trial) | source: relative cut-off within each report source
    "normalise": False,            # expand shorthand / strip boilerplate for retrieval (raw text is still what is quoted)
    "escalate": True,              # run the bounded agent on blocked buckets        # prepend phase + source codes to every embedded piece (both decks)
    "vector_weight": 0.6,          # hybrid = 0.6 * cosine + 0.4 * keyword rank (normalised within the query)
    "pool_size": 10,               # unfiltered reports that vote on the parent
    "relative_cutoff": 0.4,        # keep items scoring >= 40% of the best ...
    "min_score": 0.15,             # ... and never below this floor
    "parent_def_weight": 0.3,      # parent score = 0.3 * definition fit + 0.7 * report vote
    "parent_margin": 0.10,         # G7
    "max_definitions": 3,
    "max_reports": 12,
    "support_depth": 5,            # support is chosen from the top max_reports x depth relevant reports under the parent
    "support_refill": True,        # fill the max_reports slots after event de-duplication and sibling ownership
    "min_support": 3,              # G5 (trial value; production 10, DG-4)
    "min_parent_agreement": 0.6,   # G6
    "merge_threshold": 0.55,       # candidate de-duplication across batches
    "agent_max_calls": 5,          # escalation budget (GR-11)
    "agent_pool": 30,
    "agent_relative": 0.3,         # agent may recover reports scoring >= 30% of the bucket's best support (cut-off is 40%)
    "test_fit_margin": 0.05,       # report testing: margin between best and runner-up bucket
    "test_min_score": 0.25,
}


def relevant(items, S, key="score"):
    """Relative cut-off. With cutoff_scope='source' the cut-off is taken within each report source, because scores
    from long hand-written narratives and short template or shorthand records are not comparable (Embedding deck:
    route by record type). Definitions have no source and always use one global cut-off."""
    if not items:
        return []
    if S.get("cutoff_scope") == "source" and all("source_id" in i for i in items):
        tops = {}
        for i in items:
            tops[i["source_id"]] = max(tops.get(i["source_id"], 0.0), i[key])
        return [i for i in items if i[key] >= max(S["min_score"], S["relative_cutoff"] * tops[i["source_id"]])]
    top = max(i[key] for i in items)
    cut = max(S["min_score"], S["relative_cutoff"] * top)
    return [i for i in items if i[key] >= cut]


def unit(v):
    v = np.asarray(v, dtype=np.float32)
    return v / (np.linalg.norm(v) + 1e-12)


# ------------------------------------------------------------------ 1. de-duplicate candidates across batches
def dedupe(store, cands, S, sme):
    """Merge near-identical candidates from different discovery batches before grounding (document §10, finding 4).
    A pair merges when each is the other's best cross-batch match and their similarity clears the threshold;
    SME 'merge' forces a pair, 'keep_separate' forbids it. Returns {absorbed_id: canonical_id} and the scores."""
    w = S["vector_weight"]
    pools = {}
    for c in cands:
        hits = relevant(store.reports_hybrid(c["embedding"], f"{c['name']}. {c['definition']}", w, limit=S["pool_size"]), S)
        pools[c["candidate_id"]] = {h["report_key"] for h in hits}
    sim = {}
    for i, a in enumerate(cands):
        for b in cands[i + 1:]:
            if a["batch"] == b["batch"]:
                continue
            cos = float(np.dot(unit(a["embedding"]), unit(b["embedding"])))
            pa, pb = pools[a["candidate_id"]], pools[b["candidate_id"]]
            jac = len(pa & pb) / len(pa | pb) if pa | pb else 0.0
            sim[(a["candidate_id"], b["candidate_id"])] = sim[(b["candidate_id"], a["candidate_id"])] = round(0.5 * cos + 0.5 * jac, 4)
    forced = {(d["candidate_id"], d["target_id"]) for d in sme if d["action"] == "merge"}
    blocked = {frozenset((d["candidate_id"], d["target_id"])) for d in sme if d["action"] == "keep_separate"}
    best = {}
    for (x, y), s in sim.items():
        if frozenset((x, y)) in blocked:
            continue
        if x not in best or (s, y) > (best[x][1], best[x][0]):
            best[x] = (y, s)
    merges = {}
    pairs = set()
    for x, (y, s) in best.items():
        if best.get(y, (None,))[0] == x and s >= S["merge_threshold"]:
            pairs.add(tuple(sorted((x, y))))
    for x, y in forced:
        pairs.add(tuple(sorted((x, y))))
    for a, b in sorted(pairs):
        canon, absorbed = a, b                       # lexicographic: deterministic canonical id
        if absorbed in merges or canon in merges:
            continue
        merges[absorbed] = canon
    return merges, {f"{x}|{y}": s for (x, y), s in sim.items() if x < y and s >= S["merge_threshold"] - 0.1}


# ------------------------------------------------------------------ 2. constrained selection (rules selector)
def ground_candidate(store, cand, S, sme=(), mode="hybrid", aliases=()):
    """Same output shape as the LLM JSON, plus diagnostics. Applies SME decisions:
    reject_link -> removed from the closed set; add_link -> forced in (still verified); set_parent -> forced parent."""
    cid = cand["candidate_id"]
    texts = [f"{cand['name']}. {cand['definition']}"] + [f"{a['name']}. {a['definition']}" for a in aliases]
    vec = unit(np.mean([cand["embedding"]] + [a["embedding"] for a in aliases], axis=0))
    text = " ".join(texts)
    w = S["vector_weight"]
    rej_r = {d["target_id"] for d in sme if d["action"] == "reject_link" and d["target_type"] == "report"}
    rej_d = {d["target_id"] for d in sme if d["action"] == "reject_link" and d["target_type"] == "definition"}
    add_r = [d for d in sme if d["action"] == "add_link" and d["target_type"] == "report"]
    add_d = [d["target_id"] for d in sme if d["action"] == "add_link" and d["target_type"] == "definition"]
    set_p = [d["target_id"] for d in sme if d["action"] == "set_parent"]

    fits = store.parent_fit(vec)
    codes = [f[0] for f in fits]
    fit_n = {f[0]: max(0.0, float(f[3])) for f in fits}
    # the parent vote uses the full evidence pool: an SME rejecting a support link does not remove the report's codes
    pool_all = store.reports_hybrid(vec, text, w, limit=S["pool_size"])
    pool = relevant(pool_all, S)
    tot = sum(p["score"] for p in pool) or 1.0
    vote = {k: sum(p["score"] for p in pool if k in p["l1_codes"]) / tot for k in codes}
    wd = S["parent_def_weight"]
    score = fit_n if mode == "definition_only" else vote if mode == "vote_only" else \
        {k: wd * fit_n[k] + (1 - wd) * vote[k] for k in codes}
    ranked = sorted(codes, key=lambda k: (-round(score[k], 9), k))
    parent, runner = ranked[0], ranked[1]
    if set_p:
        parent = set_p[-1]
        runner = next(k for k in ranked if k != parent)

    defs = relevant(store.definitions_for(vec, text, w, parent=parent, exclude=rej_d), S)[:S["max_definitions"]]
    def_ids = [d["def_id"] for d in defs]
    for d in add_d:
        if d not in def_ids:
            def_ids.append(d)

    support = []
    cap = S["max_reports"] * (1 + (len(aliases) if S["merged_cap_scale"] else 0))   # merged bucket may carry both batches
    refill = S.get("support_refill", False)
    depth = S.get("support_depth", 2) if refill else 2
    ranked_sup = relevant(store.reports_hybrid(vec, text, w, parent=parent, limit=cap * depth, exclude=rej_r,
                                               support_only=True), S)
    # every relevant report under the parent, in score order: the list support is filled from (here and after siblings)
    reserve = [dict(report_key=r["report_key"], score=round(r["score"], 4), event_id=r["event_id"], chunk=r.get("chunk"))
               for r in ranked_sup]
    taken_ev = set()
    for r in reserve:
        if len(support) >= cap:
            break
        if refill and r["event_id"] in taken_ev:      # fill slots with distinct events, not records
            continue
        taken_ev.add(r["event_id"])
        sent, _ = store.best_sentence(vec, r["report_key"], text)
        support.append(dict(r, evidence=sent))
    for d in add_r:
        if d["target_id"] not in {s["report_key"] for s in support}:
            sent = d.get("value") or store.best_sentence(vec, d["target_id"], text)[0]
            support.append(dict(report_key=d["target_id"], evidence=sent, score=1.0, event_id=d["target_id"], sme=d["decision_id"]))
    # one event = one piece of support (multi-aircraft records are not independent corroboration)
    seen_ev, dedup = set(), []
    for s in support:
        if s["event_id"] in seen_ev:
            continue
        seen_ev.add(s["event_id"])
        dedup.append(s)
    support = dedup

    # context for criteria cards: definitions under other parents that match the candidate
    other_defs = [d for d in store.definitions_for(vec, text, w, limit=8) if parent not in d["parents"]]
    out = dict(candidate_id=cid, parent_code=parent, definition_ids=def_ids,
               supporting_reports=[dict(report_key=s["report_key"], evidence=s["evidence"]) for s in support], concerns="",
               max_reports=cap)
    diag = dict(candidate=cand["name"], proposed_parent=cand.get("proposed_parent"),
                co_codes=[k for k in ranked[1:] if vote[k] >= S["min_parent_agreement"]],
                parent_scores={k: round(score[k], 4) for k in ranked[:4]}, runner_up=runner,
                margin=round(score[parent] - score[runner], 4), parent_agreement=round(vote.get(parent, 0.0), 4),
                parent_forced_by_sme=bool(set_p), definitions=[dict(d, cos=round(d["cos"], 4), score=round(d["score"], 4)) for d in defs],
                support=support, other_definitions=[dict(def_id=d["def_id"], term=d["term"], parents=d["parents"], score=round(d["score"], 4))
                                                    for d in relevant(other_defs, S)[:3]],
                pool=[dict(report_key=p["report_key"], l1=p["l1_codes"], score=round(p["score"], 4), chunk=p.get("chunk")) for p in pool_all],
                pool_best=round(max([p["score"] for p in pool_all], default=0.0), 4),
                sme_applied=[d["decision_id"] for d in sme if d["action"] in ("reject_link", "add_link", "set_parent")],
                relevant_under_parent=len({r["event_id"] for r in reserve}), reserve=reserve,
                query_vec=vec, query_text=text)
    return out, diag


def resolve_siblings(grounded, store=None, S=None):
    """A report supports only the sibling (same parent) it matches best; the move is recorded (GR-6).
    SME-added links are never moved. With support_refill, ownership is decided over each bucket's whole relevant
    list, and each bucket then fills its slots, in score order, with distinct events it owns; the evidence standard
    (relative cut-off, parent filter, verified quote) is unchanged, only the slots no longer go empty."""
    refill = bool(store is not None and S and S.get("support_refill"))
    best = {}
    for out, diag in grounded:
        items = list(diag["support"]) + (diag.get("reserve", []) if refill else [])
        for s in items:
            k = (out["parent_code"], s["report_key"])
            sc = 9.0 if s.get("sme") else s["score"]
            if k not in best or sc > best[k][1] or (sc == best[k][1] and out["candidate_id"] < best[k][0]):
                best[k] = (out["candidate_id"], sc)
    for out, diag in grounded:
        cid, par = out["candidate_id"], out["parent_code"]
        if not refill:
            keep, moved = [], []
            for s in diag["support"]:
                if best[(par, s["report_key"])][0] == cid:
                    keep.append(s)
                else:
                    moved.append(dict(report_key=s["report_key"], to=best[(par, s["report_key"])][0], evidence=s["evidence"]))
        else:
            cap = out.get("max_reports", S["max_reports"])
            have = {s["report_key"]: s for s in diag["support"]}
            keep = [s for s in diag["support"] if s.get("sme")]
            seen = {s["event_id"] for s in keep}
            moved, n = [], 0
            for r in diag.get("reserve", []):
                if n >= cap:
                    break
                owner = best[(par, r["report_key"])][0]
                if owner != cid:
                    if r["report_key"] in have:
                        moved.append(dict(report_key=r["report_key"], to=owner, evidence=have[r["report_key"]]["evidence"]))
                    continue
                if r["event_id"] in seen:
                    continue
                seen.add(r["event_id"])
                s = have.get(r["report_key"])
                if s is None:
                    sent, _ = store.best_sentence(diag["query_vec"], r["report_key"], diag["query_text"])
                    s = dict(r, evidence=sent)
                keep.append(s); n += 1
        diag["support"] = keep
        diag["moved_to_sibling"] = moved
        out["supporting_reports"] = [dict(report_key=s["report_key"], evidence=s["evidence"]) for s in keep]
    return grounded


# ------------------------------------------------------------------ 3. LLM selector (constrained prompt)
def build_prompt(template, store, cand, diag, S, k_reports=10):
    vec, text = diag["query_vec"], diag["query_text"]
    parents = store.parent_fit(vec)
    pool = store.reports_hybrid(vec, text, S["vector_weight"], limit=k_reports, support_only=True)
    # edges-first packing ("lost in the middle"): strongest evidence at the start and the end of the list
    pool = [pool[i] for i in range(0, len(pool), 2)] + [pool[i] for i in range(len(pool) - 1 - (len(pool) % 2 == 1), 0, -2)]
    defs = store.q("SELECT def_id, term, body, parents FROM industry_definition ORDER BY embedding <=> %s, def_id LIMIT 8", (vec,))
    fill = {
        "CANDIDATE_ID": cand["candidate_id"], "CANDIDATE_NAME": cand["name"], "CANDIDATE_DEFINITION": cand["definition"],
        "PROPOSED_PARENT": cand.get("proposed_parent") or "none",
        "PARENT_LIST": "\n".join(f"- {p[0]} ({p[1]}): {p[2]}" for p in parents),
        "DEFINITION_LIST": "\n".join(f"- {d[0]} [{', '.join(d[3])}] {d[1]}: {d[2]}" for d in defs),
        "REPORT_LIST": "\n".join(f"- {r['report_key']} [{', '.join(r['l1_codes'])}]: {r['narrative']}" for r in pool),
    }
    for k, v in fill.items():
        template = template.replace("{" + k + "}", v)
    return template


def call_llm_cmd(cmd, prompt):
    """Any approved model behind a command: prompt on stdin, JSON on stdout (DG-3, model registry)."""
    res = subprocess.run(cmd, shell=True, input=prompt, text=True, capture_output=True, timeout=900, check=True)
    txt = res.stdout
    return json.loads(txt[txt.find("{"): txt.rfind("}") + 1])

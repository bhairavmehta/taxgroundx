"""The unified grounding pipeline: one bounded, re-runnable run from recorded inputs to a versioned taxonomy draft.

  0 snapshot + validate inputs      (NFR-REP-01, NFR-QAL-01)
  1 route + normalise records       (raw text kept for quotes)
  2 index in pgvector               (hybrid vector + keyword)
  3 read SME decisions back         (release store, SRS-TAX-04)
  4 de-duplicate candidates         (merge cross-batch twins before grounding)
  5 ground from closed sets         (rules selector or constrained LLM; sibling rule)
  6 build criteria cards            (SRS-TAX-03)
  7 verify G1–G10                   (same checks for every selector)
  8 escalate blocked candidates     (bounded agent, <= 5 calls, cannot publish)
  9 decide outcome                  (release candidate | SME review | returned | abstained | merged)
 10 store run record                (SSSOM-style links, cards, checks, agent calls)
 11 versioned hierarchy + changelog (revisions attributed to SME input, a report, data, settings or code)
"""
import csv
import datetime as dt
import hashlib
import json
import shutil
from pathlib import Path

import numpy as np

from . import agent as A
from . import criteria as CR
from . import ground as G
from . import text as T
from .embed import LocalEmbedder, SentenceTransformerEmbedder
from .store import Store, jdump
from .verify import verify

PKG = Path(__file__).resolve().parent
ROOT = PKG.parent
SCHEMA_VERSION = "2.0"
PROMPT_FILE = ROOT / "prompts" / "constrained_grounding.md"
PREDICATE = {"parent": "skos:broadMatch", "definition": "skos:relatedMatch", "report": "sssom:hasSupportingEvidence"}


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()


def code_version():
    h = hashlib.sha256()
    for f in sorted(PKG.glob("*.py")) + [ROOT / "db" / "schema.sql", PROMPT_FILE]:
        h.update(f.read_bytes())
    return "tg-" + h.hexdigest()[:10]


def prompt_version():
    return "constrained_grounding@" + sha(PROMPT_FILE.read_bytes())[:8]


def load_inputs(data_dir):
    data_dir = Path(data_dir)
    files = {n: data_dir / f"{n}.json" for n in ("icao_categories", "industry_definitions", "sample_reports", "candidates")}
    raw = {n: json.loads(f.read_text(encoding="utf-8")) for n, f in files.items()}
    return files, raw["icao_categories"]["categories"], raw["industry_definitions"]["definitions"], \
        raw["sample_reports"]["reports"], raw["candidates"]["candidates"]


# ====================================================================== run
def run(db, data, out_root, dataset=None, settings=None, selector="rules", llm_outputs=None, llm_cmd=None,
        model=None, quiet=False):
    say = (lambda *a: None) if quiet else print
    S = dict(G.DEFAULT_SETTINGS, **(settings or {}))
    dataset = dataset or Path(data).name
    started = dt.datetime.now(dt.timezone.utc)
    run_id = f"run-{dataset}-{started.strftime('%Y%m%dT%H%M%S%f')[:-3]}"
    out = Path(out_root) / run_id
    (out / "inputs").mkdir(parents=True, exist_ok=True)

    # 0. snapshot + validate --------------------------------------------------------------
    files, parents, defs, reports_in, cands_in = load_inputs(data)
    manifest_files = {}
    for n, f in files.items():
        shutil.copy2(f, out / "inputs" / f.name)
        manifest_files[f.name] = sha(f.read_bytes())
    input_hash = sha(jdump(manifest_files))
    reports, cands, issues = T.validate_inputs(parents, defs, reports_in, cands_in)
    answer_key = {c["candidate_id"]: dict(parent=c.get("expected_parent"), reports=c.get("expected_reports", []),
                                          overlaps=c.get("overlaps", [])) for c in cands}
    for c in cands:                                   # the answer key never reaches the pipeline
        for k in ("expected_parent", "expected_reports", "overlaps"):
            c.pop(k, None)
    settings_hash = sha(jdump(S))[:12]
    T.NORMALISE = S["normalise"]

    # 1–2. route, normalise, index ---------------------------------------------------------
    corpus = ([T.normalise(f"{p['name']}. {p['definition']}") for p in parents] +
              [T.normalise(f"{d['term']}. {d['text']}") for d in defs] +
              [T.normalise(r["narrative"]) for r in reports] +
              [T.normalise(f"{c['name']}. {c['definition']}") for c in cands])
    emb = SentenceTransformerEmbedder(model) if model else LocalEmbedder(corpus)
    store = Store(db)
    store.retrieval = S["retrieval"]
    store.lexical = S["lexical"]
    store.units = S["units"]
    store.ensure_schema((ROOT / "db" / "schema.sql").read_text(), emb.dim)
    store.load_working_set(emb, parents, defs, reports, cands, version=f"{dataset}@{input_hash[:8]}", header=S["context_header"])
    lookup = store.lookup()
    lanes = {}
    for r in reports:
        lanes[r["_lane"]] = lanes.get(r["_lane"], 0) + 1
    say(f"[{run_id}] {len(parents)} parents · {len(defs)} definitions · {len(reports)} reports {lanes} · "
        f"{len(cands)} candidates · {len(issues)} validation issues · embedder {emb.name}")

    # 3. SME decisions read back ------------------------------------------------------------
    cids = [c["candidate_id"] for c in cands]
    sme_all = store.sme_decisions(set(cids))
    sme_by = {cid: [d for d in sme_all if d["candidate_id"] == cid] for cid in cids}
    prev = store.last_run(dataset)
    base_release = store.latest_release()

    # 4. de-duplicate -------------------------------------------------------------------------
    dcands = store.candidates()
    cmap = {c["candidate_id"]: c for c in dcands}
    merges, merge_scores = G.dedupe(store, dcands, S, sme_all)
    canon = [c for c in dcands if c["candidate_id"] not in merges]
    aliases = {c["candidate_id"]: [cmap[a] for a, k in sorted(merges.items()) if k == c["candidate_id"]] for c in canon}
    if merges:
        say(f"  merged before grounding: " + ", ".join(f"{a}→{k}" for a, k in sorted(merges.items())))

    # 5. ground -------------------------------------------------------------------------------
    grounded = [G.ground_candidate(store, c, S, sme_by[c["candidate_id"]], aliases=aliases[c["candidate_id"]]) for c in canon]
    G.resolve_siblings(grounded, store, S)
    sel_name = "rules"
    if selector != "rules":
        tpl = PROMPT_FILE.read_text(encoding="utf-8")
        (out / "prompts").mkdir(exist_ok=True)
        for i, (o, d) in enumerate(grounded):
            c = cmap[o["candidate_id"]]
            prompt = G.build_prompt(tpl, store, c, d, S)
            (out / "prompts" / f"{c['candidate_id']}.md").write_text(prompt, encoding="utf-8")
            ans = None
            if llm_outputs and (Path(llm_outputs) / f"{c['candidate_id']}.json").exists():
                ans = json.loads((Path(llm_outputs) / f"{c['candidate_id']}.json").read_text(encoding="utf-8"))
            elif llm_cmd:
                ans = G.call_llm_cmd(llm_cmd, prompt)
            if ans:
                ans["candidate_id"] = c["candidate_id"]
                grounded[i] = (ans, d)
        sel_name = "llm-file" if llm_outputs else "llm-cmd"

    names = {c["candidate_id"]: c["name"] for c in dcands}
    all_outputs = [o for o, _ in grounded]
    results = []
    for o, d in grounded:
        cid = o["candidate_id"]
        c = cmap[cid]
        sme = sme_by[cid]
        # 6. criteria card ---------------------------------------------------------------------
        card = CR.build_card(store, c, o, d, lookup, all_outputs, names, S, sme)
        # 7. verify -----------------------------------------------------------------------------
        status, checks = verify(o, lookup, S, c.get("proposed_parent"), d, card, sme, set(cids))
        agent_calls, proposals, outcome = [], [], None
        # abstain: nothing in the corpus resembles the candidate
        if d["pool_best"] < S["min_score"]:
            status, outcome = "abstain", "abstained"
        # 8. escalate ---------------------------------------------------------------------------
        elif status == "not_grounded" and S["escalate"]:
            failed = {ch.id for ch in checks if not ch.passed and ch.severity == "block"}
            rej = {x["target_id"] for x in sme if x["action"] == "reject_link" and x["target_type"] == "report"}
            sess = A.plan(A.AgentSession(store, c, o, d, S, rej), failed)
            agent_calls, proposals = sess.calls, sess.proposals
            outcome = "escalated_to_sme" if proposals else None
            outcome = outcome or "returned_to_discovery"
        elif status == "not_grounded":
            outcome = "returned_to_discovery"
        # 9. decide -----------------------------------------------------------------------------
        outcome = outcome or {"grounded": "release_candidate", "needs_review": "sme_review"}[status]
        approved = any(x["action"] == "approve_bucket" for x in sme)
        results.append(dict(candidate_id=cid, name=c["name"], definition=c["definition"], batch=c["batch"],
                            proposed_parent=c.get("proposed_parent"), aliases=[a["candidate_id"] for a in aliases[cid]],
                            output=o, status=status, outcome=outcome, sme_approved=approved,
                            checks=[ch.to_dict() for ch in checks], card=card, agent_calls=agent_calls, proposals=proposals,
                            diag={k: v for k, v in d.items() if k not in ("query_vec", "query_text", "reserve")}))
    for a, k in sorted(merges.items()):
        results.append(dict(candidate_id=a, name=cmap[a]["name"], definition=cmap[a]["definition"], batch=cmap[a]["batch"],
                            proposed_parent=cmap[a].get("proposed_parent"), aliases=[], merged_into=k,
                            output=dict(candidate_id=a, parent_code=None, definition_ids=[], supporting_reports=[], concerns=""),
                            status="merged", outcome="merged", sme_approved=False, checks=[], card=[], agent_calls=[],
                            proposals=[], diag=dict(merge_score=merge_scores.get("|".join(sorted((a, k)))))))
    results.sort(key=lambda r: r["candidate_id"])

    # 11a. canonical output hash + taxonomy version --------------------------------------------
    canonical = [dict(c=r["candidate_id"], m=r.get("merged_into"), p=r["output"]["parent_code"],
                      d=r["output"]["definition_ids"], r=r["output"]["supporting_reports"], s=r["status"],
                      k=[(x["kind"], x["cite_type"], x["cite_id"], x.get("quote")) for x in r["card"]]) for r in results]
    output_hash = sha(jdump(canonical))
    tax_version = f"{dataset}-draft-{output_hash[:10]}"
    hierarchy = build_hierarchy(results, lookup, tax_version, run_id, base_release)

    # 10. store run record ---------------------------------------------------------------------
    manifest = dict(files=manifest_files, snapshot=str((out / "inputs").resolve()), report_keys=sorted(r["report_key"] for r in reports),
                    validation_issues=issues, routing=lanes)
    store.q("""INSERT INTO pipeline_run VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (run_id, started, dataset, input_hash, jdump(manifest), jdump(S), settings_hash, emb.name, sel_name,
             prompt_version(), code_version(), SCHEMA_VERSION, base_release["version"] if base_release else None,
             len(sme_all), output_hash, tax_version))
    today = started.date()
    for r in results:
        o = r["output"]
        store.q("INSERT INTO grounding_result VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (run_id, r["candidate_id"], r.get("merged_into"), o["parent_code"],
                 bool(o["parent_code"]) and o["parent_code"] != r["proposed_parent"], r["status"], r["outcome"],
                 jdump(r["checks"]), jdump(r["diag"])))
        for row in sssom_rows(r, lookup, run_id, sel_name, today, sme_by.get(r["candidate_id"], [])):
            store.q("INSERT INTO grounding_link VALUES (" + ",".join(["%s"] * 17) + ")", [row[k] for k in SSSOM_COLS])
        for x in r["card"]:
            store.q("INSERT INTO criteria_card VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (run_id, r["candidate_id"], x["seq"], x["kind"], x["text"], x["cite_type"], x["cite_id"], x.get("quote"), x["origin"]))
        for i, call in enumerate(r["agent_calls"]):
            store.q("INSERT INTO agent_call VALUES (%s,%s,%s,%s,%s,%s)", (run_id, r["candidate_id"], i, call["tool"], jdump(call["args"]), jdump(call["result"])))

    # 11b. changelog ------------------------------------------------------------------------------
    revisions = changelog(store, run_id, prev, dict(input_hash=input_hash, settings_hash=settings_hash, code_version=code_version(),
                                                     report_keys=set(manifest["report_keys"])), results, sme_all)
    for v in revisions:
        store.q("INSERT INTO revision VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (run_id, v["prev_run_id"], v["candidate_id"], v["change_type"], v["target"], v["before"], v["after"], v["cause_type"], v["cause_ref"]))

    # evaluation against the answer key (evaluation only) + guardrails ---------------------------
    metrics = score(results, answer_key, merges)
    guards = guardrails(results, lookup, S, cids)
    summary = dict(run_id=run_id, dataset=dataset, taxonomy_version=tax_version, output_hash=output_hash,
                   input_hash=input_hash, settings_hash=settings_hash, code_version=code_version(), selector=sel_name,
                   embedder=emb.name, prompt_version=prompt_version(), schema_version=SCHEMA_VERSION,
                   base_release=base_release, previous_run=prev["run_id"] if prev else None, sme_decisions_read=len(sme_all),
                   status={s: sum(r["status"] == s for r in results) for s in ("grounded", "needs_review", "not_grounded", "merged", "abstain")},
                   metrics=metrics, guardrails_blocked=f"{sum(g['blocked'] for g in guards)}/{len(guards)}",
                   revisions=len(revisions), validation_issues=len(issues), routing=lanes, merges=merges)
    write_outputs(out, summary, S, results, hierarchy, revisions, guards, lookup, manifest)
    latest = Path(out_root) / "latest"
    if latest.is_symlink() or latest.exists():
        latest.unlink()
    latest.symlink_to(out.name)
    say(f"  status {summary['status']} · parents {metrics['parent_correct']} · precision {metrics['precision']} "
        f"recall {metrics['recall']} (merge-aware {metrics['merge_precision']}/{metrics['merge_recall']}) · "
        f"guardrails {summary['guardrails_blocked']} · revisions {len(revisions)} · hash {output_hash[:12]}")
    say(f"  outputs → {out}")
    return summary


# ====================================================================== pieces
SSSOM_COLS = ["run_id", "subject_id", "subject_label", "predicate_id", "object_id", "object_label", "link_type",
              "mapping_justification", "confidence", "evidence_quote", "mapping_tool", "mapping_tool_version",
              "mapping_date", "author_id", "reviewer_id", "sme_decision_id", "comment"]


def sssom_rows(r, lookup, run_id, selector, day, sme):
    parents, defs, reps = lookup
    o = r["output"]
    if not o["parent_code"]:
        return []
    by_target = {}
    for d in sme:
        if d["action"] in ("accept", "add_link", "set_parent"):
            by_target[(d["target_type"], d["target_id"])] = d
    diag = r["diag"]
    sup_score = {s["report_key"]: s["score"] for s in diag.get("support", [])}
    def_score = {d["def_id"]: d["score"] for d in diag.get("definitions", [])}
    rows = []

    def row(lt, obj, label, conf, quote=None, comment=""):
        d = by_target.get((lt, obj))
        rows.append(dict(run_id=run_id, subject_id=r["candidate_id"], subject_label=r["name"], predicate_id=PREDICATE[lt],
                         object_id=obj, object_label=label, link_type=lt,
                         mapping_justification="semapv:ManualMappingCuration" if d else "semapv:CompositeMatching",
                         confidence=conf, evidence_quote=quote, mapping_tool="taxground", mapping_tool_version=code_version(),
                         mapping_date=day, author_id=f"taxground:{selector}", reviewer_id=d["reviewer"] if d else None,
                         sme_decision_id=d["decision_id"] if d else None, comment=f"status={r['status']}" + (f"; {comment}" if comment else "")))
    row("parent", o["parent_code"], parents.get(o["parent_code"], {}).get("name", "NOT ALLOWED"),
        diag.get("parent_scores", {}).get(o["parent_code"]), comment=f"proposed={r['proposed_parent']}")
    for d in o["definition_ids"]:
        row("definition", d, defs.get(d, {}).get("term", "NOT FOUND"), def_score.get(d))
    for s in o["supporting_reports"]:
        rr = reps.get(s["report_key"], {})
        row("report", s["report_key"], rr.get("lane", "NOT FOUND"), sup_score.get(s["report_key"]), s["evidence"],
            comment=f"raw layer: stage-2 codes {'+'.join(rr.get('l1', []))} -> harmonised layer: bucket under {o['parent_code']}")
    return rows


def build_hierarchy(results, lookup, version, run_id, base_release):
    parents, defs, _ = lookup
    tree = {}
    for r in results:
        if r["status"] in ("merged", "abstain") or not r["output"]["parent_code"]:
            continue
        p = r["output"]["parent_code"]
        tree.setdefault(p, dict(code=p, name=parents.get(p, {}).get("name"), level="CICTT L1", buckets=[]))
        card = r["card"]
        tree[p]["buckets"].append(dict(
            bucket_id=r["candidate_id"], name=r["name"], level="L2", definition=r["definition"], status=r["status"],
            publishable=r["status"] == "grounded" or (r["status"] == "needs_review" and r["sme_approved"]),
            merged_from=r["aliases"], industry_definitions=r["output"]["definition_ids"],
            include=[dict(text=c["text"], cite=f"{c['cite_type']}:{c['cite_id']}", quote=c.get("quote")) for c in card if c["kind"] == "include"],
            exclude=[dict(text=c["text"], cite=f"{c['cite_type']}:{c['cite_id']}", quote=c.get("quote")) for c in card if c["kind"] in ("exclude", "boundary")],
            examples=[dict(report_key=c["cite_id"], quote=c["quote"]) for c in card if c["kind"] == "example_pos"],
            failed_checks=[c["id"] for c in r["checks"] if not c["passed"]]))
    return dict(taxonomy_version=version, run_id=run_id, base_release=base_release["version"] if base_release else None,
                levels=["CICTT L1 (ICAO parent)", "L2 bucket"], parents=[tree[k] for k in sorted(tree)],
                not_in_hierarchy=[dict(bucket_id=r["candidate_id"], status=r["status"], merged_into=r.get("merged_into"))
                                  for r in results if r["status"] in ("merged", "abstain")])


def changelog(store, run_id, prev, now, results, sme_all):
    if not prev:
        return []
    prow = store.q("SELECT input_manifest, settings_hash, code_version FROM pipeline_run WHERE run_id = %s", (prev["run_id"],))[0]
    prev_keys = set(prow[0].get("report_keys", []))
    old_res = store.run_results(prev["run_id"])
    old_links = {}
    for s, lt, obj, _ in store.run_links(prev["run_id"]):
        old_links.setdefault(s, set()).add((lt, obj))
    old_cards = {}
    for cid, kind, txt, ct, ci in store.run_cards(prev["run_id"]):
        old_cards.setdefault(cid, set()).add(f"{kind}|{ct}|{ci}")
    prev_sme = set()
    for (dg,) in store.q("SELECT diagnostics FROM grounding_result WHERE run_id = %s", (prev["run_id"],)):
        prev_sme |= set((dg or {}).get("sme_applied", []))
    prev_started = store.q("SELECT started_at FROM pipeline_run WHERE run_id = %s", (prev["run_id"],))[0][0]
    new_sme = [d for d in sme_all if d["decided_at"] > prev_started]
    revs = []

    parent_of = {}
    for cid, v in old_res.items():
        parent_of.setdefault(cid, set()).add(v["parent"])
    for r in results:
        parent_of.setdefault(r["candidate_id"], set()).add(r["output"]["parent_code"])

    def fmt(ds, via=None):
        return "; ".join(f"sme:{d['decision_id']}" + (f" on {d['candidate_id']}" if via else "") +
                         (f" (prompted by report {d['prompting_report']})" if d["prompting_report"] else "") for d in ds)

    def cause(cid, target=None):
        direct = [d for d in new_sme if d["candidate_id"] == cid and d["action"] not in ("approve_bucket", "accept")]
        exact = [d for d in direct if target and d["target_id"] == target]
        if exact:
            return "sme", fmt(exact)
        if direct:
            return "sme", fmt(direct)
        # knock-on: an SME decision on a sibling under the same parent changed this bucket's siblings or evidence
        mine = parent_of.get(cid, set()) - {None}
        via = [d for d in new_sme if d["candidate_id"] != cid and d["action"] not in ("approve_bucket", "accept")
               and parent_of.get(d["candidate_id"], set()) & mine]
        if via:
            return "sme", "via sibling: " + fmt(via, via=True)
        if target and target not in prev_keys and target in now["report_keys"]:
            return "report", f"report:{target} (new in inputs)"
        if now["input_hash"] != prev["input_hash"]:
            return "data", f"input {prev['input_hash'][:8]}→{now['input_hash'][:8]}"
        if now["settings_hash"] != prev["settings_hash"]:
            return "settings", f"settings {prev['settings_hash']}→{now['settings_hash']}"
        if now["code_version"] != prev["code_version"]:
            return "code", f"{prev['code_version']}→{now['code_version']}"
        return "none", "unexplained change: investigate"

    for r in results:
        cid = r["candidate_id"]
        o = old_res.get(cid)
        new_links = set()
        if r["output"]["parent_code"]:
            new_links = {("parent", r["output"]["parent_code"])} | {("definition", d) for d in r["output"]["definition_ids"]} | \
                        {("report", s["report_key"]) for s in r["output"]["supporting_reports"]}
        if o is None:
            revs.append(dict(candidate_id=cid, change_type="bucket_added", target=cid, before=None, after=r["status"], cause=cause(cid)))
            continue
        if o["parent"] != r["output"]["parent_code"]:
            revs.append(dict(candidate_id=cid, change_type="parent", target="parent", before=o["parent"], after=r["output"]["parent_code"], cause=cause(cid, r["output"]["parent_code"])))
        if o["status"] != r["status"]:
            revs.append(dict(candidate_id=cid, change_type="status", target="status", before=o["status"], after=r["status"], cause=cause(cid)))
        for lt, obj in sorted(new_links - old_links.get(cid, set())):
            if lt != "parent":
                revs.append(dict(candidate_id=cid, change_type="link_added", target=f"{lt}:{obj}", before=None, after=obj, cause=cause(cid, obj)))
        for lt, obj in sorted(old_links.get(cid, set()) - new_links):
            if lt != "parent":
                revs.append(dict(candidate_id=cid, change_type="link_removed", target=f"{lt}:{obj}", before=obj, after=None, cause=cause(cid, obj)))
        new_c = {x["key"] for x in r["card"]}
        for k in sorted(new_c - old_cards.get(cid, set())):
            revs.append(dict(candidate_id=cid, change_type="criterion_added", target=k, before=None, after=k, cause=cause(cid, k.split("|")[-1])))
        for k in sorted(old_cards.get(cid, set()) - new_c):
            revs.append(dict(candidate_id=cid, change_type="criterion_removed", target=k, before=k, after=None, cause=cause(cid, k)))
    for v in revs:
        v["cause_type"], v["cause_ref"] = v.pop("cause")
        v["prev_run_id"] = prev["run_id"]
    return revs


def score(results, key, merges):
    live = [r for r in results if r["status"] != "merged"]
    if not any(v.get("parent") for v in key.values()):          # real data: no answer key, nothing to score against
        for r in results:
            r["metrics"] = dict(parent_correct=None, tp=None, fp=[], fn=[])
        return dict(answer_key=False, buckets=len(live), parent_correct="n/a", parent_rate=None, precision=None, recall=None,
                    merge_precision=None, merge_recall=None, merges_found=len(merges), merges_correct=None, twin_pairs_in_key=0)
    tp = fp = fn = 0
    for r in results:
        if r["status"] == "merged":
            continue
        got = {s["report_key"] for s in r["output"]["supporting_reports"]}
        exp = set(key.get(r["candidate_id"], {}).get("reports", []))
        r["metrics"] = dict(parent_correct=r["output"]["parent_code"] == key.get(r["candidate_id"], {}).get("parent"),
                            tp=len(got & exp), fp=sorted(got - exp), fn=sorted(exp - got))
        tp, fp, fn = tp + len(got & exp), fp + len(got - exp), fn + len(exp - got)
    # merge-aware: a canonical bucket is scored against the union of its own and its absorbed twins' answer keys
    mtp = mfp = mfn = 0
    for r in live:
        group = [r["candidate_id"]] + r["aliases"]
        exp = set().union(*(set(key.get(g, {}).get("reports", [])) for g in group))
        got = {s["report_key"] for s in r["output"]["supporting_reports"]}
        mtp, mfp, mfn = mtp + len(got & exp), mfp + len(got - exp), mfn + len(exp - got)
    has_key = any(v.get("parent") for v in key.values())
    true_pairs = {tuple(sorted((a, b))) for a, v in key.items() for b in v.get("overlaps", [])}
    found = {tuple(sorted((a, k))) for a, k in merges.items()}
    pc = sum(r["metrics"]["parent_correct"] for r in live)
    return dict(answer_key=has_key, buckets=len(live),
                parent_correct=f"{pc}/{len(live)}", parent_rate=round(pc / len(live), 3) if live else None,
                precision=round(tp / (tp + fp), 3) if tp + fp else None, recall=round(tp / (tp + fn), 3) if tp + fn else None,
                merge_precision=round(mtp / (mtp + mfp), 3) if mtp + mfp else None,
                merge_recall=round(mtp / (mtp + mfn), 3) if mtp + mfn else None,
                merges_found=len(found), merges_correct=len(found & true_pairs), twin_pairs_in_key=len(true_pairs))


def guardrails(results, lookup, S, cids):
    """Faulty answers an unconstrained model might give, run through the same verifier. All must be blocked."""
    parents, defs, reps = lookup
    base_r = next((r for r in results if r["status"] == "grounded"), None)
    if not base_r:
        return []
    base, card = base_r["output"], base_r["card"]
    par = base["parent_code"]
    other_def = next(d for d, v in sorted(defs.items()) if par not in v["parents"])
    other_rep = next(k for k, v in sorted(reps.items()) if par not in v["l1"] and v["level"] != "none")
    first = base["supporting_reports"][0]
    inc_def = next(c for c in card if c["kind"] == "include")
    sup_ex = next(c for c in card if c["kind"] == "example_pos")
    exc = [c for c in card if c["kind"] in ("exclude", "boundary")]
    fake_sme = [dict(decision_id="GUARD-1", action="reject_link", target_type="report", target_id=first["report_key"],
                     candidate_id=base_r["candidate_id"])]
    tests = [
        ("Parent not in the allowed list", dict(base, parent_code="RUNWAY-SAFETY"), card, ()),
        ("Invented definition id", dict(base, definition_ids=base["definition_ids"] + ["IND-99"]), card, ()),
        ("Definition from another parent", dict(base, definition_ids=[other_def]), card, ()),
        ("Paraphrased evidence", dict(base, supporting_reports=[dict(first, evidence="The crew landed on a taxiway at night.")] + base["supporting_reports"][1:]), card, ()),
        ("Report from another parent", dict(base, supporting_reports=base["supporting_reports"] + [dict(report_key=other_rep, evidence=T.sentences(reps[other_rep]["text"])[0])]), card, ()),
        ("Invented report key", dict(base, supporting_reports=base["supporting_reports"] + [dict(report_key="UNKNOWN-999", evidence="Invented evidence sentence.")]), card, ()),
        ("Criterion cites an invented definition", base, card + [dict(inc_def, kind="include", cite_type="definition", cite_id="IND-99")], ()),
        ("Criterion quote paraphrased", base, [dict(c, quote="A paraphrase of the report.") if c is sup_ex else c for c in card], ()),
        ("Exclusion cites a supporting report", base, card + [dict(sup_ex, kind="exclude")], ()),
        ("Card without any exclusion", base, [c for c in card if c not in exc], ()),
        ("SME-rejected report reinserted", base, card, fake_sme),
    ]
    out = []
    for name, o, cd, sme in tests:
        st, ch = verify(o, lookup, S, None, None, cd, list(sme), set(cids))
        failed = [x.id for x in ch if not x.passed]
        out.append(dict(test=name, status=st, failed_checks=" ".join(failed), base_candidate=base_r["candidate_id"],
                        blocked=st == "not_grounded"))
    return out


# ====================================================================== files
def write_outputs(out, summary, S, results, hierarchy, revisions, guards, lookup, manifest):
    parents, defs, reps = lookup
    (out / "manifest.json").write_text(json.dumps(dict(summary=summary, settings=S, inputs=manifest), indent=1, default=str))
    (out / "grounding_results.json").write_text(json.dumps(dict(summary=summary, settings=S, results=results), indent=1, default=str))
    (out / "taxonomy.json").write_text(json.dumps(hierarchy, indent=1, default=str))
    with open(out / "grounding_table.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["candidate_id", "name", "proposed_parent", "grounded_parent", "merged_into", "definitions", "supporting_reports",
                    "include_criteria", "exclude_criteria", "status", "outcome", "failed_checks"])
        for r in results:
            o = r["output"]
            w.writerow([r["candidate_id"], r["name"], r["proposed_parent"], o["parent_code"], r.get("merged_into", ""),
                        " ".join(o["definition_ids"]), " ".join(s["report_key"] for s in o["supporting_reports"]),
                        sum(c["kind"] == "include" for c in r["card"]), sum(c["kind"] in ("exclude", "boundary") for c in r["card"]),
                        r["status"], r["outcome"], " ".join(c["id"] for c in r["checks"] if not c["passed"])])
    # SSSOM TSV with YAML header
    day = summary["run_id"].split("-")[-1][:8]
    with open(out / "links.sssom.tsv", "w", newline="", encoding="utf-8") as f:
        f.write(f"# curie_map:\n#   skos: http://www.w3.org/2004/02/skos/core#\n#   semapv: https://w3id.org/semapv/vocab/\n"
                f"#   sssom: https://w3id.org/sssom/\n# mapping_set_id: taxground:{summary['taxonomy_version']}\n"
                f"# mapping_set_version: {summary['taxonomy_version']}\n# mapping_date: {day[:4]}-{day[4:6]}-{day[6:8]}\n"
                f"# comment: run {summary['run_id']}; output hash {summary['output_hash']}\n")
        w = csv.writer(f, delimiter="\t")
        w.writerow(SSSOM_COLS)
        for r in results:
            for row in sssom_rows(r, lookup, summary["run_id"], summary["selector"], f"{day[:4]}-{day[4:6]}-{day[6:8]}", []):
                w.writerow([row[k] if row[k] is not None else "" for k in SSSOM_COLS])
    # criteria cards
    L = [f"# Criteria cards · taxonomy {summary['taxonomy_version']}", "",
         f"Run {summary['run_id']} · selector {summary['selector']} · embedder {summary['embedder']} · reports are synthetic.", ""]
    for r in results:
        if r["card"]:
            L.append(CR.card_markdown(r, r["output"], r["card"], lookup, r["status"], summary["taxonomy_version"]))
            L.append("**Checks:** " + " · ".join(f"{c['id']} {'pass' if c['passed'] else 'FAIL'}" for c in r["checks"]) + "\n")
        elif r["status"] == "merged":
            L.append(f"### {r['candidate_id']} · {r['name']}\n\n*Merged into {r['merged_into']} before grounding.*\n")
    (out / "criteria_cards.md").write_text("\n".join(L), encoding="utf-8")
    with open(out / "guardrail_tests.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["test", "status", "failed_checks", "base_candidate", "blocked"])
        w.writeheader(); w.writerows(guards)
    # changelog
    C = [f"# Changelog · {summary['taxonomy_version']}", "", f"Run {summary['run_id']} vs previous run {summary['previous_run'] or '(none)'}.", ""]
    if not summary["previous_run"]:
        C.append("First run for this dataset: every bucket is new.")
    elif not revisions:
        C.append("No changes. Same inputs, settings and code reproduce the same taxonomy (output hash equal).")
    else:
        C += ["| Bucket | Change | Target | Before | After | Cause | Reference |", "|---|---|---|---|---|---|---|"]
        e = lambda x: str(x or "").replace("|", "\\|")
        C += [f"| {v['candidate_id']} | {v['change_type']} | {e(v['target'])} | {e(v['before'])} | {e(v['after'])} | {v['cause_type']} | {e(v['cause_ref'])} |" for v in revisions]
    (out / "changelog.md").write_text("\n".join(C) + "\n", encoding="utf-8")
    # SME review template: one row per link and per criterion
    with open(out / "sme_review_template.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["reviewed_run_id", "candidate_id", "action", "target_type", "target_id", "value", "rationale", "prompting_report", "current"])
        for r in results:
            if r["status"] == "merged":
                w.writerow([summary["run_id"], r["candidate_id"], "", "candidate", r["merged_into"], "", "", "", f"merged into {r['merged_into']} (keep_separate to undo)"])
                continue
            o = r["output"]
            if o["parent_code"]:
                w.writerow([summary["run_id"], r["candidate_id"], "", "parent", o["parent_code"], "", "", "", f"status {r['status']}"])
            for d in o["definition_ids"]:
                w.writerow([summary["run_id"], r["candidate_id"], "", "definition", d, "", "", "", defs.get(d, {}).get("term", "")])
            for s in o["supporting_reports"]:
                w.writerow([summary["run_id"], r["candidate_id"], "", "report", s["report_key"], "", "", "", s["evidence"]])
            for c in r["card"]:
                if c["kind"] != "example_pos":
                    w.writerow([summary["run_id"], r["candidate_id"], "", "criterion", c["key"], "", "", "", c["text"]])
    from .report import write_review_pack
    write_review_pack(out, summary, results, hierarchy, revisions, guards, lookup)

"""Criteria cards (SRS-TAX-03): definition, parent, inclusion / exclusion criteria and linked example reports.

Every criterion carries one citation that the verifier (G9) resolves: the parent code, a crosswalked definition,
a report with a verbatim quote, a sibling bucket, or an SME decision. Nothing on a card is free text without a source.
"""
import collections
import re

from . import text as T
from .ground import relevant


def _sentence_with(text, stem):
    for s in T.sentences(text):
        if any(T.stem(w) == stem for w in T.content_words(s)):
            return s
    return T.sentences(text)[0] if T.sentences(text) else text


def build_card(store, cand, out, diag, lookup, all_outputs, names, S, sme=()):
    parents, defs, reps = lookup
    p = out["parent_code"]
    pname = parents.get(p, {}).get("name", p)
    card = []

    def add(kind, txt, ctype, cid, quote=None, origin="derived"):
        card.append(dict(kind=kind, text=txt, cite_type=ctype, cite_id=cid, quote=quote, origin=origin))

    # ---- inclusion
    add("include", f"The occurrence meets the CICTT {p} ({pname}) definition.", "parent", p)
    add("include", f"Core definition: {cand['definition']}", "candidate", cand["candidate_id"])
    for d in out["definition_ids"]:
        if d in defs:
            add("include", f"Matches '{defs[d]['term']}' ({defs[d]['source']}): {defs[d]['body']}", "definition", d)
    # signature terms: frequent in the bucket's evidence, rare in its near-misses
    sup = out["supporting_reports"]
    near = [x for x in relevant([dict(x) for x in diag["pool"]], S) if p not in x["l1"]]
    if len(sup) >= 2:
        df = collections.Counter()
        surface = {}
        for s in sup:
            ws = {T.stem(w) for w in T.content_words(s["evidence"])}
            for w in T.content_words(s["evidence"]):
                surface.setdefault(T.stem(w), w)
            df.update(ws)
        near_df = collections.Counter()
        for x in near:
            near_df.update({T.stem(w) for w in T.content_words(reps[x["report_key"]]["text"])})
        generic = {T.stem(w) for w in T.content_words(pname)} | {"aircraft", "crew", "flight", "airport", "report"}
        terms = []
        for st, n in df.items():
            share = n / len(sup)
            nshare = near_df[st] / len(near) if near else 0.0
            if n >= 2 and share >= 0.4 and nshare < share / 2 and st not in generic:
                terms.append((-(share - nshare), st))
        for _, st in sorted(terms)[:3]:
            hits = [s for s in sup if st in {T.stem(w) for w in T.content_words(s["evidence"])}]
            ex = hits[0]
            add("include", f"Narrative describes '{surface[st]}' ({len(hits)} of {len(sup)} supporting reports).",
                "report", ex["report_key"], ex["evidence"])

    # ---- exclusion
    moved = collections.defaultdict(list)
    for m in diag.get("moved_to_sibling", []):
        moved[m["to"]].append(m)
    for sib, ms in sorted(moved.items()):
        m = ms[0]
        add("exclude", f"Belongs to sibling {sib} '{names.get(sib, sib)}' when it matches that bucket better "
                       f"({len(ms)} report(s) assigned there).", "report", m["report_key"], m["evidence"])
    sibs = sorted(o["candidate_id"] for o in all_outputs
                  if o["parent_code"] == p and o["candidate_id"] != out["candidate_id"] and o["candidate_id"] not in moved)
    for sib in sibs[:3]:
        add("boundary", f"Distinguish from sibling {sib} '{names.get(sib, sib)}' under the same parent.", "sibling", sib)
    seen_codes = set()
    for x in near:
        code = next((c for c in x["l1"] if c != p), None)
        if not code or code in seen_codes or len(seen_codes) >= 3:
            continue
        seen_codes.add(code)
        q = store.best_sentence(diag["query_vec"], x["report_key"], diag["query_text"])[0]
        add("exclude", f"Coded {code} ({parents.get(code, {}).get('name', code)}) rather than {p}: similar wording, "
                       f"different occurrence category.", "report", x["report_key"], q)
    for d in [d for d in diag.get("other_definitions", []) if p not in d["parents"]]:   # relative to THIS output's parent
        add("exclude", f"Not '{d['term']}' — that definition is crosswalked to {', '.join(d['parents'])}, not {p}.",
            "definition", d["def_id"])
    r = diag["runner_up"] if diag["runner_up"] != p else next(iter(k for k in diag["parent_scores"] if k != p), diag["runner_up"])
    add("exclude", f"Events better described by CICTT {r} ({parents.get(r, {}).get('name', r)}) "
                   f"(runner-up parent, margin {diag['margin']:.2f}).", "parent", r)

    # ---- linked example reports
    for s in sup:
        add("example_pos", f"Example: {s['report_key']}", "report", s["report_key"], s["evidence"])

    # ---- SME revisions to the card
    removed = {d["target_id"] for d in sme if d["action"] == "remove_criterion"}
    card = [c for c in card if f"{c['kind']}|{c['cite_type']}|{c['cite_id']}" not in removed]
    for d in sme:
        if d["action"] == "add_criterion":
            add(d["target_id"] or "include", d["value"], "sme", d["decision_id"], origin="sme")
    for i, c in enumerate(card):
        c["seq"] = i
        c["key"] = f"{c['kind']}|{c['cite_type']}|{c['cite_id']}"
    return card


def card_markdown(cand, out, card, lookup, status, version):
    parents, defs, _ = lookup
    p = out["parent_code"]
    L = [f"### {cand['candidate_id']} · {cand['name']}", "",
         f"*Taxonomy version {version} · status {status.replace('_', ' ')} · parent {p} {parents.get(p, {}).get('name', '')}*", "",
         f"**Definition.** {cand['definition']}", "", "**Include when**"]
    L += [f"- {c['text']}  `[{c['cite_type']}:{c['cite_id']}]`" + (f"  \n  > {c['quote']}" if c.get("quote") and c["cite_type"] == "report" else "")
          for c in card if c["kind"] == "include"]
    L += ["", "**Exclude when**"]
    L += [f"- {c['text']}  `[{c['cite_type']}:{c['cite_id']}]`" + (f"  \n  > {c['quote']}" if c.get("quote") else "")
          for c in card if c["kind"] in ("exclude", "boundary")]
    L += ["", "**Linked example reports**"]
    L += [f"- {c['cite_id']}: \"{c['quote']}\"" for c in card if c["kind"] == "example_pos"] or ["- none"]
    return "\n".join(L) + "\n"

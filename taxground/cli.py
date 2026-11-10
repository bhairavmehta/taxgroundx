"""taxground command line.

  taxground run      --db DSN --data FOLDER [--out out] [--selector rules|llm-file|llm-cmd] [--set key=value ...]
  taxground review   --db DSN --file decisions.csv --reviewer NAME           # SME decisions -> release store
  taxground release  --db DSN --run RUN_ID --version v1.0 --approver NAME    # SME-approved, frozen taxonomy release
  taxground test     --db DSN --version v1.0|RUN_ID --reports FILE.json      # test reports against a taxonomy version
  taxground diff     --db DSN --a RUN_ID --b RUN_ID
  taxground gate     --db DSN --run RUN_ID [--thresholds gate.json]          # CI release gate
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

from . import ground as G
from . import pipeline as P
from . import text as T
from .store import Store, jdump

ACTIONS = {"accept", "reject_link", "add_link", "set_parent", "merge", "keep_separate", "add_criterion", "remove_criterion", "approve_bucket"}


def _store(a):
    return Store(a.db)


def cmd_run(a):
    S = {}
    for kv in a.set or []:
        k, v = kv.split("=", 1)
        S[k] = type(G.DEFAULT_SETTINGS[k])(v)
    s = P.run(a.db, a.data, a.out, dataset=a.dataset, settings=S, selector=a.selector, llm_outputs=a.llm_outputs,
              llm_cmd=a.llm_cmd, model=a.model)
    print(json.dumps(dict(run_id=s["run_id"], taxonomy_version=s["taxonomy_version"], output_hash=s["output_hash"]), indent=1))


def cmd_review(a):
    st = _store(a)
    runs = {r[0]: r[1] for r in st.q("SELECT run_id, taxonomy_version FROM pipeline_run")}
    now = dt.datetime.now(dt.timezone.utc)
    ok, bad = 0, []
    with open(a.file, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for i, r in enumerate(rows, 2):
        act = (r.get("action") or "").strip()
        if not act:
            continue
        run_id = r.get("reviewed_run_id", "").strip()
        cid, ttype, tid = r["candidate_id"].strip(), (r.get("target_type") or "").strip(), (r.get("target_id") or "").strip()
        err = None
        if act not in ACTIONS:
            err = f"unknown action {act}"
        elif run_id not in runs:
            err = f"unknown reviewed run {run_id}"
        elif not st.q("SELECT 1 FROM grounding_result WHERE run_id=%s AND candidate_id=%s", (run_id, cid)):
            err = f"bucket {cid} not in run {run_id}"
        elif act in ("reject_link", "accept") and ttype in ("report", "definition", "parent") and \
                not st.q("SELECT 1 FROM grounding_link WHERE run_id=%s AND subject_id=%s AND link_type=%s AND object_id=%s", (run_id, cid, ttype, tid)):
            err = f"{ttype} {tid} is not linked to {cid} in {run_id}"
        elif act == "add_link" and ttype == "report" and not st.q("SELECT 1 FROM report WHERE report_key=%s", (tid,)):
            err = f"report {tid} unknown"
        elif act == "add_link" and ttype == "definition" and not st.q("SELECT 1 FROM industry_definition WHERE def_id=%s", (tid,)):
            err = f"definition {tid} unknown"
        elif act == "set_parent" and not st.q("SELECT 1 FROM icao_category WHERE code=%s AND in_scope AND NOT co_code_only", (tid,)):
            err = f"parent {tid} is not an allowed CICTT parent"
        elif act == "remove_criterion" and not st.q("SELECT 1 FROM criteria_card WHERE run_id=%s AND candidate_id=%s AND kind||'|'||cite_type||'|'||cite_id=%s", (run_id, cid, tid)):
            err = f"criterion {tid} not on {cid}'s card in {run_id}"
        if err:
            bad.append(f"line {i}: {err}")
            continue
        body = jdump([run_id, cid, act, ttype, tid, r.get("value", ""), a.reviewer])
        did = "D-" + hashlib.sha256(body.encode()).hexdigest()[:10]
        if st.q("SELECT 1 FROM sme_decision WHERE decision_id=%s", (did,)):
            continue
        # a newer decision on the same target supersedes the older one
        st.q("""UPDATE sme_decision SET superseded_by=%s WHERE superseded_by IS NULL AND candidate_id=%s AND target_id IS NOT DISTINCT FROM %s
                AND target_type IS NOT DISTINCT FROM %s""", (did, cid, tid or None, ttype or None))
        st.q("INSERT INTO sme_decision VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL)",
             (did, run_id, runs[run_id], cid, act, ttype or None, tid or None, r.get("value") or None, a.reviewer,
              r.get("rationale") or None, r.get("prompting_report") or None, now))
        ok += 1
    print(f"{ok} decision(s) stored in the release store; {len(bad)} rejected")
    for b in bad:
        print("  " + b)
    return 1 if bad and not ok else 0


def cmd_release(a):
    st = _store(a)
    run = st.q("SELECT run_id, output_hash, taxonomy_version, dataset FROM pipeline_run WHERE run_id=%s", (a.run,))
    if not run:
        sys.exit(f"unknown run {a.run}")
    res = st.q("SELECT candidate_id, status FROM grounding_result WHERE run_id=%s", (a.run,))
    approved = {r[0] for r in st.q("SELECT candidate_id FROM sme_decision WHERE action='approve_bucket' AND superseded_by IS NULL")}
    include = [c for c, s in res if s == "grounded" or (s == "needs_review" and c in approved)]
    held = [c for c, s in res if s == "needs_review" and c not in approved]
    if held and not a.allow_held:
        sys.exit(f"{len(held)} bucket(s) need SME approval before release: {', '.join(sorted(held))}. "
                 f"Approve them (approve_bucket) or pass --allow-held to release without them.")
    if st.q("SELECT 1 FROM taxonomy_release WHERE version=%s", (a.version,)):
        sys.exit(f"version {a.version} is already released; versions are immutable, choose a new one")
    src = Path(a.out) / a.run / "taxonomy.json"
    if not src.exists():
        sys.exit(f"{src} not found: pass the --out folder that holds run {a.run}")
    tax = json.loads(src.read_text())          # read everything before recording the release, so a failure leaves no row
    out = Path(a.out) / f"release-{a.version}"
    out.mkdir(parents=True, exist_ok=True)
    for p in tax["parents"]:
        p["buckets"] = [b for b in p["buckets"] if b["bucket_id"] in include]
    tax["parents"] = [p for p in tax["parents"] if p["buckets"]]
    tax.update(release=a.version, approved_by=a.approver, content_hash=run[0][1], held_back=sorted(held))
    (out / "taxonomy.json").write_text(json.dumps(tax, indent=1))
    st.q("INSERT INTO taxonomy_release VALUES (%s,%s,'approved',%s,%s,%s,%s,%s)",
         (a.version, a.run, a.approver, dt.datetime.now(dt.timezone.utc), run[0][1], len(include),
          f"draft {run[0][2]}; held back: {', '.join(sorted(held)) or 'none'}"))
    print(f"Released {a.version}: {len(include)} buckets from {a.run} (approved by {a.approver}); held back {len(held)}. → {out}")


def _resolve_version(st, v):
    r = st.q("SELECT run_id FROM taxonomy_release WHERE version=%s", (v,))
    if r:
        return r[0][0], v
    r = st.q("SELECT run_id, taxonomy_version FROM pipeline_run WHERE run_id=%s OR taxonomy_version=%s ORDER BY run_id DESC LIMIT 1", (v, v))
    if not r:
        sys.exit(f"unknown taxonomy version {v}")
    return r[0][0], r[0][1]


def cmd_test(a):
    """Test reports against one taxonomy version (SRS-TAX-04). The version's embedder is rebuilt from its recorded
    inputs, each report is scored against every bucket under its coded parent(s) by nearest supporting evidence
    and bucket definition, and anything that does not fit cleanly becomes a revision prompt for SMEs."""
    st = _store(a)
    run_id, version = _resolve_version(st, a.version)
    man = st.q("SELECT input_manifest, settings, dataset FROM pipeline_run WHERE run_id=%s", (run_id,))[0]
    snap, S = Path(man[0]["snapshot"]), dict(G.DEFAULT_SETTINGS, **man[1])
    files, parents, defs, reports, cands = P.load_inputs(snap)
    reports, cands, _ = T.validate_inputs(parents, defs, reports, cands)
    corpus = ([T.normalise(f"{p['name']}. {p['definition']}") for p in parents] + [T.normalise(f"{d['term']}. {d['text']}") for d in defs] +
              [T.normalise(r["narrative"]) for r in reports] + [T.normalise(f"{c['name']}. {c['definition']}") for c in cands])
    from .embed import LocalEmbedder
    emb = LocalEmbedder(corpus)
    rtext = {r["report_key"]: r for r in reports}
    released = st.q("SELECT 1 FROM taxonomy_release WHERE version=%s", (version,))
    res = st.q("SELECT candidate_id, parent_code, status FROM grounding_result WHERE run_id=%s AND status IN ('grounded','needs_review')", (run_id,))
    if released:                                   # a release is tested on exactly the buckets it published
        rel = json.loads((Path(a.out) / f"release-{version}" / "taxonomy.json").read_text())
        keep = {b["bucket_id"] for p in rel["parents"] for b in p["buckets"]}
        res = [x for x in res if x[0] in keep]
    buckets = {}
    for cid, par, status in res:
        links = [r[0] for r in st.q("SELECT object_id FROM grounding_link WHERE run_id=%s AND subject_id=%s AND link_type='report'", (run_id, cid))]
        c = next(x for x in cands if x["candidate_id"] == cid)
        crit = st.q("SELECT kind, text, quote FROM criteria_card WHERE run_id=%s AND candidate_id=%s AND kind IN ('include','exclude')", (run_id, cid))
        exc_txt = [q or t for k, t, q in crit if k == "exclude"]
        inc_txt = [q or t for k, t, q in crit if k == "include"]
        buckets_crit = dict(exc=emb.encode([T.normalise(x) for x in exc_txt]) if exc_txt else np.zeros((0, emb.dim)),
                            exc_txt=exc_txt, inc=emb.encode([T.normalise(x) for x in inc_txt]) if inc_txt else np.zeros((0, emb.dim)))
        buckets[cid] = dict(parent=par, name=c["name"], status=status, **buckets_crit,
                            dvec=emb.encode([T.normalise(f"{c['name']}. {c['definition']}")])[0],
                            evec=emb.encode([T.normalise(rtext[k]["narrative"]) for k in links]) if links else np.zeros((0, emb.dim)))
    tests = json.loads(Path(a.reports).read_text())["reports"]
    test_id = f"test-{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S')}"
    rows, now = [], dt.datetime.now(dt.timezone.utc)
    pnames = {p["code"]: p["name"] for p in parents}
    for t in tests:
        v = emb.encode([T.normalise(t["narrative"])])[0]
        codes = set(t.get("l1_codes") or [])
        cand_b = {k: b for k, b in buckets.items() if not codes or b["parent"] in codes}
        scored = []
        for k, b in cand_b.items():
            near = float(np.max(b["evec"] @ v)) if len(b["evec"]) else 0.0
            scored.append((round(0.6 * near + 0.4 * float(b["dvec"] @ v), 4), k))
        scored.sort(reverse=True)
        best, runner = (scored + [(0.0, None), (0.0, None)])[:2]
        margin = round(best[0] - runner[0], 4)
        ss = T.sentences(t["narrative"])
        quote = ""
        if best[1] and ss:
            sv = emb.encode([T.normalise(s) for s in ss])
            quote = ss[int(np.argmax(sv @ buckets[best[1]]["dvec"]))]
        exc_hit = None
        if best[1]:
            b = buckets[best[1]]
            inc_sim = float(np.max(b["inc"] @ v)) if len(b["inc"]) else 0.0      # like with like: criterion text vs criterion text
            if len(b["exc"]):
                j = int(np.argmax(b["exc"] @ v))
                if float(b["exc"][j] @ v) > inc_sim:
                    exc_hit = b["exc_txt"][j]
        if not cand_b:
            verdict, prompt = "out_of_scope", f"No bucket under {', '.join(sorted(codes)) or 'any parent'} in {version}: consider a new bucket under {', '.join(sorted(codes))}."
        elif best[0] < S["test_min_score"]:
            verdict = "no_fit"
            prompt = (f"Nearest bucket {best[1]} '{buckets[best[1]]['name']}' scores {best[0]:.2f} (< {S['test_min_score']}): "
                      f"propose a new bucket under {buckets[best[1]]['parent']} ({pnames.get(buckets[best[1]]['parent'])}) or widen {best[1]}'s inclusion criteria.")
        elif exc_hit:
            verdict = "excluded"
            prompt = f"Closest bucket {best[1]} excludes it ('{exc_hit[:120]}'): route to the bucket the criterion names, or add a new bucket."
        elif runner[1] and margin < S["test_fit_margin"]:
            verdict = "ambiguous"
            prompt = f"Fits {best[1]} and {runner[1]} almost equally (margin {margin:.2f}): sharpen the exclusion criteria between them."
        else:
            verdict, prompt = "fits", None
        rows.append(dict(report_key=t["report_key"], bucket=best[1], parent=buckets[best[1]]["parent"] if best[1] else None,
                         score=best[0], runner_up=runner[1], margin=margin, verdict=verdict, quote=quote, prompt=prompt,
                         expected=t.get("_expected_bucket")))
        st.q("INSERT INTO report_test VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
             (test_id, version, t["report_key"], best[1], rows[-1]["parent"], best[0], runner[1], margin, verdict, quote, prompt, now))
    out = Path(a.out) / f"{test_id}-{version}"
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "report_test.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    with open(out / "revision_prompts.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["reviewed_run_id", "candidate_id", "action", "target_type", "target_id", "value", "rationale", "prompting_report", "suggestion"])
        for r in rows:
            if r["prompt"]:
                w.writerow([run_id, r["bucket"] or "", "", "", "", "", "", r["report_key"], r["prompt"]])
    tally = {v: sum(r["verdict"] == v for r in rows) for v in ("fits", "ambiguous", "excluded", "no_fit", "out_of_scope")}
    print(f"Tested {len(rows)} reports against {version} ({'release' if released else 'draft'} from {run_id}): {tally}")
    for r in rows:
        exp = f" (expected {r['expected']})" if r.get("expected") else ""
        print(f"  {r['report_key']:<10} {r['verdict']:<12} {r['bucket'] or '-':<5} {r['score']:.2f}{exp}" + (f"  → {r['prompt']}" if r["prompt"] else ""))
    print(f"→ {out}")


def cmd_diff(a):
    st = _store(a)
    la, lb = {}, {}
    for s, lt, o, _ in st.run_links(a.a):
        la.setdefault(s, set()).add((lt, o))
    for s, lt, o, _ in st.run_links(a.b):
        lb.setdefault(s, set()).add((lt, o))
    n = 0
    for c in sorted(set(la) | set(lb)):
        add, rem = lb.get(c, set()) - la.get(c, set()), la.get(c, set()) - lb.get(c, set())
        for x in sorted(add):
            print(f"+ {c} {x[0]}:{x[1]}"); n += 1
        for x in sorted(rem):
            print(f"- {c} {x[0]}:{x[1]}"); n += 1
    rev = st.q("SELECT candidate_id, change_type, target, cause_type, cause_ref FROM revision WHERE run_id=%s", (a.b,))
    print(f"{n} link difference(s); {len(rev)} recorded revision(s) in {a.b}")
    for r in rev:
        print(f"  {r[0]} {r[1]} {r[2]} ← {r[3]} {r[4]}")


DEFAULT_GATE = {"parent_rate_min": 0.9, "precision_min": 0.80, "recall_min": 0.80, "guardrails_all_blocked": True,
                "cards_complete": True, "sssom_complete": True, "reproducible": True}


def cmd_gate(a):
    st = _store(a)
    th = dict(DEFAULT_GATE, **(json.loads(Path(a.thresholds).read_text()) if a.thresholds else {}))
    summ = json.loads((Path(a.out) / a.run / "manifest.json").read_text())["summary"]
    res = json.loads((Path(a.out) / a.run / "grounding_results.json").read_text())["results"]
    m = summ["metrics"]
    me = st.q("SELECT input_hash, settings_hash, code_version, output_hash FROM pipeline_run WHERE run_id=%s", (a.run,))[0]
    twins = st.q("""SELECT run_id, output_hash FROM pipeline_run WHERE input_hash=%s AND settings_hash=%s AND code_version=%s
                    AND run_id <> %s AND sme_decisions = (SELECT sme_decisions FROM pipeline_run WHERE run_id=%s)""", (me[0], me[1], me[2], a.run, a.run))
    live = [r for r in res if r["status"] != "merged"]
    rows = st.q("""SELECT count(*) FILTER (WHERE subject_id IS NULL OR predicate_id IS NULL OR object_id IS NULL OR mapping_justification IS NULL
                   OR mapping_tool_version IS NULL OR (link_type='report' AND evidence_quote IS NULL)), count(*) FROM grounding_link WHERE run_id=%s""", (a.run,))[0]
    g, n = summ["guardrails_blocked"].split("/")
    checks = [
        ("Parents correct", m["parent_rate"] is None or m["parent_rate"] >= th["parent_rate_min"], f"{m['parent_correct']} (≥ {th['parent_rate_min']:.0%})"),
        ("Report precision (merge-aware)", m["merge_precision"] is None or m["merge_precision"] >= th["precision_min"], f"{m['merge_precision']} (≥ {th['precision_min']})"),
        ("Report recall (merge-aware)", m["merge_recall"] is None or m["merge_recall"] >= th["recall_min"], f"{m['merge_recall']} (≥ {th['recall_min']})"),
        ("Guardrail faults blocked", g == n and int(n) > 0, f"{g}/{n}"),
        ("Every bucket has a verified criteria card (G9)", all(any(c["id"] == "G9" and c["passed"] for c in r["checks"]) for r in live if r["status"] != "abstain"),
         f"{sum(any(c['id']=='G9' and c['passed'] for c in r['checks']) for r in live)}/{len(live)}"),
        ("SSSOM link rows complete", rows[0] == 0, f"{rows[1]} rows, {rows[0]} incomplete"),
        ("Reproducible: equal inputs, settings, code → equal output hash", bool(twins) and all(t[1] == me[3] for t in twins),
         f"{len(twins)} twin run(s): " + (", ".join(t[0] for t in twins) or "none — rerun to prove")),
    ]
    width = max(len(c[0]) for c in checks)
    for name, ok, det in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name:<{width}}  {det}")
    passed = all(c[1] for c in checks)
    (Path(a.out) / a.run / "gate.json").write_text(json.dumps([dict(check=c[0], passed=c[1], detail=c[2]) for c in checks], indent=1))
    print("GATE " + ("PASSED" if passed else "FAILED"))
    return 0 if passed else 1


def main(argv=None):
    ap = argparse.ArgumentParser(prog="taxground", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", default=os.environ.get("TAXGROUND_DB", "postgresql://grounding@localhost:5433/grounding"))
    ap.add_argument("--out", default="out")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("--data", required=True); r.add_argument("--dataset")
    r.add_argument("--selector", default="rules", choices=["rules", "llm-file", "llm-cmd"]); r.add_argument("--llm-outputs"); r.add_argument("--llm-cmd")
    r.add_argument("--model"); r.add_argument("--set", action="append", help="override a setting, e.g. --set min_support=10")
    v = sub.add_parser("review"); v.add_argument("--file", required=True); v.add_argument("--reviewer", required=True)
    rl = sub.add_parser("release"); rl.add_argument("--run", required=True); rl.add_argument("--version", required=True)
    rl.add_argument("--approver", required=True); rl.add_argument("--allow-held", action="store_true")
    t = sub.add_parser("test"); t.add_argument("--version", required=True); t.add_argument("--reports", required=True)
    d = sub.add_parser("diff"); d.add_argument("--a", required=True); d.add_argument("--b", required=True)
    g = sub.add_parser("gate"); g.add_argument("--run", required=True); g.add_argument("--thresholds")
    a = ap.parse_args(argv)
    return {"run": cmd_run, "review": cmd_review, "release": cmd_release, "test": cmd_test, "diff": cmd_diff, "gate": cmd_gate}[a.cmd](a) or 0


if __name__ == "__main__":
    sys.exit(main())

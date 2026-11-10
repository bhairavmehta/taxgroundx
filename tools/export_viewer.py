"""Export one run into the data files the Grounding Viewer reads.

  python3 tools/export_viewer.py --db DSN --run out_ntsb/<run_id> --data data/ntsb --out viewer/

Writes viewer/data/run.json (buckets, checks, cards, parent selection, guardrails, the full text of every report the
run references) and viewer/data/corpus-N.json (a compact copy of every report for the browser and Try tab).
Must run against the database the run used, while its working set is still loaded.
"""
import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from taxground import ground as G  # noqa: E402
from taxground import text as T  # noqa: E402
from taxground.store import Store  # noqa: E402

EXCERPT = 900          # characters of each report kept in the compact corpus (cause + start of the analysis)
PER_FILE = 7000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    run = Path(a.run)
    res = json.loads((run / "grounding_results.json").read_text())
    summary, S, results = res["summary"], res["settings"], res["results"]
    data = Path(a.data)
    reports = json.loads((data / "sample_reports.json").read_text())
    rmap = {r["report_key"]: r for r in reports["reports"]}
    parents = json.loads((data / "icao_categories.json").read_text())["categories"]
    defs = json.loads((data / "industry_definitions.json").read_text())["definitions"]
    occmap = json.loads((data / "occ_to_cictt.json").read_text()) if (data / "occ_to_cictt.json").exists() else None

    # parent selection: definition fit only, report vote only, combined (selected)
    st = Store(a.db)
    st.retrieval, st.lexical, st.units = S.get("retrieval", "linear"), S.get("lexical", "fts"), S.get("units", "report")
    T.NORMALISE = S.get("normalise", False)
    cands = {c["candidate_id"]: c for c in st.candidates()}
    psel = []
    for r in results:
        if r["status"] == "merged":
            continue
        c = cands[r["candidate_id"]]
        al = [cands[x] for x in r["aliases"]]
        row = dict(candidate_id=r["candidate_id"], proposed=r["proposed_parent"], selected=r["output"]["parent_code"])
        for mode in ("definition_only", "vote_only"):
            o, _ = G.ground_candidate(st, c, S, mode=mode, aliases=al)
            row[mode] = o["parent_code"]
        psel.append(row)
        print("  parent modes", row, flush=True)

    # every report the run references
    used = set()
    for r in results:
        used |= {s["report_key"] for s in r["output"]["supporting_reports"]}
        used |= {p["report_key"] for p in r["diag"].get("pool", [])}
        used |= {m["report_key"] for m in r["diag"].get("moved_to_sibling", [])}
        used |= {x["cite_id"] for x in r["card"] if x["cite_type"] == "report"}
        used |= {p["target_id"] for p in r.get("proposals", []) if p.get("target_type") == "report"}
    full = {k: dict(text=rmap[k]["narrative"], codes=rmap[k]["l1_codes"], occ=rmap[k].get("source_codes", ""),
                    event=rmap[k].get("event_id"), findings_text=rmap[k].get("findings", ""), **rmap[k].get("meta", {}))
            for k in sorted(used) if k in rmap}

    guards = list(csv.DictReader(open(run / "guardrail_tests.csv")))
    slim = []
    for r in results:
        d = r["diag"]
        slim.append(dict(
            id=r["candidate_id"], name=r["name"], definition=r["definition"], batch=r["batch"], proposed=r["proposed_parent"],
            aliases=r["aliases"], merged_into=r.get("merged_into"), status=r["status"], outcome=r["outcome"],
            parent=r["output"]["parent_code"], defs=r["output"]["definition_ids"], support=r["output"]["supporting_reports"],
            card=[{k: x.get(k) for k in ("kind", "text", "cite_type", "cite_id", "quote", "origin", "key")} for x in r["card"]],
            checks=r["checks"], agent=[dict(tool=x["tool"], args=x["args"]) for x in r.get("agent_calls", [])],
            proposals=r.get("proposals", []),
            diag=dict(parent_scores=d.get("parent_scores"), agreement=d.get("parent_agreement"), margin=d.get("margin"),
                      runner_up=d.get("runner_up"), co_codes=d.get("co_codes"), pool=d.get("pool"),
                      moved=d.get("moved_to_sibling"), support_scores={s["report_key"]: s["score"] for s in d.get("support", [])},
                      support_chunks={s["report_key"]: s.get("chunk") for s in d.get("support", [])},
                      def_scores={x["def_id"]: x["score"] for x in d.get("definitions", [])}, merge_score=d.get("merge_score"))))
    out = Path(a.out) / "data"
    out.mkdir(parents=True, exist_ok=True)
    by_code = {}
    for r in reports["reports"]:
        for c in r["l1_codes"]:
            by_code[c] = by_code.get(c, 0) + 1
    bundle = dict(summary=summary, settings=S, note=reports.get("_note"), mapping=occmap,
                  parents=[dict(code=p["code"], name=p["name"], definition=p["definition"], in_scope=p["in_scope"],
                                co_code_only=p.get("co_code_only", False), reports=by_code.get(p["code"], 0)) for p in parents],
                  definitions=[dict(id=d["id"], term=d["term"], source=d["source"], text=d["text"], parents=d["parents"]) for d in defs],
                  buckets=slim, parent_selection=psel, guardrails=guards, reports=full,
                  corpus=dict(total=len(reports["reports"]), files=[], excerpt=EXCERPT))
    rows = []
    for r in reports["reports"]:
        m = r.get("meta", {})
        rows.append([r["report_key"], m.get("date", ""), m.get("make", ""), m.get("model", ""), m.get("part", ""),
                     m.get("injury", ""), r["l1_codes"], m.get("defining", ""), r["narrative"][:EXCERPT], r.get("event_id")])
    for i in range(0, len(rows), PER_FILE):
        name = f"corpus-{i // PER_FILE + 1}.json"
        (out / name).write_text(json.dumps(dict(cols=["key", "date", "make", "model", "part", "injury", "codes", "defining", "text", "event", "findings"],
                                                rows=rows[i:i + PER_FILE]), separators=(",", ":")))
        bundle["corpus"]["files"].append(f"data/{name}")
    (out / "run.json").write_text(json.dumps(bundle, separators=(",", ":"), default=str))
    print(f"run.json {(out / 'run.json').stat().st_size / 1e6:.1f} MB · {len(full)} full reports · "
          f"{len(bundle['corpus']['files'])} corpus files · {len(psel)} parent-selection rows")


if __name__ == "__main__":
    main()

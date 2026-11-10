"""Combine the package candidates with extra discovery batches into the run's candidates.json.
  python3 tools/merge_candidates.py --base data/ntsb/candidates_package.json --add data/discovery/ntsb_batch_d.json --out data/ntsb/candidates.json"""
import argparse, json, pathlib
ap = argparse.ArgumentParser(); ap.add_argument("--base", required=True); ap.add_argument("--add", nargs="*", default=[]); ap.add_argument("--out", required=True)
a = ap.parse_args()
base = json.loads(pathlib.Path(a.base).read_text()); cands = list(base["candidates"]); notes = [base.get("_note", "")]
seen = {c["candidate_id"] for c in cands}
for f in a.add:
    extra = json.loads(pathlib.Path(f).read_text())
    for c in extra["candidates"]:
        if c["candidate_id"] in seen:
            raise SystemExit(f"duplicate candidate id {c['candidate_id']} in {f}")
        seen.add(c["candidate_id"]); cands.append(c)
    notes.append(extra.get("_note", ""))
pathlib.Path(a.out).write_text(json.dumps(dict(_note=" ".join(n for n in notes if n), candidates=cands), indent=1))
print(a.out, len(cands), "candidates")

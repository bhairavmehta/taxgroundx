"""Build a report-testing file (SRS-TAX-04) from the ingested NTSB reports.

  python3 tools/make_test_reports.py --data data/ntsb --out build/test_reports.json [--holdout-from 2026-01-01] [--n 200]

With --holdout-from, every report dated on or after that day is MOVED out of data/ntsb/sample_reports.json into the
test file, so the taxonomy is built without them and they are genuinely new when tested (run this before grounding).
Without it, the n most recent reports are copied as a smoke test: they were part of the corpus, so the verdicts show
the test machinery working, not generalisation.
"""
import argparse
import json
import pathlib


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--holdout-from")
    ap.add_argument("--n", type=int, default=200)
    a = ap.parse_args()
    src = pathlib.Path(a.data) / "sample_reports.json"
    doc = json.loads(src.read_text())
    reps = doc["reports"]
    date = lambda r: (r.get("meta") or {}).get("date") or ""
    if a.holdout_from:
        test = [r for r in reps if date(r) >= a.holdout_from]
        keep = [r for r in reps if date(r) < a.holdout_from]
        doc["reports"] = keep
        doc["_holdout"] = dict(from_date=a.holdout_from, held_out=len(test))
        src.write_text(json.dumps(doc))
        note = f"Hold-out: {len(test)} NTSB reports dated {a.holdout_from} or later, removed from the grounding corpus."
    else:
        test = sorted(reps, key=date, reverse=True)[:a.n]
        note = f"Smoke test: the {len(test)} most recent NTSB reports, which are also in the grounding corpus."
    rows = [dict(report_key=r["report_key"], source_id=r.get("source_id"), phase=r.get("phase"), l1_codes=r["l1_codes"],
                 narrative=r["narrative"] + ("\n" + r["findings"] if r.get("findings") else "")) for r in test]
    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(dict(_note=note, reports=rows), indent=1))
    print(out, note)


if __name__ == "__main__":
    main()

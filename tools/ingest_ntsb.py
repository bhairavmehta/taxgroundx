"""Turn the NTSB avall.mdb (CAROL download) into taxground inputs.

  mdb-export avall.mdb <table> > <table>.csv   for events, aircraft, narratives, Findings, Events_Sequence
  python3 tools/ingest_ntsb.py --csv DIR --out data/ntsb [--from-year 2008] [--candidates data/combined/candidates.json]

One report per aircraft record (report_key = NTSB number, plus '/2' for the second aircraft of an event), so
multi-aircraft events share an event_id and count once in G5. Report text = probable cause + analysis narrative,
kept raw. Stage-2 Level 1 codes come from the record's occurrences (Events_Sequence) through OCC_TO_CICTT below:
our own mapping, versioned here, pending SME validation (no official NTSB-occurrence-to-CICTT crosswalk was found).
Answer-key fields are never produced: there is no answer key for real data.
"""
import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

csv.field_size_limit(10 ** 9)
MAPPING_VERSION = "ntsb-occ-cictt-0.1 (draft, pending SME validation)"

# NTSB occurrence (eventsoe_no) -> CICTT Level 1. None = no category of its own (a consequence or a step).
OCC_TO_CICTT = {
    "000": "UNK", "010": "OTHR", "020": "OTHR", "030": "OTHR", "040": "OTHR", "050": "OTHR", "060": None,
    "070": "ADRM", "080": "RAMP", "081": "RAMP", "082": "RAMP",
    "090": "ARC", "091": "ARC", "092": "ARC", "093": "ARC", "094": "SCF-NP", "095": "ARC", "096": "LOC-G", "097": "LOC-G",
    "100": "ATM", "110": "CABIN", "120": "CFIT", "130": None, "140": "SCF-PP",
    "150": "F-NI", "160": "F-NI", "170": "F-POST", "180": "F-POST",
    "190": "FUEL", "191": "FUEL", "192": "FUEL", "193": "FUEL", "194": "FUEL",
    "200": "GCOL", "210": "ICE", "220": "LALT",
    "230": "LOC-G", "231": "LOC-G", "232": "LOC-G",
    "240": "LOC-I", "241": "LOC-I", "242": "LOC-I", "243": "LOC-I", "244": "LOC-I", "245": "LOC-I",
    "250": "MAC", "260": "MAC", "270": "LOC-I", "271": "LOC-I",
    "280": "NAV", "281": "NAV", "282": "NAV", "283": "NAV", "284": "RI",
    "300": "RE", "310": "WILD", "320": "RI", "330": "SCF-NP",
    "331": "SCF-NP", "332": "SCF-NP", "333": "SCF-NP", "334": "SCF-NP", "335": "SCF-NP", "336": "SCF-NP", "337": "SCF-NP", "338": "SCF-NP",
    "340": "SCF-PP", "341": "SCF-PP", "342": "SCF-PP", "343": "SCF-PP", "350": "SEC",
    "360": "TURB", "361": "TURB", "362": "TURB", "370": "USOS", "380": "RE", "390": "WSTRW", "400": "OTHR",
    "401": "UIMC", "402": "UIMC", "410": "CFIT", "420": "MAC", "430": "LOC-I", "440": None, "441": None,
    "450": "OTHR", "460": "EVAC", "470": "CTOL", "480": "EXTL", "490": "CTOL", "500": "LOC-I", "510": "OTHR",
    "600": "OTHR", "850": "MED", "900": "OTHR", "901": "BIRD", "990": "UNK",
}
CONSEQUENCE_ONLY = {"470", "170", "180"}       # impact and post-impact fire/explosion
# CICTT categories that the NTSB data adds to the trial's parent list (definitions paraphrased from CICTT).
EXTRA_PARENTS = [
    ("LOC-G", "Loss of Control – Ground", "Loss of aircraft control while the aircraft is on the ground, such as a ground loop, nose-over or directional control loss during takeoff or landing roll."),
    ("GCOL", "Ground Collision", "Collision while taxiing to or from a runway in use, with another aircraft, a vehicle, a person or an obstacle."),
    ("CTOL", "Collision with Obstacle(s) During Takeoff and Landing", "Collision with an obstacle during takeoff or landing while airborne, such as trees, wires or terrain near the runway."),
    ("LALT", "Low Altitude Operations", "Collision or near collision with obstacles or terrain while intentionally operating near the surface, excluding takeoff and landing."),
    ("F-POST", "Fire/Smoke (Post-Impact)", "Fire or smoke resulting from impact."),
    ("UIMC", "Unintended Flight in IMC", "Continued visual flight into instrument meteorological conditions, or loss of visual reference."),
    ("WILD", "Collision with Wildlife", "Collision with an animal other than a bird on the ground or in the air."),
    ("SEC", "Security Related", "Criminal or security acts such as hijacking, sabotage or laser attack."),
    ("EVAC", "Evacuation", "An evacuation with injuries, an unnecessary evacuation, or an evacuation hampered by equipment or procedures."),
    ("MED", "Medical", "Illness or incapacitation of a crew member or passenger."),
    ("EXTL", "External Load Related Occurrences", "Occurrences during or as a result of external load or sling operations."),
    ("ADRM", "Aerodrome", "Occurrences involving aerodrome design, service or functionality issues."),
    ("UNK", "Unknown or Undetermined", "Insufficient information exists to categorize the occurrence."),
]


def read(dirp, name):
    with open(Path(dirp) / f"{name}.csv", encoding="utf-8", errors="replace", newline="") as f:
        return list(csv.DictReader(f))


def iso(d):
    m = re.match(r"(\d{2})/(\d{2})/(\d{2})", d or "")
    return f"20{m.group(3)}-{m.group(1)}-{m.group(2)}" if m else ""


def clean(t):
    return re.sub(r"\s+", " ", (t or "").replace("\r", " ")).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--from-year", type=int, default=2008)
    ap.add_argument("--candidates", default=str(Path(__file__).resolve().parents[1] / "data" / "combined" / "candidates.json"))
    ap.add_argument("--base", default=str(Path(__file__).resolve().parents[1] / "data" / "combined"))
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)

    events = {e["ev_id"]: e for e in read(a.csv, "events") if e["ev_year"] and int(e["ev_year"]) >= a.from_year}
    acft = {(x["ev_id"], x["Aircraft_Key"]): x for x in read(a.csv, "aircraft") if x["ev_id"] in events}
    occ = defaultdict(list)
    for x in read(a.csv, "Events_Sequence"):
        if x["ev_id"] in events:
            occ[(x["ev_id"], x["Aircraft_Key"])].append(x)
    find = defaultdict(list)
    for x in read(a.csv, "Findings"):
        if x["ev_id"] in events:
            find[(x["ev_id"], x["Aircraft_Key"])].append(x)
    reports, skipped = [], defaultdict(int)
    for n in read(a.csv, "narratives"):
        k = (n["ev_id"], n["Aircraft_Key"])
        if n["ev_id"] not in events:
            continue
        cause, anal = clean(n["narr_cause"]), clean(n["narr_accp"])
        if anal.lower() == "import":
            anal = ""
        if not cause and not anal:
            skipped["no narrative"] += 1
            continue
        e, ac = events[n["ev_id"]], acft.get(k, {})
        seq = sorted(occ.get(k, []), key=lambda x: int(x["Occurrence_No"] or 0))
        codes, defining = [], None
        for s in seq:
            c = OCC_TO_CICTT.get(s["eventsoe_no"])
            # impact with terrain/object (470) closes most accident sequences: a category only when it defines the event
            if s["eventsoe_no"] in CONSEQUENCE_ONLY and s["Defining_ev"] != "1":
                c = None
            if s["Defining_ev"] == "1":
                defining = dict(code=s["eventsoe_no"], text=s["Occurrence_Description"].strip(), cictt=c)
            if c and c not in codes:
                codes.append(c)
        if defining and defining["cictt"] in codes:            # defining event's category first
            codes.remove(defining["cictt"]); codes.insert(0, defining["cictt"])
        if not codes:
            skipped["no mappable occurrence"] += 1
            continue
        phase = (defining or {}).get("text", "").split(" ")[0] if defining else ""
        fs = sorted(find.get(k, []), key=lambda x: int(x["finding_no"] or 0))
        findings = "; ".join(f"({x['Cause_Factor'] or '-'}) {clean(x['finding_description'])}" for x in fs)
        # coded findings verbalized as their own raw section: cause (C) and contributing factor (F)
        kind = {"C": "Cause", "F": "Contributing factor"}
        findings_text = " ".join(f"{kind.get(x['Cause_Factor'], 'Finding')}: {re.sub(r'\s+-\s+[CF]$', '', clean(x['finding_description']))}."
                                 for x in fs)
        text = (f"Probable cause: {cause} " if cause else "") + anal
        key = e["ntsb_no"] + ("" if n["Aircraft_Key"] == "1" else f"/{n['Aircraft_Key']}")
        reports.append(dict(
            report_key=key, source_id="NTSB-CAROL", event_id=n["ev_id"], phase=phase, l1_codes=codes,
            source_codes="; ".join(f"{s['eventsoe_no']} {s['Occurrence_Description'].strip()}" for s in seq),
            narrative=text.strip(), findings=findings_text,
            sections=dict(summary=(f"Probable cause: {cause}" if cause else ""), analysis=anal),
            meta=dict(date=iso(e["ev_date"]), city=e["ev_city"], state=e["ev_state"], country=e["ev_country"],
                      injury=e["ev_highest_injury"], make=clean(ac.get("acft_make")), model=clean(ac.get("acft_model")),
                      part=ac.get("far_part", ""), category=ac.get("acft_category", ""), damage=ac.get("damage", ""),
                      defining=(defining or {}).get("text", ""), findings=findings[:1500])))
    reports.sort(key=lambda r: r["report_key"])

    base = Path(a.base)
    cats = json.loads((base / "icao_categories.json").read_text())["categories"]
    have = {c["code"] for c in cats}
    for code, name, d in EXTRA_PARENTS:
        if code not in have:
            cats.append(dict(code=code, name=name, in_scope=code != "UNK", definition=d,
                             team_note="Added for NTSB data; definition paraphrased from CICTT."))
    for c in cats:
        if c["code"] == "OTHR":
            c["in_scope"] = False
    defs = json.loads((base / "industry_definitions.json").read_text())
    cands = json.loads(Path(a.candidates).read_text())
    for c in cands["candidates"]:
        for k in ("expected_parent", "expected_reports", "overlaps"):
            c.pop(k, None)
    note = (f"NTSB CAROL avall.mdb, events {a.from_year} onward. Real reports. L1 codes via {MAPPING_VERSION}. "
            f"Definitions are paraphrases; candidates are the 37 discovery candidates from the trial package.")
    (out / "sample_reports.json").write_text(json.dumps(dict(_note=note, mapping_version=MAPPING_VERSION, reports=reports)))
    (out / "icao_categories.json").write_text(json.dumps(dict(_note=note, categories=cats), indent=1))
    (out / "industry_definitions.json").write_text(json.dumps(dict(defs, _note=note), indent=1))
    (out / "candidates.json").write_text(json.dumps(dict(_note=note, candidates=cands["candidates"]), indent=1))
    (out / "occ_to_cictt.json").write_text(json.dumps(dict(version=MAPPING_VERSION, mapping=OCC_TO_CICTT), indent=1))
    print(f"{len(reports)} reports from {len(events)} events; skipped {dict(skipped)}; {len(cats)} parents")


if __name__ == "__main__":
    main()

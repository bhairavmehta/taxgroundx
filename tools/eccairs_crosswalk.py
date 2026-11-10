"""Crosswalk ECCAIRS 1.3.0.12 events (attribute 390) to CICTT Level 1 parents and add them as industry definitions.

  python3 tools/eccairs_crosswalk.py --events data/eccairs_events.json --defs data/ntsb/industry_definitions.json

Rules are matched in order against an event's own name and its path in the ECCAIRS hierarchy; every matching rule
adds its parent, so an event can map to several. Events no rule matches are left out (not applicable). The crosswalk
is ours, versioned below, and needs SME approval (I-8) like the rest of the crosswalk.
"""
import argparse
import json
import re

VERSION = "eccairs390-cictt-0.2"
# (field, regex, parents). field: name = the event's own name; path = any level of its ECCAIRS path
RULES = [
    ("path", r"incursions generally|runway incursion", ["RI"]),
    ("name", r"wrong runway|wrong (taxiway|surface)|take-?off from (a )?taxiway|landing on (a )?taxiway", ["RI"]),
    ("name", r"excursion|veer[- ]?off|overrun|aircraft off movement area", ["RE"]),
    ("path", r"aircraft off movement area", ["RE"]),
    ("name", r"hard landing|tail ?strike|abnormal runway contact|heavy landing|landing gear up landing|wheels-?up", ["ARC"]),
    ("name", r"loss of control.*ground|ground loop|nose ?over|dynamic rollover|ground resonance", ["LOC-G"]),
    ("name", r"loss of control|stall|spin\b|upset|unusual attitude|loss of lift", ["LOC-I"]),
    ("name", r"airprox|near (mid-?air )?collision|separation|acas|tcas|mid-?air|collision avoidance", ["MAC"]),
    ("name", r"turbulence|wake vortex|wake turbulence", ["TURB"]),
    ("name", r"wind ?shear|thunderstorm|microburst", ["WSTRW"]),
    ("name", r"\bicing\b|ice accretion|airframe ic|frost|de-?icing|anti-?icing", ["ICE"]),
    ("name", r"\bbird", ["BIRD"]),
    ("name", r"animal|wildlife strike", ["WILD"]),
    ("name", r"controlled flight into terrain|\bcfit\b|terrain (awareness|warning)|gpws|taws", ["CFIT"]),
    ("path", r"cabin safety", ["CABIN"]),
    ("name", r"unruly|disruptive passenger|passenger injur|cabin crew injur|turbulence injur", ["CABIN"]),
    ("name", r"post-?impact fire|fire after impact", ["F-POST"]),
    ("name", r"\bfire\b|smoke|fumes|burning smell|overheat", ["F-NI"]),
    ("name", r"fuel (exhaustion|starvation|contamination|quantity|low|management|planning)|low fuel|minimum fuel|fuel emergency|wrong fuel", ["FUEL"]),
    ("path", r"ground handling", ["RAMP"]),
    ("name", r"push-?back|towing|towed aircraft|loading|de-?boarding|refuel", ["RAMP"]),
    ("name", r"undershoot|landing short|short of the runway", ["USOS"]),
    ("name", r"collision with obstacle|collision with terrain|obstacle collision|wire strike|tree", ["CTOL"]),
    ("name", r"ground collision|collision while taxi|taxi.*collision|vehicle.*collision|collision.*vehicle", ["GCOL"]),
    ("name", r"low (altitude|flying)|flight below minimum", ["LALT"]),
    # airborne strikes of wires, tall structures and trees happen mostly in intentional low flight (CICTT LALT)
    ("name", r"power line|cable or wire|\bwires?\b|tall structure|tree/tall vegetation", ["LALT"]),
    ("name", r"\bimc\b|instrument meteorological|loss of visual reference|vfr into", ["UIMC"]),
    ("name", r"evacuation", ["EVAC"]),
    ("name", r"medical|incapacitat|illness", ["MED"]),
    ("name", r"sabotage|unlawful|security|bomb|hijack|laser|interference with aircraft from the ground", ["SEC"]),
    ("name", r"external load|sling", ["EXTL"]),
    ("path", r"aircraft navigation", ["NAV"]),
    ("name", r"altitude deviation|level bust|route deviation|navigation error|position error|gnss|gps", ["NAV"]),
    ("path", r"aerodrome & ground aids", ["ADRM"]),
    ("path", r"air navigation services", ["ATM"]),
]
ENGINE_ATA = re.compile(r"^(61|7[1-9]|8[0-5])00\b")   # propellers and powerplant chapters


def parents_for(e):
    found = []
    for field, rx, ps in RULES:
        hay = e["name"] + " " + e["short"] if field == "name" else " / ".join(e["path"])
        if re.search(rx, hay, re.I):
            found += [p for p in ps if p not in found]
    top = e["path"][0].lower()
    if top.startswith("aircraft/system/component") and len(e["path"]) >= 2:
        ata = e["path"][1]
        p = "SCF-PP" if ENGINE_ATA.match(ata) else "SCF-NP"
        if not found or found == ["F-NI"]:
            found.append(p)
    if top == "unknown":
        found = ["UNK"]
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", required=True)
    ap.add_argument("--defs", required=True)
    a = ap.parse_args()
    ev = json.load(open(a.events))
    defs = json.load(open(a.defs))
    keep = [d for d in defs["definitions"] if not d["id"].startswith("ECC-")]
    added, by_parent = 0, {}
    for e in ev["events"]:
        if not e["definition"] or e["level"] == 1:
            continue
        ps = parents_for(e)
        if not ps:
            continue
        keep.append(dict(id=f"ECC-{e['code']}", source=f"ECCAIRS 1.3.0.12 · Events (390) · {e['code']} · {' › '.join(e['path'][:-1])}",
                         term=e["name"], parents=ps, text=e["definition"]))
        added += 1
        for p in ps:
            by_parent[p] = by_parent.get(p, 0) + 1
    defs["definitions"] = keep
    defs["eccairs_crosswalk_version"] = VERSION
    json.dump(defs, open(a.defs, "w"), indent=1)
    print(f"added {added} ECCAIRS definitions ({len(keep)} total); per parent: {dict(sorted(by_parent.items()))}")


if __name__ == "__main__":
    main()

"""Text handling: sentence split, normalisation for retrieval, record routing and validation.

Rule from the embedding study: raw text stays the citation source of truth. Normalisation only feeds
retrieval (vectors and keyword index); evidence quotes are always taken from, and checked against, raw text.
"""
import re

STOP = set("""a an the and or of to in on at for from by with without is are was were be been it its this that
than then as into over under after before during other such any all not no can may per their there which while
we our they he she his her them who whom also had has have did do does about out up down off very just only
""".split())

# ASRS / NTSB shorthand -> words. Indexed alongside the raw form (deck: "index both forms").
ABBREV = {
    "rwy": "runway", "rwys": "runways", "twy": "taxiway", "twys": "taxiways", "fo": "first officer",
    "capt": "captain", "acft": "aircraft", "clrd": "cleared", "clnc": "clearance", "apch": "approach",
    "dep": "departure", "arr": "arrival", "tkof": "takeoff", "ldg": "landing", "alt": "altitude",
    "hdg": "heading", "wx": "weather", "pax": "passengers", "ft": "feet", "kts": "knots", "nm": "nautical miles",
    "fa": "flight attendant", "ias": "indicated airspeed", "tcas": "tcas traffic collision avoidance",
    "ra": "resolution advisory", "ta": "traffic advisory", "gpws": "gpws ground proximity warning",
    "egpws": "egpws terrain warning", "fms": "fms flight management system", "atc": "atc air traffic control",
    "notam": "notam notice", "apu": "auxiliary power unit", "rto": "rejected takeoff", "ga": "go-around",
}
BOILERPLATE = [
    r"This report is based on .*? NTSB\.?",                       # NTSB disclaimer family (real extracts)
    r"The NTSB did not travel to the scene of this accident\.?",
]


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]


NORMALISE = True


def normalise(text):
    """Lower-case, strip boilerplate, expand shorthand. Used only for retrieval."""
    if not NORMALISE:
        return text
    if NORMALISE == "append":        # index both forms: raw text plus the expansions of any shorthand found
        extra = [ABBREV[w.lower()] for w in re.findall(r"[A-Za-z]+", text) if w.lower() in ABBREV and (w.isupper() or w.islower())]
        return text + (" " + " ".join(dict.fromkeys(extra)) if extra else "")
    t = text
    for pat in BOILERPLATE:
        t = re.sub(pat, " ", t, flags=re.I | re.S)
    out = []
    for tok in re.findall(r"[A-Za-z0-9][A-Za-z0-9\-']*(?:[.,]\d+)?|[^\sA-Za-z\d]", t):
        low = tok.lower()
        out.append(ABBREV.get(low, low) if low in ABBREV and (tok.isupper() or tok.islower()) else low)
    return re.sub(r"\s+([.,;:!?])", r"\1", " ".join(out)).strip()


def content_words(text):
    return [w for w in re.findall(r"[a-z][a-z\-]+", normalise(text)) if w not in STOP and len(w) > 2]


def stem(w):
    for suf in ("ings", "ing", "ies", "ied", "es", "ed", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: -len(suf)]
    return w


def keyword_query(text):
    words = sorted(set(w.replace("-", "") for w in content_words(text)))
    return " | ".join(words) if words else "none"


def is_shorthand(text):
    toks = re.findall(r"[A-Za-z]+", text)
    hits = sum(1 for t in toks if t.lower() in ABBREV and t.lower() not in ("atc", "tcas", "ft"))
    return hits >= 2


INJECTION = re.compile(r"ignore (all |any )?(previous|prior|above) (instructions|context)|disregard (the|all) (above|previous)|"
                       r"system prompt|you are now|<\\s*script|\\bassistant:|\\bBEGIN INSTRUCTIONS\\b", re.I)


def route_report(r):
    """Assign a routing lane and evidence level (deck: 'route every record before embedding it').

    Lanes: narrative (full text) · shorthand (ASRS-style, expanded before indexing) · notification
    (foreign/notice record, mostly template: never support) · thin (too short to quote a cause from).
    """
    words = len(re.findall(r"\w+", r.get("narrative", "")))
    key = r.get("report_key", "")
    if INJECTION.search(r.get("narrative", "")):          # control layer 1: scan at ingest, never quote from it
        return "quarantined", "none"
    if re.match(r"^[A-Z]{3}\d{2}WA\d+", key) or r.get("record_type") == "notification":
        return "notification", "none"
    if words < 12:
        return "thin", "thin"
    if is_shorthand(r["narrative"]):
        return "shorthand", "full"
    return "narrative", "full"


def validate_inputs(parents, definitions, reports, candidates):
    """Validate every record (NFR-QAL-01). Returns (clean reports, clean candidates, issues).
    Fields starting with '_' (e.g. the synthetic answer key '_truth') are removed so they never reach the pipeline."""
    issues = []
    codes = {p["code"] for p in parents}
    def_ids = set()
    for d in definitions:
        if d["id"] in def_ids:
            issues.append(("definition", d["id"], "duplicate id"))
        def_ids.add(d["id"])
        bad = [p for p in d["parents"] if p not in codes]
        if bad:
            issues.append(("definition", d["id"], f"crosswalk to unknown parent {bad}"))
    clean_r, seen = [], set()
    for r in reports:
        r = {k: v for k, v in r.items() if not k.startswith("_")}
        k = r.get("report_key")
        if not k or k in seen:
            issues.append(("report", k, "missing or duplicate report_key")); continue
        if not r.get("narrative", "").strip():
            issues.append(("report", k, "empty narrative")); continue
        unknown = [c for c in r.get("l1_codes", []) if c not in codes]
        if unknown:
            issues.append(("report", k, f"unknown L1 codes {unknown} (dropped)"))
            r["l1_codes"] = [c for c in r["l1_codes"] if c in codes]
        seen.add(k)
        clean_r.append(r)
    clean_c, seen = [], set()
    for c in candidates:
        c = {k: v for k, v in c.items()}
        if c["candidate_id"] in seen:
            issues.append(("candidate", c["candidate_id"], "duplicate id")); continue
        seen.add(c["candidate_id"])
        if c.get("proposed_parent") and c["proposed_parent"] not in codes:
            issues.append(("candidate", c["candidate_id"], f"proposed parent {c['proposed_parent']} unknown"))
        c.setdefault("batch", re.match(r"[A-Za-z]+", c["candidate_id"]).group(0))
        clean_c.append(c)
    return clean_r, clean_c, issues

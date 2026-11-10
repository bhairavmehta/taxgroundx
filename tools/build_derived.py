"""Collect every derived table, estimate and statistic of a run into one folder, with lineage, and a workbook.

  python3 tools/build_derived.py --run out_ntsb/run-... [--test out_ntsb/test-...] [--data data/ntsb]
      [--techniques viewer/data/techniques.json] [--clusters build/discovery_clusters.json]
      [--synthetic build/synthetic] [--history out_ntsb_rep out_ntsb] [--csv build/csv] [--out derived]

Writes derived/<run_id>/:
  csv/<NN_table>.csv      one file per table, the same rows as the workbook tab
  lineage.json            for each table: the source files (path, sha256), the generator, row count
  derived_workbook.xlsx   Index tab with hyperlinks and lineage, then one tab per table; summary figures are formulas
  README.md               how the folder was made and how to rebuild it
Every row carries trace columns: run_id and source (file plus locator, e.g. grounding_results.json#results[7].diag.support[2]).
"""
import argparse, collections, csv, datetime as dt, hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


# ---------------------------------------------------------------- manufacturer and root type (same rules as the viewer)
CORP = set("INC INCORPORATED CORP CORPORATION CO COMPANY LLC LTD LIMITED GMBH SA AG PLC AIRCRAFT AIRCRAFTS AIRPLANE AIRPLANES ACFT IND "
           "INDUSTRIES INDUSTRIE MFG MANUFACTURING HELICOPTER HELICOPTERS AVN AVIATION DESIGN TEXTRON CANADA INTERNATIONAL INTL DIV DIVISION OF THE".split())
MAKES = [["CESSNA"], ["PIPER", "NEW PIPER"], ["BEECH", "BEECHCRAFT"], ["BOEING", "THE BOEING"], ["AIRBUS"], ["BELL"], ["CIRRUS"], ["MOONEY"], ["AIR TRACTOR"], ["ROBINSON"],
         ["DE HAVILLAND", "DEHAVILLAND", "DHC"], ["GRUMMAN", "GRUMMAN AMERICAN"], ["DIAMOND"], ["AVIAT"], ["BOMBARDIER", "CANADAIR"], ["EMBRAER"], ["EUROCOPTER"], ["SIKORSKY"],
         ["MD HELICOPTERS", "MD HELICOPTER", "MCDONNELL DOUGLAS HELICOPTER"], ["MCDONNELL DOUGLAS"], ["AMERICAN CHAMPION"], ["CHAMPION"], ["SCHWEIZER"], ["HUGHES"], ["ENSTROM"],
         ["VANS", "VAN'S"], ["AEROSPATIALE"], ["SOCATA"], ["MAULE"], ["AERONCA"], ["LUSCOMBE"], ["STINSON"], ["TAYLORCRAFT"], ["BELLANCA"], ["ERCOUPE"], ["AYRES"], ["LANCAIR"],
         ["TECNAM", "COSTRUZIONI AERONAUTICHE TECNA"], ["FLIGHT DESIGN"], ["ZENITH"], ["RANS"], ["ROCKWELL"], ["RAYTHEON"], ["NORTH AMERICAN"]]
MAKE_KEY = sorted([(re.sub(r"[^A-Z]", "", v), c, re.sub(r"\s+", " ", v.replace("'", " "))) for c, *al in MAKES for v in [c] + al], key=lambda x: -len(x[2]))


def norm_make(m):
    w = [x for x in re.sub(r"[^A-Z0-9 ]+", " ", (m or "").upper()).split() if x]
    while len(w) > 1 and w[0] == "THE":
        w.pop(0)
    raw = " ".join(w)
    while len(w) > 1 and w[-1] in CORP:
        w.pop()
    cut = " ".join(w)
    for t in (raw, cut):
        for k, c, a in MAKE_KEY:
            if t == a or t.startswith(a + " ") or t.replace(" ", "") == k:
                return c
    return cut or "UNKNOWN"


def type_root(m):
    t = re.sub(r"^(CESSNA|PIPER|BOEING|ROBINSON|AIRBUS|BELL|BEECH|MOONEY|CIRRUS)\s+", "", (m or "").upper()).strip()
    parts = [p for p in re.split(r"[\s\-/(.,]+", t) if p]
    if not parts:
        return "—"
    h = parts[0]
    if re.fullmatch(r"[A-Z]+", h) and len(parts) > 1 and parts[1][:1].isdigit():
        h += parts[1]
    if re.match(r"^B7\d\d", h):
        h = h[1:]
    f = re.match(r"^[A-Z]*\d+", h)
    return f.group(0) if f else h[:8]


# ---------------------------------------------------------------- helpers
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def rel(p):
    try:
        return str(pathlib.Path(p).resolve().relative_to(ROOT))
    except ValueError:
        return str(p)


class F:
    """A formula cell: the workbook gets the live formula, the CSV gets the value computed here (and the two are compared after recalculation)."""
    def __init__(self, formula, value):
        self.formula, self.value = formula, value


class Book:
    """Tables in order; each has columns, rows, a description, its sources and optional formula summary rows."""
    def __init__(self, run_id):
        self.run_id, self.tables = run_id, []

    def add(self, name, desc, cols, rows, sources, generator, widths=None, wrap=(), summary=None, fmt=None):
        self.tables.append(dict(name=name, desc=desc, cols=cols, rows=rows, sources=[s for s in sources if s],
                                generator=generator, widths=widths or {}, wrap=set(wrap), summary=summary or [], fmt=fmt or {}))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--test")
    ap.add_argument("--data", default="data/ntsb")
    ap.add_argument("--techniques", default="viewer/data/techniques.json")
    ap.add_argument("--clusters")
    ap.add_argument("--synthetic")
    ap.add_argument("--history", nargs="*", default=[], help="folders that hold earlier run-* folders")
    ap.add_argument("--csv", help="NTSB CSV export folder (for occurrence-code meanings)")
    ap.add_argument("--eccairs", default="data/eccairs_events.json")
    ap.add_argument("--viewer-run", default="viewer/data/run.json", help="viewer export, for the three-way parent selection")
    ap.add_argument("--out", default="derived")
    a = ap.parse_args()

    run = pathlib.Path(a.run)
    G = json.loads((run / "grounding_results.json").read_text())
    S = G["summary"]
    RID = S["run_id"]
    out = pathlib.Path(a.out) / RID
    (out / "csv").mkdir(parents=True, exist_ok=True)
    bk = Book(RID)
    gr = run / "grounding_results.json"
    inp = run / "inputs"
    reports = json.loads((inp / "sample_reports.json").read_text())["reports"]
    R = {r["report_key"]: r for r in reports}
    cands = json.loads((inp / "candidates.json").read_text())["candidates"]
    defs = json.loads((inp / "industry_definitions.json").read_text())
    cats = json.loads((inp / "icao_categories.json").read_text())["categories"]
    res = G["results"]

    def rmeta(k):
        r = R.get(k) or {}
        m = r.get("meta") or {}
        return dict(date=m.get("date", ""), make=m.get("make", ""), model=m.get("model", ""), mk=norm_make(m.get("make")), ty=type_root(m.get("model")),
                    part=(m.get("part") or "").lstrip("0"), injury=m.get("injury", ""), codes=" ".join(r.get("l1_codes", [])), event=r.get("event_id", ""))

    # 01 run summary ------------------------------------------------------------------------------
    rows = [["Run id", RID, "manifest.json#summary.run_id"], ["Dataset", S.get("dataset"), "summary.dataset"],
            ["Taxonomy version", S.get("taxonomy_version"), "summary.taxonomy_version"], ["Output hash", S.get("output_hash"), "summary.output_hash"],
            ["Input hash", S.get("input_hash"), "summary.input_hash"], ["Settings hash", S.get("settings_hash"), "summary.settings_hash"],
            ["Code version", S.get("code_version"), "summary.code_version"], ["Selector", S.get("selector"), "summary.selector"],
            ["Embedder", S.get("embedder"), "summary.embedder"], ["Prompt version", S.get("prompt_version"), "summary.prompt_version"],
            ["Previous run", S.get("previous_run"), "summary.previous_run"], ["SME decisions read", S.get("sme_decisions_read"), "summary.sme_decisions_read"],
            ["Guardrails blocked", S.get("guardrails_blocked"), "summary.guardrails_blocked"], ["Revisions vs previous run", S.get("revisions"), "summary.revisions"],
            ["Validation issues", S.get("validation_issues"), "summary.validation_issues"]]
    rows += [[f"Routing lane: {k}", v, f"summary.routing.{k}"] for k, v in (S.get("routing") or {}).items()]
    rows += [[f"Setting: {k}", v if not isinstance(v, bool) else str(v).lower(), f"settings.{k}"] for k, v in G["settings"].items()]
    rows += [[f"Input file: {k}", v, "manifest.json#inputs.files (sha256)"] for k, v in json.loads((run / "manifest.json").read_text())["inputs"]["files"].items()]
    summ = [("Candidates", "=COUNTA('03_Buckets'!A:A)-1"), ("Grounded", "=COUNTIF('03_Buckets'!H:H,\"grounded\")"),
            ("Needs review", "=COUNTIF('03_Buckets'!H:H,\"needs_review\")"), ("Not grounded", "=COUNTIF('03_Buckets'!H:H,\"not_grounded\")"),
            ("Merged", "=COUNTIF('03_Buckets'!H:H,\"merged\")"), ("Grounded share of live buckets", "=B{g}/(B{c}-B{m})"),
            ("Support links", "=COUNTA('05_Support'!A:A)-1"), ("SSSOM link rows", "=COUNTA('06_SSSOM_Links'!A:A)-1"),
            ("Mean support events per live bucket", "=AVERAGEIF('03_Buckets'!H:H,\"<>merged\",'03_Buckets'!K:K)")]
    bk.add("01_Run_Summary", "Run identity, hashes, settings and recorded input files; figures at the top are live formulas over the data tabs.",
           ["item", "value", "source"], rows, [gr, run / "manifest.json"], "taxground run (pipeline.py)", widths={"A": 42, "B": 70, "C": 46},
           summary=summ)

    # 02 run history ------------------------------------------------------------------------------
    hist = []
    for folder in a.history:
        for d in sorted(pathlib.Path(folder).glob("run-*")):
            f = d / "grounding_results.json"
            if not f.exists():
                continue
            j = json.loads(f.read_text())
            c = collections.Counter(r["status"] for r in j["results"])
            s = j["settings"]
            hist.append([d.name, j["summary"].get("output_hash", "")[:12], s.get("units", "report"), "on" if s.get("support_refill") else "off",
                         len(j["results"]), j["summary"].get("sme_decisions_read", 0), c["grounded"], c["needs_review"], c["not_grounded"], c["merged"],
                         len([x for x in j.get("inputs_defs", [])]) or "", rel(f)])
    for h in hist:
        h.pop(10)
    bk.add("02_Run_History", "Every NTSB run on disk, oldest first: what changed between runs and the outcome counts. Same hash = same taxonomy.",
           ["run_id", "output_hash", "units", "support_refill", "candidates", "sme_decisions", "grounded", "needs_review", "not_grounded", "merged", "source"],
           hist, [], "taxground run, one folder per run", widths={"A": 32, "L": 60})

    # 03 buckets, 04 checks, 05 support, 07 criteria, 08 parent scores, 09 pool, 10 siblings ------------------------------------
    cand = {c["candidate_id"]: c for c in cands}
    b_rows, ch_rows, s_rows, c_rows, p_rows, pool_rows, sib_rows = [], [], [], [], [], [], []
    for i, r in enumerate(res):
        d, o = r.get("diag") or {}, r.get("output") or {}
        cid = r["candidate_id"]
        failed = [k["id"] for k in r.get("checks", []) if not k["passed"]]
        loc = f"{rel(gr)}#results[{i}]"
        merged_into = (S.get("merges") or {}).get(cid, "")
        b_rows.append([cid, r.get("batch") or re.match(r"[A-Z]+", cid).group(0), r["name"], r["definition"], r.get("proposed_parent") or "",
                       o.get("parent_code", ""), merged_into, r["status"], r.get("outcome") or "", " ".join(failed),
                       len(d.get("support", [])), d.get("relevant_under_parent"), len(d.get("moved_to_sibling", [])),
                       d.get("parent_agreement"), d.get("margin"), d.get("runner_up", ""), " ".join(o.get("definition_ids", [])),
                       len(r.get("card") or []), len(r.get("agent_calls") or []), " ".join(r.get("aliases") or []), RID, loc])
        for k in r.get("checks", []):
            ch_rows.append([cid, k["id"], k["name"], "pass" if k["passed"] else ("block" if k["severity"] == "block" else "review"), k["severity"], k["detail"], RID, loc + ".checks"])
        for j, s in enumerate(d.get("support", [])):
            m = rmeta(s["report_key"])
            s_rows.append([cid, o.get("parent_code", ""), j + 1, s["report_key"], m["event"], s.get("score"), s.get("chunk") or "", s.get("evidence", ""),
                           m["date"], m["mk"], m["ty"], m["make"], m["model"], m["part"], m["injury"], m["codes"], "sme" if s.get("sme") else "rules", RID, f"{loc}.diag.support[{j}]"])
        for j, c in enumerate(r.get("card") or []):
            c_rows.append([cid, c.get("seq", j), c["kind"], c["text"], c.get("cite_type", ""), c.get("cite_id", ""), c.get("quote") or "", c.get("origin", ""), RID, f"{loc}.card[{j}]"])
        for rank, (code, sc) in enumerate((d.get("parent_scores") or {}).items(), 1):
            p_rows.append([cid, rank, code, sc, "yes" if code == o.get("parent_code") else "", r.get("proposed_parent") or "", RID, f"{loc}.diag.parent_scores"])
        for j, p in enumerate(d.get("pool", [])):
            m = rmeta(p["report_key"])
            pool_rows.append([cid, j + 1, p["report_key"], " ".join(p.get("l1", [])), "yes" if o.get("parent_code") in p.get("l1", []) else "", p["score"], p.get("chunk") or "",
                              m["date"], m["mk"], m["ty"], RID, f"{loc}.diag.pool[{j}]"])
        for j, mv in enumerate(d.get("moved_to_sibling", [])):
            sib_rows.append([cid, mv["report_key"], mv["to"], mv.get("evidence", ""), RID, f"{loc}.diag.moved_to_sibling[{j}]"])
    bk.add("03_Buckets", "One row per discovery candidate: proposed and grounded parent, status, failed checks, evidence depth, parent agreement and margin.",
           ["candidate_id", "batch", "name", "definition", "proposed_parent", "grounded_parent", "merged_into", "status", "outcome", "failed_checks",
            "support_events", "relevant_events_under_parent", "reports_moved_to_sibling", "parent_agreement", "parent_margin", "runner_up_parent",
            "definition_ids", "criteria_lines", "agent_calls", "merged_aliases", "run_id", "source"],
           b_rows, [gr], "ground.ground_candidate + verify.verify + pipeline.run", widths={"C": 42, "D": 70, "Q": 34, "V": 52}, wrap={"C", "D"},
           fmt={"N": "0.0%", "O": "0.000"})
    bk.add("04_Checks", "Every check G1–G10 for every live bucket. block = not grounded; review = sent to an SME.",
           ["candidate_id", "check", "name", "result", "severity", "detail", "run_id", "source"], ch_rows, [gr], "verify.verify", widths={"C": 48, "F": 60, "H": 52})
    bk.add("05_Support", "Every supporting report link: the verbatim evidence sentence, retrieval score, the chunk kind that matched, and the aircraft.",
           ["candidate_id", "parent", "rank", "report_key", "event_id", "score", "chunk_kind", "evidence_quote", "date", "manufacturer", "type_root",
            "make_raw", "model_raw", "part", "injury", "report_cicTT_codes".replace("cicTT", "cictt"), "selected_by", "run_id", "source"],
           s_rows, [gr, inp / "sample_reports.json"], "ground.ground_candidate + ground.resolve_siblings (support_refill)",
           widths={"H": 80, "S": 56}, wrap={"H"}, fmt={"F": "0.000"})
    sssom = [l for l in (run / "links.sssom.tsv").read_text().splitlines() if not l.startswith("#")]
    rd = list(csv.reader(sssom, delimiter="\t"))
    bk.add("06_SSSOM_Links", "The stored link rows (SSSOM style): bucket → parent, definitions and reports, with justification, confidence and evidence.",
           rd[0] + ["source"], [x + [f"{rel(run / 'links.sssom.tsv')}#row{n}"] for n, x in enumerate(rd[1:], 1)], [run / "links.sssom.tsv"],
           "pipeline.write_outputs (SSSOM export)", widths={"C": 40, "F": 40, "J": 70}, wrap={"J"})
    bk.add("07_Criteria", "Criteria cards (SRS-TAX-03): include, exclude and boundary lines, each with one citation the verifier resolves (G9).",
           ["candidate_id", "seq", "kind", "text", "cite_type", "cite_id", "quote", "origin", "run_id", "source"], c_rows, [gr], "criteria.build_card",
           widths={"D": 70, "G": 60, "J": 48}, wrap={"D", "G"})
    vr = pathlib.Path(a.viewer_run)
    three = {}
    if vr.exists():
        for x in json.loads(vr.read_text()).get("parent_selection", []):
            three[x["candidate_id"]] = x
    p_rows = [x[:6] + [three.get(x[0], {}).get("definition_only", ""), three.get(x[0], {}).get("vote_only", "")] + x[6:] for x in p_rows]
    bk.add("08_Parent_Scores", "Parent choice per bucket: the top four scores (0.3 × definition fit + 0.7 × report vote), plus the parent each signal alone would pick.",
           ["candidate_id", "rank", "parent", "score", "selected", "proposed", "definition_only_pick", "vote_only_pick", "run_id", "source"], p_rows,
           [gr, vr if vr.exists() else None], "ground.ground_candidate (+ tools/export_viewer.py for the single-signal picks)", fmt={"D": "0.000"})
    bk.add("09_Pool", "The closest reports that voted on each bucket's parent, with their codes and whether they carry the grounded parent.",
           ["candidate_id", "rank", "report_key", "report_codes", "has_grounded_parent", "score", "chunk_kind", "date", "manufacturer", "type_root", "run_id", "source"],
           pool_rows, [gr], "store.reports_chunks (hybrid 0.6 / 0.4)", fmt={"F": "0.000"}, widths={"L": 52})
    bk.add("10_Sibling_Moves", "Reports a bucket gave up because a sibling under the same parent matched them better (GR-6).",
           ["candidate_id", "report_key", "moved_to", "evidence_quote", "run_id", "source"], sib_rows, [gr], "ground.resolve_siblings", widths={"D": 80}, wrap={"D"})

    # 11 merges -------------------------------------------------------------------------------------
    mr = []
    for i, r in enumerate(res):
        if r["status"] == "merged":
            mr.append([r["candidate_id"], r["name"], (S.get("merges") or {}).get(r["candidate_id"], ""), (r.get("diag") or {}).get("merge_score", ""), RID, f"{rel(gr)}#results[{i}]"])
    bk.add("11_Merges", "Cross-batch twins merged before grounding (0.5 × cosine + 0.5 × Jaccard of retrieved pools, mutual best match, ≥ 0.55).",
           ["candidate_id", "name", "merged_into", "similarity", "run_id", "source"], mr, [gr], "ground.dedupe", widths={"B": 50})

    # 12 definitions, 13 parents, 14 occurrence map, 15 ECCAIRS -----------------------------------------------------------------------
    df = pathlib.Path(inp / "industry_definitions.json")
    d_rows = []
    linked = collections.Counter(x[4] for x in rd[1:])
    for n, x in enumerate(defs["definitions"]):
        org = "ECCAIRS 1.3.0.12 crosswalk" if x["id"].startswith("ECC-") else "package"
        d_rows.append([x["id"], x["term"], " ".join(x["parents"]), org, x["source"], x["text"], F(f"=COUNTIF('06_SSSOM_Links'!E:E,A{n + 2})", linked.get(x["id"], 0)), f"{rel(df)}#definitions[{n}]"])
    bk.add("12_Definitions", "Every industry definition the selector could cite, its CICTT parents and origin; times_linked is a live count over 06_SSSOM_Links.",
           ["def_id", "term", "parents", "origin", "source_document", "text", "times_linked", "source"], d_rows, [df],
           "tools/ingest_ntsb.py + tools/eccairs_crosswalk.py", widths={"B": 40, "E": 60, "F": 80}, wrap={"F"})
    code_n = collections.Counter(c for r in reports for c in r["l1_codes"])
    ndef = collections.Counter(p for x in defs["definitions"] for p in x["parents"])
    pr = []
    bst = collections.Counter(((r.get("output") or {}).get("parent_code"), r["status"]) for r in res)
    tot_codes = sum(code_n.values())
    for n, c in enumerate(cats):
        row = n + 2
        pr.append([c["code"], c["name"], "yes" if c.get("in_scope", True) else "no", c.get("definition", ""), code_n.get(c["code"], 0), ndef.get(c["code"], 0),
                   F(f"=COUNTIFS('03_Buckets'!F:F,A{row},'03_Buckets'!H:H,\"grounded\")", bst[(c["code"], "grounded")]),
                   F(f"=COUNTIFS('03_Buckets'!F:F,A{row},'03_Buckets'!H:H,\"needs_review\")", bst[(c["code"], "needs_review")]),
                   F(f"=E{row}/SUM($E$2:$E${len(cats) + 1})", round(code_n.get(c["code"], 0) / tot_codes, 6)), f"{rel(inp / 'icao_categories.json')}#categories[{n}]"])
    bk.add("13_CICTT_Parents", "The 33 CICTT Level-1 parents: reports coded to each, definitions crosswalked, and live counts of grounded and review buckets.",
           ["code", "name", "in_scope", "definition", "reports_coded", "definitions", "grounded_buckets", "review_buckets", "share_of_code_assignments", "source"],
           pr, [inp / "icao_categories.json", inp / "sample_reports.json", df], "tools/ingest_ntsb.py", widths={"B": 34, "D": 80}, wrap={"D"}, fmt={"I": "0.0%"})
    occ = json.loads((pathlib.Path(a.data) / "occ_to_cictt.json").read_text())
    meaning = {}
    if a.csv and (pathlib.Path(a.csv) / "ct_seqevt.csv").exists():
        for x in csv.DictReader(open(pathlib.Path(a.csv) / "ct_seqevt.csv", encoding="utf-8", errors="replace")):
            meaning[x["code"].zfill(3)] = x["meaning"]
    om = [[k, meaning.get(k, ""), v or "(not mapped)", "consequence only" if k in ("470", "170", "180") else "", f"{rel(pathlib.Path(a.data) / 'occ_to_cictt.json')}#mapping.{k}"]
          for k, v in sorted(occ["mapping"].items())]
    bk.add("14_NTSB_Occ_Map", f"NTSB occurrence code → CICTT parent ({occ['version']}). Consequence-only codes count only when they are the defining event.",
           ["ntsb_occurrence_code", "meaning", "cictt_parent", "rule", "source"], om, [pathlib.Path(a.data) / "occ_to_cictt.json", pathlib.Path(a.csv or ".") / "ct_seqevt.csv" if a.csv else None],
           "tools/ingest_ntsb.py (OCC map)", widths={"B": 44})
    ecc = json.loads(pathlib.Path(a.eccairs).read_text())["events"] if pathlib.Path(a.eccairs).exists() else []
    edef = {x["id"]: x for x in defs["definitions"] if x["id"].startswith("ECC-")}
    er = [[e["code"], e["name"], e["level"], " › ".join(e["path"][:-1]), " ".join(edef[f"ECC-{e['code']}"]["parents"]) if f"ECC-{e['code']}" in edef else "",
           "crosswalked" if f"ECC-{e['code']}" in edef else ("no definition" if not e.get("definition") else "no rule matched"), (e.get("definition") or "")[:500],
           defs.get("eccairs_crosswalk_version", ""), f"{rel(a.eccairs)}#events[{n}]"] for n, e in enumerate(ecc)]
    bk.add("15_ECCAIRS_Crosswalk", "All 809 ECCAIRS 1.3.0.12 attribute-390 events and the CICTT parents our draft crosswalk gives them (SME approval needed).",
           ["eccairs_code", "name", "level", "path", "cictt_parents", "status", "definition", "crosswalk_version", "source"], er,
           [a.eccairs, df], "tools/parse_eccairs.py + tools/eccairs_crosswalk.py", widths={"B": 50, "D": 60, "G": 70}, wrap={"G"})

    # 16 reports index and corpus statistics ------------------------------------------------------------------
    ri = []
    for n, r in enumerate(reports):
        m = r.get("meta") or {}
        ri.append([r["report_key"], r.get("event_id", ""), m.get("date", ""), m.get("date", "")[:4], norm_make(m.get("make")), type_root(m.get("model")), m.get("make", ""),
                   m.get("model", ""), (m.get("part") or "").lstrip("0"), m.get("injury", ""), m.get("damage", ""), " ".join(r["l1_codes"]), r.get("source_id", ""),
                   len(r.get("narrative", "")), len(r.get("findings", "")), (m.get("defining") or ""), f"{rel(inp / 'sample_reports.json')}#reports[{n}]"])
    bk.add("16_Reports_Index", "Every NTSB report in the run, with normalised manufacturer and root aircraft type (same rules as the viewer). Filter here, then look up by key.",
           ["report_key", "event_id", "date", "year", "manufacturer", "type_root", "make_raw", "model_raw", "part", "injury", "damage", "cictt_codes", "source_id",
            "narrative_chars", "findings_chars", "defining_event", "source"], ri, [inp / "sample_reports.json"], "tools/ingest_ntsb.py; normalisation in tools/build_derived.py",
           widths={"P": 50, "Q": 52})
    n_rep = len(ri) + 1
    yrs = sorted({x[3] for x in ri if x[3]})
    yc, yf = collections.Counter(x[3] for x in ri), collections.Counter(x[3] for x in ri if x[9] == "FATL")
    mc, mf = collections.Counter(x[4] for x in ri), collections.Counter(x[4] for x in ri if x[9] == "FATL")
    tc, tf = collections.Counter((x[4], x[5]) for x in ri), collections.Counter((x[4], x[5]) for x in ri if x[9] == "FATL")
    bk.add("17_Corpus_by_Year", "Reports and fatal reports per year: live COUNTIFS over 16_Reports_Index.",
           ["year", "reports", "fatal", "fatal_share", "share_of_all"],
           [[y, F(f"=COUNTIF('16_Reports_Index'!D$2:D${n_rep},A{i + 2})", yc[y]),
             F(f"=COUNTIFS('16_Reports_Index'!D$2:D${n_rep},A{i + 2},'16_Reports_Index'!J$2:J${n_rep},\"FATL\")", yf[y]),
             F(f"=IF(B{i + 2}=0,0,C{i + 2}/B{i + 2})", round(yf[y] / yc[y], 6)), F(f"=B{i + 2}/SUM($B$2:$B${len(yrs) + 1})", round(yc[y] / sum(yc[z] for z in yrs), 6))]
            for i, y in enumerate(yrs)],
           ["16_Reports_Index"], "formulas over 16_Reports_Index", fmt={"D": "0.0%", "E": "0.0%"})
    mk = collections.Counter(x[4] for x in ri).most_common(60)
    bk.add("18_Corpus_by_Make", "The 60 most common normalised manufacturers: live counts over 16_Reports_Index, with the number of raw spellings folded into each.",
           ["manufacturer", "reports", "fatal", "share", "raw_spellings"],
           [[m, F(f"=COUNTIF('16_Reports_Index'!E$2:E${n_rep},A{i + 2})", mc[m]),
             F(f"=COUNTIFS('16_Reports_Index'!E$2:E${n_rep},A{i + 2},'16_Reports_Index'!J$2:J${n_rep},\"FATL\")", mf[m]),
             F(f"=B{i + 2}/{len(ri)}", round(mc[m] / len(ri), 6)), len({x[6] for x in ri if x[4] == m})] for i, (m, _) in enumerate(mk)],
           ["16_Reports_Index"], "formulas over 16_Reports_Index", fmt={"D": "0.0%"})
    ty = collections.Counter((x[4], x[5]) for x in ri).most_common(150)
    bk.add("19_Corpus_by_Type", "The 150 most common manufacturer + root types (737, 172, PA28…): live counts, and the raw model strings folded into each.",
           ["manufacturer", "type_root", "reports", "fatal", "raw_models", "example_models"],
           [[m, t, F(f"=COUNTIFS('16_Reports_Index'!E$2:E${n_rep},A{i + 2},'16_Reports_Index'!F$2:F${n_rep},B{i + 2})", tc[(m, t)]),
             F(f"=COUNTIFS('16_Reports_Index'!E$2:E${n_rep},A{i + 2},'16_Reports_Index'!F$2:F${n_rep},B{i + 2},'16_Reports_Index'!J$2:J${n_rep},\"FATL\")", tf[(m, t)]),
             len({x[7] for x in ri if x[4] == m and x[5] == t}), ", ".join(sorted({x[7] for x in ri if x[4] == m and x[5] == t})[:8])] for i, ((m, t), _) in enumerate(ty)],
           ["16_Reports_Index"], "formulas over 16_Reports_Index", widths={"F": 70})

    # 20-23 technique measurements ----------------------------------------------------------------------
    tp = pathlib.Path(a.techniques)
    if tp.exists():
        T = json.loads(tp.read_text())
        lanes = S.get("routing") or {}
        rows = [["lane", k, v, F(f"=C{n + 2}/SUM($C$2:$C${len(lanes) + 1})", round(v / sum(lanes.values()), 6)), f"{rel(gr)}#summary.routing.{k}"] for n, (k, v) in enumerate(lanes.items())]
        base = len(rows) + 2
        for k, v in T["chunks"]["by_kind"].items():
            rows.append(["chunk kind", k, v, F(f"=C{len(rows) + 2}/{T['chunks']['total']}", round(v / T["chunks"]["total"], 6)), f"{rel(tp)}#chunks.by_kind.{k}"])
        for k, v in T["chunks"]["mean_len"].items():
            rows.append(["mean chunk length (chars)", k, v, "", f"{rel(tp)}#chunks.mean_len.{k}"])
        rows += [["chunks total", "", T["chunks"]["total"], "", f"{rel(tp)}#chunks.total"],
                 ["median narrative length (chars)", "", T["corpus"]["median_narrative"], "", f"{rel(tp)}#corpus.median_narrative"],
                 ["embedding", T["embedding"]["name"], T["embedding"]["dim"], "", f"{rel(tp)}#embedding.dim"],
                 ["mean cosine, same-parent report pairs", "", T["embedding"]["mean_same"], "", f"{rel(tp)}#embedding.mean_same"],
                 ["mean cosine, different-parent pairs", "", T["embedding"]["mean_diff"], "", f"{rel(tp)}#embedding.mean_diff"]]
        rows += [["variance share of embedding direction", f"PC{i + 1}", v, "", f"{rel(tp)}#embedding.pc_var[{i}]"] for i, v in enumerate(T["embedding"]["pc_var"])]
        rows += [["support links by winning chunk kind", k, v, "", f"{rel(tp)}#run.support_kinds.{k}"] for k, v in T["run"]["support_kinds"].items()]
        bk.add("20_Corpus_and_Chunks", "Routing lanes, section-aware chunks (counts and lengths), embedding geometry, and which chunk kind carried support.",
               ["measure", "key", "value", "share", "source"], rows, [tp], "tools/technique_stats.py", widths={"A": 40, "E": 50}, fmt={"D": "0.0%"})
        hrows = []
        for name, key in (("narrative length", "narrative_len"), ("findings length", "findings_len")):
            h = T["corpus"][key]
            hrows += [[name, h["edges"][i], h["edges"][i + 1], c, f"{rel(tp)}#corpus.{key}"] for i, c in enumerate(h["counts"])]
        for k, h in T["chunks"]["len_hist"].items():
            hrows += [[f"chunk length · {k}", h["edges"][i], h["edges"][i + 1], c, f"{rel(tp)}#chunks.len_hist.{k}"] for i, c in enumerate(h["counts"])]
        for k in ("cos_same", "cos_diff"):
            h = T["embedding"][k]
            hrows += [[f"cosine · {'same' if k == 'cos_same' else 'different'} parent", h["edges"][i], h["edges"][i + 1], c, f"{rel(tp)}#embedding.{k}"] for i, c in enumerate(h["counts"])]
        bk.add("21_Distributions", "Histogram bins behind the Techniques charts: text lengths, chunk lengths, cosine of random report pairs.",
               ["distribution", "bin_from", "bin_to", "count", "source"], hrows, [tp], "tools/technique_stats.py", widths={"A": 36, "E": 46})
        ex = T["example"]
        bk.add("22_Hybrid_Example", f"Worked hybrid-retrieval example for {ex['candidate']} · {ex['name']}: score = {ex['w']} × cosine + {1 - ex['w']:.1f} × normalised keyword; kept if ≥ cut-off.",
               ["rank", "report_key", "codes", "chunk_kind", "cosine", "keyword_norm", "score_stored", "score_recomputed", "cut_off", "kept", "source"],
               [[i + 1, p["key"], " ".join(p["codes"]), p.get("chunk") or "", p["cos"], p["kw"], p["score"], F(f"={ex['w']}*E{i + 2}+{round(1 - ex['w'], 2)}*F{i + 2}", round(ex["w"] * p["cos"] + (1 - ex["w"]) * p["kw"], 6)),
                 ex["cut"], F(f"=IF(G{i + 2}>=I{i + 2},\"yes\",\"no\")", "yes" if p["score"] >= ex["cut"] else "no"), f"{rel(tp)}#example.pool[{i}]"] for i, p in enumerate(ex["pool"])],
               [tp], "tools/technique_stats.py (store.reports_chunks)", fmt={"E": "0.000", "F": "0.000", "G": "0.000", "H": "0.000", "I": "0.000"})
        md = T["modes"]
        mrows = []
        for r in md["rows"]:
            for l in md["labels"]:
                m = r["modes"][l]
                mrows.append([r["id"], r["name"], r["parent"], l, m["agree"], m["overlap"], m["kinds"].get("summary", 0), m["kinds"].get("findings", 0), m["kinds"].get("narrative", 0),
                              f"{rel(tp)}#modes.rows[{r['id']}].{l}"])
        bk.add("23_Retrieval_Modes", "Five retrieval configurations × every live bucket: share of the top 10 coded with the grounded parent, and overlap with chunks·hybrid.",
               ["candidate_id", "name", "grounded_parent", "mode", "top10_parent_agreement", "jaccard_vs_chunks_hybrid", "top10_summary_chunks", "top10_findings_chunks",
                "top10_narrative_chunks", "source"], mrows, [tp], "tools/technique_stats.py", widths={"B": 40, "D": 24, "J": 46}, fmt={"E": "0.0%", "F": "0.0%"},
               summary=[(f"Mean agreement · {l}", f"=AVERAGEIF(D:D,\"{l}\",E:E)") for l in md["labels"]])

    # 24 guardrails, 25 gate, 26 report tests, 27 revision prompts -------------------------------------------------
    gt = list(csv.reader(open(run / "guardrail_tests.csv")))
    bk.add("24_Guardrails", "Faults an unconstrained model might produce, injected into a grounded bucket and run through the same verifier.",
           gt[0] + ["run_id", "source"], [x + [RID, f"{rel(run / 'guardrail_tests.csv')}#row{n}"] for n, x in enumerate(gt[1:], 1)], [run / "guardrail_tests.csv"],
           "pipeline (guardrail tests)", widths={"A": 50})
    gj = run / "gate.json"
    if gj.exists():
        g = json.loads(gj.read_text())
        bk.add("25_Gate", "Release gate: the seven checks a run must pass before release (accuracy rows need an answer key; real data has none yet).",
               ["check", "passed", "detail", "source"], [[x["check"], "PASS" if x["passed"] else "FAIL", x["detail"], f"{rel(gj)}#[{n}]"] for n, x in enumerate(g)], [gj],
               "taxground gate (cli.cmd_gate)", widths={"A": 60, "C": 50})
    if a.test and pathlib.Path(a.test, "report_test.csv").exists():
        tdir = pathlib.Path(a.test)
        tr = list(csv.reader(open(tdir / "report_test.csv")))
        hdr = tr[0]
        rows = []
        for n, x in enumerate(tr[1:], 1):
            m = rmeta(x[0])
            rows.append(x + [m["date"], m["mk"], m["ty"], tdir.name, f"{rel(tdir / 'report_test.csv')}#row{n}"])
        verd = ["fits", "ambiguous", "excluded", "no_fit", "out_of_scope"]
        vi = chr(ord("A") + hdr.index("verdict"))
        bk.add("26_Report_Tests", "New reports scored against a released version (SRS-TAX-04): verdict, best bucket, runner-up and the revision it prompts.",
               hdr + ["date", "manufacturer", "type_root", "test_run", "source"], rows, [tdir / "report_test.csv"], "taxground test (cli.cmd_test)",
               widths={"H": 60, "I": 70}, wrap={"I"}, fmt={"D": "0.000", "F": "0.000"},
               summary=[(f"Verdict: {v}", f"=COUNTIF({vi}:{vi},\"{v}\")") for v in verd])
        rp = list(csv.reader(open(tdir / "revision_prompts.csv")))
        bk.add("27_Revision_Prompts", "Every non-fitting test verdict as a draft SME decision row, carrying the prompting report.",
               rp[0] + ["source"], [x + [f"{rel(tdir / 'revision_prompts.csv')}#row{n}"] for n, x in enumerate(rp[1:], 1)], [tdir / "revision_prompts.csv"],
               "taxground test", widths={"I": 90}, wrap={"I"})

    # 28 discovery clusters, 29 discovery batch D, 30 synthetic, 31 changelog ------------------------------------------------
    if a.clusters and pathlib.Path(a.clusters).exists():
        cl = json.loads(pathlib.Path(a.clusters).read_text())
        bk.add("28_Discovery_Clusters", "k-means clusters of real reports inside each parent: distinctive words and most common coded findings (worksheet for batch D).",
               ["parent", "cluster", "size", "distinctive_terms", "top_findings", "example_reports", "source"],
               [[c["parent"], c["cluster"], c["size"], ", ".join(c["terms"]), " || ".join(f"{f} ({n})" for f, n in c["findings"]), " ".join(e["key"] for e in c["examples"]),
                 f"{rel(a.clusters)}#[{n}]"] for n, c in enumerate(cl)], [a.clusters], "tools/discover_clusters.py", widths={"D": 60, "E": 90}, wrap={"D", "E"})
    bd = ROOT / "data" / "discovery" / "ntsb_batch_d.json"
    if bd.exists():
        D = json.loads(bd.read_text())["candidates"]
        st = {r["candidate_id"]: r for r in res}
        bk.add("29_Batch_D", "Discovery batch D (drafted by Claude from the cluster worksheet, pending SME review) and how each candidate grounded.",
               ["candidate_id", "name", "definition", "proposed_parent", "grounded_parent", "status", "failed_checks", "source"],
               [[c["candidate_id"], c["name"], c["definition"], c["proposed_parent"], (st.get(c["candidate_id"], {}).get("output") or {}).get("parent_code", ""),
                 st.get(c["candidate_id"], {}).get("status", ""), " ".join(k["id"] for k in st.get(c["candidate_id"], {}).get("checks", []) if not k["passed"]),
                 f"{rel(bd)}#candidates[{n}]"] for n, c in enumerate(D)], [bd, gr], "data/discovery/ntsb_batch_d.json + taxground run", widths={"B": 44, "C": 80}, wrap={"C"})
    if a.synthetic:
        srows = []
        for d in sorted(pathlib.Path(a.synthetic).glob("run-*")):
            f = d / "grounding_results.json"
            if not f.exists():
                continue
            j = json.loads(f.read_text())
            m, c = j["summary"].get("metrics", {}), collections.Counter(r["status"] for r in j["results"])
            srows.append([j["summary"]["dataset"], d.name, j["summary"]["output_hash"][:12], m.get("parent_correct"), m.get("precision"), m.get("recall"),
                          m.get("merge_precision"), m.get("merge_recall"), c["grounded"], c["needs_review"], c["not_grounded"], c["merged"], j["summary"].get("sme_decisions_read", 0), rel(f)])
        bk.add("30_Synthetic_Accuracy", "The three hand-labelled synthetic answer keys (build step 0): parent accuracy and report-link precision and recall.",
               ["dataset", "run_id", "output_hash", "parents_correct", "precision", "recall", "precision_merge_aware", "recall_merge_aware", "grounded", "needs_review",
                "not_grounded", "merged", "sme_decisions", "source"], srows, [], "taxground run on data/trial, data/sample_b, data/combined",
               fmt={"E": "0.0%", "F": "0.0%", "G": "0.0%", "H": "0.0%"}, widths={"N": 60})
    prev = S.get("previous_run")
    cl_path = None
    for folder in [run.parent] + [pathlib.Path(h) for h in a.history]:
        for d in sorted(folder.glob("run-*"), reverse=True):
            t = d / "changelog.md"
            if t.exists() and "|" in t.read_text():
                cl_path = t
                break
        if cl_path:
            break
    if cl_path:
        lines = [l for l in cl_path.read_text().splitlines() if l.startswith("|")]
        tab = [[c.strip() for c in l.strip("|").split("|")] for l in lines if not re.match(r"^\|\s*-", l)]
        if tab:
            bk.add("31_Changelog", f"The most recent changelog with changes ({cl_path.parent.name}): every revision with its cause, tried in order (SME, sibling, new report, data, settings, code).",
                   tab[0] + ["source"], [x + [f"{rel(cl_path)}#line"] for x in tab[1:]], [cl_path], "pipeline (changelog attribution)", widths={"A": 14, "D": 60})

    write(bk, out, a, S)


# ---------------------------------------------------------------- writers
def write(bk, out, a, S):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.table import Table, TableStyleInfo

    lineage = dict(run_id=bk.run_id, built=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), generator="tools/build_derived.py",
                   command=" ".join(["python3", "tools/build_derived.py"] + sys.argv[1:]), tables=[])
    FONT = "Arial"
    hdr_fill, hdr_font = PatternFill("solid", fgColor="0E1A26"), Font(name=FONT, bold=True, color="FFFFFF", size=10)
    body, bold, link = Font(name=FONT, size=10), Font(name=FONT, size=10, bold=True), Font(name=FONT, size=10, color="1F5FB4", underline="single")
    title = Font(name=FONT, size=16, bold=True, color="0E1A26")
    note = Font(name=FONT, size=9, italic=True, color="5B6977")
    trace_fill = PatternFill("solid", fgColor="EEF2F5")
    sum_fill = PatternFill("solid", fgColor="FFF4DC")
    thin = Border(bottom=Side(style="thin", color="D0D9E1"))
    checks = []
    wb = Workbook()
    idx = wb.active
    idx.title = "00_Index"
    for t in bk.tables:
        # csv
        cp = out / "csv" / f"{t['name']}.csv"
        with open(cp, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(t["cols"])
            w.writerows([[v.value if isinstance(v, F) else v for v in row] for row in t["rows"]])
        srcs = []
        for s in t["sources"]:
            p = pathlib.Path(s) if not isinstance(s, str) or "/" in str(s) or str(s).endswith((".json", ".csv", ".tsv", ".md")) else None
            if p is not None and p.exists():
                srcs.append(dict(path=rel(p), sha256=sha(p)))
            else:
                srcs.append(dict(path=str(s), sha256=None))
        lineage["tables"].append(dict(table=t["name"], description=t["desc"], rows=len(t["rows"]), columns=t["cols"], generator=t["generator"],
                                      sources=srcs, csv=rel(cp)))
        # sheet
        ws = wb.create_sheet(t["name"])
        start = 1
        if t["summary"]:
            ws.cell(1, 1, "Summary (live formulas)").font = bold
            for i, (lab, fml) in enumerate(t["summary"]):
                r = i + 2
                ws.cell(r, 1, lab).font = body
                c = ws.cell(r, 2, fml.format(c=2, g=3, m=6) if "{" in fml else fml)
                c.font = body
                if any(w in lab.lower() for w in ("share", "agreement")):
                    c.number_format = "0.0%"
                ws.cell(r, 1).fill = ws.cell(r, 2).fill = sum_fill
            start = len(t["summary"]) + 3
        for j, h in enumerate(t["cols"], 1):
            c = ws.cell(start, j, h)
            c.font, c.fill = hdr_font, hdr_fill
            c.alignment = Alignment(vertical="center", wrap_text=True)
        trace_cols = {j for j, h in enumerate(t["cols"], 1) if h in ("source", "run_id", "test_run")}
        for i, row in enumerate(t["rows"]):
            for j, v in enumerate(row, 1):
                if isinstance(v, F):
                    assert start == 1, f"{t['name']}: row formulas assume the header is on row 1"
                    checks.append((t["name"], start + 1 + i, j, v.value))
                    v = v.formula
                c = ws.cell(start + 1 + i, j, v)
                c.font = body
                if j in trace_cols:
                    c.fill = trace_fill
                    c.font = Font(name=FONT, size=9, color="5B6977")
                col = get_column_letter(j)
                if col in t["fmt"]:
                    c.number_format = t["fmt"][col]
                if col in t["wrap"]:
                    c.alignment = Alignment(wrap_text=True, vertical="top")
        last = start + len(t["rows"])
        for j, h in enumerate(t["cols"], 1):
            col = get_column_letter(j)
            ws.column_dimensions[col].width = t["widths"].get(col, min(max(12, len(h) + 2), 30))
        ws.freeze_panes = ws.cell(start + 1, 2)
        if t["rows"]:
            ref = f"A{start}:{get_column_letter(len(t['cols']))}{last}"
            tb = Table(displayName=re.sub(r"[^A-Za-z0-9]", "_", "T" + t["name"]), ref=ref)
            tb.tableStyleInfo = TableStyleInfo(name="TableStyleLight9", showRowStripes=True)
            ws.add_table(tb)
        ws.sheet_view.zoomScale = 90
    # index
    idx["A1"] = "Derived data · taxonomy grounding run"
    idx["A1"].font = title
    meta = [("Run", bk.run_id), ("Taxonomy version", S.get("taxonomy_version")), ("Output hash", S.get("output_hash")), ("Input hash", S.get("input_hash")),
            ("Embedder", S.get("embedder")), ("Built", lineage["built"]), ("Command", lineage["command"]),
            ("How to read", "Each tab is one table; the same rows are in csv/<tab>.csv. Grey columns on the right (run_id, source) trace every row to the file and record it came from. "
                            "Orange cells at the top of a tab are live formulas over the data tabs. lineage.json lists every source file with its sha256."),
            ("Status of the content", "Real NTSB data; no answer key. The NTSB-occurrence and ECCAIRS crosswalks and discovery batch D are drafts pending SME approval. "
                                      "The embedder is a stand-in (TF-IDF + SVD) until DG-2 is decided.")]
    for i, (k, v) in enumerate(meta, 3):
        idx.cell(i, 1, k).font = bold
        c = idx.cell(i, 2, v)
        c.font = body
        c.alignment = Alignment(wrap_text=True, vertical="top")
    r0 = len(meta) + 5
    heads = ["Tab", "What it holds", "Rows", "Generated by", "Source files (sha256 prefix)", "CSV"]
    for j, h in enumerate(heads, 1):
        c = idx.cell(r0, j, h)
        c.font, c.fill = hdr_font, hdr_fill
    for i, (t, L) in enumerate(zip(bk.tables, lineage["tables"]), r0 + 1):
        c = idx.cell(i, 1, t["name"])
        c.hyperlink = f"#'{t['name']}'!A1"
        c.font = link
        idx.cell(i, 2, t["desc"]).font = body
        idx.cell(i, 3, f"=COUNTA('{t['name']}'!A:A)-1-{(len(t['summary']) + 1) if t['summary'] else 0}").font = body
        checks.append(("00_Index", i, 3, len(t["rows"])))
        idx.cell(i, 4, t["generator"]).font = body
        idx.cell(i, 5, "\n".join(f"{s['path']} ({(s['sha256'] or 'derived tab')[:12]})" for s in L["sources"]) or "derived from the run folders listed in the tab").font = Font(name=FONT, size=9)
        idx.cell(i, 6, L["csv"]).font = Font(name=FONT, size=9)
        for j in (2, 4, 5):
            idx.cell(i, j).alignment = Alignment(wrap_text=True, vertical="top")
        for j in range(1, 7):
            idx.cell(i, j).border = thin
    for col, wd in zip("ABCDEF", (24, 70, 8, 34, 60, 36)):
        idx.column_dimensions[col].width = wd
    idx.column_dimensions["B"].width = 90
    idx.freeze_panes = idx.cell(r0 + 1, 1)
    xp = out / "derived_workbook.xlsx"
    wb.save(xp)
    (out / "lineage.json").write_text(json.dumps(lineage, indent=1))
    (out / "formula_checks.json").write_text(json.dumps(checks))
    (out / "README.md").write_text(f"""# Derived data · {bk.run_id}

Built by `tools/build_derived.py` on {lineage['built']} from the run folder and its recorded inputs.

    {lineage['command']}

| File | What |
|---|---|
| `derived_workbook.xlsx` | 00_Index (hyperlinked, with lineage) + {len(bk.tables)} tabs; summary figures are live formulas |
| `csv/` | one CSV per tab, same rows |
| `lineage.json` | per table: description, row count, generator, source files with sha256 |

Every row carries `run_id` and `source` (file + locator such as `grounding_results.json#results[7].diag.support[2]`), so any number can be
traced to the record that produced it. Rebuild with `STEPS=15 ./build_all.sh`.

Tables: {', '.join(t['name'] for t in bk.tables)}
""")
    print(xp, f"{len(bk.tables)} tabs", f"{sum(len(t['rows']) for t in bk.tables):,} rows")


if __name__ == "__main__":
    main()

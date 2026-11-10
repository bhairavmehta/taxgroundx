"""Measure the retrieval techniques on the real working set, for the viewer's Techniques tab.

Writes viewer/data/techniques.json: corpus and chunk shapes, embedding geometry (2-D map, same/different parent
cosine), a worked hybrid-scoring example with its relative cut-off, and a comparison of retrieval modes per candidate.
Every number comes from the database the run used; nothing is typed in by hand except the run-mode history.
"""
import argparse, json, math, pathlib, random, sys, time
import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from taxground.store import Store                       # noqa: E402
from taxground import ground as G                        # noqa: E402


def hist(vals, lo, hi, step):
    edges = list(np.arange(lo, hi + step, step))
    counts = [0] * (len(edges) - 1)
    over = 0
    for v in vals:
        if v >= hi:
            over += 1
            continue
        counts[int((v - lo) // step)] += 1
    return dict(edges=[round(float(e), 3) for e in edges], counts=counts, over=over)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--results", required=True, help="grounding_results.json of the run shown in the viewer")
    ap.add_argument("--out", required=True)
    ap.add_argument("--example", default="B25")
    ap.add_argument("--history", nargs="*", default=[], help="label=run_dir, oldest first, for the run-history chart")
    ap.add_argument("--skip-modes", action="store_true", help="reuse the retrieval-mode comparison from an existing --out file")
    a = ap.parse_args()
    st = Store(a.db)
    S = dict(G.DEFAULT_SETTINGS); S.update(min_support=10, units="chunks")
    random.seed(7)
    T = {}

    # 1. corpus shape -----------------------------------------------------------------------------
    rows = st.q("SELECT length(narrative), length(findings), source_id, evidence_level FROM report")
    T["corpus"] = dict(reports=len(rows),
                       narrative_len=hist([r[0] for r in rows], 0, 8000, 250),
                       findings_len=hist([r[1] for r in rows], 0, 2000, 100),
                       median_narrative=int(np.median([r[0] for r in rows])),
                       sources={k: sum(1 for r in rows if r[2] == k) for k in sorted({r[2] for r in rows})},
                       evidence={k: sum(1 for r in rows if r[3] == k) for k in sorted({r[3] for r in rows})})

    # 2. chunks -----------------------------------------------------------------------------------
    ch = st.q("SELECT kind, length(body), report_key FROM report_chunk")
    kinds = sorted({c[0] for c in ch})
    per = {}
    for c in ch:
        per[c[2]] = per.get(c[2], 0) + 1
    T["chunks"] = dict(total=len(ch), by_kind={k: sum(1 for c in ch if c[0] == k) for k in kinds},
                       mean_len={k: round(float(np.mean([c[1] for c in ch if c[0] == k]))) for k in kinds},
                       len_hist={k: hist([c[1] for c in ch if c[0] == k], 0, 1600, 100) for k in kinds},
                       per_report=hist(list(per.values()), 1, 16, 1),
                       example=[dict(kind=k, header=h, body=b[:420]) for k, h, b in st.q(
                           "SELECT kind, header, body FROM report_chunk WHERE report_key = %s ORDER BY seq LIMIT 4", ("CEN13FA130",))])

    # 3. embedding geometry -----------------------------------------------------------------------
    emb = st.q("SELECT report_key, l1_codes, embedding FROM report WHERE cardinality(l1_codes) = 1")
    top = {}
    for _, codes, _ in emb:
        top[codes[0]] = top.get(codes[0], 0) + 1
    show = [k for k, _ in sorted(top.items(), key=lambda x: -x[1]) if k != "OTHR"][:7]
    pick = [e for e in emb if e[1][0] in show]
    random.shuffle(pick)
    pick = pick[:2400]
    X = np.array([np.asarray(e[2].to_numpy() if hasattr(e[2], "to_numpy") else e[2], dtype=np.float32) for e in pick])
    Xc = X - X.mean(0)
    U, Sv, Vt = np.linalg.svd(Xc, full_matrices=False)
    P = Xc @ Vt[:2].T
    var = (Sv ** 2) / (Sv ** 2).sum()
    lab = [e[1][0] for e in pick]
    same, diff = [], []
    n = len(pick)
    for _ in range(6000):
        i, j = random.randrange(n), random.randrange(n)
        if i == j:
            continue
        (same if lab[i] == lab[j] else diff).append(float(X[i] @ X[j]))
    T["embedding"] = dict(dim=int(X.shape[1]), name="local-lsa-%d" % X.shape[1], parents=show,
                          map=[[round(float(p[0]), 4), round(float(p[1]), 4), show.index(l)] for p, l in zip(P, lab)],
                          pc_var=[round(float(v), 4) for v in var[:12]],
                          cos_same=hist(same, -0.2, 1.0, 0.05), cos_diff=hist(diff, -0.2, 1.0, 0.05),
                          mean_same=round(float(np.mean(same)), 3), mean_diff=round(float(np.mean(diff)), 3))

    # 4. worked example: hybrid score and relative cut-off ---------------------------------------------
    cands = {c["candidate_id"]: c for c in st.candidates()}
    c = cands[a.example]
    text = f"{c['name']}. {c['definition']}"
    st.units = "chunks"
    pool = st.reports_hybrid(c["embedding"], text, S["vector_weight"], limit=40)
    kwmax = max((p["kw"] for p in pool), default=1) or 1
    best = pool[0]["score"] if pool else 1
    T["example"] = dict(candidate=a.example, name=c["name"], definition=c["definition"], w=S["vector_weight"],
                        cutoff=S["relative_cutoff"], min_score=S["min_score"],
                        pool=[dict(key=p["report_key"], codes=p["l1_codes"], cos=round(p["cos"], 4),
                                   kw=round(p["kw"] / kwmax, 4), score=p["score"], chunk=p.get("chunk")) for p in pool],
                        cut=round(max(S["min_score"], S["relative_cutoff"] * best), 4))
    parent_rows = st.q("SELECT count(*) FROM report WHERE %s = ANY(l1_codes)", ("ICE",))
    T["example"]["parent_reports"] = parent_rows[0][0]

    # 5. retrieval modes, per live candidate --------------------------------------------------------
    res = json.load(open(a.results))["results"]
    live = [r for r in res if r["status"] != "merged"]
    modes = [("Whole report · hybrid", dict(units="report", retrieval="linear", lexical="fts"), 0.6),
             ("Chunks · hybrid", dict(units="chunks", retrieval="linear", lexical="fts"), 0.6),
             ("Chunks · vector only", dict(units="chunks", retrieval="linear", lexical="fts"), 1.0),
             ("Chunks · keyword only", dict(units="chunks", retrieval="linear", lexical="fts"), 0.0),
             ("Whole report · RRF", dict(units="report", retrieval="rrf", lexical="fts"), 0.6)]
    table, tops = [], {}
    t0 = time.time()
    prev = json.loads(pathlib.Path(a.out).read_text()).get("modes") if a.skip_modes and pathlib.Path(a.out).exists() else None
    for r in ([] if prev else live):
        c = cands[r["candidate_id"]]
        par = (r.get("output") or {}).get("parent_code")
        text = f"{c['name']}. {c['definition']}"
        row = dict(id=r["candidate_id"], name=r["name"], parent=par, status=r["status"], modes={})
        for label, cfg, w in modes:
            st.units, st.retrieval, st.lexical = cfg["units"], cfg["retrieval"], cfg["lexical"]
            hits = st.reports_hybrid(c["embedding"], text, w, limit=10)
            keys = [h["report_key"] for h in hits]
            tops[(r["candidate_id"], label)] = keys
            row["modes"][label] = dict(agree=round(sum(1 for h in hits if par in h["l1_codes"]) / max(len(hits), 1), 3),
                                       kinds={k: sum(1 for h in hits if h.get("chunk") == k) for k in ("summary", "findings", "narrative")})
        base = tops[(r["candidate_id"], "Chunks · hybrid")]
        for label, _, _ in modes:
            o = tops[(r["candidate_id"], label)]
            row["modes"][label]["overlap"] = round(len(set(o) & set(base)) / max(len(set(o) | set(base)), 1), 3)
        table.append(row)
    st.units, st.retrieval, st.lexical = "chunks", "linear", "fts"
    T["modes"] = prev or dict(labels=[m[0] for m in modes], rows=table, seconds=round(time.time() - t0, 1),
                      mean_agree={m[0]: round(float(np.mean([r["modes"][m[0]]["agree"] for r in table])), 3) for m in modes},
                      mean_overlap={m[0]: round(float(np.mean([r["modes"][m[0]]["overlap"] for r in table])), 3) for m in modes})

    # 6. the shown run: which chunk kind carried support, and how deep the evidence goes -----------------
    kinds_sup, depth = {}, []
    for r in live:
        d = r.get("diag") or {}
        for s in d.get("support", []):
            kinds_sup[s.get("chunk") or "report"] = kinds_sup.get(s.get("chunk") or "report", 0) + 1
        depth.append(dict(id=r["candidate_id"], status=r["status"], parent=(r.get("output") or {}).get("parent_code"),
                          support=len(d.get("support", [])), relevant=d.get("relevant_under_parent"),
                          moved=len(d.get("moved_to_sibling", []))))
    T["run"] = dict(support_kinds=kinds_sup, depth=depth)
    hist_rows = []
    for item in a.history:
        label, d = item.split("=", 1)
        j = json.load(open(pathlib.Path(d) / "grounding_results.json"))
        cnt = {}
        for r in j["results"]:
            cnt[r["status"]] = cnt.get(r["status"], 0) + 1
        hist_rows.append(dict(label=label, run=pathlib.Path(d).name, candidates=len(j["results"]), units=j["settings"].get("units"),
                              refill=bool(j["settings"].get("support_refill")), counts=cnt,
                              definitions=j.get("summary", {}).get("definitions")))
    T["history"] = hist_rows
    pathlib.Path(a.out).write_text(json.dumps(T, separators=(",", ":")))
    print(a.out, f"{pathlib.Path(a.out).stat().st_size / 1e6:.2f} MB", "modes in", T["modes"]["seconds"], "s")


if __name__ == "__main__":
    main()

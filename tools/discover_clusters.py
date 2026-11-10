"""Data-driven discovery aid: cluster real reports inside each CICTT parent and describe each cluster by its
distinctive words (class TF-IDF) and its most common coded findings, so new candidate buckets can be drafted.
Output is a worksheet for a discovery author or SME; it never writes candidates itself."""
import argparse, collections, json, pathlib, re, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from taxground.store import Store  # noqa: E402

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--db", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--parents", default="LOC-I,LOC-G,SCF-PP,FUEL,RE,ARC,CFIT,SCF-NP,UIMC,LALT,MAC,GCOL,ICE,TURB,CTOL,WILD")
    ap.add_argument("--k", type=int, default=6); ap.add_argument("--min_size", type=int, default=40)
    a = ap.parse_args()
    from sklearn.cluster import KMeans
    from sklearn.feature_extraction.text import TfidfVectorizer
    st = Store(a.db); out = []
    for par in a.parents.split(","):
        rows = st.q("SELECT report_key, embedding, findings, narrative FROM report WHERE %s = ANY(l1_codes) AND evidence_level <> 'none'", (par,))
        if len(rows) < a.k * a.min_size:
            continue
        X = np.array([np.asarray(r[1].to_numpy() if hasattr(r[1], "to_numpy") else r[1]) for r in rows])
        km = KMeans(n_clusters=a.k, n_init=5, random_state=7).fit(X)
        docs = [" ".join(r[3] for r, l in zip(rows, km.labels_) if l == c) for c in range(a.k)]
        tv = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=40000, sublinear_tf=True, min_df=1)
        M = tv.fit_transform(docs); vocab = np.array(tv.get_feature_names_out())
        for c in range(a.k):
            idx = [i for i, l in enumerate(km.labels_) if l == c]
            if len(idx) < a.min_size:
                continue
            terms = [t for t in vocab[np.argsort(-M[c].toarray()[0])[:40]] if not re.search(r"\d", t)][:14]
            fnd = collections.Counter()
            for i in idx:
                for line in re.findall(r"(?:Cause|Contributing factor|Finding): ([^.]+)", rows[i][2]):
                    fnd[" - ".join(line.split("-")[:4])] += 1
            cen = km.cluster_centers_[c]; near = sorted(idx, key=lambda i: -float(X[i] @ cen))[:3]
            out.append(dict(parent=par, cluster=c, size=len(idx), terms=terms, findings=fnd.most_common(5),
                            examples=[dict(key=rows[i][0], text=rows[i][3][:260]) for i in near]))
    pathlib.Path(a.out).write_text(json.dumps(out, indent=1))
    for o in out:
        print(f"{o['parent']}#{o['cluster']} n={o['size']} | {', '.join(o['terms'][:10])}\n   " + " || ".join(f"{f} ({n})" for f, n in o['findings'][:3]))

if __name__ == "__main__":
    main()

"""PostgreSQL + pgvector store: working set, retrieval primitives, run record and release store."""
import json
import re

import numpy as np

from . import text as T

WORKING_TABLES = ["icao_category", "industry_definition", "report", "report_sentence", "report_chunk", "candidate"]
CHUNK_CHARS = 1100


def event_header(r):
    m = r.get("meta") or {}
    parts = [r["report_key"], m.get("date"), " ".join(x for x in (m.get("make"), m.get("model")) if x),
             ("Part " + m["part"].lstrip("0")) if m.get("part") else "", m.get("injury"), r.get("phase")]
    return "[" + " | ".join(p for p in parts if p) + "]"


def pack(text, limit=CHUNK_CHARS):
    """Sentence-packed pieces of about `limit` characters; a sentence is never split."""
    out, cur = [], ""
    for s in T.sentences(text):
        if cur and len(cur) + 1 + len(s) > limit:
            out.append(cur); cur = s
        else:
            cur = (cur + " " + s).strip()
    if cur:
        out.append(cur)
    return out


def chunks_for(r):
    """Section-aware chunks: summary (probable cause), findings (coded causes and factors), narrative pieces."""
    sec = r.get("sections") or {}
    out = []
    if sec.get("summary"):
        out.append(("summary", sec["summary"]))
    if r.get("findings"):
        out.append(("findings", r["findings"]))
    body = sec.get("analysis") if sec else r["narrative"]
    for piece in pack(body or ("" if sec else r["narrative"])):
        out.append(("narrative", piece))
    return out or [("narrative", r["narrative"])]


class Store:
    def __init__(self, dsn):
        import psycopg
        from pgvector.psycopg import register_vector
        self.conn = psycopg.connect(dsn, autocommit=True)
        self.conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
        register_vector(self.conn)

    def q(self, sql, params=()):
        with self.conn.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall() if cur.description else []

    # ------------------------------------------------------------------ schema + working set
    def ensure_schema(self, schema_sql, dim):
        # Working-set tables are rebuilt each run from recorded inputs (vector size can change with the embedder);
        # run-record and release-store tables are created once and only ever appended to.
        self.conn.execute("DROP TABLE IF EXISTS " + ", ".join(WORKING_TABLES) + " CASCADE")
        self.conn.execute(schema_sql.replace("{DIM}", str(dim)))

    def load_working_set(self, emb, parents, definitions, reports, candidates, version, header=True):
        pv = emb.encode([f"{p['name']}. {p['definition']}" for p in parents])
        for p, v in zip(parents, pv):
            self.q("INSERT INTO icao_category VALUES (%s,%s,%s,%s,%s,%s,%s)",
                   (p["code"], p["name"], p["definition"], p["in_scope"], p.get("co_code_only", False), version, v))
        dv = emb.encode([T.normalise(f"{d['term']}. {d['text']}") for d in definitions])
        for d, v in zip(definitions, dv):
            self.q("INSERT INTO industry_definition (def_id, source, term, body, parents, version, embedding) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                   (d["id"], d["source"], d["term"], d["text"], d["parents"], version, v))
        norms = [T.normalise(r["narrative"]) for r in reports]
        # contextual header (both decks): every embedded piece carries its report's phase and source codes
        hdr = {r["report_key"]: T.normalise(f"[{r.get('phase') or ''} | {r.get('source_codes') or ''}]") if header else "" for r in reports}
        vstr = lambda v: "[" + ",".join(f"{x:.6f}" for x in v) + "]"
        B = 2000                                   # bulk COPY in batches: real corpora have ~1M sentences
        with self.conn.cursor() as cur:
            for i in range(0, len(reports), B):
                chunk, nchunk = reports[i:i + B], norms[i:i + B]
                rv = emb.encode([f"{hdr[r['report_key']]} {n}".strip() for r, n in zip(chunk, nchunk)])
                sent_rows, sent_txt = [], []
                chunk_rows = []
                with cur.copy("""COPY report (report_key, source_id, event_id, report_class, evidence_level, phase, l1_codes,
                                 source_codes, narrative, findings, norm_text, embedding) FROM STDIN""") as cp:
                    for r, n, v in zip(chunk, nchunk, rv):
                        lane, level = T.route_report(r)
                        r["_lane"], r["_level"] = lane, level
                        cp.write_row((r["report_key"], r["source_id"], r.get("event_id") or r["report_key"], lane, level,
                                      r.get("phase"), r["l1_codes"], r.get("source_codes", ""), r["narrative"],
                                      r.get("findings", ""), n, vstr(v)))
                        quotable = T.sentences(r["narrative"])[:self.max_sentences] + T.sentences(r.get("findings", ""))
                        for j, sx in enumerate(quotable):
                            sent_rows.append((r["report_key"], j, sx)); sent_txt.append(T.normalise(sx))
                        h = event_header(r)
                        for j, (kind, body) in enumerate(chunks_for(r)):
                            chunk_rows.append((r["report_key"], j, kind, h, body, T.normalise(body)))
                if chunk_rows:
                    cvv = emb.encode([f"{T.normalise(h)} {nb}" for (_, _, _, h, _, nb) in chunk_rows])
                    with cur.copy("COPY report_chunk (report_key, seq, kind, header, body, norm_text, embedding) FROM STDIN") as cp:
                        for row, v in zip(chunk_rows, cvv):
                            cp.write_row(row + (vstr(v),))
                if sent_rows:
                    sv = emb.encode([f"{hdr[k]} {x}".strip() for (k, _, _), x in zip(sent_rows, sent_txt)])
                    with cur.copy("COPY report_sentence (report_key, seq, sentence, norm_text, embedding) FROM STDIN") as cp:
                        for (k, j, sx), n2, v in zip(sent_rows, sent_txt, sv):
                            cp.write_row((k, j, sx, n2, vstr(v)))
        self.build_bm25({r["report_key"]: f"{r['narrative']} {r.get('findings') or ''} {r.get('source_codes') or ''}" for r in reports})
        cv = emb.encode([T.normalise(f"{c['name']}. {c['definition']}") for c in candidates]) if candidates else []
        for c, v in zip(candidates, cv):
            self.q("INSERT INTO candidate VALUES (%s,%s,%s,%s,%s,%s)",
                   (c["candidate_id"], c["batch"], c["name"], c["definition"], c.get("proposed_parent"), v))

    # ------------------------------------------------------------------ retrieval primitives
    def parent_fit(self, vec):
        return self.q("""SELECT code, name, definition, 1 - (embedding <=> %s) AS cos FROM icao_category
                         WHERE in_scope AND NOT co_code_only ORDER BY embedding <=> %s, code""", (vec, vec))

    units = "report"          # report: one vector per report | chunks: section-aware chunks, best chunk per report
    max_sentences = 80        # sentences indexed per report for evidence quotes (quotes stay verbatim)
    retrieval = "linear"      # linear: w*cos + (1-w)*keyword (trial) | rrf: RRF fusion + coverage/phrase rerank (RAG deck s.8)
    lexical = "fts"           # fts: PostgreSQL full text (ts_rank_cd) | bm25: Okapi BM25 over the run's report index

    # ------------------------------------------------------------------ Okapi BM25 (k1=1.2, b=0.75)
    def build_bm25(self, docs, k1=1.2, b=0.75):
        import collections, math
        toks = {k: [T.stem(w) for w in T.content_words(t)] for k, t in docs.items()}
        df = collections.Counter(w for ws in toks.values() for w in set(ws))
        n = len(toks)
        self._bm = dict(tf={k: collections.Counter(ws) for k, ws in toks.items()}, dl={k: len(ws) for k, ws in toks.items()},
                        idf={w: math.log(1 + (n - d + 0.5) / (d + 0.5)) for w, d in df.items()},
                        avgdl=sum(len(ws) for ws in toks.values()) / max(n, 1), k1=k1, b=b)

    def bm25(self, text, keys):
        m = self._bm
        q = [T.stem(w) for w in T.content_words(text)]
        out = {}
        for k in keys:
            tf, dl, sc = m["tf"][k], m["dl"][k], 0.0
            for w in q:
                f = tf.get(w, 0)
                if f:
                    sc += m["idf"][w] * f * (m["k1"] + 1) / (f + m["k1"] * (1 - m["b"] + m["b"] * dl / m["avgdl"]))
            out[k] = sc
        return out


    def reports_hybrid(self, vec, text, w, parent=None, limit=10, exclude=(), support_only=False):
        if self.units == "chunks":
            return self.reports_chunks(vec, text, w, parent, limit, exclude, support_only)
        if self.retrieval == "rrf":
            return self.reports_rrf(vec, text, w, parent, limit, exclude, support_only)
        if self.lexical == "bm25":
            return self.reports_linear_bm25(vec, text, w, parent, limit, exclude, support_only)
        conds, params = [], [vec, T.keyword_query(text)]
        if parent:
            conds.append("l1_codes @> %s"); params.append([parent])
        if exclude:
            conds.append("NOT (report_key = ANY(%s))"); params.append(list(exclude))
        if support_only:
            conds.append("evidence_level <> 'none'")
        where = ("WHERE " + " AND ".join(conds)) if conds else ""
        params.append(limit)
        rows = self.q(f"""
            WITH s AS (
              SELECT report_key, l1_codes, narrative, event_id, source_id, 1 - (embedding <=> %s) AS cos,
                     ts_rank_cd(tsv, to_tsquery('english', %s)) AS kw
              FROM report {where})
            SELECT report_key, l1_codes, narrative, event_id, cos, kw,
                   {w} * cos + {1 - w} * coalesce(kw / NULLIF(max(kw) OVER (), 0), 0) AS score, source_id
            FROM s ORDER BY score DESC, report_key LIMIT %s""", params)
        return [dict(report_key=r[0], l1_codes=list(r[1]), narrative=r[2], event_id=r[3], cos=float(r[4]),
                     kw=float(r[5]), score=round(float(r[6]), 6), source_id=r[7]) for r in rows]

    def _filtered(self, parent, exclude, support_only):
        conds, params = [], []
        if parent:
            conds.append("l1_codes @> %s"); params.append([parent])
        if exclude:
            conds.append("NOT (report_key = ANY(%s))"); params.append(list(exclude))
        if support_only:
            conds.append("evidence_level <> 'none'")
        return (" AND ".join(conds) if conds else "TRUE"), params

    def reports_linear_bm25(self, vec, text, w, parent=None, limit=10, exclude=(), support_only=False):
        where, params = self._filtered(parent, exclude, support_only)
        rows = self.q(f"""SELECT report_key, l1_codes, narrative, event_id, 1 - (embedding <=> %s), source_id FROM report WHERE {where}""",
                      [vec] + params)
        bm = self.bm25(text, [r[0] for r in rows])
        top = max(bm.values(), default=0.0) or 1.0
        out = [dict(report_key=r[0], l1_codes=list(r[1]), narrative=r[2], event_id=r[3], cos=float(r[4]), kw=round(bm[r[0]], 4),
                    score=round(w * float(r[4]) + (1 - w) * bm[r[0]] / top, 6), source_id=r[5]) for r in rows]
        out.sort(key=lambda r: (-r["score"], r["report_key"]))
        return out[:limit]

    def reports_chunks(self, vec, text, w, parent=None, limit=10, exclude=(), support_only=False, per_channel=1000):
        """Section-aware retrieval. Two channels nominate chunks, the 1,000 nearest by vector and the 1,000 best
        full-text matches (GIN index); the hybrid score (0.6 cosine + 0.4 keyword rank normalised within the query)
        is computed on their union; each report takes its best chunk, and the kind of that chunk is kept."""
        conds, params = [], []
        if parent:
            conds.append("r.l1_codes @> %s"); params.append([parent])
        if exclude:
            conds.append("NOT (r.report_key = ANY(%s))"); params.append(list(exclude))
        if support_only:
            conds.append("r.evidence_level <> 'none'")
        where = " AND ".join(conds) if conds else "TRUE"
        kq = T.keyword_query(text)
        rows = self.q(f"""
            WITH q AS (SELECT to_tsquery('english', %s) AS tq),
            dense AS (SELECT ch.report_key, ch.seq FROM report_chunk ch JOIN report r ON r.report_key = ch.report_key
                      WHERE {where} ORDER BY ch.embedding <=> %s LIMIT {per_channel}),
            lex AS (SELECT ch.report_key, ch.seq FROM report_chunk ch JOIN report r ON r.report_key = ch.report_key, q
                    WHERE {where} AND ch.tsv @@ q.tq ORDER BY ts_rank_cd(ch.tsv, q.tq) DESC LIMIT {per_channel}),
            cand AS (SELECT * FROM dense UNION SELECT * FROM lex),
            c AS (SELECT ch.report_key, ch.kind, 1 - (ch.embedding <=> %s) AS cos, ts_rank_cd(ch.tsv, q.tq) AS kw
                  FROM cand JOIN report_chunk ch USING (report_key, seq), q),
            s AS (SELECT report_key, kind, cos, kw, {w} * cos + {1 - w} * coalesce(kw / NULLIF(max(kw) OVER (), 0), 0) AS score FROM c),
            b AS (SELECT DISTINCT ON (report_key) report_key, kind, cos, kw, score FROM s ORDER BY report_key, score DESC, kind)
            SELECT b.report_key, r.l1_codes, r.narrative, r.event_id, b.cos, b.kw, b.score, r.source_id, b.kind
            FROM b JOIN report r ON r.report_key = b.report_key ORDER BY b.score DESC, b.report_key LIMIT %s""",
            [kq] + params + [vec] + params + [vec, limit])
        return [dict(report_key=x[0], l1_codes=list(x[1]), narrative=x[2], event_id=x[3], cos=float(x[4]), kw=float(x[5]),
                     score=round(float(x[6]), 6), source_id=x[7], chunk=x[8]) for x in rows]

    def reports_rrf(self, vec, text, w, parent=None, limit=10, exclude=(), support_only=False, k=60, per_channel=200):
        """Two retrievers each nominate up to 200 candidates (pgvector cosine; PostgreSQL full text), weighted reciprocal
        rank fusion merges them, then a rerank adds query-term coverage and phrase matches:
            score = ( RRF/max + 0.6*coverage + 0.4*phrase ) / 2          (scaled to 0..1)"""
        conds, params = [], []
        if parent:
            conds.append("l1_codes @> %s"); params.append([parent])
        if exclude:
            conds.append("NOT (report_key = ANY(%s))"); params.append(list(exclude))
        if support_only:
            conds.append("evidence_level <> 'none'")
        where = " AND ".join(conds) if conds else "TRUE"
        kq = T.keyword_query(text)
        dense = self.q(f"""SELECT report_key FROM report WHERE {where} ORDER BY embedding <=> %s, report_key LIMIT %s""", params + [vec, per_channel])
        if self.lexical == "bm25":
            keys = [r[0] for r in self.q(f"SELECT report_key FROM report WHERE {where}", params)]
            bm = self.bm25(text, keys)
            lex = [(k,) for k, v in sorted(bm.items(), key=lambda kv: (-kv[1], kv[0])) if v > 0][:per_channel]
        else:
            lex = self.q(f"""SELECT report_key FROM (SELECT report_key, ts_rank_cd(tsv, to_tsquery('english', %s)) kw FROM report WHERE {where}) s
                             WHERE kw > 0 ORDER BY kw DESC, report_key LIMIT %s""", [kq] + params + [per_channel])
        fused = {}
        for wt, rows in ((w, dense), (1 - w, lex)):
            for rank, (key,) in enumerate(rows, 1):
                fused[key] = fused.get(key, 0.0) + wt / (k + rank)
        if not fused:
            return []
        rows = self.q("""SELECT report_key, l1_codes, narrative, event_id, norm_text, 1 - (embedding <=> %s), source_id
                         FROM report WHERE report_key = ANY(%s)""", (vec, list(fused)))
        qw = [T.stem(x) for x in T.content_words(text)]
        qset, pairs = set(qw), {(a, b) for a, b in zip(qw, qw[1:])}
        top = max(fused.values())
        out = []
        for key, l1, narr, ev, norm, cos, src in rows:
            dw = [T.stem(x) for x in re.findall(r"[a-z][a-z\-]+", norm) if x not in T.STOP and len(x) > 2]
            cov = len(qset & set(dw)) / len(qset) if qset else 0.0
            phr = len(pairs & set(zip(dw, dw[1:]))) / len(pairs) if pairs else 0.0
            sc = (fused[key] / top + 0.6 * cov + 0.4 * phr) / 2
            out.append(dict(report_key=key, l1_codes=list(l1), narrative=narr, event_id=ev, cos=float(cos), kw=round(cov, 4), score=round(sc, 6), source_id=src))
        out.sort(key=lambda r: (-r["score"], r["report_key"]))
        return out[:limit]

    def definitions_for(self, vec, text, w, parent=None, limit=5, exclude=()):
        conds, params = [], [vec, T.keyword_query(text)]
        if parent:
            conds.append("parents @> %s"); params.append([parent])
        if exclude:
            conds.append("NOT (def_id = ANY(%s))"); params.append(list(exclude))
        where = ("WHERE " + " AND ".join(conds)) if conds else ""
        params.append(limit)
        rows = self.q(f"""
            WITH s AS (
              SELECT def_id, source, term, body, parents, 1 - (embedding <=> %s) AS cos,
                     ts_rank_cd(tsv, to_tsquery('english', %s)) AS kw
              FROM industry_definition {where})
            SELECT def_id, source, term, body, parents, cos,
                   {w} * cos + {1 - w} * coalesce(kw / NULLIF(max(kw) OVER (), 0), 0) AS score
            FROM s ORDER BY score DESC, def_id LIMIT %s""", params)
        return [dict(def_id=r[0], source=r[1], term=r[2], body=r[3], parents=list(r[4]), cos=float(r[5]),
                     score=float(r[6])) for r in rows]

    def best_sentence(self, vec, report_key, text=""):
        rows = self.q("""SELECT sentence, 1 - (embedding <=> %s),
                                ts_rank_cd(to_tsvector('english', norm_text), to_tsquery('english', %s)), seq
                         FROM report_sentence WHERE report_key = %s ORDER BY seq""", (vec, T.keyword_query(text), report_key))
        if not rows:
            return "", 0.0
        top_kw = max(float(r[2]) for r in rows) or 1.0
        best = max(rows, key=lambda r: (round(0.5 * float(r[1]) + 0.5 * float(r[2]) / top_kw, 6), -r[3]))
        return best[0], float(best[1])

    def candidates(self):
        rows = self.q("SELECT candidate_id, batch, name, definition, proposed_parent, embedding FROM candidate ORDER BY candidate_id")
        return [dict(candidate_id=r[0], batch=r[1], name=r[2], definition=r[3], proposed_parent=r[4],
                     embedding=np.asarray(r[5].to_numpy(), dtype=np.float32)) for r in rows]

    def lookup(self):
        """Closed sets the verifier checks against."""
        parents = {r[0]: dict(name=r[1], in_scope=r[2], co_code_only=r[3], definition=r[4])
                   for r in self.q("SELECT code, name, in_scope, co_code_only, definition FROM icao_category")}
        defs = {r[0]: dict(parents=list(r[1]), term=r[2], source=r[3], body=r[4])
                for r in self.q("SELECT def_id, parents, term, source, body FROM industry_definition")}
        reps = {r[0]: dict(l1=list(r[1]), text=r[2] + ("\n" + r[6] if r[6] else ""), level=r[3], lane=r[4], event_id=r[5])
                for r in self.q("SELECT report_key, l1_codes, narrative, evidence_level, report_class, event_id, findings FROM report")}
        return parents, defs, reps

    # ------------------------------------------------------------------ release store
    def sme_decisions(self, candidate_ids=None):
        rows = self.q("""SELECT decision_id, reviewed_run_id, reviewed_version, candidate_id, action, target_type, target_id,
                                value, reviewer, rationale, prompting_report, decided_at
                         FROM sme_decision WHERE superseded_by IS NULL ORDER BY decided_at, decision_id""")
        keys = ["decision_id", "reviewed_run_id", "reviewed_version", "candidate_id", "action", "target_type", "target_id",
                "value", "reviewer", "rationale", "prompting_report", "decided_at"]
        out = [dict(zip(keys, r)) for r in rows]
        return [d for d in out if candidate_ids is None or d["candidate_id"] in candidate_ids]

    def last_run(self, dataset, before=None):
        rows = self.q("""SELECT run_id, input_hash, settings_hash, code_version, output_hash FROM pipeline_run
                         WHERE dataset = %s AND output_hash IS NOT NULL AND (%s::text IS NULL OR run_id < %s)
                         ORDER BY run_id DESC LIMIT 1""", (dataset, before, before))
        return dict(zip(["run_id", "input_hash", "settings_hash", "code_version", "output_hash"], rows[0])) if rows else None

    def latest_release(self):
        rows = self.q("SELECT version, run_id FROM taxonomy_release ORDER BY approved_at DESC LIMIT 1")
        return dict(version=rows[0][0], run_id=rows[0][1]) if rows else None

    def run_links(self, run_id):
        rows = self.q("""SELECT subject_id, link_type, object_id, evidence_quote FROM grounding_link WHERE run_id = %s""", (run_id,))
        return rows

    def run_results(self, run_id):
        return {r[0]: dict(parent=r[1], status=r[2], merged_into=r[3])
                for r in self.q("SELECT candidate_id, parent_code, status, merged_into FROM grounding_result WHERE run_id = %s", (run_id,))}

    def run_cards(self, run_id):
        return self.q("SELECT candidate_id, kind, text, cite_type, cite_id FROM criteria_card WHERE run_id = %s", (run_id,))


def jdump(x):
    return json.dumps(x, default=str, sort_keys=True)


def safe_id(s):
    return re.sub(r"[^A-Za-z0-9_.:-]", "_", s)

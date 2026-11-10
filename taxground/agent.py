"""Escalation agent for candidates that fail a blocking check (document §4.4, GR-11).

Bounded by design: a fixed tool list, at most S['agent_max_calls'] calls per candidate, every call logged,
and it can never publish or change a bucket: what it finds becomes proposals (add a link, merge with a sibling,
more data needed) in the SME review pack. An SME who accepts one records add_link / merge, the next run reads
that decision back, and the same checks G1–G10 verify the result. The planner here is deterministic (no model is available in this environment); an approved
LLM can replace `plan()` behind the same tool interface and budget.
"""
from .ground import relevant

TOOLS = ("search_reports", "read_report", "search_definitions", "propose_merge", "request_more_data")


class Budget(Exception):
    pass


class AgentSession:
    def __init__(self, store, cand, out, diag, S, rejected):
        self.store, self.cand, self.S, self.rejected = store, cand, S, rejected
        self.out = {k: (list(v) if isinstance(v, list) else v) for k, v in out.items()}
        self.out["supporting_reports"] = [dict(s) for s in out["supporting_reports"]]
        self.diag, self.calls, self.proposals = diag, [], []

    def call(self, tool, **args):
        assert tool in TOOLS
        if len(self.calls) >= self.S["agent_max_calls"]:
            raise Budget()
        res = getattr(self, "_" + tool)(**args)
        self.calls.append(dict(tool=tool, args=args, result=res))
        return res

    # ---- tools
    def _search_reports(self, parent, k):
        have = {s["report_key"] for s in self.out["supporting_reports"]}
        moved = {m["report_key"] for m in self.diag.get("moved_to_sibling", [])}
        hits = self.store.reports_hybrid(self.diag["query_vec"], self.diag["query_text"], self.S["vector_weight"],
                                         parent=parent, limit=k, exclude=self.rejected | have | moved, support_only=True)
        # only near-misses of the relative cut-off: at least agent_relative x the bucket's weakest kept support
        kept = [s["score"] for s in self.diag.get("support", [])] or [0.0]
        floor = max(self.S["min_score"], self.S["agent_relative"] * max(kept))
        hits = [h for h in hits if h["score"] >= floor]
        return [dict(report_key=h["report_key"], score=round(h["score"], 4)) for h in hits]

    def _read_report(self, report_key):
        q, cos = self.store.best_sentence(self.diag["query_vec"], report_key, self.diag["query_text"])
        return dict(report_key=report_key, evidence=q, sentence_cos=round(cos, 4))

    def _search_definitions(self, parent):
        ds = self.store.definitions_for(self.diag["query_vec"], self.diag["query_text"], self.S["vector_weight"], parent=parent, limit=3)
        return [dict(def_id=d["def_id"], score=round(d["score"], 4)) for d in ds if d["score"] >= self.S["min_score"]]

    def _propose_merge(self, other):
        self.proposals.append(dict(action="merge", target_id=other))
        return dict(proposed="merge", with_=other)

    def _request_more_data(self, reason):
        self.proposals.append(dict(action="request_more_data", reason=reason))
        return dict(requested=reason)


def plan(sess, failed):
    """Deterministic planner: fix what failed, inside the budget."""
    p = sess.out["parent_code"]
    try:
        if "G2" in failed:
            for d in sess.call("search_definitions", parent=p)[: sess.S["max_definitions"]]:
                if d["def_id"] not in sess.out["definition_ids"]:
                    sess.proposals.append(dict(action="add_link", target_type="definition", target_id=d["def_id"], score=d["score"]))
        if "G5" in failed:
            moved = sess.diag.get("moved_to_sibling", [])
            if moved:
                sib = max({m["to"] for m in moved}, key=lambda s: (sum(m["to"] == s for m in moved), s))
                sess.call("propose_merge", other=sib)
            need = sess.S["min_support"] - len(sess.out["supporting_reports"])
            hits = sess.call("search_reports", parent=p, k=sess.S["agent_pool"])
            for h in hits:
                if need <= 0:
                    break
                r = sess.call("read_report", report_key=h["report_key"])
                if r["evidence"]:            # a proposal for the SME, never a link: the agent cannot change the bucket
                    sess.proposals.append(dict(action="add_link", target_type="report", target_id=r["report_key"],
                                               value=r["evidence"], score=h["score"]))
                    need -= 1
            if need > 0:
                sess.call("request_more_data", reason=f"{need} more supporting report(s) under {p} needed for G5")
        if not ({"G2", "G5"} & failed):
            sess.call("request_more_data", reason="blocking checks " + ", ".join(sorted(failed)) + " need SME or discovery input")
    except Budget:
        pass
    return sess

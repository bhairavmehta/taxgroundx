"""Deterministic verifier. The same checks apply to rules output, LLM output and agent output (GR-7).

G1–G8 are the trial checks. G9 and G10 are new:
  G9  criteria card is grounded: >=1 inclusion from the parent or a crosswalked definition, >=1 exclusion,
      >=1 linked example; every citation resolves; every quote is verbatim (SRS-TAX-03)
  G10 SME decisions read back from the release store are honoured: no rejected link reappears, a parent
      set by an SME is used, SME-added links are present (SRS-TAX-04)
"""
from dataclasses import dataclass, asdict


@dataclass
class Check:
    id: str
    name: str
    passed: bool
    detail: str
    severity: str = "block"     # block -> not grounded; review -> needs SME review

    def to_dict(self):
        return asdict(self)


def verify(output, lookup, S, proposed_parent=None, diag=None, card=None, sme=(), candidate_ids=()):
    parents, defs, reps = lookup
    p = output.get("parent_code")
    checks = []
    ok_parent = p in parents and parents[p]["in_scope"] and not parents[p]["co_code_only"]
    checks.append(Check("G1", "Parent is an allowed CICTT category", ok_parent, f"parent = {p}"))

    ids = output.get("definition_ids", [])
    bad_defs = [d for d in ids if d not in defs]
    wrong_x = [d for d in ids if d in defs and p not in defs[d]["parents"]]
    n_defs = len(ids) - len(bad_defs) - len(wrong_x)
    checks.append(Check("G2", "Definitions exist and are crosswalked to the parent",
                        not bad_defs and not wrong_x and n_defs >= 1 and len(ids) <= S["max_definitions"] + 2,
                        f"{n_defs} valid" + (f"; unknown {bad_defs}" if bad_defs else "") +
                        (f"; not crosswalked to {p}: {wrong_x}" if wrong_x else "")))

    sup = output.get("supporting_reports", [])
    bad_keys = [s["report_key"] for s in sup if s["report_key"] not in reps]
    not_quoted = [s["report_key"] for s in sup if s["report_key"] in reps
                  and (len(s.get("evidence", "")) < 10 or s["evidence"] not in reps[s["report_key"]]["text"])]
    off_parent = [s["report_key"] for s in sup if s["report_key"] in reps and p not in reps[s["report_key"]]["l1"]]
    no_evid = [s["report_key"] for s in sup if s["report_key"] in reps and reps[s["report_key"]]["level"] == "none"]
    checks.append(Check("G3", "Every report exists, is coded to the parent and carries evidence",
                        not bad_keys and not off_parent and not no_evid,
                        "ok" if not (bad_keys or off_parent or no_evid) else
                        f"unknown {bad_keys}; not under {p}: {off_parent}; notification-only: {no_evid}"))
    checks.append(Check("G4", "Evidence is quoted word for word", not not_quoted,
                        "all quotes found in the raw report text" if not not_quoted else f"not found in report: {not_quoted}"))
    valid = {s["report_key"] for s in sup} - set(bad_keys + not_quoted + off_parent + no_evid)
    events = {reps[k]["event_id"] for k in valid}
    cap = output.get("max_reports", S["max_reports"])
    checks.append(Check("G5", f"At least {S['min_support']} supporting events (at most {cap})",
                        S["min_support"] <= len(events) and len(sup) <= cap, f"{len(events)} valid events, {len(sup)} links"))

    if diag is not None:
        agree = diag["parent_agreement"]
        checks.append(Check("G6", "Evidence sits under the parent (agreement)", agree >= S["min_parent_agreement"],
                            f"{agree:.0%} of the closest reports are coded {p}", "review"))
        checks.append(Check("G7", "Clear winner among parents", diag["margin"] >= S["parent_margin"],
                            f"margin {diag['margin']:.2f} over {diag['runner_up']}", "review"))
    if proposed_parent:
        sme_set = diag is not None and diag.get("parent_forced_by_sme")
        checks.append(Check("G8", "Matches the parent proposed by discovery (or set by an SME)",
                            p == proposed_parent or bool(sme_set),
                            f"proposed {proposed_parent}, grounded {p}" + (" (SME set parent)" if sme_set else ""), "review"))

    if card is not None:
        checks.append(check_card(card, output, lookup, candidate_ids, sme))
    if sme:
        checks.append(check_sme(output, sme))

    if any(not c.passed and c.severity == "block" for c in checks):
        status = "not_grounded"
    elif any(not c.passed for c in checks):
        status = "needs_review"
    else:
        status = "grounded"
    return status, checks


def check_card(card, output, lookup, candidate_ids, sme):
    parents, defs, reps = lookup
    p = output["parent_code"]
    support = {s["report_key"] for s in output.get("supporting_reports", [])}
    sme_ids = {d["decision_id"] for d in sme}
    problems = []
    for c in card:
        t, i = c["cite_type"], c["cite_id"]
        if t == "parent" and i not in parents:
            problems.append(f"unknown parent {i}")
        elif t == "definition":
            if i not in defs:
                problems.append(f"unknown definition {i}")
            elif c["kind"] == "include" and p not in defs[i]["parents"]:
                problems.append(f"inclusion {i} not crosswalked to {p}")
            elif c["kind"] == "exclude" and p in defs[i]["parents"]:
                problems.append(f"exclusion {i} is crosswalked to {p}")
        elif t == "report":
            if i not in reps:
                problems.append(f"unknown report {i}")
            elif not c.get("quote") or c["quote"] not in reps[i]["text"]:
                problems.append(f"quote for {i} not verbatim")
            elif c["kind"] in ("include", "example_pos") and i not in support:
                problems.append(f"{c['kind']} cites {i}, which is not a supporting report")
            elif c["kind"] == "exclude" and i in support:
                problems.append(f"exclusion cites supporting report {i}")
        elif t in ("candidate", "sibling") and i not in candidate_ids:
            problems.append(f"unknown bucket {i}")
        elif t == "sme" and i not in sme_ids:
            problems.append(f"unknown SME decision {i}")
    n_inc = sum(c["kind"] == "include" and c["cite_type"] in ("parent", "definition", "sme") for c in card)
    n_exc = sum(c["kind"] in ("exclude", "boundary") for c in card)
    n_ex = sum(c["kind"] == "example_pos" for c in card)
    if not (n_inc and n_exc and n_ex):
        problems.append(f"needs inclusion, exclusion and example (have {n_inc}/{n_exc}/{n_ex})")
    return Check("G9", "Criteria card is complete and every citation resolves", not problems,
                 f"{len(card)} entries: {n_inc} grounded inclusions, {n_exc} exclusions, {n_ex} examples" if not problems
                 else "; ".join(problems[:4]))


def check_sme(output, sme):
    problems = []
    links = {("report", s["report_key"]) for s in output.get("supporting_reports", [])} | \
            {("definition", d) for d in output.get("definition_ids", [])}
    for d in sme:
        if d["action"] == "reject_link" and (d["target_type"], d["target_id"]) in links:
            problems.append(f"{d['decision_id']}: rejected {d['target_type']} {d['target_id']} is back")
        if d["action"] == "add_link" and (d["target_type"], d["target_id"]) not in links:
            problems.append(f"{d['decision_id']}: SME-added {d['target_type']} {d['target_id']} is missing")
        if d["action"] == "set_parent" and output.get("parent_code") != d["target_id"]:
            problems.append(f"{d['decision_id']}: SME parent {d['target_id']} not used")
    applied = [d for d in sme if d["action"] in ("reject_link", "add_link", "set_parent", "add_criterion", "remove_criterion")]
    return Check("G10", "SME decisions from the release store are honoured", not problems,
                 f"{len(applied)} decision(s) applied" if not problems else "; ".join(problems[:3]))

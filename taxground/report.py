"""Self-contained HTML review pack for one run: hierarchy, criteria cards, checks, changelog, guardrails,
and an SME decision sheet that produces the CSV `taxground review` imports (SRS-EVL-01 / SRS-TAX-04)."""
import html
import json

CSS = r"""
/* Layout: sticky summary band, then a two-pane workbench (hierarchy rail | bucket detail) that stacks on phones. */
:root{
  --bg:#f4f6f8; --panel:#ffffff; --ink:#14202c; --muted:#56657a; --line:#d6dde5; --sunk:#e9eef3;
  --accent:#1f5f8b; --accent-ink:#ffffff; --accent-soft:#dce9f3;
  --ok:#1d6b45; --ok-soft:#dcefe4; --warn:#8a5a00; --warn-soft:#f6ead1; --bad:#a3271f; --bad-soft:#f6dcd9; --info:#4b4f9c; --info-soft:#e3e4f5;
  --f-head:'Barlow Semi Condensed','Arial Narrow',Arial,sans-serif; --f-body:'IBM Plex Sans',system-ui,Arial,sans-serif; --f-mono:'IBM Plex Mono',ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --bg:#0f161d; --panel:#16202a; --ink:#e4ebf2; --muted:#9aa9b9; --line:#2a3846; --sunk:#1c2834;
  --accent:#7fb6dc; --accent-ink:#0f161d; --accent-soft:#1d3346;
  --ok:#6fcf9b; --ok-soft:#173528; --warn:#e5b45a; --warn-soft:#3a2c12; --bad:#f08a80; --bad-soft:#40201d; --info:#a9adf0; --info-soft:#26284a; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0f161d; --panel:#16202a; --ink:#e4ebf2; --muted:#9aa9b9; --line:#2a3846; --sunk:#1c2834;
  --accent:#7fb6dc; --accent-ink:#0f161d; --accent-soft:#1d3346;
  --ok:#6fcf9b; --ok-soft:#173528; --warn:#e5b45a; --warn-soft:#3a2c12; --bad:#f08a80; --bad-soft:#40201d; --info:#a9adf0; --info-soft:#26284a; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.5 var(--f-body);margin:0}
.wrap{max-width:1280px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:20px 48px;display:flex;flex-direction:column;gap:20px}
h1,h2,h3{font-family:var(--f-head);margin:0;text-wrap:balance;letter-spacing:.2px}
h1{font-size:30px;font-weight:600} h2{font-size:22px;font-weight:600} h3{font-size:17px;font-weight:600}
.mono{font-family:var(--f-mono);font-size:12.5px}
.label{font-size:11.5px;letter-spacing:1.2px;text-transform:uppercase;color:var(--muted);font-weight:600}
.muted{color:var(--muted)}
header.top{display:flex;flex-wrap:wrap;gap:12px 28px;align-items:flex-end;justify-content:space-between}
.meta{display:flex;flex-wrap:wrap;gap:6px 18px;color:var(--muted);font-size:13px}
.meta b{color:var(--ink);font-weight:500}
.band{display:flex;flex-wrap:wrap;gap:1px;background:var(--line);border:1px solid var(--line);border-radius:8px;overflow:hidden}
.band>div{background:var(--panel);padding:12px 14px;display:flex;flex-direction:column;gap:2px;min-width:0;flex:1 1 130px}
.band .v{font-family:var(--f-head);font-size:24px;font-weight:600;font-variant-numeric:tabular-nums}
.reqs{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.req{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:14px 16px;display:flex;flex-direction:column;gap:6px;min-width:0}
.req .hd{display:flex;justify-content:space-between;gap:8px;align-items:center}
.pill{display:inline-flex;align-items:center;gap:4px;padding:1px 9px;border-radius:999px;font-size:12px;font-weight:600;white-space:nowrap}
.p-grounded,.p-pass,.p-met{background:var(--ok-soft);color:var(--ok)}
.p-needs_review,.p-review{background:var(--warn-soft);color:var(--warn)}
.p-not_grounded,.p-fail,.p-gap{background:var(--bad-soft);color:var(--bad)}
.p-merged,.p-abstain{background:var(--info-soft);color:var(--info)}
nav.tabs{display:flex;gap:4px;flex-wrap:wrap;border-bottom:1px solid var(--line)}
nav.tabs button{font:600 14px var(--f-body);color:var(--muted);background:none;border:0;border-bottom:3px solid transparent;padding:8px 12px;cursor:pointer}
nav.tabs button[aria-selected="true"]{color:var(--ink);border-bottom-color:var(--accent)}
button:focus-visible,select:focus-visible,input:focus-visible,textarea:focus-visible,a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.bench{display:grid;grid-template-columns:300px minmax(0,1fr);gap:16px;align-items:start}
@media (max-width:820px){.bench{grid-template-columns:minmax(0,1fr)}}
.rail{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:8px;display:flex;flex-direction:column;gap:2px;max-height:78vh;overflow:auto}
.rail .par{padding:8px 8px 2px;display:flex;justify-content:space-between;gap:6px}
.rail button{all:unset;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:8px;padding:6px 8px;border-radius:6px;font-size:13.5px}
.rail button:hover{background:var(--sunk)}
.rail button[aria-current="true"]{background:var(--accent-soft)}
.rail button .nm{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.dot{width:9px;height:9px;border-radius:50%;flex:none}
.d-grounded{background:var(--ok)} .d-needs_review{background:var(--warn)} .d-not_grounded{background:var(--bad)} .d-merged,.d-abstain{background:var(--info)}
.detail{display:flex;flex-direction:column;gap:14px;min-width:0}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;min-width:0}
.chain{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:13.5px}
.chain .node{background:var(--sunk);border-radius:6px;padding:4px 10px}
.chain .arr{color:var(--muted)}
.crit{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px}
@media (max-width:700px){.crit{grid-template-columns:minmax(0,1fr)}}
ul.cl{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
ul.cl li{display:flex;flex-direction:column;gap:3px;padding-left:12px;border-left:3px solid var(--line)}
ul.cl.inc li{border-left-color:var(--ok)} ul.cl.exc li{border-left-color:var(--bad)}
.cite{font-family:var(--f-mono);font-size:11.5px;color:var(--accent)}
blockquote{margin:0;padding:4px 10px;background:var(--sunk);border-radius:4px;font-size:13.5px}
.tblwrap{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--panel)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:11.5px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);background:var(--sunk);font-weight:600}
td.num{font-variant-numeric:tabular-nums}
.checks{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:6px}
.chk{display:flex;gap:8px;align-items:flex-start;font-size:13px;padding:6px 8px;border-radius:6px;background:var(--sunk)}
.chk b{font-family:var(--f-mono);font-size:12px}
.sme{display:flex;flex-direction:column;gap:8px}
.sme select{font:13px var(--f-body);padding:3px 6px;border:1px solid var(--line);border-radius:5px;background:var(--panel);color:var(--ink)}
.row{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
input[type=text],textarea{font:13px var(--f-body);padding:6px 8px;border:1px solid var(--line);border-radius:6px;background:var(--panel);color:var(--ink)}
textarea{width:100%;min-height:140px;font-family:var(--f-mono);font-size:12px}
.btn{font:600 13px var(--f-body);background:var(--accent);color:var(--accent-ink);border:0;border-radius:6px;padding:7px 14px;cursor:pointer}
.btn.ghost{background:var(--sunk);color:var(--ink)}
.note{font-size:13px;color:var(--muted)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = r"""
const D = JSON.parse(document.getElementById('data').textContent);
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const label = s => ({grounded:'Grounded',needs_review:'Needs review',not_grounded:'Not grounded',merged:'Merged',abstain:'Abstained'}[s] || s);
const decisions = new Map();
let current = null;

function rail(){
  const byParent = {};
  D.results.forEach(r => { const p = r.status === 'merged' ? 'Merged before grounding' : (r.output.parent_code || 'None'); (byParent[p] = byParent[p] || []).push(r); });
  const keys = Object.keys(byParent).sort((a,b) => (a.startsWith('Merged') ? 1 : 0) - (b.startsWith('Merged') ? 1 : 0) || a.localeCompare(b));
  $('#rail').innerHTML = keys.map(p => {
    const pname = (D.parents[p] || {}).name || '';
    return `<div class="par"><span class="label">${esc(p)} ${esc(pname)}</span><span class="label">${byParent[p].length}</span></div>` +
      byParent[p].map(r => `<button data-id="${esc(r.candidate_id)}" aria-current="${r.candidate_id===current}">
        <span class="nm"><span class="mono">${esc(r.candidate_id)}</span> ${esc(r.name)}</span><span class="dot d-${r.status}" title="${label(r.status)}"></span></button>`).join('');
  }).join('');
  $('#rail').querySelectorAll('button').forEach(b => b.onclick = () => show(b.dataset.id));
}

function sel(cid, type, id){
  const k = `${cid}|${type}|${id}`, v = decisions.get(k)?.action || '';
  const opts = type === 'criterion' ? ['', 'accept', 'remove_criterion'] : type === 'parent' ? ['', 'accept', 'approve_bucket'] : ['', 'accept', 'reject_link'];
  return `<select data-k="${esc(k)}" aria-label="SME decision for ${esc(type)} ${esc(id)}">${opts.map(o => `<option value="${o}" ${o===v?'selected':''}>${o || '—'}</option>`).join('')}</select>`;
}

function show(cid){
  current = cid; rail();
  const r = D.results.find(x => x.candidate_id === cid);
  const o = r.output, P = D.parents, card = r.card || [];
  if (r.status === 'merged') {
    $('#detail').innerHTML = `<div class="panel"><div class="row"><h2>${esc(r.candidate_id)} · ${esc(r.name)}</h2><span class="pill p-merged">Merged</span></div>
      <p>Folded into <button class="btn ghost" data-go="${esc(r.merged_into)}">${esc(r.merged_into)}</button> before grounding: both batches describe the same events
      (similarity ${esc(r.diag.merge_score ?? '')}). To keep them apart, record <span class="mono">keep_separate</span> in the SME sheet.</p>
      <p class="muted">${esc(r.definition)}</p></div>`;
    $('#detail').querySelector('[data-go]').onclick = e => show(e.target.dataset.go);
    return;
  }
  const inc = card.filter(c => c.kind === 'include'), exc = card.filter(c => c.kind === 'exclude' || c.kind === 'boundary'), ex = card.filter(c => c.kind === 'example_pos');
  const cl = list => list.map(c => `<li><span>${esc(c.text)}</span><span class="cite">${esc(c.cite_type)}:${esc(c.cite_id)}${c.origin==='sme'?' · SME':''}</span>
      ${c.quote && c.cite_type==='report' && c.kind!=='example_pos' ? `<blockquote>${esc(c.quote)}</blockquote>` : ''}<span>${sel(cid,'criterion',c.key)}</span></li>`).join('');
  const defs = o.definition_ids.map(d => `<tr><td class="mono">${esc(d)}</td><td>${esc((D.defs[d]||{}).term)}</td><td class="muted">${esc((D.defs[d]||{}).source)}</td><td>${sel(cid,'definition',d)}</td></tr>`).join('');
  const reps = ex.map(c => `<tr><td class="mono">${esc(c.cite_id)}</td><td>${esc(c.quote)}</td><td>${sel(cid,'report',c.cite_id)}</td></tr>`).join('');
  const checks = r.checks.map(c => `<div class="chk"><span class="pill ${c.passed?'p-pass':(c.severity==='block'?'p-fail':'p-review')}">${c.passed?'pass':(c.severity==='block'?'block':'review')}</span>
      <span><b>${esc(c.id)}</b> ${esc(c.name)}<br><span class="muted">${esc(c.detail)}</span></span></div>`).join('');
  const moved = (r.diag.moved_to_sibling||[]).map(m => `${m.report_key} → ${m.to}`).join(', ');
  const agent = (r.agent_calls||[]).map((a,i) => `<tr><td class="num">${i+1}</td><td class="mono">${esc(a.tool)}</td><td class="mono">${esc(JSON.stringify(a.args))}</td></tr>`).join('');
  $('#detail').innerHTML = `
  <div class="panel">
    <div class="row" style="justify-content:space-between"><h2>${esc(r.candidate_id)} · ${esc(r.name)}</h2>
      <span class="row"><span class="pill p-${r.status}">${label(r.status)}</span><span class="muted" style="font-size:13px">${esc(r.outcome.replace(/_/g,' '))}</span></span></div>
    <p style="margin:0">${esc(r.definition)}</p>
    <div class="chain"><span class="node"><span class="label">Bucket</span> ${esc(cid)}${r.aliases.length?' + '+esc(r.aliases.join(', ')):''}</span><span class="arr">→</span>
      <span class="node"><span class="label">ICAO parent</span> ${esc(o.parent_code)} ${esc((P[o.parent_code]||{}).name)} ${sel(cid,'parent',o.parent_code)}</span><span class="arr">→</span>
      <span class="node"><span class="label">Definitions</span> ${o.definition_ids.length}</span><span class="arr">→</span>
      <span class="node"><span class="label">Reports</span> ${o.supporting_reports.length}</span></div>
    <div class="note">Proposed by discovery: ${esc(r.proposed_parent)} · parent scores ${esc(JSON.stringify(r.diag.parent_scores))} · agreement ${Math.round((r.diag.parent_agreement||0)*100)}%${moved?` · given to siblings: ${esc(moved)}`:''}</div>
  </div>
  <div class="panel"><h3>Criteria card</h3>
    <div class="crit"><div><div class="label">Include when</div><ul class="cl inc">${cl(inc)}</ul></div>
    <div><div class="label">Exclude when</div><ul class="cl exc">${cl(exc)}</ul></div></div></div>
  <div class="panel"><h3>Industry definitions</h3><div class="tblwrap"><table><tr><th>Id</th><th>Term</th><th>Source</th><th>SME</th></tr>${defs || '<tr><td colspan="4">None</td></tr>'}</table></div></div>
  <div class="panel"><h3>Linked example reports</h3><div class="tblwrap"><table><tr><th>Report</th><th>Evidence, quoted word for word</th><th>SME</th></tr>${reps || '<tr><td colspan="3">None</td></tr>'}</table></div></div>
  <div class="panel"><h3>Checks</h3><div class="checks">${checks}</div></div>
  ${agent ? `<div class="panel"><h3>Escalation agent · ${r.agent_calls.length} of ${D.settings.agent_max_calls} calls</h3><div class="tblwrap"><table><tr><th>#</th><th>Tool</th><th>Arguments</th></tr>${agent}</table></div>
    <div class="note">Proposals: ${esc(JSON.stringify(r.proposals))}. The agent cannot publish: a rescued bucket goes to SME review.</div></div>` : ''}`;
  $('#detail').querySelectorAll('select').forEach(s => s.onchange = () => {
    const [c, t, id] = s.dataset.k.split('|'); const tid = s.dataset.k.slice(c.length + t.length + 2);
    if (s.value) decisions.set(s.dataset.k, {candidate_id:c, action:s.value, target_type:t, target_id:tid}); else decisions.delete(s.dataset.k);
    sheet();
  });
}

function sheet(){
  const rows = [['reviewed_run_id','candidate_id','action','target_type','target_id','value','rationale','prompting_report']];
  decisions.forEach(d => rows.push([D.summary.run_id, d.candidate_id, d.action, d.target_type, d.target_id, '', $('#why').value, '']));
  $('#csv').value = rows.map(r => r.map(v => /[",\n]/.test(v) ? `"${String(v).replace(/"/g,'""')}"` : v).join(',')).join('\n');
  $('#count').textContent = `${decisions.size} decision${decisions.size===1?'':'s'}`;
}

function tabs(){
  document.querySelectorAll('nav.tabs button').forEach(b => b.onclick = () => {
    document.querySelectorAll('nav.tabs button').forEach(x => x.setAttribute('aria-selected', x === b));
    document.querySelectorAll('section[data-tab]').forEach(s => s.hidden = s.dataset.tab !== b.dataset.tab);
  });
}

$('#copy').onclick = async () => {
  try { await navigator.clipboard.writeText($('#csv').value); $('#copied').textContent = 'Copied. Save it as decisions.csv and run taxground review.'; }
  catch(e){ $('#csv').select(); $('#copied').textContent = 'Copy blocked here: the sheet is selected, press Ctrl+C or Cmd+C.'; }
};
$('#why').oninput = sheet;
tabs(); rail();
show((D.results.find(r => r.status === 'needs_review') || D.results[0]).candidate_id); sheet();
"""


def write_review_pack(out, summary, results, hierarchy, revisions, guards, lookup):
    parents, defs, reps = lookup
    slim = []
    for r in results:
        slim.append(dict(candidate_id=r["candidate_id"], name=r["name"], definition=r["definition"], status=r["status"],
                         outcome=r["outcome"], proposed_parent=r["proposed_parent"], aliases=r["aliases"],
                         merged_into=r.get("merged_into"), output=r["output"], card=r["card"], checks=r["checks"],
                         agent_calls=[dict(tool=a["tool"], args=a["args"]) for a in r["agent_calls"]], proposals=r["proposals"],
                         diag={k: r["diag"].get(k) for k in ("parent_scores", "parent_agreement", "moved_to_sibling", "merge_score")}))
    from .ground import DEFAULT_SETTINGS
    data = dict(summary=summary, results=slim, parents={k: dict(name=v["name"]) for k, v in parents.items()},
                defs={k: dict(term=v["term"], source=v["source"]) for k, v in defs.items()}, settings=DEFAULT_SETTINGS)
    m, st = summary["metrics"], summary["status"]
    live = [r for r in results if r["status"] not in ("merged",)]
    carded = [r for r in live if r["card"] and any(c["id"] == "G9" and c["passed"] for c in r["checks"])]
    n_links = sum(1 + len(r["output"]["definition_ids"]) + len(r["output"]["supporting_reports"]) for r in live if r["output"]["parent_code"])
    reqs = [
        ("SRS-TAX-01", "Ground every bucket",
         f"{len([r for r in live if r['output']['parent_code']])} buckets traced to one CICTT parent, crosswalked definitions and coded reports with verbatim quotes; {n_links} SSSOM-style link rows.",
         "met"),
        ("SRS-TAX-02", "Bounded, re-runnable pipeline",
         f"One command from recorded inputs; closed sets, agent capped at {DEFAULT_SETTINGS['agent_max_calls']} calls; versioned hierarchy {summary['taxonomy_version']}; output hash {summary['output_hash'][:12]}.",
         "met"),
        ("SRS-TAX-03", "Criteria and examples",
         f"{len(carded)} of {len(live)} buckets carry a verified criteria card (definition, parent, include and exclude criteria, linked examples; G9).",
         "met" if len(carded) == len(live) else "gap"),
        ("SRS-TAX-04", "Test reports, record revisions",
         f"{summary['sme_decisions_read']} SME decisions read back; {summary['revisions']} revisions vs previous run, each with a cause; report testing with `taxground test`.",
         "met"),
    ]
    band = [("Buckets", len(live)), ("Grounded", st["grounded"]), ("Needs review", st["needs_review"]),
            ("Not grounded", st["not_grounded"]), ("Merged", st["merged"]),
            ("Parents correct", m["parent_correct"]) if m["answer_key"] else ("Parents", "—"),
            ("Report precision", f"{m['merge_precision']:.0%}" if m["merge_precision"] is not None else "—"),
            ("Report recall", f"{m['merge_recall']:.0%}" if m["merge_recall"] is not None else "—"),
            ("Guardrails blocked", summary["guardrails_blocked"])]
    rev_rows = "".join(f"<tr><td class='mono'>{html.escape(v['candidate_id'])}</td><td>{html.escape(v['change_type'])}</td><td class='mono'>{html.escape(str(v['target']))}</td>"
                       f"<td>{html.escape(str(v['before'] or ''))}</td><td>{html.escape(str(v['after'] or ''))}</td><td><span class='pill p-{'met' if v['cause_type'] in ('sme','report') else 'review'}'>{html.escape(v['cause_type'])}</span></td>"
                       f"<td class='mono'>{html.escape(v['cause_ref'])}</td></tr>" for v in revisions)
    g_rows = "".join(f"<tr><td>{html.escape(g['test'])}</td><td><span class='pill p-{'pass' if g['blocked'] else 'fail'}'>{'blocked' if g['blocked'] else 'NOT blocked'}</span></td>"
                     f"<td class='mono'>{html.escape(g['failed_checks'])}</td></tr>" for g in guards)
    page = f"""<title>Bucket Review Pack</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Semi+Condensed:wght@500;600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header class="top">
  <div style="display:flex;flex-direction:column;gap:4px;min-width:0">
    <span class="label">OBJ-2 · Risk-category taxonomy · SME review pack</span>
    <h1>Taxonomy {html.escape(summary['taxonomy_version'])}</h1>
    <div class="meta"><span>Run <b class="mono">{html.escape(summary['run_id'])}</b></span><span>Selector <b>{html.escape(summary['selector'])}</b></span>
      <span>Embedder <b>{html.escape(summary['embedder'])}</b></span><span>Code <b class="mono">{html.escape(summary['code_version'])}</b></span>
      <span>Base release <b>{html.escape((summary['base_release'] or {}).get('version', 'none') if summary['base_release'] else 'none')}</b></span></div>
  </div>
  <div class="note" style="max-width:420px">Reports in this pack are synthetic trial data. Definitions are paraphrases. Nothing here is published until an SME approves a release.</div>
</header>
<div class="band">{''.join(f'<div><span class="label">{k}</span><span class="v">{html.escape(str(v))}</span></div>' for k, v in band)}</div>
<div class="reqs">{''.join(f'<div class="req"><div class="hd"><h3>{i} · {t}</h3><span class="pill p-{s}">{s.upper()}</span></div><span style="font-size:13.5px">{html.escape(e)}</span></div>' for i, t, e, s in reqs)}</div>
<nav class="tabs" role="tablist">
  <button data-tab="buckets" aria-selected="true">Buckets</button><button data-tab="changes" aria-selected="false">Changelog ({len(revisions)})</button>
  <button data-tab="guards" aria-selected="false">Guardrails</button><button data-tab="sheet" aria-selected="false">SME decision sheet <span id="count" class="muted"></span></button>
</nav>
<section data-tab="buckets"><div class="bench"><div class="rail" id="rail" aria-label="Taxonomy hierarchy"></div><div class="detail" id="detail"></div></div></section>
<section data-tab="changes" hidden><div class="panel"><h3>Revisions against {html.escape(summary['previous_run'] or 'no previous run')}</h3>
  <p class="note">Every change names its cause: an SME decision (with the report that prompted it, if any), a new report, an input change, a settings change or a code change. Equal inputs, settings and code reproduce the same output hash, so “none” never appears on a clean rerun.</p>
  {'<div class="tblwrap"><table><tr><th>Bucket</th><th>Change</th><th>Target</th><th>Before</th><th>After</th><th>Cause</th><th>Reference</th></tr>' + rev_rows + '</table></div>' if revisions else '<p>No revisions in this run.</p>'}</div></section>
<section data-tab="guards" hidden><div class="panel"><h3>Faulty answers run through the same verifier</h3>
  <p class="note">Each test takes a grounded bucket and adds one fault an unconstrained model might produce. Every one must be blocked.</p>
  <div class="tblwrap"><table><tr><th>Fault</th><th>Result</th><th>Checks that failed</th></tr>{g_rows}</table></div></div></section>
<section data-tab="sheet" hidden><div class="panel sme"><h3>SME decisions for this run</h3>
  <p class="note">Pick decisions on the bucket pages (accept, reject a link, remove a criterion, approve a bucket). They collect here as CSV. Save it as <span class="mono">decisions.csv</span> and run <span class="mono">taxground review --file decisions.csv --reviewer "Your name"</span>. The next run reads them back and records each change in the changelog.</p>
  <label for="why" class="label">Rationale for these decisions</label><input type="text" id="why" placeholder="e.g. hold-short events belong to the crossing bucket">
  <textarea id="csv" aria-label="Decision CSV" readonly></textarea>
  <div class="row"><button class="btn" id="copy">Copy CSV</button><span id="copied" class="note"></span></div></div></section>
</div>
<script type="application/json" id="data">{json.dumps(data, default=str).replace('</', '<\\/')}</script>
<script>{JS}</script>
"""
    (out / "review_pack.html").write_text(page, encoding="utf-8")

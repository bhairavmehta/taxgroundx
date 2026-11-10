# taxground: unified taxonomy grounding pipeline (OBJ-2)

One bounded, re-runnable pipeline that takes candidate risk-category buckets from discovery and produces a **versioned
category hierarchy**. Each bucket is grounded to one ICAO/CICTT parent, its crosswalked industry definitions and coded
reports with word-for-word evidence. Each bucket also gets a verified **criteria card** (include and exclude criteria,
linked examples). SME decisions are written to a release store and read back on the next run. Every revision is traced
to the SME input or report that prompted it, and new reports can be tested against any taxonomy version.

It merges three sources into one codebase:
- the **grounding_trial toolkit** (retrieve → constrain → verify G1–G8 on pgvector);
- the **RAG and Grounding Methodology** deck (route → retrieve → answer → verify → decide, release gate, audit);
- the **Embedding NTSB Reports** deck (route records by type, raw text as the citation source, hybrid lexical + dense
  retrieval, grouping by event, label provenance, gold-set gating).

> All reports are **synthetic** (from the trial package). Definitions are paraphrases. The embedder is a local stand-in
> (TF-IDF + SVD) because no model can be downloaded here. Results show the method works end to end. They do not
> measure accuracy on real data.

## Requirements coverage (SR&O v2, §4.2 and §5)

| Requirement | Status | How the pipeline meets it | Evidence in a run folder |
|---|---|---|---|
| **SRS-TAX-01** Ground each bucket to its ICAO parent, industry definitions and supporting reports | Met | Closed-set choice. G1 checks the parent is in scope (not co-code-only). G2 checks definitions exist and are crosswalked to it. G3 checks reports are coded to the parent, notification-only records excluded. G4 checks quotes are verbatim from raw text. G5 checks enough distinct events. One SSSOM-style row per link (`skos:broadMatch` / `skos:relatedMatch` / `sssom:hasSupportingEvidence`, with justification, confidence, tool version, reviewer). | `links.sssom.tsv`, `grounding_link` table, `criteria_cards.md` |
| **SRS-TAX-02** Bounded, re-runnable pipeline producing a versioned hierarchy with criteria and linked examples | Met | `taxground run` reads recorded inputs (snapshotted and hashed) and rebuilds the working set in pgvector. Output is a CICTT L1 → L2 bucket hierarchy whose version id is the hash of its content. Equal inputs, settings, code and SME decisions give the same output hash, and the gate checks this. Bounded by closed sets, caps (12 reports, 3 definitions) and a 5-call agent that cannot publish. | `taxonomy.json`, `manifest.json`, `pipeline_run` table, `gate.json` |
| **SRS-TAX-03** Each bucket has a definition, include/exclude criteria, parent and linked example reports | **Met (was Partial)** | Criteria cards are now produced for every bucket and verified by **G9**. Each card needs at least one inclusion from the parent or a crosswalked definition, at least one exclusion and at least one example. Every citation must resolve, and every quote must be verbatim. Exclusions come from siblings that received the bucket's reports, near-miss reports coded to other parents, definitions crosswalked elsewhere, and the runner-up parent. | `criteria_cards.md`, `criteria_card` table, review pack |
| **SRS-TAX-04** Test reports against each taxonomy version; record revisions traceable to the prompting report or SME input | Met | `taxground test --version v1.0` scores new reports against exactly that version's buckets and applies their exclusion criteria. The verdict is fits / ambiguous / excluded / no_fit / out_of_scope, and anything other than "fits" becomes a revision prompt. `taxground review` imports SME decisions (validated against the run reviewed, with `prompting_report`). The next run reads them back (**G10** checks they are honoured). Each change is written to `revision` with its cause: an SME decision (with prompting report), a knock-on from a sibling's decision, a new report, data, settings or code. | `report_test.csv`, `revision_prompts.csv`, `changelog.md`, `sme_decision` / `revision` tables |
| NFR-TRC-01 Traceability | Met | Every link, card line and revision carries run id, code version and source ids | `grounding_link`, `revision` |
| NFR-VER-01 SME approval before publishing | Met | `taxground release` refuses buckets still under review unless an SME recorded `approve_bucket`. Releases record the approver and content hash. | `taxonomy_release`, `release-v*/taxonomy.json` |
| NFR-REP-01 Reproducibility | Met | Inputs snapshotted and hashed; deterministic embedder (fixed seed, rounded vectors); exact vector scans; tie-breaks on ids | gate check "Reproducible" |
| NFR-QAL-01 Validate every record | Met | Duplicate or empty records and unknown codes are logged. Answer-key fields (`_truth`, `expected_*`) are stripped before the pipeline sees them. | `manifest.json → validation_issues` |
| SRS-ING-03 pgvector | Met | PostgreSQL 16 + pgvector 0.8.0 (built and run locally for these results) | `db/schema.sql` |

## The pipeline, stage by stage

| # | Stage | What it does | Code |
|---|---|---|---|
| 0 | Snapshot + validate | Copy and hash inputs; validate every record; strip answer-key fields | `pipeline.load_inputs`, `text.validate_inputs` |
| 1 | Route records | Lanes: narrative, shorthand, notification (never evidence), thin, quarantined (injection text) | `text.route_report` |
| 2 | Index | pgvector (dense) + PostgreSQL full text or Okapi BM25 (lexical); raw text kept for quotes, normalized text for retrieval | `store.load_working_set`, `store.build_bm25` |
| 3 | Read back SME decisions | Active decisions from the release store, per bucket | `store.sme_decisions` |
| 4 | De-duplicate candidates | Merge mutual-best cross-batch twins (embedding cosine + overlap of retrieved reports) before grounding | `ground.dedupe` |
| 5 | Ground | Parent = 0.3 × definition fit + 0.7 × vote of closest reports. Definitions crosswalked to it. Reports coded to it, one per event. Sibling rule. Rules selector or constrained LLM. | `ground.ground_candidate`, `ground.resolve_siblings` |
| 6 | Criteria cards | Include, exclude, boundary, examples, each with one citation | `criteria.build_card` |
| 7 | Verify | G1–G8 (trial), G9 card, G10 SME decisions | `verify.verify` |
| 8 | Escalate | Bounded agent (≤5 calls, logged). Proposes links or merges to SMEs; never changes a bucket. | `agent.plan` |
| 9 | Decide | release candidate / SME review / escalated to SME / returned to discovery / abstained / merged | `pipeline.run` |
| 10 | Store | Run record, SSSOM links, cards, checks, agent calls (append-only) | `db/schema.sql` group B |
| 11 | Version + changelog | Content-hash version, hierarchy JSON, revisions with causes, review pack | `pipeline.build_hierarchy`, `pipeline.changelog`, `report.py` |

Commands:
- `review`: SME decisions into the release store.
- `release`: approved, frozen version.
- `test`: reports against a version.
- `diff`: link differences between two runs.
- `gate`: CI release gate.

## Where the two decks show up

### RAG and Grounding Methodology (38 slides)

| Slide(s) | Idea | In the pipeline |
|---|---|---|
| Plan, tiers (appendix) | Modular RAG: route → retrieve → answer → verify → decide | Stages 1–9. Answering is constrained selection from closed sets, not free text. |
| Router | Rules, not a model; abstain when out of scope | Record routing (stage 1). A bucket abstains when nothing in the corpus clears the score floor. |
| Retrieve | Pre-filter, hybrid, RRF, rerank (coverage + phrase), abstain floor | `retrieval=rrf` mode implements the slide's scoring. Parent filter as pre-filter; `min_score` floor. |
| Retrieval evidence (Lost in the Middle) | Pack strongest evidence at the edges | Edges-first ordering in the constrained prompt (`ground.build_prompt`) |
| Prompt | Answer only from evidence; JSON with ids; fallback never ungrounded | `prompts/constrained_grounding.md` + schema; the rules selector is the deterministic fallback |
| Verify flow, story-broken | Deterministic checks before judgment; inject errors to prove the checks work | G1–G10; 11 guardrail faults per run, all blocked |
| Decision | Release / caveat / block / abstain / escalate | Stage 9 outcomes |
| Control stack, layer 1 | Provenance, versioning, injection scanning | Input snapshot + hash; quarantine lane for injection text |
| Eval design, gate | Gold / silver / adversarial sets; thresholds block releases in CI | `taxground gate` (7 checks); answer keys used for evaluation only |
| Operations, governance | Versions in every log line; audit log; SME review | `pipeline_run`, SSSOM rows with tool version and reviewer, `revision` |

### Embedding NTSB Reports for Grounding & Classification (32 slides)

| Slide(s) | Idea | In the pipeline |
|---|---|---|
| Report types, notifications, router | Route every record by type before embedding; template-only notices carry little | Routing lanes; `evidence_level=none` records can never be support (G3) |
| Preprocess | Strip boilerplate, expand abbreviations, raw text stays the citation source | `text.normalise` (`normalise=append` indexes both forms); quotes always from raw text |
| Approaches, STELLA | Pair a strong dense embedder with a lexical channel (BM25) | Hybrid dense + lexical; `lexical=bm25` (Okapi) or PostgreSQL full text; `--model` for an approved embedder |
| Units, contextual | Short records are not chunked; header on each piece | Report + sentence vectors; `context_header=true` prepends phase and source codes |
| Retrieval | Hybrid → RRF → group by event → cited, checked answer | Linear or RRF fusion; one supporting report per event (G5 counts events) |
| Labels | Raw codes kept; harmonized layer records how it was mapped | Raw stage-2 codes untouched; each link records justification, tool version and reviewer; report links note raw → harmonized layer |
| Evaluation, plan, decisions | Own gold set gates every change; decide on the embedder bake-off | Gate thresholds; DG-2 embedder decision left open (stand-in used) |
| Part 3 (classification cascade, conformal sets, fine-tuning) | OBJ-3 classification | **Out of scope here** (SRS-CLS). The `test` command is the bridge: it scores reports against a version. |

## Retrieval options, measured on the three answer keys

All with the same checks. P/R are report-link precision/recall (merge-aware on the combined set).

| Setting | Trial (9) | Sample B (28) | Combined (37 → 31 after merges) | Decision |
|---|---|---|---|---|
| **Default**: linear 0.6 dense + 0.4 PostgreSQL full text, per-source cut-off | 8/9 · 97%/97% | 27/28 · 94%/93% | 29/31 · 84%/89% | Default |
| Okapi BM25 instead of full text | 9/9 · 97%/97% | 27/28 · 91%/89% | 30/31 · 86%/89% (with SMEs) | Option: mixed |
| RRF fusion + coverage/phrase rerank | 8/9 · 85–88%/93–97% | 25–27/28 · 79–80%/87–95% | 29/31 · 76–77%/88–89% | Option: lower precision on short text |
| Shorthand expansion, replace mode | 9/9 · 94%/97% | 26/28 · 91%/86% | — | Off; `append` mode available |
| Contextual header on chunks | no change | slightly lower | no change | Off with the stand-in embedder |
| Global vs per-source relative cut-off (combined) | — | — | recall 78% → 89% | Per-source (mixed report styles) |

Re-test these with the approved embedder on an SME-labelled sample. The stand-in vectors limit what the deck techniques
can show.

## Results vs the original toolkit

| Run | Toolkit (published) | Unified pipeline |
|---|---|---|
| Trial, rules | 8/9 parents · P/R 97%/97% · 6/2/1 | 8/9 · 97%/97% · 5 grounded / 3 review / 1 not grounded |
| Trial, constrained-prompt answers | 9/9 · 100%/97% | 9/9 · 100%/97% (same answers, now also checked by G9) |
| Sample B | 27/28 · 93%/90% · 20/6/2 | 27/28 · 94%/93% · 20/6/2 |
| Combined | 35/37 · 83%/79% strict (89%/84% counting overlaps) · 23/9/5 | 6 twins merged before grounding (6/6 correct) → 35/37 parents equivalent · 84%/89% merge-aware · 22/9/0 + 6 merged |
| Combined after 14 SME decisions | — | 30/31 · 86%/89% · 22/8/1 · 38 revisions, every one with a cause |
| Guardrail faults blocked | 6/6 | 11/11 (adds card and SME-decision faults) |

## Run it

```bash
pip install -r requirements.txt               # psycopg, pgvector, numpy, scikit-learn
# PostgreSQL 14+ with pgvector. Then:
export TAXGROUND_DB=postgresql://USER@HOST:5432/DB
python3 -m taxground run --data data/combined --dataset combined
python3 -m taxground test --version <run_id or release> --reports data/test_reports.json
python3 -m taxground review --file decisions.csv --reviewer "Name"     # from sme_review_template.csv or the review pack
python3 -m taxground run --data data/combined --dataset combined       # reads decisions back, writes changelog
python3 -m taxground gate --run <run_id>
python3 -m taxground release --run <run_id> --version v1.0 --approver "Name"
./demo.sh                                       # the whole lifecycle from an empty database
python3 tests/test_verify.py                    # unit tests, no database needed
```

Options:
- `--set key=value` overrides any setting in `ground.DEFAULT_SETTINGS`: `min_support=10` for production (DG-4), `lexical=bm25`, `retrieval=rrf`, `normalise=append`, `context_header=true`.
- `--selector llm-file --llm-outputs DIR` verifies saved LLM answers.
- `--selector llm-cmd --llm-cmd "..."` calls an approved model behind a command (prompt on stdin, JSON on stdout).
- `--model NAME` swaps in a sentence-transformers embedder.

Each run folder holds:

| File | Contents |
|---|---|
| `inputs/` | Recorded inputs |
| `manifest.json` | Run summary and settings |
| `grounding_results.json` | Full results |
| `grounding_table.csv` | One row per bucket |
| `links.sssom.tsv` | SSSOM-style link rows |
| `criteria_cards.md` | Criteria cards |
| `taxonomy.json` | Versioned hierarchy |
| `changelog.md` | Revisions with causes |
| `guardrail_tests.csv` | Fault tests |
| `sme_review_template.csv` | Blank SME decision sheet |
| `review_pack.html` | Self-contained reviewer page; its decision sheet produces the CSV that `review` imports |

## Real data, end to end: NTSB + ECCAIRS → viewer

Replicate from a clean machine:

```bash
./setup.sh                      # pip packages, mdb-tools, poppler, and pgvector in Docker (docker-compose.yml)
export DB="postgresql://grounding:grounding@localhost:5433/taxground"
# download avall.zip from NTSB CAROL (data.ntsb.gov → avall.zip) and the ECCAIRS 1.3.0.12 attribute 390 value list PDF
AVALL_ZIP=~/Downloads/avall.zip ECCAIRS_PDF=~/Downloads/ECCAIRS-Aviation-1.3.0.12-VL-for-AttrID-390-Events.pdf ./build_all.sh
open viewer/dist/index.html     # one self-contained page
```

The full build takes about 25 minutes on a laptop (grounding about 10, the retrieval-mode comparison about 5). It should end with 25 grounded / 22 review / 3 not grounded / 3 merged on the 53 candidates and output hash 45231e0fc8a9; a different NTSB download (newer reports) changes the counts and the hash, and the changelog says why.

One command builds everything from the two public sources:

```bash
AVALL_ZIP=~/Downloads/avall.zip \
ECCAIRS_PDF=~/Downloads/ECCAIRS-Aviation-1.3.0.12-VL-for-AttrID-390-Events.pdf \
DB="postgresql://USER@HOST:5432/DB" ./build_all.sh
```

| Step | What it does | Tool | Output |
|---|---|---|---|
| 0 checks | unit tests + three synthetic answer keys | `pytest`, `taxground run` | status, accuracy, hash per set |
| 1 export | NTSB Access tables → CSV | `mdb-export` | events, aircraft, narratives, Findings, Events_Sequence, ct_seqevt |
| 2 ingest | one report per aircraft record, findings verbalized, CICTT codes from occurrences | `tools/ingest_ntsb.py` | `data/ntsb/` (draft map `ntsb-occ-cictt-0.1`) |
| 3 eccairs | 809 ECCAIRS events parsed and crosswalked to CICTT | `pdftotext`, `tools/parse_eccairs.py`, `tools/eccairs_crosswalk.py` | definitions (draft `eccairs390-cictt-0.2`) |
| 4 holdout | test reports: true hold-out with `HOLDOUT_FROM=2026-01-01`, else the 200 most recent as a smoke test | `tools/make_test_reports.py` | `build/test_reports.json` |
| 5 discover | clusters of real reports inside each parent: distinctive words + top coded findings | `tools/discover_clusters.py` | `build/discovery_clusters.json` (needs an indexed database: after step 7 on a first build) |
| 6 candidates | 37 package candidates + discovery batch D | `tools/merge_candidates.py` | `data/ntsb/candidates.json` |
| 7 ground | index, retrieve, constrain, verify, escalate, version | `taxground run` | run folder, review pack |
| 8 twin | same inputs again; stops if the output hash differs | `taxground run`, `taxground diff` | second run folder |
| 9 review | import SME decisions (`SME_DECISIONS=file.csv`), re-run, changelog with causes | `taxground review`, `run` | `changelog.md` |
| 10 gate | seven release checks | `taxground gate` | PASS / FAIL table |
| 11 release | publish a version (`APPROVER=name`, `VERSION=v1.0`); unapproved review buckets are held back and listed | `taxground release --allow-held` | `release-<version>/taxonomy.json` |
| 12 test | score the test reports against the version | `taxground test` | `report_test.csv`, `revision_prompts.csv` |
| 13 measure | chunk and embedding geometry, worked hybrid example, retrieval modes, run history | `tools/technique_stats.py` | `viewer/data/techniques.json` |
| 14 viewer | export the run and pack one self-contained page | `tools/export_viewer.py`, `tools/pack_viewer.py` | `viewer/dist/index.html` |
| 15 derived | every derived table, estimate and statistic, traceable to its source row; formulas recalculated and cross-checked | `tools/build_derived.py`, `tools/recalc_check.py` | `derived/<run_id>/`: `derived_workbook.xlsx` (32 tabs), `csv/`, `lineage.json` |

**Derived data folder.** `derived/<run_id>/derived_workbook.xlsx` opens on an Index tab (hyperlinked, with the generator and sha256 of every source file per tab) followed by run summary and history, buckets, checks, support evidence, SSSOM links, criteria, parent scores, retrieval pools, sibling moves, merges, definitions, CICTT parents, the NTSB-occurrence and ECCAIRS crosswalks, the 27,895-report index with normalised manufacturer and root type, corpus statistics by year, manufacturer and type, chunk and embedding measurements, histogram bins, the worked hybrid example, retrieval modes, guardrails, gate, report tests, revision prompts, discovery clusters, batch D, synthetic accuracy and the changelog. Every row ends with `run_id` and `source` (file + locator, e.g. `grounding_results.json#results[7].diag.support[2]`). Summary figures and counts are live Excel formulas; `recalc_check.py` recomputes them in LibreOffice and compares each with the value computed in Python (1,321 checked, 0 mismatches on this run).

Run a subset with `STEPS="7 8 10"`; each step reads what earlier steps left on disk. Checked here end to end: steps 0–7 from `avall.zip`, then 8 (twin hash 45231e0fc8a9 reproduced), 10 (gate passed), 11 (25 buckets released, 22 held back), 12 (200 reports: 51 fits, 26 ambiguous, 77 excluded, 10 no fit, 36 out of scope).

Settings for the build: `MIN_SUPPORT` (10), `UNITS` (chunks), `FROM_YEAR` (2008), `CHECK=0` to skip step 0, `SKIP_MODES=1` to reuse the five-minute retrieval-mode comparison.

**Discovery aid.** `tools/discover_clusters.py` clusters real reports inside each CICTT parent (k-means on report vectors) and lists each cluster's distinctive words and most common coded findings. Batch D (16 general-aviation candidates: carburetor icing, fuel exhaustion and starvation, crosswind loss of control, ground loops, bounced and gear-up landings, pattern stalls, density altitude, wire strikes, VFR into IMC, connecting-rod failures, helicopter LTE and low rotor RPM, balloon landings, taxi collisions) was drafted from that worksheet. They are drafts for SME review.

**Support refill** (`support_refill`, on by default). Support is chosen from up to `max_reports × support_depth` (60) relevant reports under the parent, and the 12 slots are filled after second aircraft of one event are dropped and the sibling rule has given shared reports away. Before, slots that went to a sibling or a duplicate event stayed empty, so buckets with hundreds of matching reports failed G5. The evidence standard (relative cut-off, parent filter, verbatim quote) is unchanged, and the three synthetic answer keys give identical output hashes with it on or off.

**Viewer.** Tabs: Overview, Buckets, Check matrix, Parent selection, Guardrails, Reports, Try a candidate, Techniques, How it works. One filter bar applies to every tab: search, bucket status, CICTT parent, manufacturer (4,410 NTSB spellings normalised) and root aircraft type (737, 747, 172, PA28: variants folded), multi-select with select-all. Clicking any CICTT chip filters by it. The report reader colours the evidence sentence, the probable cause, coded causes, contributing factors, other findings, the sentences most relevant to the bucket and the bucket's words, each switchable. The Techniques tab explains embedding, chunking, hybrid retrieval, the cut-off, parent choice, support, de-duplication and checks with charts computed from the run's database.

## Known limits

- **Synthetic data, stand-in embedder, settings tuned on the same samples.** Rerun on the ~500-report SME-labelled sample (Document §10) before trusting any number.
- **The SME exclusion added to B13 doesn't catch TEST-003 under v1.0.** That release held B15 back, and the stand-in embedder doesn't score the SME's free-text exclusion strongly enough. With B15 approved, TEST-003 goes to B15.
- **De-duplication found 6 of the 9 twin pairs in the answer key.** It missed C8/B14 and C9/B22, and C2's other twin B01. Merges are deliberately strict (mutual best + threshold) and SMEs can force `merge` or `keep_separate`.
- **The agent's proposals use the same retrieval and can be weak** (one B28 proposal quotes an unrelated sentence). They are proposals only; an SME must accept them.
- **Classification (OBJ-3), severity and risk scoring are not part of this package.**
- **The exclusion check over-fires on real data.** Testing 200 recent NTSB reports gave 77 `excluded` verdicts. Some criteria cards borrow a sibling's evidence sentence as an exclusion, and that sentence can read like an inclusion (D01 carburetor icing excludes a sentence about carburetor heat not being used). SMEs should review exclusions (`remove_criterion`) before a release is used for testing.
- **Batch D and both crosswalks are Claude's drafts.** They need SME approval (I-8) before any bucket built on them is released for use.

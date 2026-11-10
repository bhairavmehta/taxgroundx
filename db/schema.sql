-- taxground unified grounding store · schema 2.0
-- PostgreSQL 14+ with pgvector. {DIM} is replaced with the embedding size at load time.
--
-- Three groups of tables, created the same way on every run (CREATE ... IF NOT EXISTS):
--   A. Working set   – the seven grounding tables of the trial toolkit (same names), refreshed each run
--                      from the run's recorded inputs. Extra columns: raw vs normalised text, routing.
--   B. Run record    – one row per run plus every link (SSSOM-style), criteria card, check and revision.
--                      Append-only: nothing in B is updated or deleted by a later run.
--   C. Release store – SME decisions, taxonomy releases and report tests. Read back by every run.
CREATE EXTENSION IF NOT EXISTS vector;

-- ============================================================== A. working set (refreshed per run)
CREATE TABLE IF NOT EXISTS icao_category (
  code          text PRIMARY KEY,
  name          text NOT NULL,
  definition    text NOT NULL,
  in_scope      boolean NOT NULL,
  co_code_only  boolean NOT NULL DEFAULT false,
  version       text NOT NULL,
  embedding     vector({DIM}) NOT NULL
);
CREATE TABLE IF NOT EXISTS industry_definition (
  def_id     text PRIMARY KEY,
  source     text NOT NULL,
  term       text NOT NULL,
  body       text NOT NULL,
  parents    text[] NOT NULL,          -- SME-approved crosswalk (I-8)
  version    text NOT NULL,
  embedding  vector({DIM}) NOT NULL,
  tsv        tsvector GENERATED ALWAYS AS (to_tsvector('english', term || ' ' || body)) STORED
);
CREATE TABLE IF NOT EXISTS report (
  report_key     text PRIMARY KEY,       -- stable source id (SRS-ING-02)
  source_id      text NOT NULL,
  event_id       text NOT NULL,          -- multi-aircraft records share one event
  report_class   text NOT NULL,          -- routing lane (narrative | shorthand | notification | thin)
  evidence_level text NOT NULL,          -- full | thin | none: none is never used as support
  phase          text,
  l1_codes       text[] NOT NULL,        -- stage-2 Level 1 codes
  source_codes   text,
  narrative      text NOT NULL,          -- RAW text: evidence may be quoted from this ...
  findings       text NOT NULL DEFAULT '', -- ... or from the coded findings, verbalized (Cause: … Contributing factor: …)
  norm_text      text NOT NULL,          -- normalised text: used for retrieval only
  embedding      vector({DIM}) NOT NULL,
  tsv            tsvector GENERATED ALWAYS AS (to_tsvector('english', norm_text || ' ' || findings || ' ' || coalesce(source_codes, ''))) STORED
);
CREATE TABLE IF NOT EXISTS report_sentence (
  report_key  text,
  seq         int,
  sentence    text NOT NULL,             -- raw sentence, quoted verbatim
  norm_text   text NOT NULL,
  embedding   vector({DIM}) NOT NULL,
  PRIMARY KEY (report_key, seq)
);
CREATE TABLE IF NOT EXISTS candidate (
  candidate_id     text PRIMARY KEY,
  batch            text NOT NULL,
  name             text NOT NULL,
  definition       text NOT NULL,
  proposed_parent  text,
  embedding        vector({DIM}) NOT NULL
);
-- Section-aware chunks (RAG deck): a summary, a findings and ~1,100-character narrative pieces per report,
-- each prefixed with the event header so it can be retrieved and cited on its own.
CREATE TABLE IF NOT EXISTS report_chunk (
  report_key  text,
  seq         int,
  kind        text NOT NULL,          -- summary | findings | narrative
  header      text NOT NULL,          -- [key | date | aircraft | Part | injury]
  body        text NOT NULL,          -- raw text of the piece
  norm_text   text NOT NULL,
  embedding   vector({DIM}) NOT NULL,
  tsv         tsvector GENERATED ALWAYS AS (to_tsvector('english', header || ' ' || norm_text)) STORED,
  PRIMARY KEY (report_key, seq)
);
CREATE INDEX IF NOT EXISTS chunk_tsv_idx ON report_chunk USING gin (tsv);
-- grounding_result and grounding_link complete the seven trial tables; they are run-scoped (group B).

-- ============================================================== B. run record (append-only)
CREATE TABLE IF NOT EXISTS pipeline_run (
  run_id          text PRIMARY KEY,
  started_at      timestamptz NOT NULL,
  dataset         text NOT NULL,
  input_hash      text NOT NULL,         -- sha256 over the recorded input files
  input_manifest  jsonb NOT NULL,        -- file hashes, snapshot folder, report keys
  settings        jsonb NOT NULL,
  settings_hash   text NOT NULL,
  embedder        text NOT NULL,
  selector        text NOT NULL,         -- rules | llm-file | llm-cmd
  prompt_version  text NOT NULL,
  code_version    text NOT NULL,
  schema_version  text NOT NULL,
  base_release    text,                  -- taxonomy release this run revises (NULL for the first)
  sme_decisions   int NOT NULL,          -- decisions read back from the release store
  output_hash     text,                  -- sha256 of the canonical outputs: equal inputs -> equal hash
  taxonomy_version text                  -- draft version id produced by this run
);
CREATE TABLE IF NOT EXISTS grounding_result (
  run_id          text,
  candidate_id    text,
  merged_into     text,                  -- set when de-duplication folded this candidate into another
  parent_code     text,
  parent_changed  boolean,
  status          text,                  -- grounded | needs_review | not_grounded | merged | abstain
  outcome         text,                  -- release_candidate | sme_review | escalated | returned | abstained | merged
  checks          jsonb,
  diagnostics     jsonb,
  PRIMARY KEY (run_id, candidate_id)
);
-- One SSSOM-style row per link (https://mapping-commons.github.io/sssom/)
CREATE TABLE IF NOT EXISTS grounding_link (
  run_id                 text,
  subject_id             text,          -- candidate bucket id
  subject_label          text,
  predicate_id           text,          -- skos:broadMatch (parent) | skos:relatedMatch (definition) | sssom:hasSupportingEvidence (report)
  object_id              text,
  object_label           text,
  link_type              text,          -- parent | definition | report
  mapping_justification  text,          -- semapv:CompositeMatching | semapv:ManualMappingCuration
  confidence             real,
  evidence_quote         text,          -- verbatim sentence for report links
  mapping_tool           text,
  mapping_tool_version   text,
  mapping_date           date,
  author_id              text,          -- pipeline selector
  reviewer_id            text,          -- SME, when an SME decision fixed or confirmed this link
  sme_decision_id        text,
  comment                text
);
CREATE TABLE IF NOT EXISTS criteria_card (
  run_id         text,
  candidate_id   text,
  seq            int,
  kind           text,                  -- include | exclude | example_pos | example_neg | boundary
  text           text NOT NULL,
  cite_type      text NOT NULL,         -- parent | definition | report | candidate | sibling
  cite_id        text NOT NULL,
  quote          text,                  -- verbatim, when cite_type = report
  origin         text NOT NULL,         -- derived | sme
  PRIMARY KEY (run_id, candidate_id, seq)
);
CREATE TABLE IF NOT EXISTS agent_call (
  run_id        text,
  candidate_id  text,
  seq           int,
  tool          text,
  args          jsonb,
  result        jsonb,
  PRIMARY KEY (run_id, candidate_id, seq)
);
CREATE TABLE IF NOT EXISTS revision (
  run_id        text,
  prev_run_id   text,
  candidate_id  text,
  change_type   text,                   -- parent | link_added | link_removed | status | criterion_added | criterion_removed | merge
  target        text,
  before_value  text,
  after_value   text,
  cause_type    text,                   -- sme | report | data | settings | code | none
  cause_ref     text                    -- sme decision id, prompting report key, or hash pair
);

-- ============================================================== C. release store (read back every run)
CREATE TABLE IF NOT EXISTS sme_decision (
  decision_id       text PRIMARY KEY,
  reviewed_run_id   text NOT NULL,      -- the run / taxonomy version the SME was looking at
  reviewed_version  text,
  candidate_id      text NOT NULL,
  action            text NOT NULL,      -- accept | reject_link | add_link | set_parent | merge | keep_separate | add_criterion | remove_criterion | approve_bucket
  target_type       text,               -- parent | definition | report | criterion | candidate
  target_id         text,
  value             text,               -- criterion text, evidence quote, or kind
  reviewer          text NOT NULL,
  rationale         text,
  prompting_report  text,               -- report that prompted the change (SRS-TAX-04), if any
  decided_at        timestamptz NOT NULL,
  superseded_by     text
);
CREATE TABLE IF NOT EXISTS taxonomy_release (
  version       text PRIMARY KEY,
  run_id        text NOT NULL,
  status        text NOT NULL,          -- approved (published needs SME approval: NFR-VER-01)
  approved_by   text NOT NULL,
  approved_at   timestamptz NOT NULL,
  content_hash  text NOT NULL,
  buckets       int NOT NULL,
  notes         text
);
CREATE TABLE IF NOT EXISTS report_test (
  test_id        text,
  version        text,                  -- taxonomy version (release or draft run) tested against
  report_key     text,
  bucket_id      text,                  -- best bucket, or NULL
  parent_code    text,
  score          real,
  runner_up      text,
  margin         real,
  verdict        text,                  -- fits | ambiguous | excluded | no_fit | out_of_scope
  evidence_quote text,
  revision_prompt text,                 -- proposed revision when verdict is not 'fits'
  tested_at      timestamptz,
  PRIMARY KEY (test_id, report_key)
);

CREATE INDEX IF NOT EXISTS report_tsv_idx ON report USING gin (tsv);
CREATE INDEX IF NOT EXISTS report_l1_idx ON report USING gin (l1_codes);
CREATE INDEX IF NOT EXISTS def_parents_idx ON industry_definition USING gin (parents);
CREATE INDEX IF NOT EXISTS link_run_idx ON grounding_link (run_id, subject_id);
-- At scale (exact scans keep trial runs bit-for-bit reproducible):
-- CREATE INDEX ON report USING hnsw (embedding vector_cosine_ops);
-- CREATE INDEX ON report_sentence USING hnsw (embedding vector_cosine_ops);

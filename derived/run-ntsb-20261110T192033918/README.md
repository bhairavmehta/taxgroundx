# Derived data · run-ntsb-20261110T192033918

Built by `tools/build_derived.py` on 2026-11-10T19:35:04+00:00 from the run folder and its recorded inputs.

    python3 tools/build_derived.py --run out_ntsb/run-ntsb-20261110T192033918 --test out_ntsb/test-20261110T192903-v0.2-test --data data/ntsb --techniques viewer/data/techniques.json --clusters /tmp/claude-0/-home-claude/87bfed0b-0f8b-56ee-90ca-c97b355370f0/scratchpad/build/discovery_clusters.json --synthetic /tmp/claude-0/-home-claude/87bfed0b-0f8b-56ee-90ca-c97b355370f0/scratchpad/build/synthetic --history out_ntsb_rep out_ntsb --csv /tmp/claude-0/-home-claude/87bfed0b-0f8b-56ee-90ca-c97b355370f0/scratchpad/build/csv --out derived

| File | What |
|---|---|
| `derived_workbook.xlsx` | 00_Index (hyperlinked, with lineage) + 31 tabs; summary figures are live formulas |
| `csv/` | one CSV per tab, same rows |
| `lineage.json` | per table: description, row count, generator, source files with sha256 |

Every row carries `run_id` and `source` (file + locator such as `grounding_results.json#results[7].diag.support[2]`), so any number can be
traced to the record that produced it. Rebuild with `STEPS=15 ./build_all.sh`.

Tables: 01_Run_Summary, 02_Run_History, 03_Buckets, 04_Checks, 05_Support, 06_SSSOM_Links, 07_Criteria, 08_Parent_Scores, 09_Pool, 10_Sibling_Moves, 11_Merges, 12_Definitions, 13_CICTT_Parents, 14_NTSB_Occ_Map, 15_ECCAIRS_Crosswalk, 16_Reports_Index, 17_Corpus_by_Year, 18_Corpus_by_Make, 19_Corpus_by_Type, 20_Corpus_and_Chunks, 21_Distributions, 22_Hybrid_Example, 23_Retrieval_Modes, 24_Guardrails, 25_Gate, 26_Report_Tests, 27_Revision_Prompts, 28_Discovery_Clusters, 29_Batch_D, 30_Synthetic_Accuracy, 31_Changelog

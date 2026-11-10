#!/usr/bin/env bash
# taxground end to end, every step of the lifecycle:
#
#   NTSB avall.zip + ECCAIRS PDF
#     0 checks            unit tests + the three synthetic answer keys
#     1 export            NTSB Access tables -> CSV
#     2 ingest            one report per aircraft record, findings verbalized, CICTT codes from occurrences
#     3 eccairs           ECCAIRS events -> definitions crosswalked to CICTT
#     4 holdout           reports for testing (true hold-out with HOLDOUT_FROM, else a smoke-test copy)
#     5 discover          cluster reports inside each parent: worksheet for drafting candidates
#     6 candidates        package candidates + discovery batch D
#     7 ground            index, retrieve, constrain, verify, escalate, version  (run folder + review pack)
#     8 twin              same inputs again: the output hash must match (reproducibility, SRS-TAX-02)
#     9 review            import SME decisions (SME_DECISIONS=file.csv), re-run, changelog with causes
#    10 gate              seven release checks
#    11 release           publish a version with an approver (needs APPROVER; held buckets listed)
#    12 test              score the test reports against the version: fits / ambiguous / excluded / no_fit / out_of_scope
#    13 measure           technique measurements for the viewer (chunks, embedding, hybrid example, modes, history)
#    14 viewer            export the run and pack one self-contained page
#    15 derived           every derived table, estimate and statistic: derived/<run_id>/ (CSV per table, lineage.json, workbook)
#
#   AVALL_ZIP=~/Downloads/avall.zip ECCAIRS_PDF=~/Downloads/ECCAIRS-...-390-Events.pdf ./build_all.sh
#   STEPS="7 8 10" ./build_all.sh          # run only some steps (each reads what earlier steps left on disk)
#
# Needs: PostgreSQL 14+ with pgvector (docker-compose.yml), mdb-tools, poppler, python3 + requirements.txt (setup.sh).
set -euo pipefail
cd "$(dirname "$0")"

DB=${DB:-${TAXGROUND_DB:-"postgresql://grounding:grounding@localhost:5433/taxground"}}
AVALL_ZIP=${AVALL_ZIP:-}; AVALL_MDB=${AVALL_MDB:-}
ECCAIRS_PDF=${ECCAIRS_PDF:-}
FROM_YEAR=${FROM_YEAR:-2008}
HOLDOUT_FROM=${HOLDOUT_FROM:-}            # e.g. 2026-01-01: reports from that day on are held out of grounding and tested
MIN_SUPPORT=${MIN_SUPPORT:-10}            # G5 production value (DG-4)
UNITS=${UNITS:-chunks}                    # chunks | report
SETTINGS=${SETTINGS:-}                    # extra --set overrides, e.g. "lexical=bm25 retrieval=rrf"
SME_DECISIONS=${SME_DECISIONS:-}          # filled sme_review_template.csv (or the review pack's export)
REVIEWER=${REVIEWER:-"SME"}
APPROVER=${APPROVER:-}                    # name recorded on the release; release is skipped without it
VERSION=${VERSION:-"v1.0"}
WORK=${WORK:-build}; OUT=${OUT:-out_ntsb}
SKIP_MODES=${SKIP_MODES:-0}
STEPS=${STEPS:-"0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"}

say() { printf '\n\033[1;33m== %s\033[0m\n' "$*"; }
need() { command -v "$1" >/dev/null || { echo "missing: $1 ($2) — see setup.sh"; exit 1; }; }
on() { [[ " $STEPS " == *" $1 "* ]]; }
tg() { python3 -m taxground --db "$DB" "$@"; }
latest() { readlink -f "$OUT/latest" 2>/dev/null || ls -d "$OUT"/run-* | sort | tail -1; }
sets() { local a=(--set min_support="$MIN_SUPPORT" --set units="$UNITS"); for kv in $SETTINGS; do a+=(--set "$kv"); done; echo "${a[@]}"; }
need python3 "python 3.10+"
mkdir -p "$WORK/csv" data/ntsb

if on 0; then
  say "0. checks: unit tests and the three synthetic answer keys"
  python3 -m pytest -q tests
  for ds in trial sample_b combined; do
    tg --out "$WORK/synthetic" run --data "data/$ds" --dataset "$ds" | grep -o "status.*hash [0-9a-f]*" | sed "s/^/  $ds: /"
  done
fi

if on 1; then
  say "1. NTSB database -> CSV"
  need mdb-export "mdb-tools"
  if [ -z "$AVALL_MDB" ]; then
    [ -n "$AVALL_ZIP" ] || { echo "set AVALL_ZIP (NTSB CAROL avall.zip) or AVALL_MDB"; exit 1; }
    mkdir -p "$WORK/avall" && python3 -c "import zipfile,sys; zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])" "$AVALL_ZIP" "$WORK/avall"
    AVALL_MDB=$(find "$WORK/avall" -iname '*.mdb' | head -1)
  fi
  for t in events aircraft narratives Findings Events_Sequence ct_seqevt; do
    mdb-export "$AVALL_MDB" "$t" > "$WORK/csv/$t.csv"; echo "  $t exported"
  done
fi

if on 2; then
  say "2. ingest"
  python3 tools/ingest_ntsb.py --csv "$WORK/csv" --out data/ntsb --from-year "$FROM_YEAR" --candidates data/combined/candidates.json
  cp data/ntsb/candidates.json data/ntsb/candidates_package.json
fi

if on 3; then
  say "3. ECCAIRS events -> definitions crosswalked to CICTT (draft, SME approval needed)"
  if [ -n "$ECCAIRS_PDF" ]; then
    need pdftotext "poppler"
    pdftotext -layout "$ECCAIRS_PDF" "$WORK/eccairs.txt"
    python3 tools/parse_eccairs.py "$WORK/eccairs.txt" data/eccairs_events.json
  fi
  if [ -f data/eccairs_events.json ]; then python3 tools/eccairs_crosswalk.py --events data/eccairs_events.json --defs data/ntsb/industry_definitions.json
  else echo "  no ECCAIRS events (set ECCAIRS_PDF); grounding uses the package definitions only"; fi
fi

if on 4; then
  say "4. test reports"
  python3 tools/make_test_reports.py --data data/ntsb --out "$WORK/test_reports.json" ${HOLDOUT_FROM:+--holdout-from "$HOLDOUT_FROM"}
fi

if on 5; then
  say "5. discovery worksheet: clusters of real reports inside each parent"
  # needs the reports indexed: on a first build it runs against the database after step 7 instead
  if python3 -c "import sys; sys.path.insert(0,'.'); from taxground.store import Store; assert Store(sys.argv[1]).q('SELECT count(*) FROM report')[0][0] > 0" "$DB" 2>/dev/null; then
    python3 tools/discover_clusters.py --db "$DB" --out "$WORK/discovery_clusters.json" > "$WORK/discovery_clusters.txt"
    head -24 "$WORK/discovery_clusters.txt"
    echo "  full worksheet: $WORK/discovery_clusters.json (batch D in data/discovery/ was drafted from it)"
  else echo "  database not indexed yet: rerun with STEPS=5 after step 7"; fi
fi

if on 6; then
  say "6. candidates: package + discovery batch D"
  python3 tools/merge_candidates.py --base data/ntsb/candidates_package.json --add data/discovery/ntsb_batch_d.json --out data/ntsb/candidates.json
fi

if on 7; then
  say "7. ground"
  tg --out "$OUT" run --data data/ntsb --dataset ntsb $(sets)
  echo "  run: $(latest)  (review pack: $(latest)/review_pack.html)"
fi

if on 8; then
  say "8. twin run: same inputs, the hash must match"
  A=$(latest); HA=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]+'/grounding_results.json'))['summary']['output_hash'])" "$A")
  tg --out "$OUT" run --data data/ntsb --dataset ntsb $(sets) >/dev/null
  B=$(latest); HB=$(python3 -c "import json,sys; print(json.load(open(sys.argv[1]+'/grounding_results.json'))['summary']['output_hash'])" "$B")
  echo "  $(basename "$A") ${HA:0:12}"; echo "  $(basename "$B") ${HB:0:12}"
  [ "$HA" = "$HB" ] && echo "  reproducible: identical output hash" || { echo "  HASHES DIFFER"; tg diff --a "$(basename "$A")" --b "$(basename "$B")"; exit 1; }
fi

if on 9; then
  say "9. SME review"
  if [ -n "$SME_DECISIONS" ]; then
    tg --out "$OUT" review --file "$SME_DECISIONS" --reviewer "$REVIEWER"
    tg --out "$OUT" run --data data/ntsb --dataset ntsb $(sets)
    echo "  decisions read back; changelog: $(latest)/changelog.md"
  else
    echo "  no SME_DECISIONS file: reviewers fill $(latest)/sme_review_template.csv or use the review pack, then rerun with STEPS=\"9 10 11 12 14\" SME_DECISIONS=file.csv"
  fi
fi

if on 10; then
  say "10. release gate"
  tg --out "$OUT" gate --run "$(basename "$(latest)")" || echo "  gate not passed (accuracy rows need an answer key; see the table above)"
fi

TEST_AGAINST=$(basename "$(latest)")
if on 11; then
  say "11. release"
  if [ -n "$APPROVER" ]; then
    tg --out "$OUT" release --run "$(basename "$(latest)")" --version "$VERSION" --approver "$APPROVER" --allow-held
    TEST_AGAINST=$VERSION
  else echo "  no APPROVER: nothing released; testing runs against the draft $(basename "$(latest)")"; fi
fi

if on 12; then
  say "12. test reports against $TEST_AGAINST"
  [ -f "$WORK/test_reports.json" ] || python3 tools/make_test_reports.py --data data/ntsb --out "$WORK/test_reports.json"
  tg --out "$OUT" test --version "$TEST_AGAINST" --reports "$WORK/test_reports.json" | tail -12
fi

if on 13; then
  say "13. measure the techniques"
  HIST=()
  for d in $(ls -d "$OUT"/run-* 2>/dev/null | sort | tail -8); do
    [ -f "$d/grounding_results.json" ] || continue
    label=$(python3 -c "import json,sys; j=json.load(open(sys.argv[1]+'/grounding_results.json')); s=j['settings']; n=len(j['results'])
print(f\"{s.get('units','report')} · refill {'on' if s.get('support_refill') else 'off'} · {n} candidates · {j['summary'].get('sme_decisions_read',0)} SME decisions\")" "$d")
    HIST+=("$label=$d")
  done
  python3 tools/technique_stats.py --db "$DB" --results "$(latest)/grounding_results.json" --out viewer/data/techniques.json \
    --history "${HIST[@]}" $([ "$SKIP_MODES" = 1 ] && echo --skip-modes)
fi

if on 14; then
  say "14. viewer"
  python3 tools/export_viewer.py --db "$DB" --run "$(latest)" --data data/ntsb --out viewer
  python3 tools/pack_viewer.py viewer viewer/dist/index.html
fi

if on 15; then
  say "15. derived data folder and workbook (traceable to every source row)"
  TEST_DIR=$(ls -d "$OUT"/test-* 2>/dev/null | sort | tail -1 || true)
  python3 tools/build_derived.py --run "$(latest)" ${TEST_DIR:+--test "$TEST_DIR"} --data data/ntsb --techniques viewer/data/techniques.json \
    --clusters "$WORK/discovery_clusters.json" --synthetic "$WORK/synthetic" --history "$OUT" --csv "$WORK/csv" --out derived
  # LibreOffice computes the workbook's formulas so values show in any viewer; then each formula is compared with Python's value
  if command -v soffice >/dev/null || command -v libreoffice >/dev/null; then python3 tools/recalc_check.py "derived/$(basename "$(latest)")"; fi
fi

say "done"
echo "  viewer:      viewer/dist/index.html (self-contained; open it or publish that one file)"
echo "  derived:     derived/$(basename "$(latest)")/derived_workbook.xlsx (+ csv/, lineage.json)"
echo "  run outputs: $(latest)  — review_pack.html, links.sssom.tsv, criteria_cards.md, changelog.md, taxonomy.json"

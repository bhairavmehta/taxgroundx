#!/usr/bin/env bash
# Full OBJ-2 lifecycle on the combined synthetic set, from an empty database:
#   run -> rerun (reproducible) -> test new reports -> SME decisions -> run (read back + changelog)
#   -> rerun (reproducible) -> gate -> release (SME approval required) -> test reports against the release
# Plus: the trial set with the constrained-prompt (LLM) answers verified by the same checks.
set -euo pipefail
cd "$(dirname "$0")"
: "${PGHOST:=/tmp/pgdata}" "${PGPORT:=5433}" "${PGUSER:=grounding}"
DB="postgresql://${PGUSER}@/tg_demo?host=${PGHOST}&port=${PGPORT}"
DBT="postgresql://${PGUSER}@/tg_demo_trial?host=${PGHOST}&port=${PGPORT}"
OUT=${OUT:-out}
for d in tg_demo tg_demo_trial; do dropdb -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" --if-exists "$d"; createdb -h "$PGHOST" -p "$PGPORT" -U "$PGUSER" "$d"; done
rm -rf "$OUT"
tg() { python3 -m taxground --db "$DB" --out "$OUT" "$@"; }

echo "== 1. first run"; tg run --data data/combined --dataset combined >/dev/null; R1=$(readlink "$OUT/latest")
echo "== 2. rerun from the same inputs";   tg run --data data/combined --dataset combined >/dev/null; R2=$(readlink "$OUT/latest")
echo "== 3. test new reports against draft $R2"; tg test --version "$R2" --reports data/test_reports.json
echo "== 4. SME decisions -> release store"; sed "s/{RUN}/$R2/" data/sme_decisions_demo.csv > "$OUT/decisions.csv"
tg review --file "$OUT/decisions.csv" --reviewer "SME-Reviewer-1" || true
echo "== 5. run reads the decisions back"; tg run --data data/combined --dataset combined >/dev/null; R3=$(readlink "$OUT/latest")
echo "== 6. rerun (reproducible with the same decisions)"; tg run --data data/combined --dataset combined >/dev/null; R4=$(readlink "$OUT/latest")
echo "== 7. gate"; tg gate --run "$R4" || true
echo "== 8. release (needs SME approval for held buckets)"; tg release --run "$R4" --version v1.0 --approver "SME-Lead" || \
  tg release --run "$R4" --version v1.0 --approver "SME-Lead" --allow-held
echo "== 9. test the same reports against release v1.0"; tg test --version v1.0 --reports data/test_reports.json
echo "== 10. trial set: constrained-prompt answers through the same verifier"
python3 -m taxground --db "$DBT" --out "$OUT" run --data data/trial --dataset trial --selector llm-file --llm-outputs data/llm_answers_trial >/dev/null
echo "runs: $R1 $R2 $R3 $R4"

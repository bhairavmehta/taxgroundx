"""Recalculate a derived workbook with LibreOffice and compare every formula with the value Python computed.
  python3 tools/recalc_check.py derived/<run_id>"""
import json, pathlib, subprocess, sys, tempfile, shutil
import openpyxl

d = pathlib.Path(sys.argv[1]); x = d / "derived_workbook.xlsx"
soffice = shutil.which("soffice") or shutil.which("libreoffice")
with tempfile.TemporaryDirectory() as t:
    # a round trip through LibreOffice writes cached values for every formula
    subprocess.run([soffice, "--headless", "--calc", "--convert-to", "xlsx", "--outdir", t, str(x)], check=True, capture_output=True, timeout=600)
    shutil.copy(pathlib.Path(t) / x.name, x)
wb = openpyxl.load_workbook(x, data_only=True, read_only=True)
bad = 0
for sh, r, c, v in json.loads((d / "formula_checks.json").read_text()):
    got = wb[sh].cell(r, c).value
    ok = got == v if isinstance(v, str) else (got is not None and abs(float(got) - float(v)) <= 1e-4 + 1e-6 * abs(float(v)))
    if not ok:
        bad += 1
        print(f"  mismatch {sh}!R{r}C{c}: workbook {got} vs computed {v}")
errs = sum(1 for ws in wb for row in ws.iter_rows(values_only=True) for v in row if isinstance(v, str) and v.startswith("#") and v.endswith(("!", "?", "0")))
print(f"  formulas cross-checked against Python: {bad} mismatches; error cells: {errs}")
sys.exit(1 if bad or errs else 0)

"""Build a self-contained viewer: viewer/index.html plus viewer/data/*.json packed (gzip + base64) into one page."""
import base64, gzip, pathlib, sys
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "viewer")
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else root / "dist" / "index.html")
page = (root / "index.html").read_text()
blocks = []
for f in ["run", "techniques"] + [p.stem for p in sorted((root / "data").glob("corpus-*.json"))]:
    if not (root / "data" / f"{f}.json").exists():
        continue
    b = base64.b64encode(gzip.compress((root / "data" / f"{f}.json").read_bytes(), 9)).decode()
    blocks.append(f'<script type="application/octet-stream" id="pk-{f}">{b}</script>')
i = page.rindex("<script>")  # data blocks go before the page's own script
page = page[:i] + "\n".join(blocks) + "\n" + page[i:]
out.parent.mkdir(parents=True, exist_ok=True); out.write_text(page)
print(out, f"{len(page)/1e6:.1f} MB")

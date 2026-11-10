"""Parse the ECCAIRS Aviation 1.3.0.12 value list for attribute 390 (Events) from its PDF text.

  pdftotext -layout ECCAIRS-Aviation-1.3.0.12-VL-for-AttrID-390-Events.pdf eccairs.txt
  python3 tools/parse_eccairs.py eccairs.txt data/eccairs_events.json

Each entry is a line ending in its numeric code, "Full name (Short name)   1234567", followed by its definition lines.
Indentation gives the level in the hierarchy; the parent of each entry is the nearest shallower entry above it.
"""
import json
import re
import sys

ENTRY = re.compile(r"^(\s*)(.+?)\s{2,}(\d{7,8})\s*$")
SKIP = re.compile(r"^\s*(ECCAIRS Aviation|\d{1,2} \w+ \d{4}\s+Attribute Values|Data Definition Standard|English|Attribute Values|1\.3\.0\.12)\b")


def main(src, dst):
    lines = open(src, encoding="utf-8", errors="replace").read().splitlines()
    entries, cur, pending = [], None, None
    for raw in lines:
        if not raw.strip() or SKIP.match(raw) or "VL for AttrID" in raw:
            continue
        m = ENTRY.match(raw)
        if m:
            indent, title, code = len(m.group(1)), m.group(2).strip(), m.group(3)
            if pending:                                   # a title that wrapped onto two lines
                title = pending + " " + title
                pending = None
            cur = dict(code=code, indent=indent, title=title, definition="")
            entries.append(cur)
            continue
        txt = raw.strip()
        # a wrapped title: the code sits on the previous line, the closing ")" of the short name on this one
        if cur and not cur["definition"] and cur["title"].count("(") > cur["title"].count(")"):
            cur["title"] += " " + txt
            continue
        if cur:
            cur["definition"] = (cur["definition"] + " " + txt).strip()
    # names: "Full name (Short name)"
    for e in entries:
        m = re.match(r"^(.*?)\s*\(([^()]*)\)\s*$", e["title"])
        e["name"], e["short"] = (m.group(1).strip(), m.group(2).strip()) if m else (e["title"], e["title"])
    # levels from indentation
    levels = sorted({e["indent"] for e in entries})
    stack = []
    for e in entries:
        e["level"] = levels.index(e["indent"]) + 1
        while stack and stack[-1]["level"] >= e["level"]:
            stack.pop()
        e["parent_code"] = stack[-1]["code"] if stack else None
        e["path"] = [s["short"] for s in stack] + [e["short"]]
        stack.append(e)
    out = [dict(code=e["code"], name=e["name"], short=e["short"], level=e["level"], parent_code=e["parent_code"],
                path=e["path"], definition=e["definition"]) for e in entries]
    json.dump(dict(source="ECCAIRS Aviation 1.3.0.12, Data Definition Standard, value list for attribute 390 (Events), 29 April 2013",
                   events=out), open(dst, "w"), indent=1)
    print(f"{len(out)} events, levels {dict((l, sum(e['level'] == l for e in out)) for l in range(1, len(levels) + 1))}")


if __name__ == "__main__":
    main(*sys.argv[1:3])

#!/usr/bin/env python3
"""Convert a fetched Notion topic page (enhanced Markdown with <table> blocks) to rows JSON.

Used in update runs to recover the previous rows, and once to import pages that were built
before this skill existed. Each <tr> after a header row becomes a row; the section's H3
heading or the first cell decides the category.

Usage:
    python parse_notion_rows.py page.md -o rows.json
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

HEADING_TO_KEY = {
    "bücher": "books", "books": "books", "journal articles": "articles", "reports": "reports",
    "websites / blogs": "websites", "websites": "websites", "blogs": "blogs",
    "(video-) tutorials": "tutorials", "cases for teaching": "cases",
    "praxisbeispiele": "examples", "real-world examples": "examples", "software": "software",
    "data": "data", "people": "people",
}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def clean(cell: str) -> str:
    text = html.unescape(cell)
    text = LINK_RE.sub(lambda m: m.group(2), text)       # keep the URL only
    text = re.sub(r"\\([\\*~`$\[\]<>{}|^])", r"\1", text)  # unescape Notion specials
    return " ".join(text.split())


def parse(markdown: str) -> list[dict]:
    rows: list[dict] = []
    category = None
    for block in re.split(r"(?=^### )", markdown, flags=re.M):
        heading = re.match(r"### (.+?)(?: \(\d+\))?\s*$", block, flags=re.M)
        if heading:
            category = HEADING_TO_KEY.get(heading.group(1).strip().lower(), category)
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", block, flags=re.S):
            cells = [clean(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)]
            if len(cells) < 7 or cells[0] == "Kategorie":
                continue
            key = HEADING_TO_KEY.get(cells[0].lower(), category) or "websites"
            rows.append({
                "category": key, "title": cells[1], "author_source": cells[2],
                "link": cells[3], "note": cells[4], "course_use": cells[5],
                "status": cells[6], "files": [],
            })
    return rows


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("page", help="Markdown as returned by the Notion fetch tool")
    p.add_argument("-o", "--out", required=True)
    args = p.parse_args(argv)
    rows = parse(Path(args.page).read_text(encoding="utf-8"))
    Path(args.out).write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(rows)} rows -> {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

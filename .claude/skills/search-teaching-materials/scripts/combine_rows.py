#!/usr/bin/env python3
"""Concatenate the research agents' JSON row files into one de-duplicated list.

Duplicates are matched on DOI, else on normalised title. When two agents found the same
item, the row with the longer note wins its note/course_use/author_source. Rows in the
`methods` category are matched on title only: a method row cites a paper (same DOI) but
is a separate teaching entry from the paper itself. Unknown categories are reported and
dropped so a typo cannot create a stray table.

Usage:
    python combine_rows.py A.json B.json C.json D.json E.json -o rows_raw.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

VALID = {"books", "articles", "reports", "websites", "blogs", "tutorials", "cases",
         "examples", "software", "data", "methods", "communities", "people"}
TEXT_FIELDS = ("title", "author_source", "link", "note", "course_use", "status")


def norm_title(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()[:100]


def key(row: dict) -> str:
    if row["category"] == "methods":
        return "m:" + norm_title(row["title"])
    doi = re.search(r"10\.\d{4,9}/\S+", row.get("link") or "")
    if doi:
        return "doi:" + doi.group(0).lower().rstrip(".,;")
    return "t:" + norm_title(row["title"])


def combine(paths: list[Path]) -> list[dict]:
    rows: list[dict] = []
    seen: dict[str, dict] = {}
    for path in paths:
        for row in json.loads(path.read_text(encoding="utf-8")):
            row["category"] = (row.get("category") or "").strip().lower()
            if row["category"] not in VALID:
                print(f"dropped (category {row['category']!r}): {row.get('title')}", file=sys.stderr)
                continue
            for field in TEXT_FIELDS:
                row[field] = " ".join(str(row.get(field) or "").split())
            row.setdefault("files", [])
            row["agent"] = path.stem
            k = key(row)
            if k in seen:
                kept = seen[k]
                if len(row["note"]) > len(kept["note"]):
                    for field in ("note", "course_use", "author_source"):
                        kept[field] = row[field]
                print(f"duplicate: {row['title'][:60]} ({kept['agent']}/{row['agent']})",
                      file=sys.stderr)
                continue
            seen[k] = row
            rows.append(row)
    return rows


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("inputs", nargs="+", help="agent JSON files (lists of rows)")
    p.add_argument("-o", "--out", required=True)
    args = p.parse_args(argv)
    rows = combine([Path(x) for x in args.inputs])
    Path(args.out).write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(rows)} rows -> {args.out}", file=sys.stderr)
    print(dict(Counter(r["category"] for r in rows)), file=sys.stderr)
    print(dict(Counter(r["status"] for r in rows)), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

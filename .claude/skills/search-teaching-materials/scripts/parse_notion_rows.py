#!/usr/bin/env python3
"""Convert a fetched Notion topic page (enhanced Markdown with <table> blocks) to rows JSON.

Used in update runs to recover the previous rows, and to import pages that were built before
this skill existed. The parser is header-driven: each table's first row names its columns,
so the standard 7-column layout, the older 6-column layout (no "Verwendung im Kurs") and
hand-made tables (Name | Kategorie | Thema | Jahr | Author | Link | Kurzbeschreibung) all
map onto the row schema in references/output-format.md. The category comes from the row's
Kategorie cell, else from the enclosing H3 heading.

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

CATEGORY_ALIASES = {
    "books": ["bücher", "buch", "books", "book", "e-book"],
    "articles": ["journal articles", "journal article", "articles", "article", "paper", "working paper"],
    "reports": ["reports", "report", "white paper"],
    "websites": ["websites / blogs", "websites", "website", "website/blog", "dokumentation"],
    "blogs": ["blogs", "blog", "newsletter", "substack"],
    "tutorials": ["(video-) tutorials", "tutorials", "tutorial", "video", "videos", "podcast",
                  "course", "kurs", "mooc"],
    "cases": ["cases for teaching", "case for teaching", "case", "cases", "case idee",
              "case study", "fallstudie", "lehrfall"],
    "examples": ["praxisbeispiele", "praxisbeispiel", "real-world examples",
                 "real world examples", "example", "beispiel"],
    "software": ["software", "package", "paket", "tool", "library"],
    "data": ["data", "daten", "dataset", "datensatz", "datasets"],
    "methods": ["stat. methoden", "statistische methoden", "methoden", "methods", "method"],
    "communities": ["communities & events", "communities", "community", "events", "event",
                    "konferenz", "conference", "meetup"],
    "people": ["people", "person", "personen", "personenkontakte", "experten", "expert",
               "guest speaker", "gastspeaker", "influencer"],
}
ALIAS_TO_KEY = {alias: key for key, aliases in CATEGORY_ALIASES.items() for alias in aliases}

# header cell (lower-cased, trimmed) -> row field
HEADER_FIELDS = {
    "kategorie": "category", "category": "category", "typ": "category",
    "titel / name": "title", "titel": "title", "title": "title", "name": "title",
    "autor / quelle / firma": "author_source", "autor": "author_source", "author": "author_source",
    "author/organisation": "author_source", "autor/organisation": "author_source",
    "quelle": "author_source", "source": "author_source",
    "link": "link", "url": "link", "links": "link",
    "notiz": "note", "note": "note", "kurzbeschreibung": "note", "beschreibung": "note",
    "description": "note", "notes": "note",
    "verwendung im kurs": "course_use", "verwendung": "course_use", "course use": "course_use",
    "einsatz": "course_use",
    "status": "status",
    "thema": "theme", "topic": "theme", "jahr": "year", "year": "year",
}
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://[^\s)\]>]+")


def clean(cell: str) -> str:
    text = html.unescape(cell).replace("<br>", " ")
    text = LINK_RE.sub(lambda m: m.group(2) if URL_RE.match(m.group(2)) else m.group(1), text)
    text = re.sub(r"\\([\\*~`$\[\]<>{}|^])", r"\1", text)  # unescape Notion specials
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)             # drop bold markers
    return " ".join(text.split())


def category_key(value: str | None, fallback: str | None) -> str:
    text = (value or "").strip().lower().rstrip(" :")
    if text in ALIAS_TO_KEY:
        return ALIAS_TO_KEY[text]
    for alias, key in ALIAS_TO_KEY.items():       # "Case for Teaching (Website)" etc.
        if text.startswith(alias):
            return key
    return fallback or "websites"


def heading_key(heading: str) -> str | None:
    text = re.sub(r"\s*\(\d+\)\s*$", "", heading).strip().lower()
    return ALIAS_TO_KEY.get(text)


def parse_table(table: str, fallback: str | None) -> list[dict]:
    trs = re.findall(r"<tr[^>]*>(.*?)</tr>", table, flags=re.S)
    if len(trs) < 2:
        return []
    header = [clean(c).lower() for c in re.findall(r"<td[^>]*>(.*?)</td>", trs[0], flags=re.S)]
    fields = [HEADER_FIELDS.get(h) for h in header]
    if "title" not in fields:
        return []  # not a resource table
    rows = []
    for tr in trs[1:]:
        cells = [clean(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)]
        data = {field: cell for field, cell in zip(fields, cells) if field}
        if not data.get("title"):
            continue
        link = data.get("link") or ""
        link = (URL_RE.search(link) or [link])[0] if link else ""
        author = data.get("author_source") or ""
        extras = [data.get(k) for k in ("year",) if data.get(k)]
        if extras:
            author = ", ".join(filter(None, [author] + extras))
        note = data.get("note") or ""
        if data.get("theme"):
            note = f"{data['theme']}. {note}".strip(". ").rstrip(".") + "." if note or data["theme"] else note
        rows.append({
            "category": category_key(data.get("category"), fallback),
            "title": data["title"], "author_source": author, "link": link, "note": note,
            "course_use": data.get("course_use") or "",
            "status": data.get("status") or "manuell; Link ungeprüft", "files": [],
        })
    return rows


def parse(markdown: str) -> list[dict]:
    rows: list[dict] = []
    for block in re.split(r"(?=^### )", markdown, flags=re.M):
        heading = re.match(r"### (.+?)\s*$", block, flags=re.M)
        fallback = heading_key(heading.group(1)) if heading else None
        for table in re.findall(r"<table[^>]*>(.*?)</table>", block, flags=re.S):
            rows.extend(parse_table(table, fallback))
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

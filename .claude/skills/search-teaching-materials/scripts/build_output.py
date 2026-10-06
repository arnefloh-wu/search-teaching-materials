#!/usr/bin/env python3
"""Render curated rows as Notion-flavoured Markdown and as GitHub Markdown.

The layout reproduces the reference Notion page "Regression": one H3 section per
category with a seven-column table
    Kategorie | Titel / Name | Autor / Quelle / Firma | Link | Notiz |
    Verwendung im Kurs | Status

Usage:
    python build_output.py rows.json --topic "Regression" \
        --notion out/notion.md --markdown out/guide.md [--intro "..."] [--date 2026-10-06]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

# key -> (section heading, value of the "Kategorie" column)
CATEGORIES = {
    "books": ("Bücher", "Bücher"),
    "articles": ("Journal Articles", "Journal Articles"),
    "reports": ("Reports", "Reports"),
    "websites": ("Websites", "Websites"),
    "blogs": ("Blogs", "Blogs"),
    "tutorials": ("(Video-) Tutorials", "(Video-) Tutorials"),
    "cases": ("Cases for Teaching", "Cases for Teaching"),
    "examples": ("Praxisbeispiele", "Praxisbeispiele"),
    "software": ("Software", "Software"),
    "data": ("Data", "Data"),
    "methods": ("Statistische Methoden", "Statistische Methoden"),
    "communities": ("Communities & Events", "Communities & Events"),
    "people": ("People", "People"),
}
ALIASES = {label.lower(): key for key, pair in CATEGORIES.items() for label in pair}
ALIASES.update({"real world examples": "examples", "real-world examples": "examples",
                "videos": "tutorials", "video tutorials": "tutorials", "datasets": "data",
                "websites / blogs": "websites", "experts": "people", "guest speakers": "people",
                "personenkontakte": "people", "stat. methoden": "methods"})
COLUMNS = ["Kategorie", "Titel / Name", "Autor / Quelle / Firma", "Link", "Notiz",
           "Verwendung im Kurs", "Status"]
MONTHS_DE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August",
             "September", "Oktober", "November", "Dezember"]
URL_RE = re.compile(r"https?://[^\s)\]>]+")
NOTION_SPECIAL = re.compile(r"([\\*~`$\[\]<>{}|^])")


def category_key(value: str) -> str:
    key = (value or "").strip()
    if key in CATEGORIES:
        return key
    try:
        return ALIASES[key.lower()]
    except KeyError:
        raise SystemExit(f"unknown category {value!r}; use one of {', '.join(CATEGORIES)}")


def german_date(day: dt.date) -> str:
    return f"{day.day}. {MONTHS_DE[day.month - 1]} {day.year}"


def notion_text(text: str | None) -> str:
    """Escape Notion specials and turn bare URLs into links."""
    text = " ".join(str(text or "").split())
    parts, pos = [], 0
    for m in URL_RE.finditer(text):
        url = m.group(0).rstrip(".,;")
        parts.append(NOTION_SPECIAL.sub(r"\\\1", text[pos:m.start()]))
        parts.append(f"[{NOTION_SPECIAL.sub(r'\\\1', url)}]({url})")
        pos = m.start() + len(url)
    parts.append(NOTION_SPECIAL.sub(r"\\\1", text[pos:]))
    return "".join(parts)


def notion_link(link: str | None) -> str:
    url = (URL_RE.search(link or "") or [None])[0] if link else None
    return notion_text(url) if url else notion_text(link)


def gfm_text(text: str | None) -> str:
    text = " ".join(str(text or "").split()).replace("|", "\\|")
    return URL_RE.sub(lambda m: f"<{m.group(0).rstrip('.,;')}>", text)


def group(rows: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {key: [] for key in CATEGORIES}
    for row in rows:
        grouped[category_key(row.get("category", ""))].append(row)
    return grouped


def cells(row: dict, key: str) -> list[str]:
    return [CATEGORIES[key][1], row.get("title"), row.get("author_source"), row.get("link"),
            row.get("note"), row.get("course_use"), row.get("status") or "neu; Link ungeprüft"]


def heading(topic: str, day: dt.date) -> str:
    return f"Quellen zu {topic} (Agentensuche, {german_date(day)})"


def render_notion(rows: list[dict], topic: str, intro: str, day: dt.date) -> str:
    grouped = group(rows)
    out = [f"## {notion_text(heading(topic, day))}"]
    if intro:
        out.append(notion_text(intro))
    for key, items in grouped.items():
        if not items:
            continue
        out.append(f"### {notion_text(CATEGORIES[key][0])} ({len(items)})")
        out.append('<table fit-page-width="true" header-row="true">')
        out.append("<tr>\n" + "\n".join(f"<td>{c}</td>" for c in COLUMNS) + "\n</tr>")
        for row in items:
            values = cells(row, key)
            rendered = [notion_text(v) for v in values]
            rendered[3] = notion_link(values[3])
            out.append("<tr>\n" + "\n".join(f"<td>{v}</td>" for v in rendered) + "\n</tr>")
        out.append("</table>")
    return "\n".join(out) + "\n"


def render_markdown(rows: list[dict], topic: str, intro: str, day: dt.date) -> str:
    grouped = group(rows)
    out = [f"# {heading(topic, day)}", ""]
    if intro:
        out += [intro, ""]
    out += ["| Kategorie | Anzahl |", "|---|---|"]
    out += [f"| {CATEGORIES[k][0]} | {len(v)} |" for k, v in grouped.items() if v]
    out.append("")
    for key, items in grouped.items():
        if not items:
            continue
        out += [f"## {CATEGORIES[key][0]} ({len(items)})", "",
                "| " + " | ".join(COLUMNS[1:]) + " |",
                "|" + "---|" * (len(COLUMNS) - 1)]
        for row in items:
            out.append("| " + " | ".join(gfm_text(v) for v in cells(row, key)[1:]) + " |")
        out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("rows", help="JSON file with a list of curated rows")
    p.add_argument("--topic", required=True)
    p.add_argument("--intro", default="", help="summary paragraph under the heading")
    p.add_argument("--date", help="YYYY-MM-DD (default: today)")
    p.add_argument("--notion", help="write Notion-flavoured Markdown here")
    p.add_argument("--markdown", help="write GitHub Markdown here")
    args = p.parse_args(argv)

    rows = json.loads(Path(args.rows).read_text(encoding="utf-8"))
    day = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    if not (args.notion or args.markdown):
        p.error("give --notion and/or --markdown")
    for target, render in ((args.notion, render_notion), (args.markdown, render_markdown)):
        if target:
            Path(target).parent.mkdir(parents=True, exist_ok=True)
            Path(target).write_text(render(rows, args.topic, args.intro, day), encoding="utf-8")
            print(f"wrote {target}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

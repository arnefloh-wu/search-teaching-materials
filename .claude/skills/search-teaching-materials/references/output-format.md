# Output format

## Row schema (JSON)

Every research agent returns a JSON list of rows with these keys. Strings are plain text
(no Markdown); the builder escapes and formats them.

```json
{
  "category": "articles",
  "title": "Spotlights, Floodlights, and the Magic Number Zero",
  "author_source": "Spiller, Fitzsimons, Lynch and McClelland, Journal of Marketing Research 50(2), 277-288, 2013, article",
  "link": "https://doi.org/10.1509/jmr.12.0420",
  "note": "Marketing's reference for probing interactions: spotlight tests, floodlight (Johnson-Neyman) regions, why median splits are wrong.",
  "course_use": "Reading for the moderation session; floodlight plot as lab extension. Paywalled, WU-Lizenz prüfen.",
  "status": "neu; Link geprüft",
  "access": "paid",
  "files": []
}
```

| Key | Required | Content |
|---|---|---|
| `category` | yes | one of the keys below |
| `title` | yes | title, or product/dataset/person name |
| `author_source` | yes | authors or organisation, venue, year, type (book, article, report, course, repo, dataset, person role) |
| `link` | yes | one canonical URL (DOI preferred for publications; profile URL for people) |
| `note` | yes | what in the resource is useful for teaching this topic: chapter, dataset, example, length, caveats |
| `course_use` | yes | how to use it: reading, lab, warm-up, background, guest talk, project data; plus access: free / open access / paid (approx. price) / WU-Lizenz prüfen |
| `status` | yes | see labels below |
| `access` | no | `free`, `open_access`, `paid`, `wu_licence`, `login` |
| `files` | no | filenames saved by `fetch_assets.py` (filled by the script) |
| `link_check` | no | HTTP result written by `verify_links.py` |

## Categories

| key | Notion heading | What belongs here |
|---|---|---|
| `books` | Bücher | textbooks, monographs, free online books |
| `articles` | Journal Articles | journal articles, classic methods papers, working papers |
| `reports` | Reports | industry, consultancy, government and standards reports, white papers |
| `websites` | Websites | documentation sites, course sites, reference pages, tools' guides |
| `blogs` | Blogs | blogs, Substack/Medium posts, newsletter archives (individual authors or companies) |
| `tutorials` | (Video-) Tutorials | YouTube videos/playlists, MOOCs, recorded lectures, workshop recordings |
| `cases` | Cases for Teaching | HBP, Case Centre, Ivey, SAGE, Emerald, WU EMCEE cases; teaching notes; classroom labs with data |
| `examples` | Praxisbeispiele | documented real-world applications: company blog posts, conference talks, Kaggle solutions, public analyses |
| `software` | Software | packages, libraries, apps, notebooks (with version and licence) |
| `data` | Data | datasets and data portals (size, variables, licence) |
| `people` | People | experts, practitioners, influencers, potential guest speakers (see people-search.md) |

## Status labels

The label has two parts separated by `; `: run marker and verification.

- Run marker: `neu` (added in this run) or `bestehend` (carried over from a previous run by
  `merge_rows.py`).
- Verification: `Link geprüft` (the page was fetched, by the agent or by `verify_links.py`),
  `in Suchergebnis bestätigt` (only confirmed through search-result snippets),
  `Link ungeprüft` (constructed or remembered URL, check before use).

Agents should hand over honest labels; `verify_links.py` upgrades to "Link geprüft" when a
link answers 2xx/3xx and downgrades a "geprüft" claim that fails.

## Notion page layout

```
## Quellen zu <Topic> (Agentensuche, <D. Monat YYYY>)
<intro paragraph: agents, blocks covered, row count, caveats, status legend, GitHub path>
### Bücher (n)
<table fit-page-width="true" header-row="true">  Kategorie | Titel / Name | Autor / Quelle / Firma | Link | Notiz | Verwendung im Kurs | Status
### Journal Articles (n)
...
### People (n)
```

Sections appear in the category order above; empty categories are omitted. For People the
seven columns are read as: Kategorie = People; Titel / Name = name; Autor / Quelle / Firma =
affiliation, role, location tag (Wien / Österreich / Global); Link = main professional
profile; Notiz = why relevant to the topic (publications, talks, products); Verwendung im
Kurs = guest-speaker or interview fit, format, language; Status = as above.

## GitHub README layout

Same sections rendered as GitHub tables (without the Kategorie column), preceded by a
category count table. `rows.json` sits next to it as the machine-readable source and
`notion.md` is the exact text pushed to Notion, so a re-run can diff against it.

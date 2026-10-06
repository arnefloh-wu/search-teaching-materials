# search-teaching-materials

Automated search for teaching materials, built as a Claude Code skill
(`.claude/skills/search-teaching-materials/`). One topic in, three outputs out:

| Output | Where |
|---|---|
| Resource tables (12 categories, links, notes, course use, status) | Notion: subpage of [Literature Search for Teaching](https://app.notion.com/p/3f164d53209a816a8aeed82a2da229d7) |
| Files that may be stored (open-access PDFs, data, notebooks) + README | Dropbox: `Literature Search for Teaching/<topic>/` |
| README, `rows.json`, `notion.md`, files | this repo: `topics/<topic>/` |

Categories: Bücher, Journal Articles, Reports, Websites, Blogs, (Video-) Tutorials,
Cases for Teaching, Praxisbeispiele, Software, Data, People (experts, influencers,
guest speakers in Wien / Österreich / global).

## Usage

In Claude Code (desktop or CLI) inside this repository:

```
/search-teaching-materials
```

The skill asks for the topic, then runs autonomously: parallel research agents search
open APIs (OpenAlex, Crossref, Semantic Scholar, arXiv, DOAJ, Open Library, Google Books,
YouTube, GitHub, Zenodo, Dataverse, Kaggle, data.europa.eu, data.gov), WU-licensed APIs
when keys are present (Primo/CatalogPLUS, Scopus, Web of Science, Springer, EBSCO) and the
web, in English and German. Links are checked, storable files downloaded, and the results
written to Notion, Dropbox and `topics/<topic>/` on `main`. Re-running a topic updates the
existing page: carried-over rows are marked `bestehend`, additions `neu`.

### Setup (once)

1. Copy `.claude/skills/search-teaching-materials/.env.example` to `.env` in the same
   folder and fill in the keys you have. `python .claude/skills/search-teaching-materials/scripts/search_sources.py --list`
   shows which connectors are active. Everything works without keys (web-search fallback);
   the YouTube key and a WU Primo key add the most.
2. Connect the Notion and Dropbox connectors in Claude Code (used for page creation and
   text uploads). Binary uploads to Dropbox need a Dropbox app token in `.env`.
3. Python 3.10+; the scripts use only the standard library.

### Scripts

| Script | Purpose |
|---|---|
| `search_sources.py` | query up to 20 APIs, normalised JSON, de-duplicated |
| `verify_links.py` | HTTP-check each link, set status label |
| `fetch_assets.py` | download open files for Dropbox/GitHub |
| `merge_rows.py` | merge previous and new rows (update runs) |
| `parse_notion_rows.py` | existing Notion page → rows JSON |
| `build_output.py` | rows JSON → Notion markdown + GitHub README |
| `dropbox_upload.py` | upload a folder tree to Dropbox |

## Topics

| Topic | Rows | Notion |
|---|---|---|
| [Regression](topics/Regression/) | 137 | [Regression](https://app.notion.com/p/3f064d53209a80528a4be0208e665bbd) |

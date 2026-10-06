---
name: search-teaching-materials
description: >-
  Automated literature and resource search for university teaching. Use whenever Arne
  wants teaching materials, course resources, a reading list, a resource guide, Lehrmaterial,
  Quellen or Literatur for a topic, a new Notion topic page under "Literature Search for
  Teaching", or asks to "search sources for <topic>" / "run the teaching search". Asks for
  the topic, fans out parallel agents over open and WU-licensed APIs plus web search across
  twelve categories (books, journal articles, reports, websites, blogs, video tutorials,
  teaching cases, real-world examples, software, data, people/experts/guest speakers), then
  writes a Notion subpage, a Dropbox subfolder and a GitHub topic folder named after the topic.
---

# Search Teaching Materials

Build a complete, link-checked resource guide for one teaching topic and store it in three
places: a Notion subpage, a Dropbox subfolder and a folder in the GitHub repo
`arnefloh-wu/search-teaching-materials`. The reference result is the Notion page
"Regression" (137 rows, 9 tables): aim for that depth and tone.

## Step 0: Get the topic

Ask one question and nothing else: **"Which topic should I research?"** The answer is free
text (e.g. "Regression", "Conjoint Analysis", "Marketing Mix Modelling"). Use it *as typed*
for the Notion page title, the Dropbox subfolder and the GitHub folder `topics/<topic>/`.
Folder names cannot contain `/`: for Dropbox and GitHub replace each `/` with ` & `
(e.g. "AB-Testing/Experiments in (Digital) Marketing/Retail" becomes the folder
"AB-Testing & Experiments in (Digital) Marketing & Retail"); the Notion title keeps the
original.
If the user adds context (course, session plan, Python vs. R, student level), keep it for
the "Verwendung im Kurs" column; without it, write course use generically (reading, lab,
background, guest talk) rather than inventing session numbers.

Then run fully autonomously to the end. Do not stop for an interim review; report once at
the end with the three links.

## Step 1: Set up

1. `python scripts/search_sources.py --list` shows which API connectors have keys. Read
   `references/sources.md` for what each source covers, the WU-licensed options and the
   Primo/Scopus/WoS key situation. Missing keys are not blockers: the agents fall back to
   web search and mark such rows "in Suchergebnis bestätigt".
2. Check for a previous run: search Notion for a subpage with the topic title under
   "Literature Search for Teaching" (page `3f164d53209a816a8aeed82a2da229d7`) and look for
   `topics/<topic>/rows.json` in the repo. If either exists, this is an **update run**: fetch
   the old page, `python scripts/parse_notion_rows.py old_page.md -o old_rows.json`, and
   later merge (Step 4). Existing rows keep their status prefix "bestehend", new ones get
   "neu", so the instructor sees what the re-run added.
3. Create the working directory `topics/<topic>/` in the repo (on `main`, pulled fresh).

## Step 2: Search in parallel

Spawn research agents (general-purpose) with `run_in_background: true`, one per block, and
give each one the topic, the languages (search in **English and German**; Austrian and
German sources matter for blogs, people and cases), the row schema from
`references/output-format.md`, and the instruction to return rows as a JSON list. Sensible
blocks (combine if the topic is narrow, split further if it is broad):

| Agent | Categories | Primary tools |
|---|---|---|
| A | books, articles, reports | `search_sources.py -c books,articles,reports` (OpenAlex, Crossref, Semantic Scholar, Springer, Scopus, WoS, Primo when keyed), Consensus MCP, web search for publisher pages |
| B | websites, blogs, tutorials | `search_sources.py -c tutorials` (YouTube API), web search for documentation sites, blogs, Substack, Medium, course platforms (Coursera, edX, DataCamp, LinkedIn Learning, O'Reilly) |
| C | cases, examples | web search on HBP Education, The Case Centre, Ivey, SAGE Business Cases, Emerald EMCS, WU EMCEE cases; company blogs, Think with Google, industry reports with real data for examples |
| D | software, data | `search_sources.py -c software,data` (GitHub, PyPI/CRAN pages, Zenodo, Dataverse, Kaggle, data.europa.eu, data.gov, Eurostat, OECD, World Bank) |
| E | people, communities | web search only; read `references/people-search.md` first |

Two optional categories exist for topics that need them: `methods` (sub-methods of a modelling
technique, as on the MMM page) and `communities` (hubs, Slack groups, conferences).

Tell every agent:

- No fixed cap on rows, but every row must earn its place: say in "Notiz" *what in the
  resource is useful for teaching this topic* (chapter, dataset, example, length), not a
  generic blurb. Prefer recent material; keep classics only when they are still the
  standard reference.
- Record access: free / open access / paid (approximate price) / "WU-Lizenz prüfen" for
  paywalled items. SpringerLink, Scopus-indexed journals, EBSCO Business Source, JSTOR,
  Emerald and Statista are usually reachable through the WU library.
- Status label per row (see `references/output-format.md`): "Link geprüft" only if the
  agent actually fetched the page; otherwise "in Suchergebnis bestätigt" or "Link ungeprüft".
- For `search_sources.py`, write results with `-o` and read the JSON; the `meta.errors`
  block names connectors that were blocked (common in cloud sessions). A blocked connector
  means fall back to web search for that category, not skip it.
- Return a JSON list only (no prose) so the rows can be merged mechanically.

While the agents run, write the intro paragraph for the page: topic, date, number of agents,
what the blocks covered, any caveats (version constraints of software, licence gaps).

## Step 3: Collect, verify, download

1. `python scripts/combine_rows.py <agent files> -o topics/<topic>/rows_raw.json`
   concatenates the agents' JSON and drops duplicates (same DOI or normalised title; the
   richer note wins; method rows are matched on title only, since they cite papers that
   also appear as articles). Have agents write their rows to files (one per block) rather
   than return them in their reply.
2. `python scripts/verify_links.py topics/<topic>/rows_raw.json -o topics/<topic>/rows.json`
   fetches every link and upgrades or downgrades the status label. Publisher sites that
   answer 403 to robots keep the agent's label; the HTTP result lands in `link_check`.
3. `python scripts/fetch_assets.py topics/<topic>/rows.json -d topics/<topic>/files/`
   downloads what may legally be stored: open-access PDFs, datasets, notebooks, code
   archives and permissively licensed material. It skips paywalled publisher URLs, YouTube,
   and anything whose licence is unknown and large. Record the saved filename in the row's
   `files` field. Store nothing that would violate a licence; paywalled items are listed
   in Notion with a link only.

## Step 4: Build the outputs

```
python scripts/merge_rows.py old_rows.json topics/<topic>/rows.json -o topics/<topic>/rows.json   # update runs only
python scripts/build_output.py topics/<topic>/rows.json --topic "<topic>" --intro "<intro>" \
    --notion topics/<topic>/notion.md --markdown topics/<topic>/README.md
```

The builder renders one H3 table per category in the fixed column order *Kategorie | Titel /
Name | Autor / Quelle / Firma | Link | Notiz | Verwendung im Kurs | Status*. Blogs and People
get their own tables. The README is the GitHub-flavoured copy of the same content with a
category count table on top.

## Step 5: Store

**Notion.** Create (or, in update runs, `replace_content` on) the subpage under
"Literature Search for Teaching" with the title `<topic>` and the content of `notion.md`.
Use the Notion MCP `create-pages` with `parent: {type: page_id, page_id:
3f164d53209a816a8aeed82a2da229d7}`. Pages above ~100 rows need the content split: create
the page with the intro and the first table, then `insert_content` at the end, one call per
section, splitting a long table into two consecutive tables with the same header (keep each
call under ~20 KB). Do these inserts yourself, in order; a subagent retyping 200 KB of tables
is slow and was stopped mid-way by a false-positive safety block in the first real run.
Afterwards fetch the page and compare rows per `### ` heading with the counts in the headings.
Read `notion://docs/enhanced-markdown-spec` before writing if it is not already in context.

**Dropbox.** Parent folder: `/Literature Search for Teaching` (shared link
`https://www.dropbox.com/scl/fo/trtup5zyvhwgpe263l31x/ACLm3qTdw1XXpliIi6tQ5XE?rlkey=jq383qywt3bc5zlos8204rpdm`).
Create the subfolder `/Literature Search for Teaching/<topic>` and upload `README.md`,
`rows.json` and everything in `files/`. Two routes:

- The Dropbox MCP connector (`create_folder`, `create_file`) handles folders and text
  files (Markdown, JSON, CSV, notebooks).
- Binary files (PDF, ZIP, XLSX) need `python scripts/dropbox_upload.py topics/<topic>/ "/Literature Search for Teaching/<topic>"`
  with a Dropbox app token in `.env` (see `.env.example`). If no token is set, say so in
  the final report and list the files that stayed local.

**GitHub.** Commit `topics/<topic>/` (README.md, rows.json, notion.md, files/ except
anything over 50 MB) to `main` and push. Commit message: `Add teaching materials for <topic>`
or `Update teaching materials for <topic> (<n> new rows)`.

## Step 6: Report

One short message: Notion page link, Dropbox folder path, GitHub folder link, row counts per
category, how many links verified, which connectors were skipped for lack of keys or blocked
by the network, and anything the instructor should check by hand (e.g. unverified licences,
API keys worth obtaining from the WU library).

## Quality bar (why it matters)

The page replaces hours of manual library work before a course is designed. A row that only
repeats a title wastes the instructor's time; a row that names the chapter, the dataset or
the minute in a video saves it. Likewise an unverified link labelled "geprüft" costs trust
in the whole table, so label honestly. Prefer fewer, better-annotated rows over padding,
but do not stop early when a block is rich: the Regression page has 35 articles and 18
software entries because the topic warranted it.

## Files

- `scripts/search_sources.py`: 20 API connectors, normalised JSON (`--list` shows key status)
- `scripts/combine_rows.py`: merge agent files, de-duplicate
- `scripts/verify_links.py`: HTTP check and status relabelling
- `scripts/fetch_assets.py`: downloads storable open files into `files/`
- `scripts/merge_rows.py`: merge previous and new rows for update runs
- `scripts/parse_notion_rows.py`: Notion page markdown to rows JSON
- `scripts/build_output.py`: rows JSON to Notion markdown and GitHub README
- `scripts/dropbox_upload.py`: upload a folder tree to Dropbox via API token
- `references/sources.md`: source catalogue, WU licences, how to get each key
- `references/output-format.md`: row schema, category list, status labels, table layout
- `references/people-search.md`: how to find and document experts and guest speakers
- `.env.example`: all credentials the connectors can use

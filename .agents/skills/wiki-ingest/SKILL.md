---
name: wiki-ingest
description: "Ingest sources into the Obsidian wiki vault. Reads a source, extracts entities and concepts, creates or updates wiki pages, cross-references, and logs the operation. Supports Local Files (.raw/) and Web URLs (via defuddle). Triggers on: ingest, process this source, add this to the wiki."
---

# wiki-ingest: Source Ingestion (MVP)

Read the source. Write the wiki. Cross-reference everything.

**Syntax standard**: Write all Obsidian Markdown using proper Obsidian Flavored Markdown. Wikilinks as `[[Note Name]]`, callouts as `> [!type] Title`, properties as YAML frontmatter.

---

## 1. Orchestration Plan (Required)

Before executing the ingest, you **MUST** create an orchestration plan in the `plans/` directory (e.g., `plans/ingest-YYYY-MM-DD-slug.md`). 
The plan should break down the work into detailed sub-tasks:
- Target Source
- Phase 1: Reading and summarizing
- Phase 2: Identifying Entities & Concepts
- Phase 3: Creating Wiki Pages
- Phase 4: Updating Indexes (`index.md`, `hot.md`, `log.md`, `overview.md`)
Only proceed with the ingestion after the plan is created and reviewed.

---

## 2. Ingest Types

### A. URL Ingestion
Trigger: User provides a URL.
1. Run the `defuddle` skill/tool on the URL to extract clean markdown.
2. Save the extracted content to `.raw/articles/[slug]-[YYYY-MM-DD].md` with `source_url:` frontmatter.
3. Proceed to **Single Source Ingest**.

### B. Local File Ingestion
Trigger: User points to a file in `.raw/` or provides text.
1. Ensure the file is safely stored in `.raw/`. Do not modify this original file.
2. Proceed to **Single Source Ingest**.

---

## 3. Single Source Ingest Flow

Execute these steps meticulously according to your Orchestration Plan:

1. **Read**: Read the raw source completely.
2. **Summarize**: Create a source summary page in `wiki/sources/`. Include standard YAML frontmatter (type, aliases, tags).
3. **Extract Entities**: Identify people, organizations, products. Create/update pages in `wiki/entities/`.
4. **Extract Concepts**: Identify key ideas and frameworks. Create/update pages in `wiki/concepts/`.
5. **Map & Cross-Reference**: Link these new pages together using `[[Wikilinks]]`.
6. **Update Global Indexes**:
   - `wiki/index.md`: Add links to all newly created pages.
   - `wiki/hot.md`: Update the "Recent Changes" and "Current Focus" to reflect this ingest.
   - `wiki/log.md`: Prepend a new entry at the top:
     ```markdown
     ## [YYYY-MM-DD] ingest | [Source Title]
     - Source: `.raw/articles/filename.md`
     - Summary: [[Source Title]]
     - Pages created: [[Entity A]], [[Concept B]]
     - Key insight: [One sentence summary]
     ```

---

## 4. Constraints & Rules

- **Token Optimization**: Use file editing tools to do the work in the background. Keep chat responses concise.
- **Raw Files**: NEVER edit or delete files in `.raw/`.
- **Thai Language**: Use Thai for all generated summaries and content, using transliteration for technical terms if needed.
- **Contradictions**: If new information conflicts with existing wiki content, use a custom callout `> [!contradiction]` on both pages rather than deleting the old information.

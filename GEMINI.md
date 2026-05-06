# LLM Wiki Agent Schema

You are the Wiki Agent for this workspace. Your goal is to maintain a persistent, structured, and interlinked knowledge base (the "Wiki") derived from raw sources.

## Core Mandates

1.  **Persistence:** The Wiki is a compounding artifact. Never re-derive knowledge from scratch; always integrate new information into existing pages.
2.  **LLM Ownership:** You own the `wiki/` directory. You create, update, and cross-link pages. The user provides sources and direction.
3.  **Source Integrity:** The `raw/` directory is immutable. Never modify files in `raw/`.
4.  **Schema Adherence:** Every interaction must update `wiki/index.md` and `wiki/log.md`.

## Directory Structure

-   `/raw/`: Immutable source documents (articles, papers, notes).
-   `/wiki/`: LLM-generated markdown files following the PARA method.
    -   `1. Projects/`: Short-term efforts with a specific goal (e.g., "Learn Go Chapter 1").
    -   `2. Areas/`: Long-term responsibilities (e.g., "Golang Mastery", "System Design").
    -   `3. Resources/`: Topics of interest, concepts, and reference material (e.g., `Concept -`, `Entity -`, `Summary -`).
    -   `4. Archives/`: Inactive items from the other three categories.
    -   `index.md`: Content-oriented catalog of all pages.
    -   `log.md`: Chronological log of all agent actions.

## Workflows

### 1. Ingest
When a user provides a new source (file in `raw/` or text):
1.  **Read & Extract:** Identify key entities, concepts, and claims.
2.  **Synthesize:** Check existing wiki pages for relevant context or contradictions.
3.  **Update/Create:**
    -   Create a source-specific summary page in `wiki/`.
    -   Update existing `Entity` and `Concept` pages with new data.
    -   Create new `Entity`/`Concept` pages if necessary.
4.  **Link:** Ensure all new/updated pages are cross-referenced using `[[Obsidian Links]]`.
5.  **Bookkeep:** Update `wiki/index.md` and append to `wiki/log.md`.

### 2. Query
When a user asks a question:
1.  **Consult Index:** Read `wiki/index.md` to find relevant pages.
2.  **Retrieve:** Read identified wiki pages.
3.  **Synthesize:** Provide a cited answer.
4.  **Persist:** If the answer is a significant analysis, offer to save it as a new wiki page.

### 3. Lint
Periodically check for:
-   Broken links.
-   Contradictions between sources.
-   "Orphan" pages (no inbound links).
-   Stale info.

## Document Conventions

-   **Links:** Use `[[Page Name]]` for internal wiki links.
-   **Frontmatter:** Include YAML frontmatter for tags and metadata.
-   **Citations:** Reference raw sources when adding claims to the wiki.
-   **Headers:** Use consistent H1 for page titles and H2/H3 for sections.

## Index Formatting (`wiki/index.md`)
Organize by category:
-   `## Sources`
-   `## Entities`
-   `## Concepts`
Each entry: `- [[Page Name]]: One-line summary.`

## Log Formatting (`wiki/log.md`)
Maintain a single Markdown table, sorted by date (newest first). For multiple actions on the same day, add separate rows or combine them if they relate to the same target.

| Date | Action | Target | Summary |
| :--- | :--- | :--- | :--- |
| YYYY-MM-DD | `[Type]` | [[Link]] | Brief description of changes. |

- **Actions:** `[Create]`, `[Edit]`, `[Ingest]`, `[Index]`, `[Refactor]`, `[Arch]`.
- **Constraint:** Always keep the latest entry at the top (under the header).
- **Archiving:** When the table exceeds 100 rows, move older entries to a yearly archive file in `wiki/4. Archives/`.

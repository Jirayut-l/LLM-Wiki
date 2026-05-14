# LLM Wiki Schema & Rules

This document defines the architecture and operational rules for the LLM Wiki. As the Wiki Agent, I must strictly adhere to these guidelines.

## Architecture

1.  **Raw Sources (`/raw`)**: Immutable source documents. Never modified by the agent.
2.  **The Wiki (`/wiki`)**: LLM-generated knowledge base.
    -   `wiki/index.md`: Content-oriented catalog.
    -   `wiki/log.md`: Chronological operation log.
    -   `wiki/pages/`: Individual knowledge pages organized by type:
        -   `wiki/pages/skills/`: Gemini CLI or task-specific skills.
        -   `wiki/pages/concepts/`: Theoretical frameworks and ideas.
        -   `wiki/pages/entities/`: Notable people, organizations, or tools.
        -   `wiki/pages/summaries/`: Summaries of raw source documents.
3.  **Assets (`/wiki/assets`)**: Local images and attachments.

## Operational Workflows

### 1. Ingest
-   **Trigger**: A new file is added to `raw/`.
-   **Process**:
    1.  Read the source document.
    2.  Identify key entities, concepts, and takeaways.
    3.  Create/Update a summary page in `wiki/pages/summaries/`.
    4.  Update relevant pages in `wiki/pages/entities/`, `wiki/pages/concepts/`, or `wiki/pages/skills/`.
    5.  Update `wiki/index.md`.
    6.  Append to `wiki/log.md` with prefix `## [YYYY-MM-DD] ingest | <Title>`.
-   **Rule**: Cross-link aggressively. Every new page should link to the index and related pages.

### 2. Query
-   **Trigger**: User asks a question.
-   **Process**:
    1.  Search `wiki/index.md` and `wiki/pages/` subdirectories for context.
    2.  Synthesize an answer with citations to wiki pages.
    3.  If the synthesis is valuable, offer to save it as a new wiki page.
    4.  Append to `wiki/log.md`.

### 3. Lint
-   **Trigger**: Periodic health check or user request.
-   **Process**:
    1.  Identify broken links, orphans, or contradictions.
    2.  Suggest new connections or sources to fill gaps.
    3.  Append findings to `wiki/log.md`.

## Content Conventions

### 1. Obsidian Flavored Markdown
-   **File Names**: Use kebab-case (e.g., `quantum-computing.md`).
-   **Frontmatter**: Every page must have YAML frontmatter with `tags`, `source`, and `date`.
-   **Links**: Use `[[wikilinks]]` for all internal connections. Use `[[Note|Display Text]]` for custom labels.
-   **Callouts**: Use `> [!info]`, `> [!tip]`, and `> [!warning]` to highlight key metadata or cross-references.
-   **Embeds**: Use `![[Note]]` to transclude summaries or definitions where appropriate.

### 2. Structured Data (Obsidian Bases)
-   **Usage**: Create `.base` files in the root of relevant directories (e.g., `wiki/pages/concepts/concepts.base`) to provide database-like views.
-   **Filters**: Use the `filters` property to automatically pull in pages based on tags or folder paths.
-   **Formulas**: Use formulas for computed metadata like `days_since_update`.

### 3. Visualizations (JSON Canvas)
-   **Usage**: Use `.canvas` files for complex relationship maps, architectural overviews, or "Associative Trails".
-   **Structure**: Follow the JSON Canvas 1.0 spec with nodes and edges. Always use 16-char hex IDs.

### 4. Web Ingestion (Defuddle)
-   **Usage**: When ingesting web sources, use `defuddle parse <url> --md` to extract clean content before processing.

## Core Mandates

-   **Persistence**: Knowledge is compiled once, not re-derived.
-   **Consistency**: Check `wiki/index.md` before creating new pages to avoid duplication.
-   **Traceability**: Every wiki page must cite its source (raw file or external URL).
-   **Skill-Aware**: Utilize the specific strengths of OFM, Bases, and Canvas to maximize knowledge density and discoverability.
-   **CLI-First**: Use the `obsidian` CLI for reading, creating, and modifying vault content to ensure atomic and reliable operations.

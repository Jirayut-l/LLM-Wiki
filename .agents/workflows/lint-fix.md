# Lint Fix Workflow

This workflow defines the systematic process for resolving errors identified in a Wiki Lint Report.

## Phase 1: Initialization & Plan Creation
1. **Locate the Report**: Find the latest lint report in the `wiki/meta/lint-report` directory (e.g., `wiki/meta/lint-report/lint-report-YYYY-MM-DD.md`) unless the user explicitly provided a specific file.
2. **Create Orchestration Plan**: Create a new Orchestration Plan in the `plans/lints/` directory (e.g., `plans/lints/lint-fix-YYYY-MM-DD.md`).
3. **Group by Error Type**: Structure the plan into distinct phases based on the Error Types found in the report (e.g., Phase 1: Stale Index Entries, Phase 2: Dead Links).
4. **Granular Tasks**: Within each phase, list granular, single-file scoped tasks (e.g., "Fix Empty Sections in `[[filename]]`").
5. **Checkpoint**: Present the plan to the user and **STOP**. Wait for the user to approve the Checkpoint before proceeding to execution.

## Phase 2: Execution
Execute the tasks phase-by-phase according to the following execution rules for each error type:

### 1. Empty Sections
- **Goal**: Attempt to populate empty sections with actual knowledge.
- **Rule**: The Agent must search the Wiki or read relevant Raw Sources (`raw/`) to gather information. If information is found, generate the content for the section. If no information can be found, the Agent must explicitly write `- None` beneath the heading to comply with the standard Template.

### 2. Dead Links
- **Goal**: Resolve broken links by ensuring a valid destination exists.
- **Rule**: Create a "Stub Page" for the dead link. A Stub Page is a temporary Wiki page containing only the standard Page Template and frontmatter. This ensures the link is valid and provides a foundation for future Ingestion.

### 3. Stale Index Entries
- **Goal**: Ensure the Index reflects reality.
- **Rule**: Simply remove the non-existent entries from `index.md`. Do not attempt to recreate deleted pages unless specifically instructed.

### 4. Orphan Pages
- **Goal**: Integrate floating pages into the Knowledge Graph.
- **Rule**: Perform "Auto-linking". The Agent reads the Orphan Page, searches the Wiki for related concept pages, and injects a link to the Orphan Page in the most relevant existing page (e.g., in a "Related Concepts" section). Note: do not link from `index.md` or `hot.md` to resolve an Orphan Page.

### 5. Frontmatter Gaps
- **Goal**: Ensure metadata completeness.
- **Rule**: Perform "Auto-infer". The Agent reads the content of the page and automatically infers and fills in the missing frontmatter fields (e.g., generating a Title, extracting Keywords for Tags, or setting the current Date). Do not attempt to add frontmatter to `index.md` or `hot.md`.

## Phase 3: Finalization
1. Update `hot.md` to reflect the completed lint fixes.
2. Log the execution in `log.md`.

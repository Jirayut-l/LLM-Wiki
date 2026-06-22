# 2. Type-Specific Templates

Date: 2026-06-22

## Status

Accepted (Supersedes [0001 Strict Base Template](0001-strict-base-template.md))

## Context

Previously, ADR 0001 enforced a single strict base `TEMPLATE.md` with standardized headings for all wiki pages. When sections had no data, the LLM Agent was required to write `- None` to prevent automated parsing and linting tools from breaking.

As the wiki grew, the introduction of multiple distinct page types (`concept`, `entity`, `source`, `summary`) revealed the limitations of a monolithic template. For example, a `summary` page naturally does not need the same core structure as a `source` page. Forcing them into the same template resulted in excessive `- None` noise and caused the `wiki-lint` skill to behave inconsistently by flagging sections that were intentionally left blank or structurally irrelevant to the specific type.

## Decision

We have decided to move from a Single Strict Template model to a **Type-Specific Templates** model:

1. **Multiple Templates**: We will introduce a `_templates/` directory containing distinct templates for each page type (e.g., `_templates/concept.md`, `_templates/source.md`, `_templates/summary.md`).
2. **Type-Driven Structure**: Each template will define only the YAML frontmatter and headings relevant to its specific `type`.
3. **No More `- None` Requirements**: Because the template headings are inherently suitable for the content type, the `- None` workaround is abolished. If a section has no data (e.g., no related concepts), the LLM Agent must omit/delete the heading entirely to keep the page clean and prevent `wiki-lint` from flagging it.
4. **Linting Awareness**: The `wiki-lint` skill (and any future automated tools) must be updated to validate a page's structure against its corresponding type template rather than a universal standard.

## Consequences

- **Positive**: Eliminates visual clutter (`- None`) and makes pages more human-readable.
- **Positive**: `wiki-lint` will be more accurate, eliminating false positives caused by forcing unrelated structures onto pages.
- **Positive**: Greater flexibility to introduce highly specialized page types in the future without disrupting existing ones.
- **Negative**: The Agent must explicitly lookup and use the correct file in `_templates/` when generating a new page, slightly increasing the complexity of page creation prompts.

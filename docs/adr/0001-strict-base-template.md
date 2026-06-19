# 1. Strict Base Template for Wiki Pages

Date: 2026-06-19

## Status

Accepted

## Context

The wiki utilizes an LLM Agent to automatically generate, ingest, and maintain markdown files at scale. To ensure structural consistency, a `TEMPLATE.md` file defines the core YAML frontmatter and markdown headings that every page must include.

A challenge arises when a page does not have data for a specific section (e.g., a new concept with no `## Related` or `## Sources`). There is a trade-off between:
- **Human Readability:** Removing empty sections keeps the page clean and visually uncluttered.
- **Machine Parsability & Automation:** Keeping a predictable, immutable structure simplifies programmatic parsing, linting (Wiki Lint), and future automated updates by the Agent.

Furthermore, different page types (`concept`, `entity`, `source`) require distinct metadata, which conflicts with having a single monolithic template.

## Decision

We have decided to enforce a **Strict Base Template** model with the following rules:

1. **Single Source of Truth:** `TEMPLATE.md` is the absolute reference for the base page structure. `CONTEXT.md` will no longer hardcode structural examples to prevent drift.
2. **Immutability of Base Elements:** The core standard headings defined in `TEMPLATE.md` must *never* be deleted from a generated page, even if empty.
3. **Explicit Empty States:** If a section has no data, the Agent must explicitly write `- None` beneath the heading rather than removing the heading.
4. **Dynamic Extensions:** `TEMPLATE.md` acts as the base. The Agent is allowed to dynamically append type-specific YAML frontmatter fields (e.g., `url:`) or sub-headings *below* the standard ones, but cannot alter the core base structure.

## Consequences

- **Positive:** Automated tools (linters, parsers) and the LLM Agent have a highly predictable structure to work with, reducing parsing errors and edge-cases.
- **Positive:** Centralizing the definition in `TEMPLATE.md` makes future global structure updates straightforward.
- **Negative:** Human readers will occasionally encounter pages with multiple empty sections marked with `- None`, which may feel slightly bureaucratic or noisy.

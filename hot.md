# Hot Cache

**Last Updated:** 2026-06-28

## Current Focus
*   Resolved issues from the latest lint report to maintain Wiki health.

## Active Files
*   `plans/deduplicate_sources.md`
*   `index.md`

## Decisions in Flight
*   How to effectively set up limits (cost/tokens) for Dynamic Workflows to prevent runaway costs?
*   Should we integrate more lightweight models like Haiku into our own automated summarization tools?
*   What are the cost implications or token limits associated with running long or frequent automated workflows (Routines) on Claude Code?

## Recent Changes
*   Deduplicated and standardized source files (renamed to `snake_case.md` and merged duplicates) via Orchestration Plan `plans/deduplicate_sources.md`.
*   Systematically fixed all issues from Lint Report 2026-06-27 via Orchestration Plan (stubbed 15 dead links, auto-linked 2 orphans, filled frontmatter gaps for Claude, resolved invalid sections in claude_code).
*   Systematically fixed all issues from Lint Report 2026-06-24 via Orchestration Plan (stubbed 15 dead links, auto-linked 12 orphans, filled frontmatter gaps, resolved empty sections, and cleaned 27 stale entries in index.md).
*   Ingested Claude Prompt Caching concepts, Token Dashboard, and Session Handoff.
*   Updated `index.md` and `log.md` with new Wiki pages for Prompt Caching.


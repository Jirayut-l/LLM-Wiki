# 1. Wiki Knowledge Synthesis Strategy

Date: 2026-06-27

## Status

Accepted

## Context

When the Agent performs the `ingest` workflow on a new Raw Source, it often encounters information about concepts or entities that already exist in the Wiki (verified via the Pre-flight Entity Check against `index.md`). We needed a standardized strategy for how to integrate this new, sometimes overlapping or conflicting, information into the existing Wiki pages without destroying the current knowledge base or creating unreadable append-only logs.

## Decision

We have decided on the following workflow for updating existing Wiki pages during ingestion:

1. **Synthesized Source of Truth**: Existing pages will act as a unified source of truth. New information will be merged (synthesized) into the existing document structure (e.g., adding to the definition, updating properties) rather than appending a new section like "Updates from Source B" at the bottom.
2. **Preserve & Compare for Conflicts**: If the new source contradicts the existing information, the Agent will **not** overwrite the old data. Instead, it will preserve both perspectives (e.g., "Source A states X, while Source B argues Y") to maintain the nuance and diversity of knowledge.
3. **Staging with Full File Copy**: During the Staging Phase, the Agent will create a complete copy of the existing page in `plans/drafts/` (e.g., `draft_concept_name.md`), perform the synthesis on this draft, and present the whole file for the user to review. This ensures the user can see the final state in context before committing it to the `wiki/` directory.
4. **Full Autonomy for Subagents**: To reduce bottlenecks, Subagents will be given the Raw Source and the original Wiki file, and they will be fully responsible for reading, comparing, synthesizing, and generating the full draft file autonomously.

## Consequences

- **Positive**: The Wiki will remain structured, clean, and highly readable as a synthesized knowledge base rather than a fragmented log.
- **Positive**: Users have full visibility and control over changes before they are committed, thanks to the Full File Copy staging.
- **Negative**: The Agent and Subagents will consume more tokens during the Staging Phase because they must read and write the entire file contents even for small updates.

# 2. Static Agent-Maintained Index over Dynamic Dataview

Date: 2026-06-14

## Status

Accepted

## Context

We are using a Flat Directory structure with Obsidian Properties. In a typical Obsidian workflow, users rely on the Dataview plugin to dynamically generate index tables. However, the LLM Wiki relies on the LLM reading the `index.md` file first to navigate the knowledge base. The LLM cannot execute or render Dataview queries; it only sees the raw markdown code.

## Decision

We will use a **Static Agent-Maintained Index** (`index.md`). We explicitly reject the use of Dataview for the central index. Instead, the LLM Agent is required to manually update (bookkeep) `index.md` as plain markdown text on every Ingest operation.

## Consequences

- **Pros:** The LLM can read `index.md` natively and instantly grasp the entire map of the Wiki. It perfectly aligns with the philosophy that the LLM performs the "grunt work" of bookkeeping.
- **Cons:** The LLM must perform an extra file modification step during every ingest. There is a slight risk of formatting drift over time, which will be mitigated by the `Lint` operation.

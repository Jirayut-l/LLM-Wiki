# 3. Unified Topic Synthesis Model

Date: 2026-06-27

## Status

Accepted

## Context

Previously, the Wiki structure included a dedicated `wiki/summarize` directory (with its own `summary.md` template) intended for aggregating knowledge from multiple sources. Meanwhile, `wiki/sources` was used for extracting information from individual inputs, and `wiki/concepts` was strictly reserved for academic or theoretical principles.

This structure caused behavioral overlap and confusion for the Agent. When a single piece of information was ingested, `wiki/sources` and `wiki/summarize` served nearly identical functions. Furthermore, there was ambiguity regarding where to place topic-level summaries that synthesized multiple sources but didn't quite reach the rigorous standard of a "Concept", or where to place aggregations of information about specific concrete objects (like a tool or a person).

## Decision

We have decided to eliminate the dedicated `summarize` layer and redefine the boundaries of our existing knowledge buckets based on structure and concreteness:

1. **Abolish `wiki/summarize`**: The `summarize` directory and its corresponding `summary.md` template have been permanently removed.
2. **Strict 1:1 Rule for Sources**: `wiki/sources` is now strictly limited to a 1:1 mapping with external raw inputs (1 Source = 1 File). It serves as a metadata index and a summary of *only* that specific piece of content. Multiple URLs or articles cannot be aggregated into a single Source page.
3. **Expand Concepts for Abstract Topic Synthesis**: `wiki/concepts` is no longer restricted to pure academic principles. It now handles all N:1 Topic Synthesis for abstract ideas, methods, or themes. Any knowledge resulting from combining multiple sources to form a generalized topic overview will be categorized as a Concept.
4. **Entities for Concrete Topic Synthesis**: `wiki/entities` now mirrors the Topic Synthesis capability of Concepts, but strictly for "Proper Nouns" (concrete people, places, tools, organizations). Synthesizing multiple articles about "Claude Code" (a specific tool) goes into an Entity, not a Concept.

## Consequences

- **Positive**: Eliminates decision paralysis for the Agent when deciding between creating a Source, a Summary, or a Concept.
- **Positive**: Establishes a crystal-clear distinction between Metadata (Sources) and Synthesized Knowledge (Concepts/Entities).
- **Positive**: Provides a clear boundary between abstract topics (Concepts) and concrete things (Entities) when aggregating knowledge.
- **Negative**: Topic overviews might initially feel slightly "diluted" in the `concepts` folder if they are merely news aggregations rather than profound principles, though this trade-off is worth the structural clarity.

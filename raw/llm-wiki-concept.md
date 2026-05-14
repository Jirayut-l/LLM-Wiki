# LLM Wiki: A Pattern for Building Personal Knowledge Bases using LLMs

The core idea is to move beyond simple RAG (Retrieval-Augmented Generation) where an LLM rediscovers knowledge from scratch for every query. Instead, the LLM incrementally builds and maintains a persistent wiki—a structured, interlinked collection of markdown files.

## Key Layers
1. **Raw Sources**: Immutable curated collection of source documents.
2. **The Wiki**: LLM-generated markdown files (summaries, entity pages, etc.).
3. **The Schema**: Configuration file (e.g., GEMINI.md) defining structure and workflows.

## Operations
- **Ingest**: Processing new sources into the wiki.
- **Query**: Asking questions against the compiled wiki knowledge.
- **Lint**: Periodically health-checking the wiki for consistency and gaps.

## Key Components
- **index.md**: Content-oriented catalog.
- **log.md**: Chronological record of operations.

## Inspiration
Related to Vannevar Bush's Memex (1945)—a personal, curated knowledge store with associative trails between documents. The LLM handles the maintenance burden that previously made such systems unsustainable for individuals.

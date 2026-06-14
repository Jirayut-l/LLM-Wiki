# 1. Explicit Agent Workflows

Date: 2026-06-14

## Status

Accepted

## Context

We need a way to orchestrate the Agent to perform complex, multi-step tasks (like "Ingest") by utilizing various available skills (`defuddle`, `obsidian-markdown`, `json-canvas`, etc.). We could either rely on the LLM's dynamic reasoning to pick and choose skills on the fly, or explicitly document predefined Workflows.

## Decision

We will use **Explicit Workflows** stored in `.agents/workflows/`. Each workflow will be a markdown file that explicitly outlines the step-by-step process the Agent must follow to achieve a specific goal. 

To inform the Agent of what skills are required before it begins, every workflow file will use YAML frontmatter to list its dependencies. For example:
```yaml
---
name: Web Ingestion
skills:
  - defuddle
  - obsidian-markdown
---
```

## Consequences

- **Pros:** Highly predictable and consistent behavior. Easy to debug and version control. Ensures the Agent doesn't hallucinate non-existent skills or skip critical steps like updating logs and indexes.
- **Cons:** Less flexible. Requires maintaining a new folder of documentation. New use-cases will require writing a new workflow file instead of just casually prompting the Agent.

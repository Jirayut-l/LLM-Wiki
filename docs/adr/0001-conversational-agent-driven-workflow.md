# 1. Conversational Agent-Driven Workflow

Date: 2026-06-14

## Status

Accepted

## Context

We need to decide how the LLM interacts with the file system to ingest new Raw Sources and maintain the Wiki. The two main approaches are a headless, automated CLI/Watchdog process that ingests files automatically, or a conversational approach where the user manually prompts a chat-based LLM agent to process files and update the Wiki.

## Decision

We will use a **Conversational Agent-Driven Workflow**. The user will drop raw files into the workspace and explicitly interact with an LLM Agent (via a chat interface) to trigger the `Ingest`, `Query`, and `Lint` operations.

## Consequences

- **Pros:** The user remains tightly in the loop, allowing them to guide the LLM on what to emphasize during ingestion. The LLM can ask clarifying questions before writing to the Wiki.
- **Cons:** It requires active user participation to trigger the pipeline; it is not a fully automated "drop and forget" system. It relies on the LLM's context window and the user's prompts rather than hardcoded scripts.

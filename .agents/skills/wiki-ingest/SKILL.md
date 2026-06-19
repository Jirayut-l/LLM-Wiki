---
name: wiki-ingest
description: "Ingest sources into the Obsidian wiki vault. Reads a source, extracts entities and concepts, creates or updates wiki pages, cross-references, and logs the operation. Supports Local Files (.raw/) and Web URLs (via defuddle). Triggers on: ingest, process this source, add this to the wiki."
---

# wiki-ingest: Source Ingestion (Trigger)

This skill serves as the **Entry Point** for ingesting any new source (URL or Local File) into the knowledge base.

## Primary Instruction

When triggered by the user, **DO NOT** attempt to perform the ingestion steps manually or ad-hoc. 

Instead, you **MUST** immediately execute the Unified Ingestion Workflow defined in:
`[ingestion.md](file:///Users/spectrum/Resources/LLM-Wiki/.agents/workflows/ingestion.md)`

Please read the workflow file and follow its phases, orchestration plan rules, and check-pointing requirements strictly.

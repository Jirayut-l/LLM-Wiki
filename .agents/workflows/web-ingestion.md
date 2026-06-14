---
name: Web Ingestion
description: Process for ingesting a web URL into the persistent Wiki
skills:
  - defuddle
  - obsidian-markdown
---

# Web Ingestion Workflow

Use this workflow when the user provides a web URL and asks to ingest it into the knowledge base.

## Steps

1. **Extract Content**
   - Invoke the `defuddle` skill to extract clean markdown from the provided URL.
   
2. **Process and Format**
   - Read the extracted markdown content.
   - Synthesize the knowledge according to the Wiki rules in `CONTEXT.md`.
   - Invoke the `obsidian-markdown` skill to properly format and create a new `.md` page in the Wiki.

3. **Update the Index**
   - Add a reference to the newly created Wiki page in `index.md`.

4. **Log the Action**
   - Record the ingestion event in `log.md` with an audit trace detailing which files were created.

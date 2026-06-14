---
name: Ingestion
description: Standard unified process for ingesting any raw source (Local File or Web URL) into the Wiki using an Orchestration Plan with strict Checkpoints.
skills:
  - defuddle
  - obsidian-markdown
---

# Unified Ingestion Workflow

Use this workflow **every time** the user asks to "ingest" a file, raw source, or web URL into the knowledge base. This ensures a systematic, step-by-step approach where the user has full control over the quality of the Wiki through Checkpoints.

## Steps

1. **Extract and Analyze the Source**
   - **If the user provides a Web URL:** Invoke the `defuddle` skill to extract clean markdown from the provided URL.
   - **If the user provides a Local File:** Read the target raw source file (usually from the `raw/` directory).
   - Read the extracted or raw content and identify the main concepts, techniques, or entities that need to be extracted and added to the Wiki.

2. **Create the Orchestration Plan**
   - Create a new markdown file in the `plans/` directory named `ingest_[topic_name]__plan.md`.
   - Follow the structure defined in `docs/template_orchestration_plan.md`.
   - Break down the ingestion into logical **Phases** (e.g., Phase 1: Core Concepts, Phase 2: Techniques).
   - The final Phase must always be **Index & Audit Log Update**.
   - Include a **Checkpoint** at the end of every Phase. The Agent MUST stop and wait for the user to type "อนุมัติ" (Approve) before proceeding to the next Phase.
   - Present the summary of the created plan to the user and wait for their approval to start Phase 1.

3. **Execute Phases Step-by-Step**
   - Execute the tasks for the current Phase (e.g., creating or updating Wiki pages).
   - Always use `TEMPLATE.md` when creating new Wiki pages. Synthesize the knowledge according to the Wiki rules in `CONTEXT.md` and properly format using the `obsidian-markdown` skill.
   - Check off (`[x]`) the tasks in the Orchestration Plan file as they are completed.
   - Stop execution at the end of the Phase and ask the user for "อนุมัติ" (Checkpoint). Do not proceed to the next Phase until explicit approval is given.

4. **Final Updates (Index & Logs)**
   - In the final Phase, update `index.md` by listing the new concepts/entities and linking the ingested raw source.
   - Append a chronological audit trace of all created/updated files to `logs/log.md`.
   - Check off the final tasks in the plan and notify the user that the ingestion process is 100% complete.

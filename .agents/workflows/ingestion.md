---
name: Ingestion
description: Standard unified process for ingesting any raw source (Local File or Web URL) into the Wiki using an Orchestration Plan with strict Checkpoints.
skills:
  - defuddle
  - obsidian-markdown
  - json-canvas
  - obsidian-bases
  - wiki-lint
  - wiki-fold
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
   - **Granular Task Breakdown & Single-File Scope**: Sub-tasks within each Phase must be granular. Each task must explicitly target exactly **one specific file** (e.g., `[ ] Create wiki/concepts/llm.md`) to enable parallel delegation to subagents.
   - The final Phase must always be **Index, Audit Log, & Hot Cache Update**.
   - Include a **Verification** step at the end of every Staging Phase, and a single **Checkpoint** only at the final Commit Phase.
   - After creating the Orchestration Plan, immediately proceed to execute Phase 1 without waiting for user approval.

3. **Execute Phases Step-by-Step**
   - Execute the tasks for the current Phase. **If there are multiple files in a Phase, you should invoke Subagents to process each file in parallel** for maximum efficiency.
   - Determine the appropriate page `type` (e.g., `concept`, `entity`, `source`) and copy the exact frontmatter and heading structure from the corresponding template in the `_templates/` directory. Delete any sections that have no content. Synthesize the knowledge according to the Wiki rules in `CONTEXT.md` and properly format using the `obsidian-markdown` skill.
   - **Data Accuracy, Research & Content Rules**:
     - **Content Visualization & Structuring**: If the content is complex or difficult to understand, you must proactively use interactive elements to supplement the text:
       - **Simple flows/comparisons**: Use standard Markdown tables or Mermaid flowcharts.
       - **Complex networks/relationships**: Invoke the `json-canvas` skill to create a visual `.canvas` map.
       - **Structured/Repetitive data**: Invoke the `obsidian-bases` skill to create a `.base` file for database-like views.
       *(Note: Do not reduce the depth or length of the text summary when adding visualizations.)*
     - **Strict No-Hallucination**: ห้ามแต่งเติมหรือบิดเบือนข้อมูลที่อ้างอิงจากเอกสารต้นฉบับเด็ดขาด สามารถอธิบายเนื้อหาให้เข้าใจง่ายได้ แต่ต้องคงความหมายหลักไว้
     - **Web Search for Gaps**: หากข้อมูลในต้นฉบับไม่เพียงพอหรือไม่แน่ใจ ให้ใช้เครื่องมือ Web Search เพื่อค้นหาข้อมูลเพิ่มเติมมาเสริมได้ **แต่ต้องระบุแหล่งที่มาอ้างอิงให้ชัดเจน** ว่าเนื้อหาส่วนใดมาจากต้นฉบับ และส่วนใดมาจาก Web Search
     - **Unresolved Questions**: หากค้นหาข้อมูลเพิ่มเติมแล้วยังไม่พบข้อเท็จจริงที่ยืนยันได้ ให้ใส่หัวข้อใหม่ชื่อ `## Questions to follow up` ไว้ที่ด้านล่างสุดของหน้า Wiki นั้นๆ
   - Check off (`[x]`) the tasks in the Orchestration Plan file as they are completed.
   - **Phase Verification**: Invoke the `verifier` subagent (defined in `.agents/agents/verifier.md`) to review the drafted pages of this phase for accuracy and formatting against the source. If issues are found, attempt to fix them automatically (up to 2 retries). If issues persist, log them and proceed to the next Phase. Unresolved issues will be presented at the final Checkpoint.

4. **Updates Phase (Index, Logs, & Hot Cache)**
   - This must be the final Phase in your Orchestration Plan.
   - **Final Checkpoint**: This is the ONLY checkpoint in the workflow. Stop execution and present a consolidated report of the plan, all drafted files, and any unresolved verifier issues. Ask the user for explicit approval ("อนุมัติ") before making any changes to the main Wiki.
   - *Note on Log Rollup*: If `log.md` is expected to exceed 100 entries, include a note in your Checkpoint message that you will also automatically run the `wiki-fold` skill upon approval.
   - Once approved, proceed to execute the phase:
     - Move the approved draft files to their final `wiki/` locations.
     - Update `index.md` by listing the new concepts/entities and linking the ingested raw source.
     - Append a chronological audit trace of all created/updated files to `log.md`. (If over 100 entries, invoke `wiki-fold` now).
     - Update `hot.md` to briefly summarize the recent ingestion and any new open decisions or ongoing focuses. **If there were any "Questions to follow up" generated in Step 3, you MUST record them here as Open Items / Decisions in Flight.**

5. **Wiki Health Check**
   - Once all Phases (including the Updates Phase) are fully completed and verified, invoke the `wiki-lint` skill to scan the vault. Generate a health report to ensure no dead links or orphan pages were accidentally created during this ingestion. 
   - **Zero-Warning Policy**: If `wiki-lint` reports any issues, you must strongly encourage the user to resolve them immediately by running the `wiki-lint-fix` skill. Do not let issues accumulate. Notify the user that the ingestion process is complete but issues need fixing.

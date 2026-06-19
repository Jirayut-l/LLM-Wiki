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
   - Include a **Checkpoint** at the end of every Phase. The Agent MUST stop and wait for the user to type "อนุมัติ" (Approve) before proceeding to the next Phase.
   - Present the summary of the created plan to the user and wait for their approval to start Phase 1.

3. **Execute Phases Step-by-Step**
   - Execute the tasks for the current Phase (e.g., creating or updating Wiki pages). **If there are multiple files in a Phase, you should invoke Subagents to process each file in parallel** for maximum efficiency.
   - Always use `TEMPLATE.md` when creating new Wiki pages. Synthesize the knowledge according to the Wiki rules in `CONTEXT.md` and properly format using the `obsidian-markdown` skill.
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
   - Stop execution at the end of the Phase and ask the user for "อนุมัติ" (Checkpoint). Do not proceed to the next Phase until explicit approval is given.

4. **Verification**
   - **Peer Review**: Invoke the `verifier` subagent (defined in `.agents/agents/verifier.md`) to review the drafted pages for accuracy and formatting against the source.

5. **Updates (Index, Logs, & Hot Cache)**
   - In the final Phase, update `index.md` by listing the new concepts/entities and linking the ingested raw source.
   - Append a chronological audit trace of all created/updated files to `log.md`.
   - **Log Rollup Check**: After appending to `log.md`, check its length. If it exceeds 100 entries, stop and create a **Checkpoint**. Notify the user that the log is getting long and ask for explicit approval ("อนุมัติ") to invoke the `wiki-fold` skill to roll up the old log entries into meta-pages.
   - Update `hot.md` to briefly summarize the recent ingestion and any new open decisions or ongoing focuses. **If there were any "Questions to follow up" generated in Step 3, you MUST record them here as Open Items / Decisions in Flight.**
   - Check off the final tasks in the plan and notify the user that the ingestion process is 100% complete.

6. **Wiki Health Check**
   - Once verified, invoke the `wiki-lint` skill to scan the vault and generate a health report to ensure no dead links or orphan pages   were accidentally created during this ingestion.

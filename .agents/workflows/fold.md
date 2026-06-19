---
name: Fold
description: Standard workflow for rolling up wiki/log.md entries into meta-pages. Operates in a 2-step process with a checkpoint.
skills: []
---

# Unified Fold Workflow

A "fold" is a periodic rollup of `wiki/log.md` entries to keep the log manageable and synthesize past work.
This workflow operates strictly in a **2-Step Process** (Draft/Dry-run -> Commit) and requires **Extractive Summarization**.

## Phase 1: Draft / Dry-run

1. **Identify the Range**: Understand how many log entries the user wants to fold (e.g., N entries, or a date range). If not specified, default to the last 10 entries.
2. **Read the Logs**: Use file reading tools to read the target entries from `wiki/log.md`.
3. **Generate the Draft**: Summarize the activities in the chat. 
   **CRITICAL CONSTRAINT (Extractive Only)**: 
   - You must NOT invent or hallucinate any themes, facts, or actions. 
   - Every bullet point in your summary MUST be traceable to a specific log entry. 
   - Include citations in your draft (e.g., "*(อ้างอิงจาก log YYYY-MM-DD: เรื่อง...)*").
4. **Present the Draft**: Send the drafted summary to the user in the chat and ask: "ร่างการสรุป Log (Fold) ถูกต้องไหมครับ? ต้องการให้สร้างไฟล์บันทึกลงระบบเลยไหม?"
5. **Checkpoint**: **Stop and Wait**. Do not create any files or proceed to Phase 2 until the user explicitly approves.

---

## Phase 2: Commit

Once the user approves the draft at the checkpoint:

1. **Determine the Fold ID**: Generate a deterministic ID based on the range. 
   Format: `fold-from-[EARLIEST-DATE]-to-[LATEST-DATE]-n[COUNT]` 
   Example: `fold-from-2026-04-10-to-2026-04-20-n10`
   
2. **Create the Fold Page**: Write the approved summary into `wiki/folds/[FOLD-ID].md`. 
   Include YAML frontmatter:
   ```yaml
   ---
   type: meta
   title: "Fold: [EARLIEST-DATE] to [LATEST-DATE]"
   entries_count: [COUNT]
   tags: [meta, fold]
   ---
   ```
   
3. **Update the Index**: Add a link to the new fold page in `wiki/index.md` under the `## Folds` section (create the section if it doesn't exist).

4. **Update the Master Log**: Prepend a new entry at the top of `wiki/log.md` to record that a fold occurred:
   ```markdown
   ## [CURRENT-DATE] fold | Rollup of [COUNT] entries
   - Location: [[wiki/folds/[FOLD-ID].md]]
   - Range: [EARLIEST-DATE] to [LATEST-DATE]
   - Note: บีบอัดข้อมูล [COUNT] รายการ
   ```
   *(Note: For this MVP, we are doing a "soft fold", meaning we do NOT delete the original entries from `log.md`. We just create the summary.)*

---

## Workflow Constraints & Rules

- **Extractive Only**: Do not synthesize beyond what the child entries explicitly support.
- **No Deletions**: Never delete the original entries from `log.md`. This is a non-destructive rollup.
- **Thai Language**: Use Thai for all chat interactions and the content of the fold summaries.

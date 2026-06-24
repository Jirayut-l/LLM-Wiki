# Orchestration Plan: Ingest "Build a proactive agent workflow with Claude Code"

## 🎯 Goal
Ingest the transcript "Build a proactive agent workflow with Claude Code", extracting core concepts about Claude Code's "Routines" feature, its components (triggers, context, and steerability), and use cases for proactive agents. Synthesize this into structured Wiki pages.

## 🛠️ Phases

### Staging Phase 1: Source & Core Concept
- [x] Create `plans/drafts/source_build_a_proactive_agent_workflow_with_claude_code.md` (using `_templates/source.md`) to capture the metadata and overview of the transcript.
- [x] Create `plans/drafts/concept_claude_code_routines.md` (using `_templates/concept.md`) to define "Routines", the feature that turns Claude Code into a proactive teammate.
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้

### Staging Phase 2: Components & Use Cases
- [x] Create `plans/drafts/concept_routine_triggers.md` (using `_templates/concept.md`) detailing Time-based (schedule) and Event-based (GitHub events, webhooks) triggers.
- [x] Create `plans/drafts/concept_routine_context_and_steerability.md` (using `_templates/concept.md`) detailing Context (repos, connectors) and Steerability (human-in-the-loop, agent-on-agent review).
- [x] Create `plans/drafts/concept_proactive_agent_use_cases.md` (using `_templates/concept.md`) to capture use cases like documentation automation and deploy verifier.
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้

### Staging Phase 3: Synthesis & Summary
- [x] Create `plans/drafts/claude_code_routines_summary.md` (using `_templates/summary.md`) to synthesize the overall workflow of building proactive agents with Claude Code.
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้

### Commit Phase: Updates & Migration
*(Phase สุดท้ายของทุก Orchestration Plan เสมอ)*
- [x] **Move Files:** ย้ายไฟล์ทั้งหมดจาก `plans/drafts/` ไปยังตำแหน่งจริงใน `wiki/` (เช่น `wiki/sources/` และ `wiki/concepts/`)
- [x] **Update Index:** เพิ่มลิงก์และเนื้อหาใหม่ลงในไฟล์ `index.md`
- [x] **Update Master Log:** บันทึกการกระทำลงใน `log.md` (พร้อมตรวจสอบว่าถ้าเกิน 100 entries ให้แจ้งเตือนทำ Log Rollup)
- [x] **Update Hot Cache:** อัปเดต `hot.md` (ด้วย Focus ปัจจุบัน, การตัดสินใจ หรือคำถามที่ต้องตามต่อ)
- **Verification:** รัน `wiki-lint` ตรวจสอบความถูกต้องของโครงสร้างทั้งระบบ
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ถือเป็นการจบแผนงาน

## 🚦 State Management
- ให้ Agent หลักคอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดู

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Subagent)
1. **Micro-tasking & Single-File Scope:** 1 Task ต้องครอบคลุมแค่ 1 ไฟล์เท่านั้น เพื่อให้สามารถแยกงานให้ Subagent ทำคู่ขนาน (Parallel) กันได้
2. **Phase Verification:** ทุก Phase จะต้องมีการเรียก `verifier` subagent มารีวิวงานก่อนเสมอ เพื่อให้ User ได้เห็นข้อผิดพลาดและปรับแก้ก่อนอนุมัติ
3. **Strict Checkpoints:** ห้ามข้ามไปทำ Phase ถัดไปเด็ดขาด หาก User ยังไม่ได้ตรวจสอบและพิมพ์คำว่า "อนุมัติ"
4. **Cross-Referencing Guarantee:** ทุกครั้งที่มีการสร้างเนื้อหาใหม่ จะต้องทำเชื่อมโยง `[[Wikilinks]]` ไปยังเนื้อหาเดิมใน Wiki อย่างครบถ้วน
5. **Staging Isolation:** การสร้างหรือแก้ไขไฟล์เนื้อหาใหม่ในช่วง Staging Phase จะต้องทำในโฟลเดอร์ `plans/drafts/` เท่านั้น ห้ามแก้ไขไฟล์ใน `wiki/` โดยตรงเด็ดขาด จนกว่าจะได้รับอนุมัติให้เข้าสู่ Commit Phase
6. **Page Template Adherence:** คัดลอก YAML frontmatter และหัวข้อมาตรฐานจากหน้าเทมเพลตที่ตรงกับ `type` ในโฟลเดอร์ `_templates/` ทุกครั้งที่สร้างไฟล์ใหม่

## Verification Report

VERDICT: HOLD-FIX-FIRST

**HIGH** (1 finding)
- [x] plans/drafts/source_build_a_proactive_agent_workflow_with_claude_code.md:1 — Missing `url` in frontmatter, resulting in loss of the original YouTube link from the raw source.
  - **Fix:** Add `url: "https://www.youtube.com/watch?v=eSP7PLTXNy8&t=369s"` back to the frontmatter.

**MEDIUM** (1 finding)
- [x] plans/drafts/concept_claude_code_routines.md:58 — Missing connection to "Decisions in Flight" from `hot.md` regarding cost/token limits for automated workflows.
  - **Fix:** Add a `## Questions to follow up` section and include the open question about cost/token limits for Routines to track this concern.

### Phase 2 Verification Report

VERDICT: PASS

The three drafted concept files (`concept_routine_triggers.md`, `concept_routine_context_and_steerability.md`, and `concept_proactive_agent_use_cases.md`) have been successfully verified. 

**Review Details:**
- **Template Compliance:** All three files correctly implement the `_templates/concept.md` layout, including properly formatted YAML frontmatter.
- **Source Accuracy:** The extracted information directly aligns with the raw source transcript.
- **Cross-Referencing:** The `## Related` sections contain the appropriate Wikilinks.
- **Staging Isolation:** All new content is safely contained within `plans/drafts/` in accordance with the Orchestration Plan's Execution Rule #5.

### Phase 3 Verification Report

VERDICT: PASS

The Phase 3 draft (`plans/drafts/claude_code_routines_summary.md`) has been successfully verified. 

**Review Details:**
- **Template Compliance:** The file perfectly adheres to the `_templates/summary.md` layout, including properly formatted YAML frontmatter (type, aliases, tags, created, sources).
- **Source Accuracy:** The summarized content is accurate and directly synthesized from the raw transcript.
- **Cross-Referencing:** The `## Related Concepts` section contains the correct Wikilinks to the previously drafted concepts from Phases 1 and 2.
- **Staging Isolation:** The new content is safely contained within `plans/drafts/` in accordance with the Execution Rules.

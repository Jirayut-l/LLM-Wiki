# Orchestration Plan: Ingest "Give Me 10 Mins and I'll Save You Millions of Claude Tokens"

## 🎯 Goal (เป้าหมายหลัก)
Ingest knowledge about Claude Prompt Caching, Token Dashboard, Session Handoff, and Nate Herk from the raw YouTube video transcript.

## 🛠️ Phases (ลำดับการทำงาน)

### Staging Phase 1: Entities & Basic Tools
- [x] Create `plans/drafts/nate_herk.md` (Entity: Author of the video/content)
- [x] Create `plans/drafts/token_dashboard.md` (Concept/Tool: Local token tracking dashboard)
- [x] Create `plans/drafts/session_handoff.md` (Concept/Skill: Session handoff strategy)
- **Verification:** เรียบร้อยแล้ว (Verified)

## Verification Report (Phase 1)
VERDICT: SHIP

**BLOCKER** (0 findings)
**HIGH** (0 findings)
**MEDIUM** (0 findings)
**LOW** (0 findings)

### Staging Phase 2: Core Concepts
- [x] Create `plans/drafts/claude_prompt_caching.md` (Concept: Mechanisms of Prompt Caching, TTL, cost structures, and what breaks cache)
- **Verification:** เรียบร้อยแล้ว (Verified)

## Verification Report (Phase 2)
VERDICT: SHIP

**BLOCKER** (0 findings)
**HIGH** (0 findings)
**MEDIUM** (0 findings)
**LOW** (0 findings)

### Staging Phase 3: Synthesis & Summary
- [x] Create `plans/drafts/claude_prompt_caching_summary.md` (Summary: Key takeaways linking to the concept and source file)
- **Verification:** เรียบร้อยแล้ว (Verified)

## Verification Report (Phase 3)
VERDICT: SHIP

**BLOCKER** (0 findings)
**HIGH** (0 findings)
**MEDIUM** (0 findings)
**LOW** (0 findings)

### Commit Phase: Updates & Migration
*(Phase สุดท้ายของทุก Orchestration Plan เสมอ)*
- **Checkpoint:** หยุดรอให้ User ตรวจสอบผลงานทั้งหมดใน Staging (พร้อมแสดง unresolved issues ถ้ามี) และพิมพ์ "อนุมัติ" ก่อนเริ่มดำเนินการ Commit
- [ ] **Move Files:** ย้ายไฟล์ทั้งหมดจาก `plans/drafts/` ไปยังตำแหน่งจริงใน `wiki/` (เช่น `wiki/concepts/`, `wiki/entities/`)
- [ ] **Update Index:** เพิ่มลิงก์และเนื้อหาใหม่ลงในไฟล์ `index.md`
- [ ] **Update Master Log:** บันทึกการกระทำลงใน `log.md` (หากเกิน 100 entries ให้รัน `wiki-fold` skill ทันที)
- [ ] **Update Hot Cache:** อัปเดต `hot.md` (ด้วย Focus ปัจจุบัน, การตัดสินใจ หรือคำถามที่ต้องตามต่อ)
- **Verification:** รัน `wiki-lint` ตรวจสอบความถูกต้องของโครงสร้างทั้งระบบ ถือเป็นการปิดงาน

## 🚦 State Management
- ให้ Agent หลักคอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดู

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Subagent)
1. **Micro-tasking & Single-File Scope:** 1 Task ต้องครอบคลุมแค่ 1 ไฟล์เท่านั้น เพื่อให้สามารถแยกงานให้ Subagent ทำคู่ขนาน (Parallel) กันได้
2. **Phase Verification:** ทุก Phase จะต้องมีการเรียก `verifier` subagent มารีวิวงาน หากพบข้อผิดพลาดให้พยายามแก้ไขอัตโนมัติก่อน (1-2 ครั้ง) หากแก้ไม่ตกให้รวบรวมไว้รายงานใน Checkpoint สุดท้าย ไม่ต้องหยุดรอระหว่าง Phase
3. **Cross-Referencing Guarantee:** ทุกครั้งที่มีการสร้างเนื้อหาใหม่ จะต้องทำเชื่อมโยง `[[Wikilinks]]` ไปยังเนื้อหาเดิมใน Wiki อย่างครบถ้วน
4. **Staging Isolation:** การสร้างหรือแก้ไขไฟล์เนื้อหาใหม่ในช่วง Staging Phase จะต้องทำในโฟลเดอร์ `plans/drafts/` เท่านั้น ห้ามแก้ไขไฟล์ใน `wiki/` โดยตรงเด็ดขาด จนกว่าจะได้รับอนุมัติให้เข้าสู่ Commit Phase
5. **Page Template Adherence:** คัดลอก YAML frontmatter และหัวข้อมาตรฐานจากหน้าเทมเพลตที่ตรงกับ `type` ในโฟลเดอร์ `_templates/` ทุกครั้งที่สร้างไฟล์ใหม่

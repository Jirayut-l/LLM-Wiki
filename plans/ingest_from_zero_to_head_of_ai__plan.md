# Orchestration Plan: Ingest "From Zero to Head of AI in 1 Year (as a regular person)"

## 🎯 Goal (เป้าหมายหลัก)
Ingest the YouTube video transcript of the interview between Nate Herk and Ailin into the Wiki. Extract key entities (Ailin, Yang), concepts (Head of AI role, "Show Yourself" mindset), and create a central source document and summary linking them together.

## 🛠️ Phases (ลำดับการทำงาน)

### Staging Phase 1: Core Profile & Source
- [x] Create `plans/drafts/source_from_zero_to_head_of_ai.md`
- [x] Create `plans/drafts/entity_ailin.md`
- [x] Create `plans/drafts/entity_yang.md`
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้

### Staging Phase 2: Concepts
- [x] Create `plans/drafts/concept_head_of_ai.md` (Detailing the non-technical Head of AI role, strategy vs hands-on using tools like n8n/Claude Code)
- [x] Create `plans/drafts/concept_show_yourself.md` (Detailing the "Show Yourself" / Build in Public mindset, and the Transition Curve from Alex Hormozi)
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้

### Staging Phase 3: Synthesis & Summary
- [x] รวบรวมและสรุปภาพรวม เนื้อหาหลัก และ Key Takeaways ใน `plans/drafts/summary_zero_to_head_of_ai.md` เพื่อให้เชื่อมโยงไปยัง Concept หรือ Entity ได้ง่าย
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้

### Commit Phase: Updates & Migration
*(Phase สุดท้ายของทุก Orchestration Plan เสมอ)*
- **Checkpoint:** หยุดรอให้ User ตรวจสอบผลงานทั้งหมดใน Staging (พร้อมแสดง unresolved issues ถ้ามี) และพิมพ์ "อนุมัติ" ก่อนเริ่มดำเนินการ Commit
- [x] **Move Files:** ย้ายไฟล์ทั้งหมดจาก `plans/drafts/` ไปยังตำแหน่งจริงใน `wiki/` (เช่น `wiki/concepts/`)
- [x] **Update Index:** เพิ่มลิงก์และเนื้อหาใหม่ลงในไฟล์ `index.md`
- [x] **Update Master Log:** บันทึกการกระทำลงใน `log.md` (หากเกิน 100 entries ให้รัน `wiki-fold` skill ทันที)
- [x] **Update Hot Cache:** อัปเดต `hot.md` (ด้วย Focus ปัจจุบัน, การตัดสินใจ หรือคำถามที่ต้องตามต่อ)
- **Verification:** รัน `wiki-lint` ตรวจสอบความถูกต้องของโครงสร้างทั้งระบบ ถือเป็นการปิดงาน

## 🚦 State Management
- ให้ Agent หลักคอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดู

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Subagent)
1. **Micro-tasking & Single-File Scope:** 1 Task ต้องครอบคลุมแค่ 1 ไฟล์เท่านั้น เพื่อให้สามารถแยกงานให้ Subagent ทำคู่ขนาน (Parallel) กันได้
2. **Phase Verification:** ทุก Phase จะต้องมีการเรียก `verifier` subagent มารีวิวงาน หากพบข้อผิดพลาดให้พยายามแก้ไขอัตโนมัติก่อน (1-2 ครั้ง) หากแก้ไม่ตกให้รวบรวมไว้รายงานใน Checkpoint สุดท้าย ไม่ต้องหยุดรอระหว่าง Phase
3. **Cross-Referencing Guarantee:** ทุกครั้งที่มีการสร้างเนื้อหาใหม่ จะต้องทำเชื่อมโยง `[[Wikilinks]]` ไปยังเนื้อหาเดิมใน Wiki อย่างครบถ้วน
4. **Staging Isolation:** การสร้างหรือแก้ไขไฟล์เนื้อหาใหม่ในช่วง Staging Phase จะต้องทำในโฟลเดอร์ `plans/drafts/` เท่านั้น ห้ามแก้ไขไฟล์ใน `wiki/` โดยตรงเด็ดขาด จนกว่าจะได้รับอนุมัติให้เข้าสู่ Commit Phase
5. **Page Template Adherence:** คัดลอก YAML frontmatter และหัวข้อมาตรฐานจากหน้าเทมเพลตที่ตรงกับ `type` ในโฟลเดอร์ `_templates/` ทุกครั้งที่สร้างไฟล์ใหม่

## Verification Report (Phase 1)

VERDICT: SHIP

**BLOCKER** (0 findings)
**HIGH** (0 findings)
**MEDIUM** (0 findings)
**LOW** (0 findings)

## Verification Report (Phase 2)

VERDICT: SHIP

**BLOCKER** (0 findings)
**HIGH** (0 findings)
**MEDIUM** (0 findings)
**LOW** (0 findings)

## Verification Report (Phase 3)

VERDICT: SHIP

**BLOCKER** (0 findings)
**HIGH** (0 findings)
**MEDIUM** (0 findings)
**LOW** (0 findings)

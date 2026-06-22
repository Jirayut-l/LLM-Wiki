# Orchestration Plan: Ingest Claude Subagents

## 🎯 Goal (เป้าหมายหลัก)
นำเข้าและสรุปเนื้อหาจากวีดีโอ "How to Build Claude Subagents Better Than 99% of People" เพื่อแยกย่อยแนวคิดเกี่ยวกับ Claude Subagents, Dynamic Workflows, และ Progressive Disclosure เข้าสู่ Wiki

## 🛠️ Phases (ลำดับการทำงาน)

### Staging Phase 1: Source Page
- [x] สร้างไฟล์อ้างอิงแหล่งที่มา: Create `plans/drafts/how_to_build_claude_subagents_source.md` โดยใช้ `_templates/source.md`
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบรายงานจาก Verifier และพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Staging Phase 2: Core Concept (Claude Subagent)
- [x] สร้างและสรุปแนวคิดเรื่อง Claude Subagents: Create `plans/drafts/claude_subagent.md` โดยใช้ `_templates/concept.md`
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Staging Phase 3: Concept (Dynamic Workflows)
- [x] สร้างและสรุปแนวคิดเรื่อง Dynamic Workflows: Create `plans/drafts/dynamic_workflow.md` โดยใช้ `_templates/concept.md`
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Staging Phase 4: Concept (Progressive Disclosure)
- [x] สร้างและสรุปแนวคิดเรื่อง Progressive Disclosure: Create `plans/drafts/progressive_disclosure.md` โดยใช้ `_templates/concept.md`
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Staging Phase 5: Synthesis & Summary
- [x] รวบรวมและสรุปภาพรวม เนื้อหาหลัก และ Key Takeaways: Create `plans/drafts/claude_subagents_summary.md` โดยใช้ `_templates/summary.md`
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Commit Phase: Updates & Migration
*(Phase สุดท้ายของทุก Orchestration Plan เสมอ)*
- [x] **Move Files:** ย้ายไฟล์ทั้งหมดจาก `plans/drafts/` ไปยังตำแหน่งจริงใน `wiki/` (เช่น `wiki/concepts/`, `wiki/sources/`)
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

**BLOCKER** (0 findings)

**HIGH** (1 finding)
- [x] `plans/ingest_claude_subagents_plan.md:9` — Phase 1 drafts multiple Content Pages in a single phase, violating the Single-File Scope Constraint.
  - **Fix:** Split Staging Phase 1 into two separate phases (one for source, one for concept).

**MEDIUM** (0 findings)

**LOW** (1 finding)
- [ ] `plans/drafts/how_to_build_claude_subagents_source.md:26` — Contains dead links to concepts that may not exist yet (e.g., `[[Claude Code]]`, `[[Orchestration]]`).
  - **Fix:** None required at this stage; will be resolved later by Wiki Lint.

**Phase 4 Verification (Progressive Disclosure):**
- **Single-File Scope**: PASS
- **Concept Template**: PASS
- **Cross-Referencing**: PASS
- **Staging Isolation**: PASS
- **Status**: Ready for User Approval.

**Phase 5 Verification (Synthesis & Summary):**
- **Single-File Scope**: PASS
- **Summary Template**: PASS
- **Cross-Referencing**: PASS
- **Staging Isolation**: PASS
- **Status**: Ready for User Approval.

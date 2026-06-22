# Orchestration Plan: [ชื่อโปรเจค/งาน]

## 🎯 Goal (เป้าหมายหลัก)
[เป้าหมายของการทำงานนี้]

## 🛠️ Phases (ลำดับการทำงาน)

### Staging Phase 1: [หัวข้อของ Phase เช่น Core Concepts]
- [ ] งานย่อย 1 (ระบุเป้าหมายเป็น 1 ไฟล์: e.g., Create `plans/drafts/xyz.md`)
- [ ] งานย่อย 2 (e.g., Create `plans/drafts/abc.md`)
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบรายงานจาก Verifier และพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Staging Phase 2: [หัวข้อของ Phase เช่น Techniques]
- [ ] งานย่อย 1 ...
- [ ] งานย่อย 2 ...
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Staging Phase [N-1]: Synthesis & Summary
- [ ] รวบรวมและสรุปภาพรวม เนื้อหาหลัก และ Key Takeaways (เช่น Create `plans/drafts/[ชื่อหัวข้อ]_summary.md` โดยใช้ `_templates/summary.md`) เพื่อให้เชื่อมโยงไปยัง Concept หรือ Entity ได้ง่าย
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Commit Phase: Updates & Migration
*(Phase สุดท้ายของทุก Orchestration Plan เสมอ)*
- [ ] **Move Files:** ย้ายไฟล์ทั้งหมดจาก `plans/drafts/` ไปยังตำแหน่งจริงใน `wiki/` (เช่น `wiki/concepts/`)
- [ ] **Update Index:** เพิ่มลิงก์และเนื้อหาใหม่ลงในไฟล์ `index.md`
- [ ] **Update Master Log:** บันทึกการกระทำลงใน `log.md` (พร้อมตรวจสอบว่าถ้าเกิน 100 entries ให้แจ้งเตือนทำ Log Rollup)
- [ ] **Update Hot Cache:** อัปเดต `hot.md` (ด้วย Focus ปัจจุบัน, การตัดสินใจ หรือคำถามที่ต้องตามต่อ)
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
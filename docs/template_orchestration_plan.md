# Orchestration Plan: [ชื่อโปรเจค/งาน]

## 🎯 Goal (เป้าหมายหลัก)
[เป้าหมายของการทำงานนี้]

## 🛠️ Phases (ลำดับการทำงาน)

### Phase 1: [หัวข้อของ Phase เช่น Core Concepts]
- [ ] งานย่อย 1 (ระบุเป้าหมายเป็น 1 ไฟล์: e.g., Create `wiki/concepts/xyz.md`)
- [ ] งานย่อย 2 (e.g., Create `wiki/entities/abc.md`)
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบรายงานจาก Verifier และพิมพ์ "อนุมัติ" ก่อนไป Phase ถัดไป

### Phase 2: [หัวข้อของ Phase เช่น Techniques]
- [ ] งานย่อย 1 ...
- [ ] งานย่อย 2 ...
- **Verification:** เรียก `verifier` subagent ตรวจสอบความถูกต้องและรูปแบบของเนื้อหาที่ทำใน Phase นี้
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ"

### Phase [N]: Updates (Index, Logs, & Hot Cache)
*(Phase สุดท้ายของทุก Orchestration Plan เสมอ)*
- [ ] อัปเดต `index.md` เพิ่มลิงก์และเนื้อหาใหม่
- [ ] อัปเดต `log.md` (ตรวจสอบ Log Rollup หากเกิน 100 entries)
- [ ] อัปเดต `hot.md` (เพิ่ม Focus, Decisions in Flight หรือ Questions to follow up)
- **Verification:** เรียก `wiki-lint` ตรวจสอบความถูกต้องของการอัปเดตโครงสร้าง
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ถือเป็นการจบแผนงาน

## 🚦 State Management
- ให้ Agent หลักคอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดู

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Subagent)
1. **Micro-tasking & Single-File Scope:** 1 Task ต้องครอบคลุมแค่ 1 ไฟล์เท่านั้น เพื่อให้สามารถแยกงานให้ Subagent ทำคู่ขนาน (Parallel) กันได้
2. **Phase Verification:** ทุก Phase จะต้องมีการเรียก `verifier` subagent มารีวิวงานก่อนเสมอ เพื่อให้ User ได้เห็นข้อผิดพลาดและปรับแก้ก่อนอนุมัติ
3. **Strict Checkpoints:** ห้ามข้ามไปทำ Phase ถัดไปเด็ดขาด หาก User ยังไม่ได้ตรวจสอบและพิมพ์คำว่า "อนุมัติ"
4. **Cross-Referencing Guarantee:** ทุกครั้งที่มีการสร้างเนื้อหาใหม่ จะต้องทำเชื่อมโยง `[[Wikilinks]]` ไปยังเนื้อหาเดิมใน Wiki อย่างครบถ้วน
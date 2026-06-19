# Orchestration Plan: [ชื่อโปรเจค/งาน]

## 🎯 Goal (เป้าหมายหลัก)
[เป้าหมายของการทำงานนี้]

## 🛠️ Phases (ลำดับการทำงาน)

### Phase 1: [ตัวอย่างงานทั่วไป] Research & Design
- [ ] ให้ Research Agent ไปศึกษา [หัวข้อ]
- [ ] ร่าง Schema หรือโครงสร้างข้อมูล
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase ถัดไป

### Phase 2: [ตัวอย่างงาน Ingest] Two-Phase Batch Ingestion
- **Phase 2A: Parallel Extraction (ทำขนาน)**
  - [ ] สร้าง Subagents แบบขนาน (Parallel) เพื่ออ่านและ Ingest ข้อมูลหลายไฟล์พร้อมกัน
  - [ ] ให้ Subagent สร้างและเขียนหน้าเพจ Concept/Entity ตาม Structured Folders (`wiki/entities/`, `wiki/concepts/`)
- **Phase 2B: Sequential Linking & Indexing (ทำเรียงลำดับโดย Agent หลัก)**
  - [ ] Agent หลักรับไม้ต่อ ตรวจสอบหน้าเพจที่ถูกสร้างใหม่ทั้งหมด
  - [ ] ค้นหาและสร้าง `[[Wikilinks]]` เพื่อทำ Cross-referencing ให้ความรู้เชื่อมโยงกันอย่างสมบูรณ์
  - [ ] อัปเดต `index.md` รวบยอดรอบเดียวจบ

## 🚦 State Management
- ให้ Agent หลักคอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดู

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Subagent)
1. **Micro-tasking:** Subagent ห้ามทำงานเกิน 1 ไฟล์ต่อ 1 Task (ยกเว้นขั้นตอน Linking ที่กวาดหาไฟล์)
2. **Strict Checkpoints:** ห้ามทำ Task ถัดไป หาก User ยังไม่ได้ตรวจสอบและพิมพ์คำว่า "อนุมัติ" ใน Task ปัจจุบัน
3. **Cross-Referencing Guarantee:** ทุกครั้งที่มีการดึงข้อมูลใหม่เข้า Wiki (Ingest) **บังคับ** จะต้องมีขั้นตอน Sequential Linking ในตอนท้ายเสมอ เพื่ออุดช่องโหว่ปัญหาความรู้ไม่เชื่อมโยงกัน
# Orchestration Plan: Ingest Claude Prompt Caching

## 🎯 Goal (เป้าหมายหลัก)
วิเคราะห์และนำเข้า (Ingest) ข้อมูลจาก Raw Source `Give Me 10 Mins and I'll Save You Millions of Claude Tokens.md` ลงใน Wiki อย่างเป็นระบบ เพื่อให้ได้ความรู้ที่จัดโครงสร้างแล้วในเรื่อง Prompt Caching, Token Optimization และ Cache Invalidation

## 🛠️ Phases (ลำดับการทำงาน)

### Phase 1: Core Concepts Ingestion
- [x] ให้ Agent อ่านเนื้อหา Raw Source ในส่วนที่เป็นกลไกของ Caching
- [x] ให้ Agent สร้างหรืออัปเดตหน้า Wiki สำหรับเรื่อง `Prompt Caching` (เช่น wiki/prompt_caching.md) โดยสรุปประเด็นต่อไปนี้:
  - Cache ทำงานอย่างไรและช่วยประหยัด Token ได้อย่างไร (ลด Cost เหลือ 10%)
  - Cache Layers ต่างๆ (System, Project, Conversation)
  - ความแตกต่างของ Cache TTL (1 ชั่วโมงสำหรับ Claude Code/Web vs 5 นาทีสำหรับ API/Subagents)
- **Checkpoint:** หยุดรอให้ User ตรวจสอบหน้า Wiki และพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase 2

### Phase 2: Techniques & Pitfalls Ingestion
- [x] ให้ Agent อัปเดตหน้าเทคนิคการใช้งาน (เช่น wiki/token_optimization.md) จากข้อมูลในคลิป
- [x] ใส่ประเด็น Best Practices (Habits) เพื่อรักษา Cache:
  - การใช้กระบวนการ Session Handoff
  - ไม่ควร Pause ทิ้งไว้นานกว่า TTL (Time-to-Live)
  - เริ่ม Session ใหม่เสมอเมื่อเปลี่ยน Task
- [x] ใส่ประเด็น Cache Invalidation (สิ่งที่ทำให้ Cache แตกและต้องเริ่มจำใหม่):
  - การเปลี่ยน Model ระหว่างทำงาน
  - การแก้ไข System prompt (แก้ไขกลางคันจะทำให้ต้อง Recache ใหม่ทั้งหมด)
- **Checkpoint:** หยุดรอให้ User ตรวจสอบหน้า Wiki และพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase 3

### Phase 3: Index & Audit Log Update
- [x] ให้ Agent อัปเดตไฟล์ `index.md` ว่า Raw Source ไฟล์นี้ถูก Ingest เข้าสู่ระบบแล้ว
- [x] เพิ่มรายชื่อหน้า Wiki ใหม่หรือหน้าที่ถูกปรับปรุง ลงในโครงสร้าง Index
- [x] บันทึกการกระทำ (Audit Trace) ทั้งหมดลงในไฟล์ `log.md` ตามรูปแบบที่ตกลงในระบบ
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและประกาศว่าการ Ingest สำเร็จสมบูรณ์

## 🚦 State Management
- ให้ Agent คอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดูทราบว่ากำลังอยู่ในขั้นตอนไหน

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Agent)
1. **Atomic Updates:** Agent ต้องโฟกัสการแก้ไข/สร้างไฟล์ Wiki ในแต่ละหัวข้อทีละกลุ่มเนื้อหา (ตาม Phase)
2. **Strict Checkpoints:** ห้ามทำ Task ใน Phase ถัดไป หาก User ยังไม่ได้ตรวจสอบผลงานและพิมพ์คำว่า "อนุมัติ" ใน Phase ปัจจุบัน
3. **Single Agent:** ดำเนินการทั้งหมดโดย Agent หลัก ไม่ต้อง Spawn Subagent เพิ่มเติม

# Orchestration Plan: Ingest Claude Subagents

## 🎯 Goal (เป้าหมายหลัก)
เพื่อ Ingest ข้อมูลเกี่ยวกับ "How to Build Claude Subagents Better Than 99% of People" เข้าสู่ Wiki อย่างเป็นระบบ โดยแบ่งเนื้อหาเป็นส่วนแนวคิดหลัก, การตั้งค่า, และ Use cases ขั้นสูง

## 🛠️ Phases (ลำดับการทำงาน)

### Phase 1: Core Concepts & Comparisons (แนวคิดหลักและการเปรียบเทียบ)
- [x] สร้าง/อัปเดต Wiki page สำหรับแนวคิดพื้นฐานของ Subagent (What is a Subagent)
- [x] สร้าง/อัปเดต Wiki page สำหรับเปรียบเทียบ Built-In vs Custom Agents
- [x] สร้าง/อัปเดต Wiki page สำหรับเปรียบเทียบ Skills vs Subagents
- [x] สร้าง/อัปเดต Wiki page สำหรับเปรียบเทียบ Project vs Global scope
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase 2

### Phase 2: Building & Configuration (การสร้างและการตั้งค่า)
- [x] สร้าง/อัปเดต Wiki page เกี่ยวกับ Descriptions & Progressive Disclosure
- [x] สร้าง/อัปเดต Wiki page เกี่ยวกับการกำหนดข้อจำกัด (Read-Only) และการประหยัดค่าใช้จ่าย
- [x] สร้าง/อัปเดต Wiki page เกี่ยวกับขั้นตอนการสร้าง Custom Subagent
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase 3

### Phase 3: Use Cases & Advanced Workflows (กรณีการใช้งานและเวิร์กโฟลว์ขั้นสูง)
- [x] สร้าง/อัปเดต Wiki page เกี่ยวกับการใช้ Subagents เป็นผู้เชี่ยวชาญเฉพาะทาง (Specialists)
- [x] สร้าง/อัปเดต Wiki page เกี่ยวกับเงื่อนไขว่าเมื่อใดควรใช้ Subagent (When to Use a Subagent)
- [x] สร้าง/อัปเดต Wiki page เกี่ยวกับ Dynamic Workflows
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase 4

### Phase 4: Index & Audit Log Update (อัปเดตดัชนีและบันทึก)
- [x] อัปเดต `index.md` โดยเพิ่มหัวข้อ/concepts ใหม่ และลิงก์ไปยังไฟล์ต้นฉบับ
- [x] เพิ่มบันทึกการทำงาน (Audit trace) ใน `logs/log.md`
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" เพื่อจบกระบวนการ Ingestion

## 🚦 State Management
- ให้ Agent หลักคอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดู

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Subagent)
1. **Micro-tasking:** Subagent ห้ามทำงานเกิน 1 ไฟล์ต่อ 1 Task 
2. **Strict Checkpoints:** ห้ามทำ Task ถัดไป หาก User ยังไม่ได้ตรวจสอบและพิมพ์คำว่า "อนุมัติ" ใน Task ปัจจุบัน

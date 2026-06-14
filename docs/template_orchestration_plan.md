# Orchestration Plan: [ชื่อโปรเจค]

## 🎯 Goal (เป้าหมายหลัก)
[เป้าหมายของการทำงานนี้]

## 🛠️ Phases (ลำดับการทำงาน)

### Phase 1: Topic 1 Research & Database Design
- [ ] ให้ Research Agent ไปศึกษาวิธีการต่อ API ของระบบ Payment
- [ ] ให้ Database Expert ร่าง Schema ลงใน `schema.sql`
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase 2

### Phase 2: Topic 2 Backend Implementation
- [ ] สร้าง Subagent ชื่อ `backend_dev` เพื่อเขียนโค้ดตาม Schema ที่ได้รับอนุมัติ
- [ ] รัน Unit Test ทั้งหมดให้ผ่าน

## 🚦 State Management
- ให้ Agent หลักคอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดู

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Subagent)
1. **Micro-tasking:** Subagent ห้ามทำงานเกิน 1 ไฟล์ต่อ 1 Task 
2. **Strict Checkpoints:** ห้ามทำ Task ถัดไป หาก User ยังไม่ได้ตรวจสอบและพิมพ์คำว่า "อนุมัติ" ใน Task ปัจจุบัน
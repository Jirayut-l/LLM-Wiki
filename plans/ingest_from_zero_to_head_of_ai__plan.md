# Orchestration Plan: Ingest From Zero to Head of AI in 1 Year

## 🎯 Goal (เป้าหมายหลัก)
Ingest the raw source "From Zero to Head of AI in 1 Year (as a regular person)" into the Wiki by extracting key concepts (Ailin's journey, Head of AI role, Building in Public, AI Adoption Strategy) and structural entities.

## 🛠️ Phases (ลำดับการทำงาน)

### Phase 1: Core Entities & Tools
- [x] สร้างไฟล์ Wiki สำหรับบุคคล `Ailin.md` (อธิบายประวัติจาก Email Developer สู่ Head of AI)
- [x] สร้างไฟล์ Wiki สำหรับบทบาท `Head_of_AI_Role.md` (อธิบายลักษณะงาน, การวางกลยุทธ์, และทักษะที่จำเป็น)
- [ ] สร้างไฟล์ Wiki สำหรับเครื่องมือ `n8n.md` (อธิบายในบริบทของ AI Automation สำหรับผู้เริ่มต้น)
- [ ] สร้างไฟล์ Wiki สำหรับเครื่องมือ `Claude_Code.md` (อธิบายในบริบทของการพัฒนา AI)
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase 2

### Phase 2: Techniques, Strategies & Main Note
- [ ] สร้างไฟล์ Wiki สำหรับเทคนิค `Building_in_Public.md` (การแสดงผลงาน, ทำวิดีโอเพื่อใช้สมัครงานแทน Resume)
- [ ] สร้างไฟล์ Wiki สำหรับกลยุทธ์ `AI_Adoption_Strategy.md` (การจัดการการเปลี่ยนแปลง, การทำให้พนักงานยอมรับ AI)
- [ ] สร้างไฟล์ Wiki สำหรับโน้ตหลักของวิดีโอ `From_Zero_to_Head_of_AI_in_1_Year.md` (สรุปเนื้อหาหลักและเชื่อมโยงไปยัง Entity ทั้งหมด)
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" ก่อนเริ่ม Phase 3

### Phase 3: Index & Audit Log Update
- [ ] อัปเดตไฟล์ `index.md` โดยเพิ่มลิงก์ไปยังไฟล์ที่สร้างใหม่ทั้งหมด
- [ ] อัปเดตไฟล์ `logs/log.md` โดยบันทึกประวัติการ Ingest ตามรูปแบบ Audit Trace
- **Checkpoint:** หยุดรอให้ User ตรวจสอบและพิมพ์ "อนุมัติ" เพื่อเสร็จสิ้นกระบวนการ

## 🚦 State Management
- ให้ Agent หลักคอยเข้ามาติ๊กเครื่องหมาย `[x]` ในไฟล์นี้เมื่อทำแต่ละข้อเสร็จ เพื่ออัปเดตสถานะให้คนดู

## ⚠️ Execution Rules (กฎการทำงานสำหรับ Subagent)
1. **Micro-tasking:** Subagent ห้ามทำงานเกิน 1 ไฟล์ต่อ 1 Task 
2. **Strict Checkpoints:** ห้ามทำ Task ถัดไป หาก User ยังไม่ได้ตรวจสอบและพิมพ์คำว่า "อนุมัติ" ใน Task ปัจจุบัน

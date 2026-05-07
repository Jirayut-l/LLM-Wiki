---
tags: [ai, prompting, library, developer, it]
---

# Role - Developer & IT Prompt Library 💻

รวมคลัง Prompt สำหรับนักพัฒนาซอฟต์แวร์, วิศวกรข้อมูล, และสายงานไอที เพื่อเพิ่มประสิทธิภาพในการเขียนโค้ดและจัดการระบบ

---

## 🛠️ Software Development & Engineering

### 1. การตรวจสอบและปรับปรุงโค้ด (Code Debugging & Optimization)
- **Prompt:** "คุณคือ Senior Full-stack Developer [Persona] ช่วยตรวจสอบฟังก์ชัน [ภาษา] นี้ [Context/Code] เพื่อหาจุดที่อาจเกิด Memory Leak และแนะนำวิธีเพิ่มประสิทธิภาพการทำงาน [Task] โดยส่งโค้ดที่ปรับปรุงแล้วพร้อมคอมเมนต์อธิบายรายละเอียดการเปลี่ยนแปลง [Format]"
- **Usage:** ใช้เมื่อต้องการ Refactor โค้ดหรือหาคอขวดของระบบ

### 2. การเขียนเอกสารประกอบโค้ด (Documentation)
- **Prompt:** "สวมบทบาทเป็น Technical Writer [Persona] ช่วยสร้างไฟล์ README ในรูปแบบ Markdown [Format] เพื่ออธิบายตรรกะและการใช้งานของ API Endpoints [Task] ที่ระบุอยู่ในไฟล์ [Context/Source] โดยใช้ภาษาระดับมืออาชีพและเข้าใจง่าย [Format]"
- **Usage:** ใช้สร้างเอกสารประกอบโปรเจกต์อัตโนมัติ

### 3. การสรุปรายงานเชิงเทคนิค (Technical Summary)
- **Prompt:** "สวมบทบาทเป็นนักวิจัยอาวุโส [Persona] ช่วยสรุปรายงานเชิงเทคนิคฉบับนี้ @[ชื่อไฟล์] [Context] ให้คนทั่วไปเข้าใจง่าย [Format] โดยเน้นที่ความเสี่ยงหลักด้านความปลอดภัยและวิธีแก้ไข [Task]"
- **Usage:** ย่อยข้อมูลยากๆ ให้ทีมบริหารหรือลูกค้าเข้าใจง่าย

### 4. การสร้าง Unit Test (Test Generation)
- **Prompt:** "คุณคือ QA Automation Engineer [Persona] จงสร้าง Unit Test สำหรับฟังก์ชันนี้ [Context] โดยใช้ Framework [ชื่อ Framework] [Task] ครอบคลุมทั้งกรณีปกติ (Happy Path) และ Edge Cases [Format]"
- **Usage:** เพิ่มความครอบคลุมของการทดสอบ (Test Coverage)

---

## 🏗️ Data & Systems

### 4. การวิเคราะห์ Log และหาสาเหตุของปัญหา (Root Cause Analysis)
- **Prompt:** "ในฐานะ SRE Engineer [Persona] ช่วยวิเคราะห์ Log เหล่านี้ [Context] เพื่อหาสาเหตุว่าทำไม Service ถึงล่มในช่วงเวลา [ระบุเวลา] [Task] และสรุปแนวทางการแก้ไขเป็นลำดับขั้นตอน [Format]"
- **Usage:** ช่วยแก้ปัญหาในระบบ Production ได้รวดเร็วขึ้น

### 5. การแปลง SQL และ Query Optimization
- **Prompt:** "คุณคือ Database Administrator [Persona] ช่วยปรับปรุง Query SQL นี้ [Context] ที่ทำงานช้าบนฐานข้อมูล [ระบุประเภท] ให้ทำงานเร็วขึ้น [Task] พร้อมอธิบายว่าทำไมถึงปรับเปลี่ยนเช่นนั้น [Format]"
- **Usage:** ปรับปรุงประสิทธิภาพของฐานข้อมูล

---
**แหล่งอ้างอิง:** [[Summary - Gemini for Google Workspace Prompting Guide 101_Full]] และ [[Concept - LLM Configuration & Developer Guide]]

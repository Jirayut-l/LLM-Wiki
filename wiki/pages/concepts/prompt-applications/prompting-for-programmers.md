---
title: การเขียนพรอมต์สำหรับโปรแกรมเมอร์ (Prompting for Programmers)
tags:
  - concept
  - use-case
  - programming
source: "wiki/pages/concepts/prompting-for-programmers.md"
date: 2026-05-15
---

# การเขียนพรอมต์สำหรับโปรแกรมเมอร์

การใช้ AI เป็นผู้ช่วยในการเขียนโค้ด (Copilot) ช่วยเพิ่มประสิทธิภาพและลดเวลาในการทำงานที่ซ้ำซ้อน

## 🛠️ กรณีใช้งานหลัก

### 1. การสร้างโค้ด (Code Generation)
ระบุภาษา เวอร์ชัน และเฟรมเวิร์กที่ชัดเจน
> [!example] ตัวอย่างพรอมต์
> "เขียนฟังก์ชัน Python สำหรับตรวจสอบความถูกต้องของอีเมล โดยใช้ Regular Expression และต้องรองรับมาตรฐาน RFC 5322"

### 2. การค้นหาและแก้ไขบัค (Debugging)
ส่งโค้ดที่มีปัญหาและข้อความ Error ให้ AI วิเคราะห์
> [!example] ตัวอย่างพรอมต์
> "โค้ด JavaScript ต่อไปนี้ทำงานผิดพลาด [วางโค้ด] และแสดง Error: 'TypeError: Cannot read property of undefined' ช่วยวิเคราะห์สาเหตุและเสนอวิธีแก้ไข"

### 3. การอธิบายโค้ด (Code Explanation)
เหมาะสำหรับศึกษาโค้ดที่ซับซ้อนหรือโค้ดของผู้อื่น
> [!example] ตัวอย่างพรอมต์
> "ช่วยอธิบายการทำงานของอัลกอริทึมนี้ทีละขั้นตอนในภาษาที่เข้าใจง่าย: [วางโค้ด]"

### 4. การปรับปรุงโค้ด (Refactoring)
ขอให้ AI ช่วยทำให้โค้ดสะอาดขึ้นหรือมีประสิทธิภาพมากขึ้น
> [!example] ตัวอย่างพรอมต์
> "ช่วยปรับปรุงโค้ด PHP นี้ให้เป็นไปตามหลัก Clean Code และลดความซับซ้อนของโครงสร้าง If-Else: [วางโค้ด]"

---
> [!tip] เคล็ดลับสำหรับโปรแกรมเมอร์
> ระบุสภาพแวดล้อมการทำงานเสมอ เช่น "ใช้ React 18 ร่วมกับ TypeScript" เพื่อให้ได้โค้ดที่พร้อมใช้งานจริง

## 🇬🇧 English Prompt Examples

### 1. Unit Test Generation (TDD/BDD)
> [!example] Prompt Example
> "Generate comprehensive unit tests for the following React component using Jest and React Testing Library. Include edge cases for missing props and simulate user click events."

### 2. Code Review & Security Audit
> [!example] Prompt Example
> "Perform a thorough code review of this Python script. Focus on identifying potential security vulnerabilities (like SQL injection or XSS), performance bottlenecks, and adherence to PEP 8 standards."

### 3. Database & SQL Optimization
> [!example] Prompt Example
> "Optimize this PostgreSQL query to reduce execution time. Explain the changes made and suggest any indexes that should be created on the `users` and `orders` tables to support this query."

### 4. API Documentation (JSDoc/Docstrings)
> [!example] Prompt Example
> "Generate detailed JSDoc comments for this TypeScript service class. Ensure all parameters, return types, and potential thrown errors are documented."

### 5. Modernization & Refactoring
> [!example] Prompt Example
> "Refactor this legacy Java code to use modern Java 21 features, such as Pattern Matching and Records. Improve modularity and ensure it follows SOLID principles."

---
[[prompt-engineering-v7-summary|กลับสู่สรุปเทคนิค]] | [[index|กลับสู่สารบัญ]]

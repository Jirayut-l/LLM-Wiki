---
type: concept
aliases: [Progressive Disclosure, Subagent Descriptions]
tags: [claude, subagents, configuration]
created: 2026-06-14
---
# Progressive Disclosure in Claude Code

## Summary
Progressive Disclosure คือกลไกอัจฉริยะใน Claude Code ที่ช่วยประหยัด Token และเพิ่มความแม่นยำในการเรียกใช้งาน Subagents หรือ Skills โดยระบบจะอ่านเฉพาะส่วนหัวของไฟล์ก่อน (YAML front matter) เพื่อตัดสินใจว่าควรเรียกใช้งานเครื่องมือนั้นหรือไม่

## Core Content
- **การทำงานของ Progressive Disclosure:**
  - เมื่อผู้ใช้พิมพ์คำสั่ง Claude Code จะสแกนค้นหา Subagents/Skills โดยอ่านเฉพาะ `name` และ `description` ในส่วน YAML front matter เท่านั้น
  - ถ้าระบบพิจารณาแล้วว่างานที่ได้รับมอบหมายตรงกับคำอธิบาย (description) มันถึงจะโหลดเนื้อหาทั้งหมด (body) เข้ามาทำงาน ช่วยให้ไม่เปลือง Token ไปกับการอ่านคำสั่งเต็มของ agent ทุกตัวที่มีในระบบ

- **ความสำคัญของ Descriptions (คำอธิบาย):**
  - เป็นเหมือน "Trigger" (ตัวจุดชนวน) ดังนั้นคำอธิบายจะต้องมีความแม่นยำและเฉพาะเจาะจง (Precise)
  - **Misfires:** หากคำอธิบายไม่ดีพอ อาจเกิดปัญหา Misfire คือระบบเรียก agent ผิดตัว หรือไม่ยอมเรียก agent ที่ควรเรียก ซึ่งแก้ไขได้ด้วยการทดลองใช้งานและปรับแก้ Description ใหม่ให้รัดกุมขึ้น
  - หากสร้างผ่าน Claude Code คำอธิบายที่ได้มักจะยาวเกินไป แนะนำให้ลบและตัดทอนให้กระชับ เพื่อประสิทธิภาพสูงสุด

## Related
- [[Claude Subagent]]
- [[Built-In vs Custom Agents]]
- [[Creating Custom Subagents]]

## Sources
- [[How to Build Claude Subagents Better Than 99% of People]]

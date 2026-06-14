---
type: concept
aliases: [Built-In Agents, Custom Agents]
tags: [claude, subagents]
created: 2026-06-14
---
# Built-In vs Custom Agents

## Summary
ในการใช้งาน Claude Code มี Subagent ให้เลือกใช้ 2 รูปแบบหลัก คือ Built-In Agents ที่มีมาให้ในระบบโดยปริยาย และ Custom Agents ที่ผู้ใช้งานสร้างขึ้นมาเองผ่านไฟล์ Markdown เพื่อทำงานเฉพาะทางตามความต้องการของตนเอง

## Core Content
- **Built-In Agents:** 
  - เป็น Subagent พื้นฐานที่มาพร้อมกับ Claude Code เช่น "General Purpose" หรือ built-in research agent
  - ตัว Claude Code สามารถเรียกใช้งานได้อย่างอัตโนมัติ (invoke automatically) เมื่อมันพิจารณาแล้วว่ามีงานที่เหมาะสม
  - ไม่ได้ถูกกำหนดหรือสร้างโดยผู้ใช้ แต่เป็น agent อเนกประสงค์ที่มี prompt เฉพาะที่ถูกเขียนมาแล้วจากตัวระบบ
  
- **Custom Agents:**
  - สร้างขึ้นโดยผู้ใช้งานเองผ่านไฟล์ Markdown (`.md`) โดยปกติจะบันทึกอยู่ในโฟลเดอร์ `.claude/agents` ภายในโปรเจค
  - ภายในไฟล์ `.md` จะมี YAML front matter ซึ่งเป็นข้อมูลที่อธิบายตัว agent เช่น ชื่อ (name), คำอธิบาย (description), โมเดลที่ใช้ (model), สีที่แสดง (color), และสิทธิ์ในการใช้เครื่องมือ (tools)
  - ทั้ง Built-In และ Custom Agents ต่างอาศัยกลไกที่เรียกว่า "Progressive Disclosure" ในการทำงาน ซึ่งหมายความว่า Claude Code จะอ่านแค่ส่วนหน้า (YAML front matter) ก่อน เพื่อพิจารณาว่า agent ตัวนี้เหมาะสมกับคำสั่งของผู้ใช้หรือไม่ โดยไม่ต้องอ่านเนื้อหาทั้งหมดหากยังไม่ถูกเรียกใช้จริงเพื่อประหยัดจำนวน Token

## Related
- [[Claude Subagent]]
- [[Project vs Global Scope]]

## Sources
- [[How to Build Claude Subagents Better Than 99% of People]]

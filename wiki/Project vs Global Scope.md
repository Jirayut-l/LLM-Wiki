---
type: concept
aliases: [Project vs Global Scope, Project Level vs Global Level]
tags: [claude, subagents, configuration]
created: 2026-06-14
---
# Project vs Global Scope

## Summary
[[Claude Subagent|Subagents]] และ [[Skills vs Subagents|Skills]] ใน Claude Code สามารถกำหนดขอบเขต (Scope) ในการใช้งานได้ 2 ระดับ คือระดับโปรเจค (Project Level) และระดับระบบ (Global Level) ซึ่งเป็นตัวกำหนดว่าจะสามารถเรียกใช้งาน agent/skill นั้นจากที่ไหนได้บ้าง 

## Core Content
- **Project Level (ระดับโปรเจค):**
  - ไฟล์ Markdown ของ Agent หรือ Skill จะถูกบันทึกไว้ในโฟลเดอร์ `.claude` ภายใน Repository ปัจจุบัน (เช่น `.claude/agents` หรือ `.claude/skills`)
  - สามารถใช้งานได้เฉพาะเวลาที่ทำงานอยู่ภายในโปรเจคนั้นๆ
  - ข้อดีคือ เมื่อคุณแชร์หรือส่งต่อ Repository (เช่น ทาง GitHub) ผู้ร่วมงานหรือคนที่ดาวน์โหลดโปรเจคไปจะได้ Subagents หรือ Skills เหล่านั้นติดตัวไปด้วย

- **Global Level (ระดับระบบ):**
  - ไฟล์ Markdown จะถูกเก็บไว้ในระดับ User บนเครื่อง (Global directory)
  - สามารถเรียกใช้งาน Subagent หรือ Skill นั้นจากโฟลเดอร์หรือโปรเจคใดก็ได้ในเครื่อง
  - ไม่ได้ถูกแชร์ไปพร้อมกับ Repository ทำให้เหมาะสำหรับเครื่องมือหรือความสามารถเฉพาะตัวที่ผู้ใช้ตั้งใจพกติดตัวไปใช้งานส่วนบุคคล

- **การย้าย Scope:**
  - เนื่องจากทั้ง Subagents และ Skills เป็นแค่ไฟล์ Markdown ทั่วไป จึงสามารถลากย้าย (Move) หรือคัดลอกระหว่างระดับ Project และ Global ได้อย่างอิสระตามความต้องการ

## Related
- [[Built-In vs Custom Agents]]
- [[Claude Subagent]]

## Sources
- [[How to Build Claude Subagents Better Than 99% of People]]

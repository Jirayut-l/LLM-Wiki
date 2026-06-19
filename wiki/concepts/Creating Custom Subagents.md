---
type: concept
aliases: [Creating Custom Subagents]
tags: [claude, subagents, tutorial]
created: 2026-06-14
---
# Creating Custom Subagents

## Summary
ในการสร้าง Custom Subagent ใน Claude Code ผู้ใช้งานสามารถสร้างไฟล์ด้วยตนเอง (Manual Configuration) หรือใช้ AI ตัวช่วย (Generate with Claude) เพื่อให้กระบวนการสร้างและเขียน YAML front matter เป็นไปอย่างสะดวกและรวดเร็ว

## Core Content
- **การสร้างด้วย AI (Generate with Claude):**
  - สามารถพิมพ์คำสั่ง `/agents` (หรือเรียกผ่าน UI/Command palette)
  - เลือกระดับ Scope ของ Agent ([[Project vs Global Scope|Project หรือ Global]])
  - เลือก **Generate with Claude** จากนั้นให้อธิบาย (Prompt) สิ่งที่คุณต้องการให้ Subagent นี้ทำ ตัวอย่างเช่น "สร้าง Subagent ที่คอยวิจารณ์งานของฉันแบบตรงไปตรงมา" (Plan Roaster)
  - ระบุ Tool ที่อนุญาต (เช่น Read-only), เลือกรุ่นของโมเดล (Model), สีที่ใช้แสดง, และระดับความจำ (Memory เช่น Project Scope หรือ None)

- **การปรับแต่งไฟล์หลังสร้างเสร็จ:**
  - Claude จะสร้างไฟล์ `.md` ให้อัตโนมัติ (เช่น `plan_roaster.md`)
  - **ข้อควรระวัง:** ไฟล์ที่ Claude สร้างให้มักจะมี Description ในส่วนของ YAML ที่ยาวเกินไป ซึ่งส่งผลต่อระบบ [[Progressive Disclosure in Claude Code|Progressive Disclosure]] แนะนำให้คุณเข้าไปปรับแก้ (Trim down) Description ให้สั้นและกระชับ เป็นเพียงประโยคสั้นๆ ว่า "ควรเรียกใช้ Agent นี้เมื่อใด" เพื่อให้การทำงานมีประสิทธิภาพที่สุด
  - หมั่นทดลองเรียกใช้งานและอัปเดต Prompt หรือ Description อยู่เสมอเพื่อให้ Agent ตอบสนองได้อย่างแม่นยำ

## Related
- [[Built-In vs Custom Agents]]
- [[Project vs Global Scope]]
- [[Progressive Disclosure in Claude Code]]
- [[Claude Subagent]]

## Sources
- [[How to Build Claude Subagents Better Than 99% of People]]

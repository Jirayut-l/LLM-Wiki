---
type: concept
aliases: [Subagent, Claude Subagent]
tags: [claude, subagents, ai]
created: 2026-06-14
---
# Claude Subagent

## Summary
Subagent คือเครื่องมือ (feature) ที่ทรงพลังใน Claude Code ซึ่งช่วยให้ Main Session (ที่เป็นเหมือน orchestrator หรือผู้ควบคุมหลัก) สามารถมอบหมายงานให้ agent ย่อย (subagents) แยกไปทำงานแบบคู่ขนาน หรือทำงานเฉพาะทางได้ Subagent แต่ละตัวสามารถกำหนด Model ที่ใช้, Persona (บทบาทบุคลิกภาพ), และ [[Skills vs Subagents|Skills (ทักษะ)]] ที่แตกต่างกันออกไปได้

## Core Content
- **การจัดการ Context:** ข้อดีหลักของ Subagent คือการรักษา Context ของ Main Session ให้สะอาด (Clean Context) เมื่อมีการให้ AI ทำการ Research ที่ต้องอ่านไฟล์จำนวนมากหรือประมวลผลข้อความยาวๆ การส่งต่อให้ Subagent ทำงานจะทำให้ Context ของการสนทนาหลักไม่ถูกรบกวนด้วยข้อมูลขยะ
- **การประหยัดค่าใช้จ่าย:** เราสามารถกำหนดให้ Subagent ใช้ Model ที่มีราคาถูกกว่า (เช่น Claude 3.5 Haiku หรือ Sonnet) เพื่อไปทำงานที่ไม่ได้มีความซับซ้อนมาก เช่น การอ่านสรุป Research Report แทนที่จะใช้ Opus model ซึ่งมีราคาแพงกว่า ทำให้มีประสิทธิภาพสูงขึ้นในต้นทุนที่ต่ำลง
- **Specialists:** สามารถสร้าง Subagent เป็นผู้เชี่ยวชาญในเฉพาะทาง ([[Subagents as Specialists|Specialists]]) เช่น Security Auditor, Database Expert หรือ Researcher เพื่อเรียกใช้เมื่อมีงานที่สอดคล้องกับความเชี่ยวชาญนั้นๆ

## Related
- [[Built-In vs Custom Agents]]
- [[Skills vs Subagents]]
- [[Dynamic Workflows]]
- [[When to Use a Subagent]]
- [[Subagents as Specialists]]
- [[Creating Custom Subagents]]

## Sources
- [[How to Build Claude Subagents Better Than 99% of People]]

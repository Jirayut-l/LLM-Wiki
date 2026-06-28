---
type: concept
aliases: [Progressive Disclosure]
tags: [concept]
created: 2026-06-22
sources: ["[[how_to_build_claude_subagents|How to Build Claude Subagents Better Than 99% of People]]"]
title: "Progressive Disclosure"
complexity: intermediate
domain: "AI Engineering"
updated: 2026-06-28
status: developing
related: ["[[claude_code|Claude Code]]", "[[subagent|Subagent]]", "[[orchestration|Orchestration]]"]
---
# Progressive Disclosure

## Definition
Progressive Disclosure ในบริบทของ Claude Code คือกลไกที่ระบบจะอ่านข้อมูลเพียงบางส่วน (เช่น YAML front matter ที่ประกอบด้วยชื่อและคำอธิบาย) เพื่อประเมินความเกี่ยวข้องกับคำสั่งของผู้ใช้เบื้องต้น และจะดึงรายละเอียดหรือคำสั่งทั้งหมด (Body) มาใช้งานก็ต่อเมื่อพิจารณาแล้วว่าจำเป็นต้องเรียกใช้งาน (Invoke) เครื่องมือหรือ [[subagent|Subagent]] นั้นๆ จริงๆ

## How It Works
กลไกนี้ถูกออกแบบมาเพื่อเพิ่มประสิทธิภาพและประหยัดทรัพยากร (Tokens) ในการประมวลผล:
- **Front Matter as Triggers:** คำอธิบาย (`description`) ใน YAML front matter ของไฟล์ Subagent หรือ Skill ทำหน้าที่เป็นตัวกระตุ้น (Trigger) ให้โมเดลหลัก (Orchestrator) ทราบว่าเครื่องมือนี้มีหน้าที่อะไรและควรใช้เมื่อใด
- **Resource Efficiency:** โมเดลไม่จำเป็นต้องอ่านคำสั่งและ Context ทั้งหมดของทุก Agent ที่มีอยู่ในระบบ ทำให้ประหยัดค่าใช้จ่ายและไม่ทำให้ Context Window ของแชทหลักเต็มไปด้วยข้อมูลที่ไม่เกี่ยวข้อง
- **Precision in Descriptions:** การเขียนคำอธิบายที่แม่นยำและชัดเจนเป็นหัวใจสำคัญในการทำงานของกลไกนี้ หากอธิบายได้ไม่ดีอาจเกิดปัญหา Misfire (โมเดลเรียกใช้งานเมื่อไม่ต้องการ หรือไม่เรียกเมื่อต้องการ)

## Connections
- [[claude_code|Claude Code]]
- [[subagent|Subagent]]
- [[orchestration|Orchestration]]

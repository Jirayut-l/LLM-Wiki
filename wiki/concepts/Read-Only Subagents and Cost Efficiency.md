---
type: concept
aliases: [Read-Only Subagents, Subagent Cost Efficiency]
tags: [claude, subagents, cost-saving, security]
created: 2026-06-14
---
# Read-Only Subagents and Cost Efficiency

## Summary
การใช้งาน [[Claude Subagent|Subagents]] ไม่ได้มีดีแค่ความสามารถในการทำคู่ขนาน แต่ยังเป็นกุญแจสำคัญในการลดต้นทุน (Cost Efficiency) และการรักษาความปลอดภัยของข้อมูลด้วยการกำหนดสิทธิ์แบบอ่านอย่างเดียว (Read-Only)

## Core Content
- **Cost Efficiency (การประหยัดต้นทุน):**
  - **Smart Boss & Cheap Workers:** เราสามารถใช้โมเดลราคาแพง (เช่น Opus) เป็น Main Session (Boss) สำหรับการสนทนาทั่วไปและควบคุมงาน แล้วกระจายงานที่ต้องใช้ Token สูงๆ แต่ใช้ตรรกะต่ำกว่า (เช่น อ่านรายงาน 300 หน้าเพื่อหาสรุป) ไปยัง Subagent ที่ตั้งค่าเป็นโมเดลราคาถูก (เช่น Haiku หรือ Sonnet)
  - วิธีนี้จะช่วยลดค่าใช้จ่ายในการทำ Research หรืออ่านไฟล์จำนวนมหาศาลได้อย่างมหาศาล
  - **Max Turns:** สามารถจำกัดจำนวนรอบการทำงานของ Subagent ได้ (เช่น `maxTurns: 10`) เพื่อป้องกันการทำงานวนลูปแบบไม่รู้จบและป้องกันการสูญเสียเครดิตโดยใช่เหตุ

- **Read-Only Restrictions (ความปลอดภัยเชิงสิทธิ์):**
  - คุณไม่ควรใช้แค่การ Prompt สั่งว่า "ห้ามอ่านข้อมูลเหล่านั้น" แต่ควรใช้กลไกการจำกัดสิทธิ์ (Tool Restrictions)
  - ใน YAML front matter คุณสามารถตั้งค่าอนุญาตเฉพาะเครื่องมือ `read-only` (เช่น ไม่ให้ใช้เครื่องมือแก้ไขไฟล์ หรือรันคำสั่ง bash ที่กระทบระบบ)
  - เหมาะสำหรับ Subagent ที่ทำหน้าที่พิจารณาความปลอดภัย (Security Auditor) ตรวจสอบไฟล์จากที่อื่น โดยให้แน่ใจว่ามันจะไม่มีสิทธิ์เข้าไปยุ่งหรือขโมยข้อมูลใดๆ ในระบบ

**ตัวอย่าง YAML Front Matter สำหรับ Read-Only และ Cost-Saving:**
```yaml
---
name: read_only_researcher
description: ใช้สำหรับอ่านสรุปเนื้อหาจากไฟล์ข้อความยาวๆ อย่างปลอดภัย
model: claude-3-5-haiku-20241022 # ใช้โมเดลราคาประหยัด
maxTurns: 10                   # ป้องกันการวนลูปเกิน 10 รอบ
tools:
  - LS                         # อนุญาตให้ดูรายการไฟล์
  - View                       # อนุญาตให้ดูเนื้อหาไฟล์
disallowedTools:
  - RunCommand                 # ไม่อนุญาตให้รันคำสั่งใดๆ
  - Replace                    # ไม่อนุญาตให้แก้ไขไฟล์
  - Write                      # ไม่อนุญาตให้เขียนไฟล์ใหม่
---
```

## Related
- [[Claude Subagent]]
- [[Creating Custom Subagents]]
- [[Subagents as Specialists]]

## Sources
- [[How to Build Claude Subagents Better Than 99% of People]]

---
type: concept
title: "The Grill Session"
complexity: intermediate
domain: "AI Engineering"
aliases: [Grill Me, Phase 2: The Grill Session]
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
status: seed
related:
  - "[[writing_the_prd|Phase 3: Writing the PRD]]"
  - "[[human_in_the_loop_review|Human-in-the-Loop]]"
  - "[[afk_tasks|AFK Tasks]]"
  - "[[specs_to_code|Specs to Code]]"
sources:
  - "[[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]"
---

# The Grill Session

## Definition
The Grill Session (หรือ Grill Me) คือขั้นตอนในกระบวนการพัฒนาซอฟต์แวร์ด้วย AI ที่ผู้พัฒนาให้ AI ทำการสัมภาษณ์หรือตั้งคำถามเจาะลึก (Relentless Interview) เกี่ยวกับแผนงานหรือบรีฟที่ได้รับอย่างละเอียด เพื่อสร้างความเข้าใจที่ตรงกัน (Shared Understanding หรือ Design Concept) ระหว่างมนุษย์และ AI ก่อนที่จะเริ่มเขียนโค้ดหรือจัดทำเอกสารข้อกำหนด (PRD)

## How It Works
- **Initiation**: ผู้พัฒนาป้อนข้อมูลเริ่มต้น (เช่น ข้อความบรีฟจากลูกค้า) และเรียกใช้คำสั่ง (เช่น `/grill-me`) เพื่อให้ AI เริ่มต้นการสัมภาษณ์
- **Relentless Interviewing**: แทนที่ AI จะพยายามสร้างแผนงานออกมาทั้งหมดทันที AI จะค่อยๆ ตั้งคำถามทีละข้อเพื่อเจาะลึกประเด็นต่างๆ ตาม Decision Tree เพื่อแก้ไขความคลุมเครือ 
- **Interactive Alignment**: เป็นกระบวนการแบบ Human-in-the-Loop ที่ผู้พัฒนาจะต้องคอยตอบคำถาม ตัดสินใจ หรือยอมรับคำแนะนำจาก AI
- **Asset Creation**: ประวัติการสนทนาทั้งหมดที่ได้ข้อสรุปแล้ว จะกลายเป็นสินทรัพย์ (Asset) ซึ่งเปรียบเสมือน Design Concept ที่แข็งแกร่ง สำหรับนำไปให้ AI สรุปเป็น Product Requirements Document (PRD) ในเฟสถัดไป

## Why It Matters
- **ป้องกันความเข้าใจคลาดเคลื่อน (Prevent Misalignments)**: แก้ปัญหาของแนวทางการทำ "Specs to Code" ที่คนมักจะแก้ไขแต่สเปกและละเลยตัวโค้ด การถูกตั้งคำถามจะช่วยดึงผู้พัฒนากลับมาใส่ใจรายละเอียดและข้อจำกัดของระบบจริง
- **รักษาอำนาจควบคุม (Maintain Control)**: ทำให้ผู้พัฒนายังคงเป็นผู้ควบคุมทิศทางของโค้ดเบส (Code is your battleground) 
- **ช่วยรักษาบริบทให้อยู่ใน Smart Zone**: การสกัดเอารายละเอียดที่คลุมเครือให้ชัดเจนก่อน ช่วยป้องกันไม่ให้ AI สร้างแผนที่ผิดพลาดจนเสีย Context และหลุดเข้าสู่ Dumb Zone

## Examples
- การได้รับข้อความผ่าน Slack จากลูกค้าว่า "ต้องการเพิ่มระบบ Gamification" ผู้พัฒนาจะส่งข้อความนี้ให้ AI แล้ว AI จะค่อยๆ ถามเพื่อเจาะลึก เช่น "คะแนนจะได้จาก Action ไหนบ้าง?", "ระบบแต้มควรมีผลย้อนหลัง (Retroactive) กับข้อมูลในอดีตด้วยหรือไม่?" จนกระทั่งได้ข้อสรุปที่ครบถ้วนทุกประเด็นโดยไม่ตกหล่น

## Connections
- [[writing_the_prd|Phase 3: Writing the PRD]]
- [[human_in_the_loop_review|Human-in-the-Loop]]
- [[afk_tasks|AFK Tasks]]
- [[specs_to_code|Specs to Code]]

## Sources
- [[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]

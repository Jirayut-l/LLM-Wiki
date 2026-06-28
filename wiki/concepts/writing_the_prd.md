---
type: concept
title: "Phase 3: Writing the PRD"
complexity: intermediate
domain: "AI Coding Workflow"
aliases: ["Writing the PRD", "PRD Generation", "Destination Document"]
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
  - workflow
  - planning
status: seed
related: ["Phase 2: The Grill Session", "Phase 4: Slicing Work into Issues"]
sources: ["[[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]"]
---

# Phase 3: Writing the PRD

## Definition
Phase 3 เป็นขั้นตอนของการสร้างเอกสาร Product Requirements Document (PRD) ซึ่งเปรียบเสมือน "เอกสารระบุปลายทาง" (Destination Document) โดยทำหน้าที่สรุปความเข้าใจและแนวคิดการออกแบบที่ตรงกัน (Shared Design Concept) ที่ได้จากการทำ Grilling Session ใน Phase 2 ให้อยู่ในรูปแบบของเอกสารที่ชัดเจน

## How It Works
- หลังจากผ่านการตั้งคำถาม (Grill) และหาข้อสรุปอย่างละเอียดร่วมกับ AI แล้ว เราจะใช้คำสั่งหรือ Skill เพื่อให้ AI สรุปเนื้อหาทั้งหมดออกมาเป็น PRD
- โครงสร้างของ PRD มักประกอบด้วย:
  - Problem Statements (ปัญหาของผู้ใช้)
  - Solution (วิธีการแก้ปัญหา)
  - User Stories (เรื่องราวหรือพฤติกรรมการใช้งานของผู้ใช้)
  - Implementation Decisions (การตัดสินใจเชิงเทคนิค)
  - Testing Decisions (แนวทางการทดสอบ)
- กฎที่สำคัญในขั้นตอนนี้จาก Matt Pocock คือ **เมื่อ AI เขียน PRD เสร็จแล้ว ไม่จำเป็นต้องเสียเวลาอ่านทบทวน** เพราะ LLM เก่งเรื่องการสรุปเนื้อหาอยู่แล้ว และเนื่องจากเราได้มี Shared Design Concept ตั้งแต่ใน Phase 2 แล้ว การมานั่งอ่าน PRD จึงเป็นแค่การตรวจสอบความสามารถในการสรุปของ AI ซึ่งเสียเวลาโดยใช่เหตุ

## Why It Matters
การสร้าง PRD เป็นการจับภาพรวมและเป้าหมายทั้งหมดที่ได้จากการวางแผน (Alignment Phase) ให้อยู่ในรูปแบบที่เป็นรูปธรรม เป็นการเปลี่ยนบทสนทนาที่มีคุณค่า (เช่น การคุยกว่า 25k tokens) ให้เป็นสินทรัพย์ (Asset) ที่สามารถนำไปใช้เป็นข้อมูลอ้างอิงสำหรับการทำงานในเฟสต่อไปได้

## Examples
- การเปลี่ยนบริบทที่ได้จาก Grill Me Skill ให้เป็น PRD และบันทึกลงในโฟลเดอร์ issues เพื่อใช้เตรียมการเขียนโค้ดต่อไป

## Connections
- [[the_grill_session|Phase 2: The Grill Session]]
- [[slicing_work_into_issues|Phase 4: Slicing Work into Issues]]

## Sources
- [[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]] (Timestamp: 00:22:10 - 00:35:50)

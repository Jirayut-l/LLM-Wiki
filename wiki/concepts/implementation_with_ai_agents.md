---
type: concept
title: "Phase 5: Implementation with AI Agents"
complexity: intermediate
domain: "AI Engineering"
aliases: ["Implementation with AI Agents", "AFK Agents", "Night Shift", "Ralph loop"]
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
status: seed
related: []
sources: ["Full Walkthrough Workflow for AI Coding — Matt Pocock"]
---

# Phase 5: Implementation with AI Agents

## Definition
Phase 5 คือขั้นตอนการลงมือเขียนโค้ดโดยใช้ AI Agents ทำงานแบบอัตโนมัติ (AFK - Away From Keyboard) ซึ่งเป็นการทำงานต่อเนื่องจากแผนงานและ Issue ที่เตรียมไว้ในขั้นตอนก่อนหน้า ขั้นตอนนี้เปรียบเสมือน "กะกลางคืน" (Night shift) ที่ปล่อยให้ AI ทำงานสานต่อจากการวางแผนของมนุษย์ใน "กะกลางวัน" (Day shift) โดยมนุษย์สามารถออกจากกระบวนการ (Leave the loop) ชั่วคราวได้

## How It Works
- **การเตรียมพร้อม (Preparation):** แผนงานจะถูกแบ่งเป็น Issue ย่อยๆ บน Kanban board ที่มีความสัมพันธ์เชิงลำดับ (Directed Acyclic Graph - DAG) ทำให้สามารถทำหลายงานพร้อมกันได้ (Parallelization) ถ้าไม่มี Dependencies ต่อกัน
- **กลไกการทำงาน (Execution):** 
  - ข้อมูล Issue จากไฟล์ Local Markdown จะถูกรวบรวม (เช่น ผ่าน script) และส่งเข้าสู่ Context ของ LLM
  - Agent จะมีตรรกะในการเลือกงานถัดไปตามลำดับความสำคัญ (เช่น Critical bugs > Infrastructure > Tracer bullets > Polish/Refactors)
  - Agent สำรวจ Repository ทำการเขียนโค้ด และใช้หลักการ Test-Driven Development (TDD)
- **การทดสอบและปรับแต่ง (Tuning):** มักจะมีการรันลูปทำงานเพียงหนึ่งรอบ (เช่น ผ่าน `once.sh`) เพื่อสังเกตพฤติกรรมของ Agent และนำมาใช้ปรับแต่ง Prompt ก่อนที่จะปล่อยให้ทำงานแบบอัตโนมัติเต็มรูปแบบ (AFK loop) ใน Sandbox เช่น Docker

## Why It Matters
ขั้นตอนนี้เปลี่ยนบทบาทของนักพัฒนาจากการเป็นผู้ลงมือเขียนโค้ด (Coder) ไปเป็นผู้วางแผนและผู้ตรวจสอบทบทวนโค้ด (Code Reviewer/QA) แทน ทำให้สามารถขยายสเกลการทำงานด้วยการสั่งให้ AI Agents หลายตัวทำงานขนานกันได้ ช่วยลดระยะเวลาในการพัฒนาลงอย่างมาก

## Examples
- การใช้ Bash script ดึงข้อมูล Issue ใน Local เพื่อให้ Agent นำไปวิเคราะห์และเขียนโค้ดทีละ Issue
- การรัน "Ralph loop" ให้ AI Agent ทยอยเคลียร์ Kanban board ไปเรื่อยๆ โดยที่มนุษย์ไม่ต้องเฝ้าดู

## Sources
- [[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]] (00:48:15)

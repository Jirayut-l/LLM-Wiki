---
type: concept
title: "Orchestration"
complexity: intermediate
domain: ""
aliases: []
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
status: seed
related: []
sources: []
---

# Orchestration

## Definition
Orchestration (การจัดการเวิร์กโฟลว์) คือกระบวนการควบคุมและบริหารจัดการขั้นตอนการทำงานที่ซับซ้อน หรือระบบ Multi-agent ที่ต้องให้ Agent หลายตัวทำงานร่วมกัน โดยมีการแบ่งเฟสงานที่ชัดเจนและสามารถติดตามความคืบหน้าได้ผ่าน Orchestration Plan เพื่อให้งานบรรลุผลอย่างมีระบบ

## How It Works
Main Agent จะทำหน้าที่เป็น Orchestrator ที่คอยจ่ายงานให้กับ Subagents และควบคุมการทำงานให้เป็นไปตาม Orchestration Plan (ในโฟลเดอร์ `plans/`) โดยจะทำการอัปเดตไฟล์ Plan (เช่น ติ๊กเครื่องหมาย `[x]`) เมื่อแต่ละงานย่อยเสร็จสมบูรณ์ หากใช้ระบบ Agent-team หรือ Multi-agent ที่ซับซ้อน Agents อาจต้องสื่อสารกันเองเพื่อแชร์ข้อมูลและ Task list ซึ่งจะต่างจากการใช้ Subagent แบบปกติที่ทำงานแบบ 1-to-1 กับ Main Agent

## Why It Matters
ช่วยให้สามารถจัดการกระบวนการทำงานที่ซับซ้อนหรือมีหลายขั้นตอนได้อย่างเป็นระบบ ป้องกันการหลอน (Hallucination) หรือการข้ามขั้นตอน และช่วยเปิดโอกาสให้มนุษย์เข้ามาตรวจสอบการทำงาน (Human-in-the-loop) ระหว่างขั้นตอนสำคัญต่างๆ (Checkpoints) ได้

## Connections
- [[claude_subagent|Claude Subagent]]
- [[dynamic_workflow|Dynamic Workflow]]

## Sources
- [[how_to_build_claude_subagents|How to Build Claude Subagents Better Than 99% of People]]
- `CONTEXT.md`

---
type: concept
title: "Thesis of AI Engineering"
complexity: intermediate
domain: "AI Engineering"
aliases: ["The Thesis of AI Engineering"]
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
  - ai-engineering
  - software-engineering
status: seed
related: []
sources:
  - "[[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]"
---

# Thesis of AI Engineering

## Definition
ทฤษฎีนี้ระบุว่าแม้ AI จะถือเป็น paradigm ใหม่ที่เปลี่ยนแปลงหลายแง่มุมของการพัฒนา แต่พื้นฐานของ Software Engineering แบบดั้งเดิม—ซึ่งเป็นแนวปฏิบัติที่ได้รับการพิสูจน์แล้วว่ามีความสำคัญอย่างยิ่งสำหรับนักพัฒนาที่เป็นมนุษย์—ยังคงมีประสิทธิภาพและจำเป็นอย่างมากเมื่อทำงานกับ AI

## How It Works
ทฤษฎีนี้ประยุกต์ใช้หลักการ Software Engineering ที่เป็นที่ยอมรับกับ AI-assisted coding workflows กลไกสำคัญประกอบด้วย:
- **Task Sizing**: การรักษาขนาดของ task ให้เล็กและมีขอบเขตที่ชัดเจน เพื่อให้แน่ใจว่า LLM ยังคงอยู่ใน "smart zone" และหลีกเลี่ยงการเสื่อมถอยของ context (หรือ "dumb zone")
- **Structured Requirements**: การใช้เอกสารที่เป็นทางการ เช่น Product Requirements Documents (PRDs) แทนที่จะพึ่งพาเพียง conversational prompting หรือ ad-hoc chats
- **Established Workflows**: การนำ methodology แบบดั้งเดิม เช่น Test-Driven Development (TDD) มาใช้เพื่อสร้าง verifiable feedback loops สำหรับ autonomous coding agents

## Why It Matters
แนวทางนี้เปลี่ยนจุดโฟกัสของอุตสาหกรรมจากการค้นหา "AI-only" workflows ที่แปลกใหม่ ไปสู่การประยุกต์ใช้ system design ที่มีระเบียบวินัย แนวทางนี้ช่วยให้มี framework ที่เชื่อถือได้และ scalable สำหรับการสร้างแอปพลิเคชันที่ซับซ้อนด้วย AI ด้วยการป้องกันไม่ให้นักพัฒนาป้อน context ให้กับ model มากเกินไป (overloading) จึงทำให้สามารถส่งมอบ (ship) production features อย่างมีประสิทธิภาพโดยใช้ autonomous agents

## Examples
- การใช้ Test-Driven Development (TDD) เพื่อให้ constraints ที่ชัดเจนและตรวจสอบได้สำหรับ AI agent ในการ implement ฟีเจอร์
- การหั่นโปรเจกต์ขนาดใหญ่ให้เป็น "vertical slices" ที่บาง หรือ tracer bullets เพื่อช่วยให้ AI สามารถทำ task ที่แบ่งเป็นสัดส่วน (discrete, isolated) ให้เสร็จสิ้นได้อย่างอิสระโดยไม่สูญเสีย context
- การ stress-test requirement ที่กำกวมและแปลงให้เป็น PRD ที่มีโครงสร้างชัดเจนก่อนที่จะส่งมอบ task ให้กับ AI agent

## Sources
- [[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]

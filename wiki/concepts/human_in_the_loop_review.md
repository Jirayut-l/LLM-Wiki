---
type: concept
title: "Phase 6: Human-in-the-Loop Review"
complexity: intermediate
domain: "AI Coding"
aliases: ["Human-in-the-Loop Review", "QA", "Automated Review"]
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
  - ai-coding
  - workflow
status: seed
related: []
sources: ["[[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]"]
---

# Phase 6: Human-in-the-Loop Review

## Definition
ขั้นตอนที่ 6 ใน Workflow การพัฒนาซอฟต์แวร์ด้วย AI ซึ่งเป็นกระบวนการผสมผสานระหว่างการให้ AI ทบทวนโค้ดของตนเอง (Automated Review) และการให้มนุษย์เข้ามาตรวจสอบการใช้งานจริง (Manual QA) เพื่อควบคุมคุณภาพและใส่รสนิยม (Taste) ลงไปในผลงาน

## How It Works
กระบวนการในเฟสนี้ประกอบด้วย 2 ส่วนหลัก:

1. **Automated Review โดย AI:** ก่อนจะถึงมือมนุษย์ ควรให้ AI รีวิวโค้ดที่มันเพิ่งเขียนขึ้นมาเสียก่อน สิ่งสำคัญคือ **ต้องทำการเคลียร์ Context ก่อนเสมอ** เพื่อให้ AI กลับไปอยู่ใน "Smart Zone" (มี Context Window ว่างพอให้วิเคราะห์ข้อมูลได้ดี) หากไม่เคลียร์ Context และปล่อยให้มันรีวิวในบริบทเดิมที่เต็มไปด้วยประวัติการแชท AI จะทำงานใน "Dumb Zone" ส่งผลให้ตัวรีวิวทำงานได้แย่กว่าตอนที่เขียนโค้ดนั้นขึ้นมา
2. **Manual QA โดยมนุษย์:** หลังจากโค้ดผ่าน Feedback Loops (เช่น การรันเทสต์ TDD หรือ Type check) มนุษย์จะต้องเข้ามาทดสอบการใช้งานแอปพลิเคชันด้วยตัวเอง (QA) เพื่อตรวจสอบความถูกต้องและใส่ความคิดเห็นหรือทิศทางที่ต้องการ (Opinions/Taste) กลับเข้าไปใน Code base

## Why It Matters
หลายทีมมักพยายามทำให้ทุกขั้นตอนเป็นอัตโนมัติ (Automate everything) ตั้งแต่ต้นจนจบ แต่การขาดมนุษย์ในกระบวนการพัฒนามักจะทำให้ได้แอปพลิเคชันที่ขาดรสนิยม ทำงานไม่ตรงตามความตั้งใจ หรือได้ผลงานที่ด้อยคุณภาพ (Slop) การมีมนุษย์อยู่ในลูปการรีวิวจะช่วยยกระดับคุณภาพของแอปพลิเคชันให้เป็นผลงานระดับสูง (High-quality stuff) ได้อย่างแท้จริง

## Examples
- การเริ่มต้นบทสนทนาใหม่ (Clear Context) กับ AI แล้วส่งโค้ดที่เพิ่งเขียนเสร็จไปให้ตรวจสอบหาจุดบกพร่อง
- นักพัฒนาทำการล็อกอินเข้าแอปพลิเคชันด้วยตนเอง เพื่อทดลองใช้งานฟีเจอร์ Gamification ที่ AI เพิ่งสร้างขึ้น และประเมินว่าประสบการณ์ผู้ใช้ (UX) ตรงตามที่คาดหวังหรือไม่

## Connections
- [[smart_zone_and_dumb_zone|Smart Zone and Dumb Zone]]
- [[test_driven_development|Test-Driven Development (TDD)]]

## Sources
- [[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]

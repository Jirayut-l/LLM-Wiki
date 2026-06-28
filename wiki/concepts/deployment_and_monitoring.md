---
type: concept
title: "Phase 7: Deployment & Monitoring"
complexity: intermediate
domain: "AI Coding Workflow"
aliases: ["Deployment and Monitoring"]
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
status: seed
related: []
sources: ["[[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]"]
---

# Phase 7: Deployment & Monitoring

## Definition
ระยะที่ 7 ของกระบวนการเขียนโค้ดด้วย AI มุ่งเน้นไปที่การรักษาภาพรวมสถาปัตยกรรมหรือแผนผังโมดูล (Module Map) ไว้ในใจอย่างชัดเจนตลอดเวลา โดยใช้เทคนิคออกแบบเฉพาะอินเทอร์เฟซ (Interface) และมอบหมาย (Delegate) การเขียนรายละเอียดภายในให้ AI เพื่อรักษาความสามารถในการทดสอบและความเข้าใจในระบบ

## How It Works
- **การกำหนด Module อย่างเจาะจง:** ระบุชัดเจนว่ากำลังทำงานกับโมดูลใด (เช่น Progress Service, Lesson Route, Dashboard Route)
- **การมองเป็นกล่องสีเทา (Gray Boxes):** มองโมดูลต่างๆ เป็น Gray Box ที่เราเข้าใจพฤติกรรม โครงสร้าง และอินเทอร์เฟซภายนอกเป็นอย่างดี
- **การมอบหมาย (Delegation):** นักพัฒนาออกแบบอินเทอร์เฟซของโมดูล ส่วนรายละเอียดการอิมพลีเมนต์ (Implementation) ภายในให้เป็นหน้าที่ของ AI
- **การประเมิน (Reviewing):** ไม่จำเป็นต้องทบทวนโค้ด (Code Review) ทุกบรรทัดภายในโมดูล สนใจแค่ว่าโมดูลนั้นมีพฤติกรรมและการทำงานถูกต้องภายใต้เงื่อนไขที่กำหนดก็เพียงพอ

## Why It Matters
ในยุคที่ AI สามารถสร้างโค้ดจำนวนมหาศาลได้อย่างรวดเร็ว นักพัฒนามักจะสูญเสียความเข้าใจใน Code Base หรือทำงานหนักเกินไปจนหลงทาง แนวคิดนี้ช่วยแก้ปัญหาโดยทำให้นักพัฒนาสามารถเคลื่อนที่ไปข้างหน้าได้อย่างรวดเร็ว ในขณะที่ยังคงรักษาพื้นที่ในสมองไว้เพื่อมองภาพรวมของระบบได้ ช่วยรักษาสติ (Sanity) และทำให้ควบคุมทิศทางของโค้ดได้โดยไม่ถูกกลืนกินไปกับรายละเอียดย่อย

## Examples
- การพัฒนา Gamification System โดยระบุชัดเจนว่านี่คือ Deep Module ที่มี Interface บางอย่างรับผิดชอบ จากนั้นให้ AI เขียนลอจิกภายในทั้งหมด เมื่อเสร็จแล้วนักพัฒนาเพียงแค่ทดสอบจากภายนอกโมดูลว่าอินเทอร์เฟซนั้นคืนค่าและประพฤติตามที่คาดหวังหรือไม่

## Sources
- [[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]

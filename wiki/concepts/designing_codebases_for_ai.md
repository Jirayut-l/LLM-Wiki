---
type: concept
title: "Designing Codebases for AI Effectiveness"
complexity: intermediate
domain: "AI Engineering"
aliases: ["Push vs Pull Context", "Sandcastle"]
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
  - ai-coding
  - architecture
status: seed
related: []
sources: ["[[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]"]
---

# Designing Codebases for AI Effectiveness

## Definition
แนวทางการออกแบบโครงสร้างโค้ดและบริบท (Context) เพื่อให้ AI สามารถทำงานได้อย่างมีประสิทธิภาพสูงสุด โดยเน้นการบริหารจัดการข้อมูลที่ส่งให้ AI ผ่านกลยุทธ์ "Push" และ "Pull" เพื่อไม่ให้ AI ได้รับข้อมูลมากเกินความจำเป็นจนประสิทธิภาพลดลง

## How It Works
การจัดการ Context ให้ AI ทำงานร่วมกับ Codebase มี 2 กลยุทธ์หลัก:
1. **Push (การยัดเยียดข้อมูลให้ AI):** คือการบังคับส่งคำสั่งหรือบริบทไปให้ AI เสมอ เช่น การใส่กฎการเขียนโค้ด (Coding Standards) ไปใน Prompt โดยตรง กลยุทธ์นี้เหมาะสำหรับ **Automated Reviewer Agent** ที่จำเป็นต้องใช้มาตรฐานที่ตายตัวมาตรวจสอบความถูกต้องของโค้ด
2. **Pull (การให้ AI ดึงข้อมูลเอง):** คือการเตรียมข้อมูลหรือเครื่องมือ (Skills) ไว้ใน Repository แล้วเปิดโอกาสให้ AI เป็นฝ่ายเรียกดูเมื่อจำเป็น กลยุทธ์นี้เหมาะสำหรับ **Implementer Agent** เพื่อป้องกันไม่ให้ Context Window เต็มเร็วเกินไป และช่วยรักษา AI ให้อยู่ในสภาวะที่ตัดสินใจได้ดีที่สุด (Smart Zone)

## Why It Matters
หากเราป้อนข้อมูลทุกอย่างให้ AI โดยไม่บริหารจัดการ (Push มากเกินไป) จะทำให้จำนวน Token บวมและ AI จะเริ่มประมวลผลหรือตัดสินใจผิดพลาด (Dumb Zone) การออกแบบให้ AI ใช้ทักษะ Pull สำหรับการลงมือโค้ด (Implementation) และใช้เทคนิค Push สำหรับการตรวจสอบ (Review) จะช่วยให้ระบบ Agent หลายตัวทำงานคู่ขนานกันได้อย่างมีประสิทธิภาพ

## Examples
- **Sandcastle:** ไลบรารี TypeScript ที่ใช้สร้างและรัน Agent Loop ภายใน Sandbox (Docker container) โดยมีกระบวนการทำงานคือ:
  - **Planner:** เลือกส่วนของงาน (Issues) มาทำพร้อมๆ กัน
  - **Implementer (ใช้เทคนิค Pull):** รันใน Sandbox เพื่อแก้ปัญหาและสร้าง Commit โดยดึงข้อมูลเครื่องมือเฉพาะตอนที่ต้องการ
  - **Reviewer (ใช้เทคนิค Push):** ตรวจสอบโค้ดโดยรับมาตรฐานการเขียนโค้ดทั้งหมดเข้าไปพิจารณา (ต้องการโมเดลที่ฉลาดที่สุดในขั้นตอนนี้)
  - **Merger:** นำโค้ดมารวมกันและทดสอบ


## Sources
- [[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]

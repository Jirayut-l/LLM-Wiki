---
type: concept
aliases: [Routine Triggers, Claude Code Routine Triggers]
tags: [concept, ai, agent, automation, triggers]
created: 2026-06-24
sources: ["[[build_a_proactive_agent_workflow_with_claude_code|source_build_a_proactive_agent_workflow_with_claude_code]]"]
title: "Routine Triggers"
complexity: intermediate
domain: "AI Agents"
updated: 2026-06-28
status: developing
related: ["[[claude_code_routines]]", "[[build_a_proactive_agent_workflow_with_claude_code|source_build_a_proactive_agent_workflow_with_claude_code]]"]
---
# Routine Triggers

## Definition
Triggers คือองค์ประกอบสำคัญใน Claude Code Routines ที่ระบุว่าตัว Agent ควรจะเริ่มทำงานเมื่อใด การมี Triggers ช่วยให้ Claude Code สามารถทำงานเชิงรุก (Proactive) ได้โดยไม่ต้องรอให้ผู้ใช้มาสั่งงานทุกครั้ง

## How It Works
การทำงานของ Triggers แบ่งออกเป็น 2 รูปแบบหลักๆ ได้แก่:

### 1. Schedule-based (Time-based Triggers)
การตั้งค่าให้ Routine ทำงานตามรอบเวลาที่กำหนดไว้อย่างชัดเจน (เช่น ทุกสัปดาห์, ทุกเช้าวันจันทร์) 
- **วิธีการใช้งาน**: ผู้ใช้สามารถสั่งงานได้อย่างง่ายดายผ่านคำสั่ง `/schedule` ภายใน Claude Code CLI
- **ตัวอย่างการใช้งาน**: การรันตรวจสอบการเปลี่ยนแปลงของ Source code เทียบกับ Documentation repo ทุกๆ สัปดาห์

### 2. Event-based Triggers
การตั้งค่าให้ Routine เริ่มทำงานเมื่อมีเหตุการณ์บางอย่างเกิดขึ้นในระบบ (Event) ซึ่งช่วยให้ Agent ตอบสนองต่อการเปลี่ยนแปลงได้แบบ Real-time
- **Native GitHub Events**: รองรับเหตุการณ์จาก GitHub โดยตรง เช่น เมื่อมีการเปิด Issue ใหม่, เมื่อมีการตัด Release ใหม่, หรือเมื่อ PR ที่มี Label เฉพาะ (เช่น "need docs") ถูก Merge เข้าสู่ระบบ
- **Custom Webhooks**: รองรับการยิง HTTP POST Request จากระบบภายนอกเพื่อมากระตุ้นให้ Routine ทำงาน พร้อมส่ง Payload ข้อมูลมาเป็นบริบท (Context) ได้ เช่น การให้ CI/CD Pipeline เรียก Webhook หลังจากการ Deploy เสร็จสิ้น

## Connections
- [[claude_code_routines]]
- [[build_a_proactive_agent_workflow_with_claude_code|source_build_a_proactive_agent_workflow_with_claude_code]]

---
type: concept
aliases: [Proactive Agent Use Cases]
tags: [concept, ai, agent, automation, use-case]
created: 2026-06-24
sources: ["[[build_a_proactive_agent_workflow_with_claude_code|source_build_a_proactive_agent_workflow_with_claude_code]]"]
title: "Proactive Agent Use Cases"
complexity: intermediate
domain: "AI Agents"
updated: 2026-06-28
status: developing
related: ["[[claude_code_routines]]", "[[routine_triggers]]", "[[routine_context_and_steerability]]", "[[build_a_proactive_agent_workflow_with_claude_code|source_build_a_proactive_agent_workflow_with_claude_code]]"]
---
# Proactive Agent Use Cases

## Definition
ตัวอย่างการประยุกต์ใช้งานระบบ Proactive Agent ผ่านฟีเจอร์ Claude Code Routines ซึ่งเปลี่ยนบทบาทของ AI จากเพียง "เครื่องมือ" (Tool) ที่ต้องรอรับคำสั่ง กลายเป็น "เพื่อนร่วมทีม" (Teammate) ที่สามารถตอบสนองต่อปัญหาและช่วยเหลืองานของ Developer ได้อัตโนมัติ

## How It Works
การออกแบบ Use Cases ที่ดีจำเป็นต้องพิจารณา 3 ส่วนหลัก ได้แก่: 1) Trigger (เริ่มเมื่อใด) 2) Context (ต้องใช้ข้อมูล/เครื่องมืออะไร) 3) Steerability (จะตรวจสอบอย่างไร)

ตัวอย่าง Use Cases ที่น่าสนใจ:

### 1. Documentation Automation
ระบบอัตโนมัติสำหรับช่วยอัปเดตเอกสาร (Docs) เมื่อมีการเปลี่ยนแปลงใน Source code
- **Schedule-based**: รันทุกสัปดาห์เพื่อวิเคราะห์หาความแตกต่าง (Diff) ระหว่าง Source code ที่เพิ่งถูก Merge เข้ามาใหม่เทียบกับ Documentation repo และเปิด PR อัปเดต Docs หากพบส่วนที่ขาดหาย
- **Event-based (GitHub Issue)**: ทันทีที่มีการเปิด Issue ใหม่ในระบบ (ที่เกี่ยวกับ Docs) ให้ Agent ไปตรวจสอบ Issue นั้น วิเคราะห์ว่าเป็นช่องโหว่ของเอกสารจริงหรือไม่ หากจริงให้เปิด PR แก้ไข และแจ้งเตือนทีมผ่าน Slack
- **Event-based (Release/Label)**: ทำงานเมื่อมีการ Release เวอร์ชั่นใหม่ หรือเมื่อ PR ที่มี Label ว่า "need docs" ถูก Merge ให้ Agent เปิด PR ทำเอกสารของฟีเจอร์นั้นๆ

### 2. Deploy Verifier
ระบบตรวจสอบความสมบูรณ์หลังการ Deploy เพื่อช่วยตัดสินใจและดำเนินการ Rollback หากมีปัญหา
- **Trigger**: ทำงานทันทีผ่าน Webhook เมื่อ CI/CD Pipeline ทำการ Deploy เสร็จสิ้น
- **Context**: ให้ Agent เข้าถึง Source code ของ Service นั้น และเชื่อมต่อระบบ Monitoring Tools (เช่น Datadog, Grafana) และระบบสื่อสาร (Slack/Email/Twilio)
- **Workflow**: Agent จะเข้าไปตรวจสอบค่า Metrics ต่างๆ หากพบความผิดปกติจะประเมินสถานการณ์ (Go / No-go) และแจ้งเตือนทีม มนุษย์สามารถเข้าไปดู Session สด (Interactive Monitoring) และให้ Agent ช่วยดำเนินการสั่ง Rollback โค้ดได้

### 3. Backlog Manager / On-call Investigator
ระบบจัดการปัญหาหรือสรุป Backlog อัตโนมัติ
- **Workflow**: ตั้งเวลา (Schedule) ให้ Agent เข้าไปอ่านและสรุปข้อมูลใน GitHub Issues หรือช่องแชทใน Slack เพื่อจัดลำดับความสำคัญ (Prioritize) ปัญหาที่สำคัญที่สุด หรือแม้กระทั่งเปิด PR เพื่อแก้ไขบั๊กเล็กๆ น้อยๆ ที่ค้างอยู่ในระบบ

## Connections
- [[claude_code_routines]]
- [[routine_triggers]]
- [[routine_context_and_steerability]]
- [[build_a_proactive_agent_workflow_with_claude_code|source_build_a_proactive_agent_workflow_with_claude_code]]

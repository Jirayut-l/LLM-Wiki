---
type: concept
aliases: [Routine Context, Routine Steerability]
tags: [concept, ai, agent, automation, context, steerability]
created: 2026-06-24
sources: ["[[source_build_a_proactive_agent_workflow_with_claude_code]]"]
---
# Routine Context and Steerability

## Summary
Context (บริบท) และ Steerability (การควบคุมทิศทาง) เป็นสององค์ประกอบที่กำหนดขีดจำกัดความสามารถและความแม่นยำของ Claude Code Routines โดย Context จะเป็นตัวกำหนดว่า Agent มีข้อมูลและเครื่องมืออะไรให้ใช้บ้าง ส่วน Steerability คือกลไกในการควบคุมคุณภาพผลลัพธ์ไม่ให้ออกนอกลู่นอกทาง

## Core Principles

### 1. Context (บริบทและข้อมูล)
เพดานความสำเร็จของ Agent ขึ้นอยู่กับบริบทที่มันได้รับ การให้ Context แก่ Routine ประกอบไปด้วย:
- **Code Repositories**: การให้สิทธิ์การเข้าถึง Source Code และ Documentation Repositories ที่จำเป็นต่อการปฏิบัติงาน เพื่อให้ Agent สามารถอ่าน ตรวจสอบ และเขียนโค้ดกลับไปได้ (เช่น เปิด PR)
- **Additional Context**: ข้อมูลบริบทเพิ่มเติมจากภายนอก เช่น การเชื่อมต่อ Google Drive เพื่อให้ Agent ได้อ่าน Marketing Briefs หรือเอกสารแนวทางของบริษัท
- **Tools / Connectors**: การเชื่อมต่อเครื่องมือที่ใช้ในการทำงานและแจ้งเตือน เช่น Slack สำหรับส่งข้อความแจ้งเตือนมนุษย์, Monitoring Tools อย่าง Datadog หรือ Grafana สำหรับการอ่านค่าสถานะระบบ

### 2. Steerability (การควบคุมและการตรวจสอบ)
แม้ Agent จะทำงานแบบอัตโนมัติ (Proactive) แต่มนุษย์หรือระบบยังสามารถเข้าไปควบคุมหรือตรวจสอบการทำงานได้ผ่านหลายวิธีการ:
- **Interactive Monitoring (Human-in-the-loop)**: ผู้ใช้สามารถเข้าไปดู Session ของ Routine ที่กำลังรันอยู่แบบ Real-time ได้ผ่านเว็บ Claude.ai โดยสามารถสอบถาม (Ask), แทรกแซง/ชี้นำ (Nudge), สั่งหยุด (Stop) หรือสั่งให้ทำงานต่อ (Resume) ได้เสมือนรันบน Terminal เครื่องตัวเอง
- **Agent-on-agent Review**: การใช้โมเดล Generator-Critiquer ในระบบ Multi-agent โดยให้ Routine ตัวแรกสร้างผลงาน (เช่น สร้าง PR) และใช้ Routine อีกตัวหนึ่งซึ่งถูก Trigger เมื่อมี PR ใหม่ เข้ามารีวิวและทิ้งคอมเมนต์วิจารณ์ผลงาน
- **Output Verification**: การตรวจสอบผลลัพธ์ขั้นสุดท้าย เช่น การพรีวิวหน้าเอกสารที่ Agent สร้างขึ้นเพื่อยืนยันความถูกต้องก่อนกดยอมรับจริง

## Related
- [[claude_code_routines]]
- [[proactive_agent_use_cases]]
- [[source_build_a_proactive_agent_workflow_with_claude_code]]

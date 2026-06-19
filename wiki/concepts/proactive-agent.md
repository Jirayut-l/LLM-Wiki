---
type: concept
aliases: ["Proactive Agent", "Proactive Agents"]
tags: ["agents", "automation"]
created: 2026-06-19
---
# Proactive Agents

## Summary
Proactive Agent คือระบบอัตโนมัติ (automated AI workflow) ที่ออกแบบมาเพื่อทำหน้าที่เป็นเพื่อนร่วมทีมอิสระ (independent teammate) แทนที่จะเป็นแค่เครื่องมือ (passive tool) แตกต่างจาก reactive agents ที่ต้องรอคำสั่ง (prompt) จากผู้ใช้ถึงจะเริ่มทำงาน โดย proactive agents จะเริ่มทำงานอัตโนมัติตามตารางเวลาที่ตั้งไว้ (schedules/cron) หรือตามเหตุการณ์ที่เกิดขึ้น (event triggers เช่น มี GitHub issues หรือ deployments ใหม่)

## Core Content

### Reactive vs. Proactive Agents
ความแตกต่างหลักระหว่าง reactive และ proactive agents อยู่ที่วิธีการเริ่มต้นทำงาน (trigger) และรูปแบบการทำงานร่วมกับ workflow ของนักพัฒนา

| Feature (คุณสมบัติ) | Reactive Agents (เครื่องมือ) | Proactive Agents (เพื่อนร่วมทีม) |
| :--- | :--- | :--- |
| **Execution Trigger (การสั่งการ)** | Manual (ผู้ใช้ต้องกดปุ่ม Enter) | Automated (สั่งการอัตโนมัติผ่าน Schedules หรือ events เช่น webhooks/GitHub actions) |
| **Availability (ความพร้อมใช้งาน)** | ขึ้นอยู่กับเครื่อง Local (หยุดทำงานเมื่อปิดแล็ปท็อป) | Always available (รันบน managed cloud infrastructure ทำงานได้ตลอดเวลา) |
| **Role (บทบาท)** | Tool (เครื่องมือ) | Teammate (เพื่อนร่วมทีม) |
| **Infrastructure (โครงสร้างพื้นฐาน)** | Local processing (ประมวลผลบนเครื่องผู้ใช้) | Managed infrastructure (ระบบจัดการเรื่อง Hosting, state, และ connectors ให้ทั้งหมด) |

### Infrastructure Differences (ความแตกต่างด้านโครงสร้างพื้นฐาน)
ในอดีต การสร้าง proactive agents ต้องใช้การเขียนโค้ดซ้ำซ้อน (boilerplate) และจัดการ infrastructure เองทั้งหมด:
- **Traditional Approach (วิธีดั้งเดิม)**: นักพัฒนาต้องตั้งเซิร์ฟเวอร์เอง, จัดการ `cron` jobs, ดูแล session state, จัดการ data persistence, และวางระบบ authentication เอง หากเครื่อง local ดับหรือปิดไป เซสชันนั้นก็จะจบลง
- **Managed Infrastructure (โครงสร้างที่จัดการให้)**: Proactive workflows สมัยใหม่ (อย่างเช่น Routines ของ Claude Code) จะรันบน managed cloud infrastructure ซึ่งช่วยลดความซับซ้อนเรื่อง hosting, session state persistence, และ connector authentication ทำให้ agents มีสถานะ "always available" (พร้อมใช้งานเสมอ) โดยไม่สนใจว่าฮาร์ดแวร์ฝั่งผู้ใช้จะเปิดอยู่หรือไม่

### Benefits of Proactive Workflows (ข้อดีของการทำงานแบบ Proactive)
Proactive workflows ช่วยยกระดับ AI จากแค่เครื่องมือเขียนโค้ดธรรมดาให้กลายเป็นเพื่อนร่วมทีม (teammate) ข้อดีหลักๆ ประกอบด้วย:
- **Automation of Repetitive Tasks (ลดงานซ้ำซ้อน)**: งานประเภทอัปเดตเอกสาร (sync documentation) ระหว่าง codebases หรือการรีวิว PR สามารถเกิดขึ้นอัตโนมัติในเบื้องหลัง
- **Event-Driven Interventions (ตอบสนองต่อเหตุการณ์)**: Agents สามารถตอบสนองต่อเหตุการณ์ได้ทันที (เช่น การทำ CI/CD deploy หรือมี GitHub issue ใหม่) สามารถเข้าไปอ่านข้อมูลจาก monitoring tools (เช่น DataDog, Grafana) และแจ้งเตือนทีมผ่าน Slack ได้โดยไม่ต้องรอคนมาตรวจสอบ (human triage)
- **Steerability (ความสามารถในการควบคุม)**: ถึงแม้จะรันแบบ headless แต่ proactive agents ก็ยังสามารถถูกตรวจสอบและควบคุมทิศทาง (steered) โดยคนได้แบบเรียลไทม์ ผู้ใช้สามารถรันเซสชันเดิมต่อ (resume) หรือเข้าแทรกแซงหาก agent ต้องการคำแนะนำ

## Related
- [[claude-code-routines|Claude Code Routines]]
- Agent-on-agent review

## Sources
- [[Build a proactive agent workflow with Claude Code]]

## Questions to follow up
- เราจะนำแพตเทิร์น generator-critiquer (agent-on-agent review) ที่ระบุในต้นฉบับมาประยุกต์ใช้งานจริงใน workflows ของเราเองได้อย่างไรบ้าง?

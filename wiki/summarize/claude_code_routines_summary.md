---
type: summary
aliases: [Building Proactive Agents with Claude Code]
tags: [summary, ai, agent, automation]
created: 2026-06-24
sources: ["[[source_build_a_proactive_agent_workflow_with_claude_code]]"]
---
# Building Proactive Agents with Claude Code

## Overview
การสร้าง Proactive Agent (Agent เชิงรุก) ด้วย Claude Code ผ่านฟีเจอร์ Routines เป็นการเปลี่ยนกระบวนทัศน์จากการใช้ AI เป็นเพียง "เครื่องมือ" (Tool) ที่ต้องรอรับคำสั่ง ให้กลายเป็น "เพื่อนร่วมทีม" (Teammate) ที่สามารถตอบสนองต่อปัญหาได้เอง ระบบสามารถทำงานอัตโนมัติตามเงื่อนไขที่กำหนดไว้โดยรันอยู่บน Infrastructure ของ Anthropic โดยตรง ซึ่งช่วยขจัดความยุ่งยากในการสร้างและดูแลระบบพื้นฐาน (เช่น Hosting, Cron jobs) ให้กับนักพัฒนา

## Key Insights
การออกแบบและพัฒนา Workflow ของ Proactive Agent ที่มีประสิทธิภาพ ประกอบด้วย 3 องค์ประกอบหลักที่ต้องทำงานประสานกัน:
1. **Triggers (การเริ่มต้น)**: การกำหนดจุดเริ่มต้นของการทำงาน ซึ่งรองรับทั้งการตั้งเวลา (Schedule-based) และการตอบสนองต่อเหตุการณ์ (Event-based) จากระบบภายนอก เช่น GitHub Webhooks หรือ CI/CD pipelines
2. **Context (บริบทและข้อมูล)**: การกำหนดขีดความสามารถของ Agent โดยให้สิทธิ์การเข้าถึงข้อมูลที่จำเป็น (เช่น Source code repo, เอกสารใน Google Drive) และเครื่องมือที่ต้องใช้ (เช่น Slack, Datadog)
3. **Steerability (การควบคุม)**: การรักษาคุณภาพและความปลอดภัยของผลลัพธ์ ผ่านกลไกการตรวจสอบที่มนุษย์สามารถมีส่วนร่วม (Interactive Monitoring) หรือใช้โมเดล Multi-agent ในการตรวจสอบกันเอง (Agent-on-agent review)

เมื่อประกอบองค์ประกอบทั้ง 3 เข้าด้วยกัน จะสามารถแก้ปัญหาจริงที่นักพัฒนาพบเจอได้ เช่น การทำ Documentation Automation อัตโนมัติเมื่อโค้ดเปลี่ยน, การสร้างระบบ Deploy Verifier ที่คอยดูแลความปลอดภัยหลังนำระบบขึ้น, หรือการมี On-call Investigator ที่คอยจัดการ Backlog ให้

## Related Concepts
- [[concept_claude_code_routines]]
- [[concept_routine_triggers]]
- [[concept_routine_context_and_steerability]]
- [[concept_proactive_agent_use_cases]]

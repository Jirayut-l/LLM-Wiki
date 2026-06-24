---
title: "Build a proactive agent workflow with Claude Code"
type: source
aliases: []
tags: [source]
created: 2026-06-24
url: "https://www.youtube.com/watch?v=eSP7PLTXNy8&t=369s"
author: "Maya (Anthropic)"
---
# Build a proactive agent workflow with Claude Code

## Summary
นำเสนอเกี่ยวกับการใช้ฟีเจอร์ใหม่ที่ชื่อว่า Routines ใน Claude Code เพื่อสร้างเอเจนต์แบบทำงานเชิงรุก (Proactive Agents) ที่สามารถทำงานได้โดยอัตโนมัติตามตารางเวลาหรือเหตุการณ์ (Triggers) ต่างๆ โดยไม่ต้องรอให้ผู้ใช้สั่งการแบบเดิม ทำให้ Claude เปลี่ยนจากการเป็นแค่เครื่องมือ (Tool) มาเป็นเพื่อนร่วมทีม (Teammate) ที่ช่วยเหลือเรื่องการจัดการโค้ดหรือเอกสารล่วงหน้า

## Key Takeaways
- **ข้อจำกัดเดิม:** การสร้าง Proactive Agents ด้วยตัวเองมีปัญหาเรื่องความยุ่งยากในการจัดการ Infrastructure ทั้งเรื่อง Hosting, Data Persistence, Authentication และการสร้าง Trigger หรือ Cron Jobs เอง
- **การแก้ปัญหาด้วย Routines:** ฟีเจอร์ Routines ใน Claude Code มาพร้อม Managed Infrastructure ทำให้ Agent พร้อมทำงานตลอดเวลา (Always Available) โดยที่ผู้ใช้ไม่ต้องจัดการ Infra เอง
- **ประเภทของ Triggers:** 
  1. **Schedule-based (เวลา):** ตั้งเวลาทำงานตามรอบ เช่น รันตรวจสอบโค้ดเพื่อสร้าง PR ทุกสัปดาห์
  2. **Event-based (เหตุการณ์):** รองรับ Native GitHub Events (เช่น เมื่อมีการสร้าง Issue หรือ PR) หรือ Webhooks (เช่น จาก CI/CD pipeline)
- **Context & Steering:** สามารถกำหนดบริบทให้ Agent ทำงานได้มีประสิทธิภาพ (เช่น การเชื่อมต่อ Repos, Google Drive, Slack) และผู้ใช้ยังสามารถเข้าไปตรวจสอบหรือแก้ไขทิศทางการทำงานของ Agent ระหว่างที่มันทำงานอยู่ได้แบบ Real-time (Steerable) เพื่อรักษาให้เป็น Human-in-the-loop เมื่อต้องการ
- **เริ่มต้นใช้งานง่าย:** สามารถเริ่มต้นใช้งาน Routines ได้ทันทีผ่านการพิมพ์คำสั่ง `/schedule` ใน Claude Code CLI

## Related Concepts
- [[concept_claude_code_routines]]

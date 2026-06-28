---
type: source
aliases: []
tags:
  - source
created: 2026-06-14
url: "https://www.youtube.com/watch?v=e18sdZLwP7o"
file_path: "raw/How to Build Claude Subagents Better Than 99% of People.md"
author: "[[nate_herk| AI Automation]]"
---
# How to Build Claude Subagents Better Than 99% of People

## Summary
วิดีโอนี้อธิบายวิธีการสร้างและใช้งาน Subagents ใน Claude Code อย่างมีประสิทธิภาพ โดยเน้นความแตกต่างระหว่าง Built-in และ Custom agents, การเขียนคำอธิบาย (Descriptions) ที่ดี, และการแยกส่วนการทำงานเป็นทีมย่อยที่มีความเชี่ยวชาญเฉพาะด้าน (Specialists) ภายใต้แอดเจนต์หลักที่ทำหน้าที่เป็นผู้สั่งการ (Orchestrator) เพื่อช่วยประหยัดค่าใช้จ่าย รักษาบริบทหลัก (Context Window) ให้สะอาด และเพิ่มประสิทธิภาพในการทำงาน

## Key Takeaways
- **What Is a Subagent**: Subagent คืออินสแตนซ์แยกต่างหากที่มี Context Window ของตัวเอง ช่วยป้องกันไม่ให้ข้อมูลหรือผลลัพธ์ที่ยาวเกินไปมาปะปนในแชทหลัก
- **Built-In vs Custom Agents**: สามารถใช้ Agent ทั่วไปที่ Claude สร้างมาให้ หรือเขียนเป็น Custom agent ในรูปแบบไฟล์ Markdown
- **Descriptions & Progressive Disclosure**: คำอธิบายใน YAML front matter สำคัญมากในการเป็นทริกเกอร์ (Trigger) เพื่อให้ Claude ตัดสินใจว่าจะเรียกใช้ Subagent แบบอัตโนมัติหรือไม่
- **Project vs Global**: สามารถตั้งค่า Subagents ให้ใช้งานเฉพาะโปรเจกต์ (Project level) หรือกำหนดให้เป็นส่วนกลางเพื่อใช้งานได้ในทุกโปรเจกต์ (Global level)
- **Subagents as Specialists**: ควรให้ AI แต่ละตัวมีความเชี่ยวชาญเฉพาะด้าน (เช่น ผู้ตรวจสอบแนวคิดแบบโต้แย้ง หรือนักวิจัย)
- **Cost Saving & Read-Only**: สามารถประหยัดเงินได้โดยการสปิน (Spin) โมเดลที่ถูกกว่าอย่าง Haiku ไปประมวลผลข้อมูลเอกสารยาวๆ และส่งผลสรุปกลับมายัง Session หลัก รวมถึงตั้งค่าเครื่องมือเป็น Read-only เพื่อความปลอดภัยได้
- **Dynamic Workflows**: ใช้สร้างเวิร์กโฟลว์อัตโนมัติที่สั่งรัน Subagents ขนานกันหลายตัวพร้อมกัน แต่ต้องระวังเรื่องปริมาณจำกัดการใช้งานใน Session

## Related Concepts
- [[claude_code|Claude Code]]
- [[subagent|Subagent]]
- [[orchestration|Orchestration]]
- [[progressive_disclosure|Progressive Disclosure]]
- [[dynamic_workflow|Dynamic Workflows]]

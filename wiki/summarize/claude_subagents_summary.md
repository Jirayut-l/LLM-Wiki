---
type: summary
aliases: [Claude Subagents Summary]
tags: [summary, claude-code]
created: 2026-06-22
sources: ["[[how_to_build_claude_subagents_source|How to Build Claude Subagents Better Than 99% of People]]"]
---
# How to Build Claude Subagents Better Than 99% of People (Summary)

## Overview
สรุปองค์ความรู้จากวิดีโอ "How to Build Claude Subagents Better Than 99% of People" ซึ่งอธิบายเกี่ยวกับสถาปัตยกรรมและการใช้งานขั้นสูงของ Claude Code โดยเน้นไปที่การสร้างและการประยุกต์ใช้ **Claude Subagents**, **Dynamic Workflows**, และกลไก **Progressive Disclosure** เพื่อช่วยให้นักพัฒนาสามารถสเกลการทำงานที่ใช้ AI ช่วยเหลือได้อย่างมีประสิทธิภาพ ปลอดภัย และประหยัดค่าใช้จ่าย โดยไม่ทำให้ Context ของการสนทนาหลักรกเกินไป

## Key Insights
- **Clean Context & Parallel Execution**: [[Claude Subagent]] ทำงานใน Context Window ที่แยกเป็นอิสระจาก Main Session ทำให้การรันงานขนาดใหญ่หรือกิน Token เยอะๆ (เช่น การอ่านและสรุปข้อมูลปริมาณมาก) ไม่กระทบต่อบริบทหลัก นอกจากนี้ยังสามารถสปินออกไปทำงานขนานกัน (Parallel) ได้
- **Cost Optimization**: สามารถระบุให้ Subagent ใช้โมเดลที่มีขนาดเล็กลงและราคาถูกกว่า (เช่น Haiku) สำหรับงานที่ไม่ซับซ้อนมาก ในขณะที่ Main Session (Orchestrator) ยังคงใช้โมเดลที่ฉลาดที่สุด (เช่น Opus) เพื่อควบคุมงาน
- **Massive Scale Operations**: ฟีเจอร์ [[Dynamic Workflow]] (หรือ Ultra Code) ช่วยให้สามารถสปิน Subagent จำนวนหลายสิบหรือหลักร้อยตัวพร้อมกัน เพื่อทำงานย่อยๆ แบบคู่ขนาน ประหยัดเวลาอย่างมหาศาล แต่ต้องระวังเรื่อง Session Limit และค่าใช้จ่าย
- **The Role of Progressive Disclosure**: กลไกการค้นพบ Subagent และ Skill ของระบบใช้ [[Progressive Disclosure]] โดยจะอ่านแค่ Frontmatter (`description`) เพื่อตัดสินใจว่าจะเรียกใช้งานหรือไม่ การเขียนคำอธิบายให้ชัดเจนและเฉพาะเจาะจงจึงเป็นหัวใจสำคัญในการป้องกันไม่ให้ระบบเรียกใช้งานผิดพลาด (Misfire)
- **Subagents vs. Skills**: Subagent เหมาะกับงานอิสระที่ต้องการ Context แยกและรันขนาน ส่วน Skill เหมาะกับเวิร์กโฟลว์เฉพาะเจาะจงที่ทำงานแบบลำดับขั้น (Sequential) ร่วมกับ Main Session

## Related Concepts
- [[Claude Subagent]]
- [[Dynamic Workflow]]
- [[Progressive Disclosure]]
- [[how_to_build_claude_subagents_source|How to Build Claude Subagents Better Than 99% of People]]

---
type: concept
aliases: [Dynamic Workflow, Dynamic Workflows, Ultra Code]
tags: [concept, claude-code]
created: 2026-06-22
sources: ["[[How to Build Claude Subagents Better Than 99% of People]]"]
---
# Dynamic Workflows

## Summary
Dynamic Workflows เป็นฟีเจอร์ขั้นสูงใน Claude Code (เริ่มใช้งานตั้งแต่ Opus 4.8) ที่อนุญาตให้ผู้ใช้สามารถสั่งสร้างและรัน Subagents จำนวนมากเพื่อทำงานต่างๆ ได้แบบขนาน (Parallel) ในเวลาเดียวกัน ฟีเจอร์นี้เหมาะสำหรับการจัดการโปรเจกต์ขนาดใหญ่ที่มีงานย่อยที่ทำแยกกันได้อิสระ โดย Main Session จะทำหน้าที่เป็น Orchestrator จ่ายงานให้ Subagents ทั้งหมดพร้อมกัน

## Core Principles

### การทำงานแบบคู่ขนาน (Parallel Delegation)
เมื่อมีการร้องของานขนาดใหญ่ที่สามารถทำพร้อมกันได้ Claude จะพิจารณาใช้ Dynamic Workflows โดยการสปิน (Spin up) Subagents จำนวนมาก (เช่น 3 ตัว, 40 ตัว หรืออาจถึง 200 กว่าตัว ขึ้นอยู่กับสเกลของงาน) ออกไปทำงานย่อยเหล่านั้นในเวลาเดียวกัน ทำให้ประหยัดเวลาได้อย่างมหาศาลเมื่อเทียบกับการรันตามลำดับ (Sequential)

### ข้อควรระวังด้านค่าใช้จ่ายและข้อจำกัด (Cost & Session Limits)
การสปิน Subagents จำนวนมากพร้อมกันหมายถึงการเรียกใช้งาน Context Window และ Model จำนวนมากในเวลาเดียวกันอย่างรวดเร็ว (Resource Intensive) ซึ่งอาจทำให้สิ้นเปลืองค่าใช้จ่ายสูงและเสี่ยงต่อการเกินขีดจำกัดการใช้งานในแต่ละ Session (Session Limit) จึงควรใช้ฟีเจอร์นี้ด้วยความระมัดระวังเฉพาะเมื่อจำเป็นจริงๆ

### การเรียกใช้งาน (Triggering)
ช่วงแรกฟีเจอร์นี้ใช้คำว่า "workflow" เป็น Trigger แต่ต่อมาได้เปลี่ยนคำสั่งเป็น "ultra code" เพื่อหลีกเลี่ยงการไปทริกเกอร์แบบไม่ได้ตั้งใจเมื่อผู้ใช้แค่ต้องการกล่าวถึงคำว่า workflow ในบริบทอื่น อย่างไรก็ตาม การสั่งงานให้ชัดเจนว่าต้องการ "ใช้ workflow สำหรับงานนี้" ก็ยังสามารถกระตุ้นให้เกิดการสร้าง Dynamic workflow ได้เช่นกัน

## Related
- [[Claude Subagent]]
- [[How to Build Claude Subagents Better Than 99% of People]]

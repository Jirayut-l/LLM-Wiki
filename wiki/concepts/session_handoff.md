---
type: concept
aliases: ['Session Handoff']
tags: [concept]
created: 2026-06-24
sources: ["[[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens|Give Me 10 Mins and I'll Save You Millions of Claude Tokens]]"]
title: "Session Handoff"
complexity: intermediate
domain: "AI Workflow"
updated: 2026-06-28
status: developing
related: ["[[claude_prompt_caching|Prompt Caching]]", "[[claude_code|Claude Code]]"]
---
# Session Handoff

## Definition
Session Handoff คือทักษะหรือเทคนิคในการทำงานที่ช่วยประหยัด Token สำหรับการใช้งาน AI อย่างเช่น [[claude_code|Claude Code]] โดยเมื่อเซสชันการทำงานใช้เวลาเกินกำหนด (เช่น เกิน 1 ชั่วโมง) หรือเมื่อสลับงาน แทนที่จะปล่อยเซสชันเดิมที่มีประวัติยาวๆ ทิ้งไว้ ทักษะนี้จะช่วยสร้างข้อความสรุปสถานะของงาน เพื่อให้นำไปเริ่มเซสชันใหม่ได้โดยที่บริบทสำคัญไม่สูญหายไป

## How It Works
- **การสรุปบริบทสำคัญ:** ทักษะนี้จะทำการสรุปทุกสิ่งที่ได้ทำไปแล้ว ไฟล์สำคัญที่ถูกสร้างขึ้นมา การตัดสินใจที่ยังเปิดอยู่ (open decisions) และจุดที่ต้องทำงานต่อ
- **ป้องกันการสิ้นเปลือง Token จาก Cache:** เมื่อเซสชันไม่มีการเคลื่อนไหวนานเกินเวลา Time to Live (TTL) เช่น 1 ชั่วโมง หรือเมื่อมีการรีเซ็ตแคช หากเราทำงานบนประวัติแชทที่ยาวมาก การประมวลผลและสร้างแคชใหม่ทั้งหมด (Cache Create) จะใช้ Token สิ้นเปลืองมาก การทำ Session Handoff จึงช่วยตัดประวัติที่ไม่จำเป็นออก
- **ขั้นตอนการนำไปใช้:** 
  1. สร้างสรุปโดยใช้ทักษะ Session Handoff
  2. คัดลอกเนื้อหาสรุปที่ได้
  3. ทำการเคลียร์เซสชัน (ใช้คำสั่ง `/clear`) หรือเปิดเซสชันใหม่
  4. วางคำสรุปลงไปเพื่อทำงานต่อจากจุดเดิมเสมือนไม่เสียความคืบหน้า
- **รวดเร็วกว่าคำสั่ง /compact:** การใช้ Session Handoff เป็นทางเลือกที่ดีกว่าการสั่ง `/compact` เพราะมักจะประมวลผลเสร็จในเวลาไม่ถึง 1 นาที และทำงานได้ราบรื่นกว่า

## Connections
- [[claude_prompt_caching|Prompt Caching]]
- [[claude_code|Claude Code]]

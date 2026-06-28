---
type: concept
aliases: ['Prompt Caching', 'Claude Prompt Caching']
tags: [concept]
created: 2026-06-24
sources: ["[[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens|Give Me 10 Mins and I'll Save You Millions of Claude Tokens]]"]
title: "Claude Prompt Caching"
complexity: intermediate
domain: "AI Engineering"
updated: 2026-06-28
status: developing
related: ["[[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens|Give Me 10 Mins and I'll Save You Millions of Claude Tokens]]", "[[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens]]", "[[claude_code|Claude Code]]", "[[claude|Claude]]", "[[session_handoff|Session Handoff]]", "[[token_dashboard|Token Dashboard]]"]
---
# Claude Prompt Caching

## Definition
Prompt Caching คือกลไกการจดจำบริบทของ Claude ที่ช่วยลดค่าใช้จ่ายในการประมวลผลซ้ำ โดย Cache Read จะมีราคาถูกกว่า Input ปกติถึง 90% (หรือจ่ายแค่ 10%) ซึ่งจะทำงานโดยอัตโนมัติภายใต้เงื่อนไขเวลาและโครงสร้างคำสั่งที่ถูกต้อง เพื่อช่วยให้การทำงานในเซสชันที่ยาวนานหรือมีไฟล์แนบเยอะๆ ประหยัด Token ลงไปได้อย่างมหาศาล

## How It Works
- **Cache Create vs. Cache Read:** การประมวลผลข้อความใหม่ครั้งแรก (Cache Create) จะมีต้นทุนปกติ แต่หากมีข้อความเดิมที่ถูกจดจำไว้แล้ว ระบบจะดึงจาก Cache (Cache Read) มาใช้ ซึ่งมีต้นทุนเพียง 10% ของปกติ
- **Prefix Matching:** แคชจะจดจำจากส่วนต้นเสมอ (System Prompt -> Project Context -> Conversation History) หากมีการแก้ไขข้อมูลในส่วนต้น ทุกอย่างที่อยู่หลังจากนั้นจะต้องถูกประมวลผลและสร้างแคชใหม่ทั้งหมด
- **Time To Live (TTL):** อายุของแคชก่อนที่จะหมดเวลา
  - **1 ชั่วโมง:** สำหรับ Claude Subscription และ [[claude_code|Claude Code]]
  - **5 นาที:** สำหรับการใช้งานผ่าน API (โดยค่าเริ่มต้น) และการใช้ Sub-agents
- **สิ่งที่ทำให้ Cache แตก (What Breaks the Cache):**
  1. ทิ้งเซสชันไว้นานเกินระยะเวลา TTL
  2. การเปลี่ยน Model กลางเซสชัน (เช่น สลับจาก Opus เป็น Sonnet) จะทำให้แคชรีเซ็ตใหม่ทั้งหมด
  3. การเปลี่ยน System Prompt หรือแก้ไฟล์ `claude.md` ในระหว่างเซสชัน
- **แนวทางปฏิบัติ (Best Practices):**
  - ไม่ทิ้งเซสชันไว้นานเกิน TTL
  - เมื่อเปลี่ยนงาน ให้ขึ้นเซสชันใหม่ หรือใช้คำสั่ง `/clear` หรือทำ [[session_handoff|Session Handoff]]
  - หากมีเอกสารขนาดใหญ่ ควรใส่ไว้ใน Project (Project Knowledge) แทนการแปะลงในช่องแชทตรงๆ เพื่อการจดจำแคชที่มีประสิทธิภาพมากกว่า

## Connections
- [[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens|Give Me 10 Mins and I'll Save You Millions of Claude Tokens]]
- [[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens]]
- [[claude_code|Claude Code]]
- [[claude|Claude]]
- [[session_handoff|Session Handoff]]
- [[token_dashboard|Token Dashboard]]

## Questions to follow up
- None

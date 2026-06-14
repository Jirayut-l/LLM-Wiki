---
type: concept
aliases: ["Claude Prompt Caching", "Prompt Caching"]
tags: ["claude", "optimization", "caching"]
created: 2026-06-14
---
# Prompt Caching

## Summary
**Prompt Caching** เป็นระบบที่ช่วยประหยัดค่าใช้จ่ายการใช้งาน Token เมื่อมีการส่ง Context หรือเนื้อหาเดิมซ้ำๆ ให้กับโมเดลภาษาอย่าง Claude โดย Token ที่ถูกดึงมาจาก Cache จะมีราคาถูกลงมาก ทำให้ผู้ใช้สามารถประหยัดโควตารวมถึงลดระยะเวลาในการประมวลผลลงได้อย่างมีนัยสำคัญ

## Core Content

### หลักการทำงานและประโยชน์ (Cost Savings)
- **การลดค่าใช้จ่าย:** ข้อมูลที่ถูกดึงจาก Cache (Cache Read) จะมีราคาคิดเป็นเพียงแค่ **10% ของราคา Input Token ปกติ** (ถูกลงถึง 10 เท่า)
- **Cache Create vs Cache Read:** 
  - `Cache Create` คือจังหวะที่มีการเขียนข้อมูลลงไปเก็บใน Cache เป็นครั้งแรก (จ่ายราคาเต็ม 100%)
  - `Cache Read` คือการหยิบข้อมูลเดิมจากประวัติหรือจาก Cache มาใช้ซ้ำในการคุยรอบถัดไป 

### โครงสร้าง Cache Layers (Cache Growth)
เวลาที่เราโต้ตอบ ระบบจะแบ่งการจดจำ (Caching) ออกเป็นแต่ละเลเยอร์จากกว้างไปเฉพาะเจาะจง:
1. **System Layer:** คำสั่งพื้นฐาน (System Prompt) และเครื่องมือ (Tool definitions เช่น read, write) 
2. **Project Layer:** ข้อมูลประจำโปรเจค เช่น `Claude.md` (Memory), ไฟล์โค้ด หรือเอกสารต่างๆ 
3. **Conversation Layer:** ประวัติการตอบโต้ไปมา (User Messages & Replies) ที่จะโตขึ้นเรื่อยๆ ในแต่ละรอบการคุย

*ข้อดีคือหากมีการคุยต่อ ระบบจะดึงข้อมูลจาก System และ Project Layer รวมของเก่าจาก Conversation มาเป็น Cache Read แล้วประมวลผลเพิ่มแค่ Message ใหม่ล่าสุดเท่านั้น*

### อายุการใช้งานของ Cache (TTL - Time to Live)
Cache จะไม่คงอยู่ถาวร แต่จะมีหน้าต่างเวลาที่กำหนดไว้ (TTL):
- **1 ชั่วโมง (1 Hour):** สำหรับการใช้งานปกติอย่าง Claude Subscription, บริบทบนเว็บ, หรือ Claude Code ใน Terminal
- **5 นาที (5 Minutes):** สำหรับการเชื่อมต่อผ่าน API โดยตรง หรือการใช้ Subagents 

*หมายเหตุ: หากคุณทิ้งหน้าต่างแชทไว้นานเกินระยะเวลา TTL นี้ (เช่นไปกินข้าว 2 ชั่วโมง) Cache ใน Session นั้นจะถูกลบ (Un-cached) ทั้งหมด หากคุณทักกลับไปใหม่ ระบบจะต้องทำ Cache Create ข้อมูลทุกอย่างตั้งแต่บรรทัดแรกใหม่ ซึ่งสิ้นเปลืองเป็นอย่างมาก*

## Related
- [[Token Optimization]]
- [[Cache Invalidation]]

## Sources
- [[Give Me 10 Mins and I'll Save You Millions of Claude Tokens]]

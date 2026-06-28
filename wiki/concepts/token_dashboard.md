---
type: concept
aliases: ['Token Dashboard']
tags: [concept]
created: 2026-06-24
sources: ["[[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens|Give Me 10 Mins and I'll Save You Millions of Claude Tokens]]"]
title: "Token Dashboard"
complexity: beginner
domain: "AI Engineering"
updated: 2026-06-28
status: developing
related: ["[[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens|Give Me 10 Mins and I'll Save You Millions of Claude Tokens]]", "[[claude_code|Claude Code]]", "[[claude_prompt_caching|Prompt Caching]]"]
---
# Token Dashboard

## Definition
<!-- สรุปแนวคิดนี้สั้นๆ ห้ามแต่งเติมหรือบิดเบือนความหมายจากต้นฉบับเด็ดขาด -->
Token Dashboard เป็น GitHub Repository ที่เปิดให้ใช้งานฟรีสำหรับติดตามการใช้งาน Token ของ Claude ผ่าน local host โดยแสดงข้อมูลแยกประเภทระหว่าง Cache Read, Cache Create, Input Token และ Output Token เพื่อช่วยให้ผู้ใช้ตรวจสอบและบริหารจัดการการใช้ Token ได้อย่างมีประสิทธิภาพ

## How It Works
<!-- อธิบายกลไกหรือแนวคิดหลัก หากเนื้อหามีความซับซ้อน หรือมีโครงสร้าง/ความสัมพันธ์ที่ย่อยยาก ให้พิจารณาสร้าง Mermaid flowchart, .canvas (json-canvas), หรือ .base (obsidian-bases) แทรกไว้ในหัวข้อนี้ -->
- **การเก็บข้อมูลแบบ Local:** ข้อมูลประวัติและ Token จะถูกแทร็กในเครื่อง (Local device) เท่านั้น ดังนั้นหน้าแดชบอร์ดจะแสดงผลแตกต่างกันหากเปลี่ยนเครื่องใช้งาน
- **การดึงข้อมูลย้อนหลังอัตโนมัติ:** เมื่อเริ่มต้นใช้งาน ระบบจะอ่านไฟล์ประวัติการทำงานเก่าแล้วดึงข้อมูล Token เข้ามาแสดงผลได้ทันที ทำให้เห็นภาพรวมได้โดยไม่ต้องเริ่มเก็บข้อมูลใหม่จากศูนย์
- **การติดตั้งผ่าน Claude Code:** สามารถติดตั้งและใช้งานได้ง่ายเพียงนำลิงก์ GitHub Repo ไปให้ [[claude_code|Claude Code]] แล้วสั่งให้ตั้งค่าและเปิดบน local host

## Connections
<!-- ใส่ลิงก์ไปยัง Concept, Entity หรือ Source ที่เกี่ยวข้อง หากไม่มีให้ลบหัวข้อนี้ทิ้งทั้งหมด อย่าปล่อยหัวข้อเปล่าทิ้งไว้ -->
- [[give_me_10_mins_and_ill_save_you_millions_of_claude_tokens|Give Me 10 Mins and I'll Save You Millions of Claude Tokens]]
- [[claude_code|Claude Code]]
- [[claude_prompt_caching|Prompt Caching]]

## Questions to follow up
- None

---
type: concept
title: "Slicing Work into Issues"
complexity: intermediate
domain: "AI Coding"
aliases: ["Vertical Slices", "Traceable Bullets"]
created: 2026-06-28
updated: 2026-06-28
tags:
  - concept
  - ai-coding
  - workflow
status: seed
related: []
sources: 
  - "[[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]"
---

# Slicing Work into Issues

## Definition
การนำ PRD (Product Requirement Document) หรือเป้าหมายของโปรเจกต์มาแตกย่อยเป็นงานชิ้นเล็กๆ (Issue หรือ Ticket) ในรูปแบบกระดาน Kanban เพื่อกำหนดความสัมพันธ์ของการบล็อกงาน (Blocking relationships) และช่วยให้ AI สามารถทำงานเป็นสัดส่วนได้อย่างมีประสิทธิภาพ

## How It Works
กระบวนการซอยงานที่ดีจะใช้แนวคิดของการสร้าง **"Vertical Slices"** (หรือเรียกว่า Traceable Bullets) แทนการสร้างแบบ **"Horizontal Slices"**
- **Horizontal Slices (สิ่งที่ AI ชอบทำแต่ไม่ดี):** การเขียนโค้ดไปทีละเลเยอร์ เช่น สร้างส่วน Database ของทุกฟีเจอร์ก่อน แล้วค่อยทำ API จากนั้นค่อยทำ Frontend 
- **Vertical Slices (สิ่งที่ควรทำ):** การตัดฟีเจอร์เป็นชิ้นในแนวตั้งให้ครอบคลุมทุกเลเยอร์ของระบบใน Issue เดียว เช่น ในหนึ่ง Issue ควรมีการปรับ Schema, การสร้าง Service, และการมีหน้า UI เบื้องต้นเพื่อแสดงผล

```mermaid
graph TD
    subgraph "Horizontal Slices (Wrong Way)"
        direction TB
        H_UI["Frontend (All Features)"] --- H_API["API (All Features)"] --- H_DB["Database (All Features)"]
    end

    subgraph "Vertical Slices (Right Way)"
        direction LR
        subgraph "Feature 1"
            direction TB
            V1_UI["Frontend"] --- V1_API["API"] --- V1_DB["Database"]
        end
        subgraph "Feature 2"
            direction TB
            V2_UI["Frontend"] --- V2_API["API"] --- V2_DB["Database"]
        end
        subgraph "Feature 3"
            direction TB
            V3_UI["Frontend"] --- V3_API["API"] --- V3_DB["Database"]
        end
    end
```

## Why It Matters
- **ความเร็วในการรับ Feedback:** หากทำงานแบบ Horizontal เราจะไม่สามารถทดสอบระบบรวมจนกว่าการพัฒนาในเลเยอร์สุดท้าย (เช่น Frontend) จะเสร็จสิ้น ในทางกลับกัน Vertical Slices ทำให้ได้ระบบที่ทำงานร่วมกันได้และสามารถทดสอบได้ทันทีตั้งแต่ Issue แรกจบ
- **แก้ปัญหา AI ทำงานแบบไร้ทิศทาง:** การให้ AI เขียนโค้ดแบบทีละเลเยอร์เปรียบเสมือนการยิงปืนในที่มืดโดยไม่เห็นเป้า (Traceable Bullets) การซอยงานแบบ Vertical Slices จะบังคับให้ AI เห็นผลลัพธ์ของสิ่งที่ตัวเองสร้างในทุกๆ การพัฒนา

## Examples
- แทนที่จะแบ่งงานเป็น "สร้าง Database Schema สำหรับ Gamification" (Horizontal) ให้เปลี่ยนเป็นงาน "สร้างฟีเจอร์ Gamification พื้นฐานที่ประกอบด้วย Schema, Service และหน้า UI เบื้องต้น" (Vertical)

## Sources
- [[matt_pocock_ai_workflow_summary|Full Walkthrough Workflow for AI Coding — Matt Pocock]]

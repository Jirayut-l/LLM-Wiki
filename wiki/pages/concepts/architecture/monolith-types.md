---
title: "รูปแบบของ Monolith (Monolith Types)"
tags:
  - monolith
  - architecture
  - foundation
description: "ความหลากหลายของโครงสร้าง Monolith ตั้งแต่ Single-Process ไปจนถึง Modular และ Distributed"
source: "raw/building-microservices-designing-fine-grained-systems.pdf"
date: 2026-05-16
---

# รูปแบบของ Monolith

ในบริบท of Microservices, Monolith มักถูกมองว่าเป็นสิ่งที่ควรหลีกเลี่ยง แต่ Sam Newman ชี้ให้เห็นว่า Monolith มีหลายรูปแบบ และบางรูปแบบก็เป็นทางเลือกที่เหมาะสม

## 1. Single-Process Monolith
เป็นรูปแบบที่พบบ่อยที่สุด โค้ดทั้งหมดของระบบจะถูก Deploy รวมกันเป็น Unit เดียวและรันอยู่ในโปรเซสเดียว
- **ข้อดี:** ง่ายต่อการพัฒนา, ทดสอบ และ Deploy
- **ข้อเสีย:** เมื่อระบบใหญ่ขึ้นจะเกิดปัญหาในการขยาย (Scaling) และการจัดการโค้ดที่ซับซ้อน

## 2. Modular Monolith
โค้ดภายในถูกแบ่งเป็นโมดูลที่มีขอบเขตชัดเจน แต่ยังคงถูก Deploy และรันอยู่ในโปรเซสเดียว
- **ข้อดี:** ช่วยให้ทีมสามารถทำงานแยกกันได้ในระดับหนึ่ง และง่ายต่อการย้ายไปเป็น Microservices ในอดีต
- **ตัวอย่าง:** Shopify ใช้รูปแบบนี้เพื่อจัดการความซับซ้อนโดยไม่ต้องเผชิญกับปัญหาของ Distributed Systems ในช่วงแรก

## 3. Distributed Monolith
ระบบที่ประกอบด้วยบริการขนาดเล็กหลายบริการ แต่บริการเหล่านั้นมีความผูกพันกันสูง (Tightly Coupled) จนต้อง Deploy พร้อมกันเสมอ
- **คำเตือน:** นี่คือรูปแบบที่เป็นอันตรายที่สุด เพราะสูญเสียความง่ายของ Monolith แต่ต้องรับความซับซ้อนของ Distributed Systems มาทั้งหมด

---
> [!tip] คำแนะนำของ Sam Newman
> Monolith ไม่ใช่ "หนี้ทางเทคนิค" (Legacy) เสมอไป แต่มันคือทางเลือกหนึ่งซึ่งเป็น **ค่าเริ่มต้นที่สมเหตุสมผล (Sensible Default)** สำหรับหลายๆ โครงการ

**หน้าที่เกี่ยวข้อง:**
- [[building-microservices-ch1-summary|สรุปบทที่ 1: What Are Microservices?]]
- [[independent-deployability|การ Deploy อย่างอิสระ]]

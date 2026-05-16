---
title: "กฎของคอนเวย์ (Conway's Law)"
tags:
  - organization
  - architecture
  - principles
description: "โครงสร้างระบบที่ออกแบบมักจะสะท้อนถึงโครงสร้างการสื่อสารของทีมในองค์กร"
source: "raw/building-microservices-designing-fine-grained-systems.pdf"
date: 2026-05-16
---

# กฎของคอนเวย์ (Conway's Law)

Melvin Conway ได้กล่าวไว้ในปี 1968 ว่า:
> "องค์กรที่ออกแบบระบบ... จะสร้างงานออกแบบที่มีโครงสร้างเลียนแบบโครงสร้างการสื่อสารขององค์กรนั้นๆ"

## ความหมายในบริบทของ Microservices
หากโครงสร้างทีมของคุณแบ่งตามเทคนิค (เช่น ทีม Frontend, ทีม Backend, ทีม DBA) สถาปัตยกรรมของคุณก็จะมีแนวโน้มเป็นแบบ 3-Tier Architecture ที่ผูกกันแน่น

หากคุณต้องการสถาปัตยกรรมแบบ Microservices ที่ยืดหยุ่น คุณต้องปรับโครงสร้างองค์กรให้เป็น **ทีมที่สอดคล้องกับสายธุรกิจ (Stream-Aligned Teams)** ซึ่งมีคนครบทุกทักษะที่จำเป็นในการส่งมอบงานตั้งแต่ต้นจนจบ

## ผลกระทบ
- **Architecture is a copy of communication:** ถ้าการสื่อสารในองค์กรติดขัด ระบบที่ออกมาก็จะติดขัดและซับซ้อนเกินจำเป็น
- **Inverse Conway Maneuver:** เทคนิคการปรับโครงสร้างทีมให้เป็นแบบที่เราต้องการให้สถาปัตยกรรมระบบเป็น เพื่อกดดันให้ระบบเปลี่ยนไปในทิศทางนั้น

---
**หน้าที่เกี่ยวข้อง:**
- [[building-microservices-ch1-summary|สรุปบทที่ 1: What Are Microservices?]]
- [[independent-deployability|การ Deploy อย่างอิสระ]]

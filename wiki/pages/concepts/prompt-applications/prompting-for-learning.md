---
title: การเขียนพรอมต์เพื่อการเรียนรู้ (Prompting for Learning)
tags:
  - concept
  - use-case
  - learning
source: "wiki/pages/concepts/prompting-for-learning.md"
date: 2026-05-15
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# การเขียนพรอมต์เพื่อการเรียนรู้

เปลี่ยน AI ให้เป็นครูสอนส่วนตัวที่ช่วยให้คุณเข้าใจเรื่องยากๆ ได้เร็วขึ้นและจดจำได้นานขึ้น

## 🎓 เทคนิคการเรียนรู้ด้วย AI

### 1. เทคนิคไฟน์แมน (Feynman Technique)
ขอให้ AI อธิบายเรื่องยากให้ดูง่ายที่สุด
> [!example] ตัวอย่างพรอมต์
> "ช่วยอธิบายทฤษฎีสัมพัทธภาพของไอน์สไตน์ให้เด็กอายุ 5 ขวบฟัง โดยใช้การเปรียบเทียบในชีวิตประจำวัน"

### 2. การสร้างแผนการเรียน (Personalized Study Plan)
ให้ AI ช่วยจัดตารางการเรียนรู้
> [!example] ตัวอย่างพรอมต์
> "ฉันต้องการเรียนรู้วิธีการใช้โปรแกรม Photoshop ภายใน 30 วัน โดยมีเวลาเรียนวันละ 1 ชม. ช่วยสร้างแผนการเรียนรายสัปดาห์ที่เน้นพื้นฐานไปจนถึงขั้นสูง"

### 3. การสร้างแบบทดสอบ (Quizzing & Flashcards)
ทดสอบความรู้ความเข้าใจของตัวเอง
> [!example] ตัวอย่างพรอมต์
> "สร้างแบบทดสอบปรนัย 10 ข้อเกี่ยวกับประวัติศาสตร์ยุคเรเนซองส์ พร้อมเฉลยและคำอธิบายอย่างละเอียด"

### 4. การเปรียบเทียบแนวคิด (Comparative Learning)
เปรียบเทียบสิ่งที่คล้ายคลึงกันเพื่อให้เห็นความต่าง
> [!example] ตัวอย่างพรอมต์
> "ช่วยเปรียบเทียบความแตกต่างระหว่าง 'การเรียนรู้ของเครื่อง' (Machine Learning) และ 'การเรียนรู้เชิงลึก' (Deep Learning) ในรูปแบบตาราง"

### 5. **💡 แนะนำ: Prompt ที่ดีที่สุดเพื่อประสิทธิภาพสูงสุด (Best Performance Prompt)**

```markdown
[บทบาทของ AI]: คุณคือผู้เชี่ยวชาญด้าน...
[เป้าหมายหลัก]: จงอธิบาย/วิเคราะห์...
[รูปแบบผลลัพธ์]: สรุปเป็น Bullet points สั้นกระชับ (หลีกเลี่ยงการใช้น้ำท่วมทุ่ง)
[เงื่อนไขสำคัญ]: 
- หากต้องใช้โค้ด ให้ใช้ภาษามาตรฐานที่นิยมสูง (เช่น JavaScript/TypeScript) แทนภาษาเฉพาะกลุ่ม เพื่อลดจำนวน Token ในการประมวลผล [00:09:37]
- ใช้คำศัพท์ที่ตรงประเด็น ชัดเจน ไม่กำกวม
```

---
> [!tip] เคล็ดลับการเรียนรู้
> ลองใช้พรอมต์: "ฉันเข้าใจหัวข้อ [ชื่อเรื่อง] แบบนี้... [คำอธิบายของคุณ]... ฉันเข้าใจถูกต้องหรือไม่? ช่วยเสริมส่วนที่ขาดตกบกพร่องให้ที"

---
[[prompt-engineering-v7-summary|กลับสู่สรุปเทคนิค]] | [[index|กลับสู่สารบัญ]]

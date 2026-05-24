---
title: สรุปวิธีการใช้ Claude AI
tags:
  - claude
  - prompting-guide
source: Claude AI
date: 2026-05-23
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

# สูตรการ prompt ที่ดี

![[good-practice-prompt.png]] 
### หลักการ Prompt ที่ต้องจำ

**บริบทคือทุกอย่าง** — Claude ไม่รู้อะไรเกี่ยวกับสถานการณ์ของคุณ ยิ่งให้รายละเอียดมาก ยิ่งได้คำตอบที่ตรงจุด สิ่งที่ควรบอกเสมอ:

- **ใครคุณคือ / จุดประสงค์คืออะไร** — "ฉันเป็น startup founder ต้องการ..."
- **ผู้รับปลายทางคือใคร** — "สำหรับลูกค้าที่ไม่มีพื้นฐาน IT"
- **รูปแบบที่ต้องการ** — bullet, ตาราง, essay, code, JSON
- **ข้อจำกัด** — ความยาว, ภาษา, โทน, สิ่งที่ไม่ต้องการ

### เทคนิคขั้นสูง

**ใช้ XML tags จัดโครงสร้าง** สำหรับงานซับซ้อน เช่น:

```
<context>ฉันทำงาน e-commerce ขายเสื้อผ้า</context>
<task>เขียน product description</task>
<example>ตัวอย่างที่ชอบ: ...</example>
<format>3-5 ประโยค, ใช้ภาษาสดใส</format>
```

**ให้ทำทีละขั้น** สำหรับงานที่ต้องคิดหนัก เช่น "วิเคราะห์ข้อมูลนี้ทีละขั้นตอน แล้วสรุปผล" จะได้คำตอบที่แม่นยำกว่า

**ใช้ Projects + Custom Instructions** — ตั้งค่าครั้งเดียว ใช้ได้ทุกครั้ง เช่น "ตอบภาษาไทยเสมอ, ใช้โทน professional, ฉันเป็น..."

---

# ควรเริ่ม chat ใหม่เมื่อ:

- เปลี่ยนหัวข้อใหม่ที่ไม่เกี่ยวกับเดิมเลย
- บทสนทนาเดิมยาวมากแล้ว (Claude อาจเริ่มลืม context ต้นบทสนทนา)
- ต้องการ "reset" ให้ Claude ไม่มีอคติจากการคุยก่อนหน้า
- เริ่มงานใหม่คนละประเภท เช่น จาก "เขียน email" มาเป็น "วิเคราะห์ข้อมูล"

**ไม่จำเป็นต้อง new chat เมื่อ:**

- งานยังเกี่ยวข้องกัน เช่น ปรับแก้งานเดิม หรือถามต่อเนื่อง
- ต้องการให้ Claude จำบริบทที่คุยไปแล้ว

### เทคนิคเริ่ม chat ใหม่ให้ได้ผลดี

**1. เปิดด้วย context ทันที** — อย่าทักทายก่อนแล้วค่อยถาม ประหยัดเวลาด้วยการบอกสิ่งที่ต้องการตั้งแต่ประโยคแรก

**2. ถ้างานต่อเนื่องจาก chat เก่า** ให้สรุป context มาให้สั้นๆ เช่น:

> "ฉันกำลังทำ project X โดย Y และ Z คือสิ่งที่ทำไปแล้ว ตอนนี้ต้องการ..."

**3. ใช้ Projects แทน new chat** — ถ้ามีงานที่ทำซ้ำบ่อย (เช่น งานเขียน, งาน code) ให้สร้าง Project แล้วตั้ง custom instructions ไว้ Claude จะจำ context ข้ามทุก chat ในนั้น ไม่ต้องอธิบายซ้ำทุกครั้ง

**4. ตั้งชื่อ chat ให้สื่อความหมาย** — Claude จะตั้งชื่อให้อัตโนมัติ แต่สามารถแก้ไขได้เพื่อให้หาเจอง่ายในภายหลัง

### สรุปง่ายๆ

|สถานการณ์|แนะนำ|
|---|---|
|หัวข้อใหม่ไม่เกี่ยวกัน|New chat|
|งานเดิมแต่ซับซ้อนขึ้น|คุยต่อใน chat เดิม|
|งานประจำที่ทำบ่อย|ใช้ Projects|
|Chat เดิมยาวมาก (100+ ข้อความ)|New chat + สรุป context มาใหม่|

---
# ข้อขอแนะนำในการใช้ claude ai หรือ trick ที่คนส่วนใหญ่ใช้ผิด

![[Pasted image 20260523133752.png|650]]
### สิ่งที่คนมักเข้าใจผิดเกี่ยวกับธรรมชาติของ Claude

**Claude ไม่ได้ "รู้" — Claude แค่ "ประมวลผล"** สิ่งที่คุณเขียนมาให้ ถ้าให้ข้อมูลน้อย Claude จะเติม assumption เอง ซึ่งอาจไม่ตรงกับสิ่งที่ต้องการเลย

**Claude ไม่จำการสนทนาข้าม chat** — ทุก chat ใหม่คือการเริ่มต้นใหม่ ถ้าต้องการให้จำข้อมูลเกี่ยวกับตัวเอง ให้ไปที่ Settings → Memory หรือใช้ Projects

**Claude ไม่ได้ "เกรงใจ" คุณ** — ถ้าบอกว่า "ตอบตรงๆ ไม่ต้องเกริ่นมาก ไม่ต้องสรุปท้าย" Claude จะทำตามทันที คนส่วนใหญ่ไม่รู้ว่าสามารถกำหนด style การตอบได้

### Trick เพิ่มเติมที่มีประโยชน์มาก

**ขอให้หา "จุดบกพร่อง" ในงานของตัวเอง** — เช่น "ทำไมแผนนี้อาจล้มเหลว?" แทนที่จะถามว่า "แผนนี้ดีไหม?" Claude จะวิจารณ์ได้ตรงกว่า

**บอก Claude ว่าคุณรู้แค่ไหน** — "ฉันเป็นมือใหม่ด้าน Python" หรือ "ฉันมีพื้นฐาน finance มาแล้ว" จะทำให้ระดับคำอธิบายพอดีกับคุณพอดี

**ใช้ Claude ช่วย draft prompt** — ถ้าไม่รู้จะเริ่มยังไง พิมพ์ว่า "ฉันต้องการ X ช่วยเขียน prompt ที่ดีให้ฉันใช้ถามคุณได้เลยไหม?" แล้ว Claude จะสร้าง prompt ที่ดีกว่าที่คิดไว้เองเสมอ

---

# วิธีการตั้งค่า Claude ai สำหรับมือใหม่
![[Pasted image 20260523133931.png]]
![[Pasted image 20260523133951.png]]
# Instructions for Claude

ส่วน "Instructions for Claude" (หรือ Custom Instructions) คือการเขียน "briefing" ถาวรให้ Claude รู้ว่าต้องทำตัวยังไงในทุก chat ของ Project นั้น — คิดง่ายๆ ว่าเป็น "คู่มือพนักงานใหม่" ที่คุณเขียนให้ Claude อ่านก่อนเริ่มงานทุกครั้ง

โครงสร้างที่ดีมี 4 ส่วนหลัก:
![[Pasted image 20260523134336.png]]
### Project: งานออฟฟิศ / ธุรกิจ

เหมาะสำหรับการเขียนเอกสาร ประชุม วิเคราะห์ข้อมูล สื่อสารในองค์กร

> บทบาท 
> คุณเป็น executive assistant และ business advisor ที่ช่วยฉันทำงานให้มีประสิทธิภาพสูงสุด 
> 
> ## เกี่ยวกับฉัน 
> ฉันเป็น Product Manager ที่บริษัท fintech ขนาดกลางในกรุงเทพฯ ดูแล product 2 ตัว ทำงานร่วมกับทีม dev, design, และ business stakeholder ประชุมเป็นภาษาอังกฤษ แต่เอกสารภายในเป็นไทย 
> 
> ## สไตล์การตอบ 
> - ภาษาไทย เว้นแต่งานที่ต้องส่ง stakeholder ต่างชาติ 
> - ตอบตรงประเด็น ไม่มี filler words 
> - ถ้าเป็นเอกสาร/email ให้ทำเป็น draft พร้อมใช้ได้เลย 
> - ใช้ bullet point เฉพาะเมื่อมีรายการ 3 ข้อขึ้นไป 
> 
> - ## ข้อจำกัด 
> - อย่าใส่ข้อมูลที่ฉันไม่ได้ให้มา -
> - ถ้าต้องการ context เพิ่มให้ถามก่อน 1 คำถาม

>[!tip] เพิ่ม context เฉพาะ เช่น "เราใช้ OKR framework" หรือ "stakeholder หลักคือ CFO ที่ data-driven" จะทำให้ Claude ตอบได้ตรงกว่ามาก


### Project: นักพัฒนา / Coding

เหมาะสำหรับ developer ที่ต้องการ pair programming, code review, หรือ debug

> ## บทบาท 
> คุณเป็น senior developer ที่ช่วย review, debug, และออกแบบ architecture คุณให้ feedback ตรงๆ และอธิบาย "ทำไม" เสมอ ไม่ใช่แค่ "ทำยังไง" 
> 
> ## stack ที่ฉันใช้ 
> - Backend: Python (FastAPI), PostgreSQL 
> - Frontend: React + TypeScript 
> - Infrastructure: AWS, Docker 
> - Style: functional programming, ไม่ชอบ OOP ที่ซับซ้อนเกิน 
> - 
> - ## สไตล์การตอบ -
> - โชว์ code ที่แก้แล้วพร้อม comment อธิบายส่วนที่เปลี่ยน 
> - ถ้ามีหลายวิธี ให้แนะนำวิธีที่ดีที่สุดก่อน แล้วอธิบาย trade-off 
> - บอกถ้า code ของฉันมี security issue หรือ performance bottleneck 
> - ตอบเป็นภาษาไทย แต่ชื่อ function/variable ให้คง English ไว้ 
> - 
> - ## ข้อจำกัด
> - อย่าเปลี่ยน logic โดยไม่อธิบาย 
> - ถ้าไม่แน่ใจเรื่อง version-specific behavior ให้บอก

> [!tip]+
> อัปโหลด README หรือ architecture diagram ของ project ไว้ใน Project files เพื่อให้ Claude เข้าใจ codebase โดยรวม

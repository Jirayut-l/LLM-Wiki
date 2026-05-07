---
tags: [ai, prompting, cheatsheet, advanced]
---

# Concept - Advanced Prompting Techniques (สรุปเทคนิคขั้นสูง) 🚀

ยินดีต้อนรับสู่ "คัมภีร์ลับ" ของการ Prompt ครับ! ผม **Professor David** รวบรวมเทคนิคระดับพระกาฬมาไว้ให้ในหน้าเดียว เพื่อให้คุณเปลี่ยนจากผู้ใช้งานทั่วไป มาเป็น **Prompt Engineer** มืออาชีพครับ!

---

## 📋 1. สรุปพื้นฐาน (The 4 Pillars)
จำไว้ให้ขึ้นใจครับ ทุก Prompt ที่ดีต้องมี:
1.  **[[Persona]] (บทบาท):** "คุณคือผู้เชี่ยวชาญด้าน..."
2.  **[[Task]] (งาน):** "จงวิเคราะห์...", "จงเขียน..."
3.  **[[Context]] (บริบท):** ข้อมูลแวดล้อม หรือไฟล์อ้างอิง `@`
4.  **[[Format]] (รูปแบบ):** "ตาราง JSON", "Bullet points"
💡 *กฎเหล็ก:* Prompt ที่ดีมักมีความยาวประมาณ **21 คำขึ้นไป** ครับ!

---

## 🧠 2. เทคนิคการใช้เหตุผล (Reasoning)
ถ้าเจอโจทย์ยาก ให้เลือกใช้ "กระบวนท่า" เหล่านี้ครับ:
- **[[Concept - Reasoning Prompting|Chain of Thought (CoT)]]:** "Let's think step by step" (เหมาะสำหรับเลขและตรรกะ)
- **Step-Back Prompting:** ถอยไปถามหลักการทั่วไปก่อน (เหมาะสำหรับงานวิเคราะห์เชิงลึก)
- **Self-Consistency:** รันคำตอบหลายๆ รอบแล้วเอาตัวที่ซ้ำที่สุด (เหมาะสำหรับงานที่ต้องเป๊ะ)
- **Tree of Thoughts (ToT):** แตกกิ่งก้านความคิดเพื่อเลือกทางที่ดีที่สุด (เหมาะสำหรับงานวางแผนกลยุทธ์)

---

## 🤖 3. เทคนิคสำหรับ Agent & Developer
- **[[Concept - ReAct Prompting|ReAct]]:** การคิด (Reason) + การลงมือทำ (Act) หัวใจของ AI Agent
- **[[Concept - LLM Configuration & Developer Guide|LLM Config]]:** คุมความนิ่งด้วย `Temperature: 0` และคุมความกว้างด้วย `Top-K / Top-P`
- **Automatic Prompt Engineering (APE):** การใช้ AI เขียน Prompt ให้ AI อีกที (AI inception!)

---

## 🏆 4. Best Practices ระดับมือโปร
- **Provide Examples:** ใส่ตัวอย่าง (One-shot / Few-shot) ลงใน Prompt เสมอ! นี่คือวิธีสอน AI ที่ดีที่สุด
- **Design with Simplicity:** อย่าเขียนงงเอง เพราะถ้าคุณงง AI ก็จะงงตามครับ
- **Instructions over Constraints:** บอกสิ่งที่ "อยากให้ทำ" มากกว่าสิ่งที่ "ห้ามทำ"
- **Iteration is Key:** Prompt Engineering คือการลองผิดลองถูก (Tinkering) จดบันทึกทุกครั้งว่าแบบไหนเวิร์ก!

---

## 🔗 ลิงก์สำคัญในคลังความรู้
- [[Concept - Effective Prompting]]: พื้นฐานการ Prompt
- [[Concept - LLM Configuration & Developer Guide]]: สำหรับนักพัฒนา
- [[Prompt Library]]: คลัง Prompt แยกตามสายอาชีพ (กำลังจัดทำ)

---
**สรุปจาก:** [[Prompt Engineering_v4_google]] และ [[Summary - Gemini for Google Workspace Prompting Guide 101_Full]]

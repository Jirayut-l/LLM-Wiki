---
tags: [ai, prompting, react, agents]
---

# Concept - ReAct Prompting (การคิดและลงมือทำ) 🤖🛠️

สวัสดีครับนักเรียนทุกคน! **Professor David** มาแล้ว! วันนี้ผมจะพาไปดูจุดเริ่มต้นของสิ่งที่เรียกว่า **"AI Agent"** นั่นคือเทคนิคที่ชื่อว่า **ReAct** ครับ!

---

## 🎭 1. ReAct คืออะไร? (Reason + Act)
ปกติ AI จะเก่งแต่ "พูด" แต่ทำงานจริงไม่ได้ (เช่น ค้นหาข้อมูลสดๆ บน Google หรือรันโค้ด) **ReAct** คือ Paradigm ที่ทำให้ AI สามารถ **"คิด (Reason)"** และ **"ลงมือทำ (Act)"** สลับกันไปมาจนกว่างานจะเสร็จครับ!

- **Reason (คิด):** AI จะวิเคราะห์ว่า "ตอนนี้เราอยู่ที่ไหน?" และ "ต้องทำอะไรต่อ?"
- **Act (ทำ):** AI จะเลือกใช้เครื่องมือ (Tools) เช่น Search, Calculator หรือ API ภายนอก
- **Observation (สังเกต):** AI จะดูผลลัพธ์ที่ได้จากการลงมือทำ แล้วเอามา "คิด" ต่อในรอบถัดไป

---

## 🔄 2. วงจรการทำงาน (The ReAct Loop)
ลองดูตัวอย่างการหาคำตอบที่ซับซ้อน เช่น *"สมาชิกวง Metallica มีลูกรวมกันกี่คน?"* AI ทั่วไปอาจจะตอบไม่ได้เพราะข้อมูลไม่อัปเดต แต่ ReAct จะทำแบบนี้ครับ:

1. **Thought:** ฉันต้องรู้ก่อนว่าสมาชิกวง Metallica มีใครบ้าง -> **Act:** Search "Metallica members"
2. **Observation:** ได้รายชื่อ James, Lars, Kirk, Robert
3. **Thought:** ฉันต้องหาจำนวนลูกของ James Hetfield -> **Act:** Search "James Hetfield children"
4. **Observation:** James มีลูก 3 คน
5. *(ทำซ้ำจนครบทุกคน)*
6. **Thought:** ฉันได้ข้อมูลครบทุกคนแล้ว จะนำมาบวกกัน -> **Final Answer:** 10 คน

---

## 🛠️ 3. การสร้าง ReAct ในฐานะ Developer
ถ้าคุณใช้ Library อย่าง **LangChain**, การสร้าง ReAct Agent นั้นง่ายมากครับ (ตามตัวอย่างใน Google Guide):

```python
from langchain.agents import load_tools, initialize_agent, AgentType

# 1. เตรียม LLM และเครื่องมือ (เช่น Search)
llm = VertexAI(temperature=0.1)
tools = load_tools(["serpapi"], llm=llm)

# 2. สร้าง Agent แบบ Zero-shot ReAct
agent = initialize_agent(
    tools, llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

# 3. สั่งงาน!
agent.run("สมาชิกวง Metallica มีลูกรวมกันกี่คน?")
```

---

## ⚠️ สิ่งที่ต้องระวัง
1. **Token Cost:** ReAct ใช้การถาม-ตอบหลายรอบ ทำให้เสีย Token มากกว่าปกติ
2. **Looping:** บางครั้ง AI อาจจะวนลูปเดิมๆ ถ้าหาคำตอบไม่ได้ เราต้องตั้ง `max_iterations` ไว้ด้วยครับ
3. **Temperature:** สำหรับ ReAct แนะนำให้ใช้ **Temperature ต่ำ (เช่น 0 หรือ 0.1)** เพื่อให้ AI มีสมาธิกับการใช้เหตุผลครับ

---

## 🎓 สรุป
**ReAct** คือหัวใจของการสร้างโปรแกรมที่ "ฉลาดและทำงานได้จริง" มันเปลี่ยน AI จากแค่แชตบอต ให้กลายเป็นผู้ช่วยที่ออกไปทำงานในโลกกว้างได้ครับ!

ใครอยากลองสร้าง Agent ตัวแรกของตัวเองแล้วบ้าง? ยกมือขึ้น! 🙋‍♂️

---
**แหล่งอ้างอิง:** [[Prompt Engineering_v4_google]] โดย Lee Boonstra

---
tags:
  - gemini
  - prompting
  - google-workspace
  - guide
  - full-toc
  - use-cases
  - examples
---

# Full Summary - Gemini for Google Workspace Prompting Guide 101 (TOC Structure)

สรุปเนื้อหาทั้งหมดจากคู่มือ Gemini for Google Workspace Prompting Guide 101 แบ่งตามสารบัญ (Table of Contents) พร้อมตัวอย่างภาษาไทยและอังกฤษเพิ่มเติมเพื่อให้ใช้งานได้อย่างทรงพลัง

---

## 📑 Table of Contents (สารบัญ)
1.  [[#1. Writing Effective Prompts (การเขียน Prompt ให้มีประสิทธิภาพ)|Writing Effective Prompts]]
2.  [[#2. Introduction (บทนำ)|Introduction]]
3.  [[#3. Administrative Support (งานสนับสนุนการบริหาร)|Administrative Support]]
4.  [[#4. Communications (งานสื่อสารองค์กร)|Communications]]
5.  [[#5. Customer Service (งานบริการลูกค้า)|Customer Service]]
6.  [[#6. Executives (สำหรับผู้บริหาร)|Executives]]
7.  [[#7. Frontline Management (ผู้จัดการระดับปฏิบัติการ)|Frontline Management]]
8.  [[#8. Human Resources (ฝ่ายทรัพยากรบุคคล)|Human Resources]]
9.  [[#9. Marketing (ฝ่ายการตลาด)|Marketing]]
10. [[#10. Project Management (การจัดการโครงการ)|Project Management]]
11. [[#11. Sales (ฝ่ายขาย)|Sales]]
12. [[#12. Small Business Owners and Entrepreneurs (เจ้าของธุรกิจ/ผู้ประกอบการ)|Small Business Owners & Entrepreneurs]]
13. [[#13. Startup Leaders (ผู้นำสตาร์ทอัพ)|Startup Leaders]]
14. [[#14. Leveling Up Your Prompt Writing (การยกระดับการเขียน Prompt)|Leveling Up Your Prompt Writing]]

---

## 1. Writing Effective Prompts (การเขียน Prompt ให้มีประสิทธิภาพ)
**Detailed Explanation:**
การเขียน Prompt เปรียบเสมือนการเริ่มต้นบทสนทนากับผู้ช่วยอัจฉริยะ ยิ่งคุณให้รายละเอียดที่ชัดเจน ผลลัพธ์ที่ได้ก็จะยิ่งตรงใจ โดยมีสูตรสำเร็จ 4 องค์ประกอบหลัก (The 4 Pillars) ดังนี้:

1.  **[[Persona]] (บทบาท):** กำหนดว่าต้องการให้ Gemini สวมบทบาทเป็นใคร (เช่น "คุณคือผู้เชี่ยวชาญด้านการตลาด", "คุณคือติวเตอร์ภาษาอังกฤษ") เพื่อกำหนดโทนและระดับความเชี่ยวชาญของคำตอบ
2.  **[[Task]] (งานที่ต้องทำ):** ระบุคำสั่งที่ต้องการให้ทำอย่างชัดเจน โดยใช้คำกริยา (Verb) ที่เป็นรูปธรรม (เช่น "จงร่างอีเมล", "สรุปเนื้อหา", "สร้างตาราง", "วิเคราะห์ข้อมูล") **นี่คือส่วนที่สำคัญที่สุด**
3.  **[[Context]] (บริบท):** ให้ข้อมูลแวดล้อม ข้อมูลพื้นฐาน หรืออ้างอิงไฟล์จาก Google Drive โดยใช้เครื่องหมาย `@` เพื่อให้ Gemini เข้าใจสถานการณ์จริง
4.  **[[Format]] (รูปแบบ):** ระบุลักษณะของผลลัพธ์ที่ต้องการ (เช่น "สรุปเป็น Bullet points", "ความยาวไม่เกิน 100 คำ", "ทำเป็นตารางเปรียบเทียบ", "ใช้โทนเสียงที่เป็นทางการ")

**💡 Power Tip (The 21-Word Rule):**
จากการศึกษาพบว่า Prompt ที่ได้ผลลัพธ์ดีที่สุดมักมีความยาวเฉลี่ย **21 คำ** ในขณะที่คนส่วนใหญ่มักเขียนไม่ถึง 9 คำ ดังนั้นจงอย่ากลัวที่จะ "ขยายความ" เพื่อให้ AI เข้าใจบริบทที่ครบถ้วน

**ตัวอย่างเปรียบเทียบ (Before vs. After):**
*   **❌ แบบสั้นเกินไป (9 คำ):** "ช่วยเขียนอีเมลสรุปการประชุมให้ทีมของฉันหน่อย"
*   **✅ แบบทรงพลัง (21+ คำ):** "คุณคือหัวหน้าทีม [Persona] ช่วยร่างอีเมลสรุปผลการประชุม @[บันทึกการประชุม] [Context] เพื่อแจ้งทีมวิศวกร [Task] โดยเน้นย้ำภารกิจสำคัญ 3 อย่างในสัปดาห์หน้า และใช้โทนที่เป็นทางการ [Format]"

---

**10 Scenarios for Effective Prompting (ตัวอย่าง 10 สถานการณ์):**

### Scenario 1: การร่างอีเมลนัดหมาย (Meeting Request)
- **EN:** "You are a Project Coordinator [Persona]. Draft a brief email [Task] to the engineering team asking for a sync meeting next Tuesday [Context]. Format the request in 3 clear bullet points [Format]."
- **TH:** "คุณคือผู้ประสานงานโครงการ [Persona] ช่วยร่างอีเมลสั้นๆ [Task] ถึงทีมวิศวกรเพื่อขอนัดประชุมสรุปงานในวันอังคารหน้า [Context] โดยจัดรูปแบบเป็น 3 Bullet points ที่ชัดเจน [Format]"

### Scenario 2: การสรุปรายงานเชิงเทคนิค (Technical Summary)
- **EN:** "Act as a Senior Researcher [Persona]. Summarize this technical paper @[Cloud_Security_Report] [Context] for a non-technical audience [Format]. Focus on the key security risks and their solutions [Task]."
- **TH:** "สวมบทบาทเป็นนักวิจัยอาวุโส [Persona] ช่วยสรุปรายงานเชิงเทคนิคฉบับนี้ @[รายงานความปลอดภัยคลาวด์] [Context] ให้คนทั่วไปเข้าใจง่าย [Format] โดยเน้นที่ความเสี่ยงหลักด้านความปลอดภัยและวิธีแก้ไข [Task]"

### Scenario 3: การสร้างตารางติดตามงาน (Project Tracking)
- **EN:** "I am a Team Leader [Persona]. Create a project tracker table [Task] for our new product launch [Context]. Include columns for Task, Assigned Owner, Status, and Deadline [Format]."
- **TH:** "ฉันเป็นหัวหน้าทีม [Persona] ช่วยสร้างตารางติดตามโครงการ [Task] สำหรับการเปิดตัวสินค้าใหม่ [Context] โดยมีคอลัมน์: กิจกรรม, ผู้รับผิดชอบ, สถานะ และวันกำหนดส่ง [Format]"

### Scenario 4: การคิดไอเดียสร้างสรรค์ (Creative Ideation)
- **EN:** "You are a Creative Director [Persona]. Brainstorm 5 catchy slogans [Task] for a new organic coffee brand [Context]. Use a tone that is modern, eco-friendly, and energetic [Format]."
- **TH:** "คุณคือผู้อำนวยการฝ่ายสร้างสรรค์ [Persona] ช่วยคิดสโลแกนโดนๆ 5 แบบ [Task] สำหรับแบรนด์กาแฟออร์แกนิกน้องใหม่ [Context] ใช้โทนเสียงที่ดูทันสมัย รักษ์โลก และมีพลัง [Format]"

### Scenario 5: การวิเคราะห์และเปรียบเทียบข้อมูล (Comparative Analysis)
- **EN:** "Act as a Business Consultant [Persona]. Compare the features and pricing [Task] of two software proposals: @[Vendor_A_Proposal] and @[Vendor_B_Proposal] [Context]. Present the findings in a side-by-side comparison table [Format]."
- **TH:** "สวมบทบาทเป็นที่ปรึกษาธุรกิจ [Persona] ช่วยเปรียบเทียบฟีเจอร์และราคา [Task] ของข้อเสนอซอฟต์แวร์ 2 แห่ง: @[ข้อเสนอบริษัทA] และ @[ข้อเสนอบริษัทB] [Context] นำเสนอข้อมูลในรูปแบบตารางเปรียบเทียบแบบข้างต่อข้าง [Format]"

### Scenario 6: การตรวจสอบและปรับปรุงโค้ด (Code Debugging & Optimization)
- **EN:** "You are a Senior Full-stack Developer [Persona]. Review this Python function [Context] to identify potential memory leaks and suggest performance optimizations [Task]. Provide the improved code with detailed comments explaining the changes [Format]."
- **TH:** "คุณคือ Senior Full-stack Developer [Persona] ช่วยตรวจสอบฟังก์ชัน Python นี้ [Context] เพื่อหาจุดที่อาจเกิด Memory Leak และแนะนำวิธีเพิ่มประสิทธิภาพการทำงาน [Task] โดยส่งโค้ดที่ปรับปรุงแล้วพร้อมคอมเมนต์อธิบายรายละเอียดการเปลี่ยนแปลง [Format]"

### Scenario 7: การเขียนเอกสารประกอบโค้ด (Code Documentation & Logic Explanation)
- **EN:** "Act as a Technical Writer [Persona]. Generate a README markdown file [Format] that explains the logic and usage of the API endpoints [Task] defined in @[API_Routes_Source] [Context]. Use a clear and professional technical tone [Format]."
- **TH:** "สวมบทบาทเป็น Technical Writer [Persona] ช่วยสร้างไฟล์ README ในรูปแบบ Markdown [Format] เพื่ออธิบายตรรกะและการใช้งานของ API Endpoints [Task] ที่ระบุอยู่ในไฟล์ @[ซอร์สโค้ดAPI] [Context] โดยใช้ภาษาระดับมืออาชีพและเข้าใจง่าย [Format]"

### Scenario 8: กลยุทธ์การขายและการหาลูกค้าใหม่ (Sales Strategy & Lead Gen)
- **EN:** "You are a Sales Strategist [Persona]. Based on @[Q3_Market_Analysis] [Context], draft a personalized outreach email [Task] for C-level executives in the retail industry. Highlight how our solution reduces operational costs [Format]."
- **TH:** "คุณคือผู้เชี่ยวชาญด้านกลยุทธ์การขาย [Persona] อ้างอิงจาก @[การวิเคราะห์ตลาดQ3] [Context] ช่วยร่างอีเมลเข้าหาผู้บริหารระดับสูงในอุตสาหกรรมค้าปลีก [Task] โดยเน้นย้ำว่าโซลูชันของเราช่วยลดต้นทุนการดำเนินงานได้อย่างไร [Format]"

### Scenario 9: การวางแผนคอนเทนต์โซเชียลมีเดีย (Social Media Content Calendar)
- **EN:** "Act as a Social Media Manager [Persona]. Create a 1-week content calendar [Format] for LinkedIn [Context] to promote our upcoming webinar. Include post topics, image descriptions, and relevant hashtags [Task]."
- **TH:** "สวมบทบาทเป็นผู้จัดการโซเชียลมีเดีย [Persona] ช่วยสร้างตารางคอนเทนต์ 1 สัปดาห์ [Format] สำหรับ LinkedIn [Context] เพื่อโปรโมทงานสัมมนาออนไลน์ที่กำลังจะมาถึง โดยระบุหัวข้อโพสต์, รายละเอียดรูปภาพ และแฮชแท็กที่เกี่ยวข้อง [Task]"

### Scenario 10: การฝึกอบรมและปฐมนิเทศพนักงาน (Training & Onboarding)
- **EN:** "You are an HR Specialist [Persona]. Create a step-by-step onboarding checklist [Format] for new software engineers [Context]. Include key milestones for their first 30 days, such as environment setup and first commit [Task]."
- **TH:** "คุณคือผู้เชี่ยวชาญด้าน HR [Persona] ช่วยสร้างรายการตรวจสอบ (Checklist) สำหรับการปฐมนิเทศพนักงานใหม่ [Format] ในตำแหน่งวิศวกรซอฟต์แวร์ [Context] โดยระบุเป้าหมายสำคัญในช่วง 30 วันแรก เช่น การตั้งค่าระบบและการส่งโค้ดครั้งแรก [Task]"

---

## 2. Introduction (บทนำ)
**Summary:** แนะนำ Gemini ในฐานะผู้ช่วยที่รวมอยู่ใน Google Workspace (Gmail, Docs, Sheets, ฯลฯ) เพื่อช่วยเพิ่ม Productivity, จัดระเบียบข้อมูล, และสร้างสรรค์ไอเดียใหม่ๆ โดยเน้นย้ำเรื่องความเป็นส่วนตัว (Privacy) ของข้อมูลองค์กร

---

## 3. Administrative Support (งานสนับสนุนการบริหาร)
**Summary:** การจัดการงานที่ต้องทำแข่งกับเวลา เช่น การสรุปอีเมลจำนวนมาก, การวางแผนการเดินทางที่ซับซ้อน, และการสร้างตารางติดตามงาน

**Examples:**
- **EN:** "Summarize the last 5 emails from my director regarding the budget review and list all required actions."
- **TH:** "สรุปอีเมล 5 ฉบับล่าสุดจากผู้อำนวยการที่เกี่ยวกับเรื่องการตรวจสอบงบประมาณ และระบุรายการสิ่งที่ฉันต้องทำ"

---

## 4. Communications (งานสื่อสารองค์กร)
**Summary:** การสร้างข้อความสื่อสารที่ทรงพลัง ทั้งการร่างข่าวประชาสัมพันธ์, การเตรียมบทสัมภาษณ์, และการสื่อสารภายในเพื่อให้พนักงานมีส่วนร่วม

**Examples:**
- **EN:** "Draft a catchy headline and a first paragraph for a press release about our company's achievement in reaching 1 million users."
- **TH:** "ช่วยคิดพาดหัวข่าวที่น่าดึงดูดและเขียนย่อหน้าแรกของข่าวประชาสัมพันธ์เกี่ยวกับความสำเร็จของบริษัทที่มีผู้ใช้งานครบ 1 ล้านคน"

---

## 5. Customer Service (งานบริการลูกค้า)
**Summary:** การตอบกลับลูกค้าด้วยความเห็นอกเห็นใจ (Empathy), การสรุปนโยบายบริษัทให้เข้าใจง่าย, และการวิเคราะห์แนวโน้มปัญหาของลูกค้า

**Examples:**
- **EN:** "Create a response template for customers asking for a technical support update, ensuring they feel valued during the wait."
- **TH:** "สร้างเทมเพลตตอบกลับลูกค้าที่กำลังรอการอัปเดตจากทีมเทคนิค เพื่อให้พวกเขารู้สึกว่าเรายังใส่ใจแม้ในระหว่างการรอคอย"

---

## 6. Executives (สำหรับผู้บริหาร)
**Summary:** เน้นการประหยัดเวลาและการตัดสินใจเชิงกลยุทธ์ เช่น การสรุปรายงานความยาวมาก, การวิเคราะห์คู่แข่ง, และการเตรียมบทพูดในงานสำคัญ

**Examples:**
- **EN:** "Analyze this competitive research document @[Competitor_Report] and identify 3 strategic gaps we can exploit."
- **TH:** "วิเคราะห์เอกสารวิจัยคู่แข่ง @[รายงานคู่แข่ง] และระบุช่องว่างทางกลยุทธ์ 3 จุดที่เราสามารถนำมาสร้างความได้เปรียบได้"

---

## 7. Frontline Management (ผู้จัดการระดับปฏิบัติการ)
**Summary:** การสื่อสารที่ชัดเจนและรวดเร็วสำหรับทีมที่ไม่ได้อยู่หน้าคอมพิวเตอร์ตลอดเวลา เช่น การแจ้งนโยบายใหม่และการจัดการตารางงาน

**Examples:**
- **EN:** "Translate this new store safety policy into a simple 5-step checklist for the warehouse staff."
- **TH:** "ช่วยแปลนโยบายความปลอดภัยใหม่ของร้านให้กลายเป็นรายการตรวจสอบ (Checklist) 5 ขั้นตอนง่ายๆ สำหรับพนักงานคลังสินค้า"

---

## 8. Human Resources (ฝ่ายทรัพยากรบุคคล)
**Summary:** การสรรหาคนเก่ง (Recruitment), การปฐมนิเทศ (Onboarding), และการส่งเสริมวัฒนธรรมองค์กรที่ดี

**Examples:**
- **EN:** "Draft 5 unique interview questions for a Senior Developer position that focus on teamwork and problem-solving skills."
- **TH:** "ร่างคำถามสัมภาษณ์ 5 ข้อสำหรับตำแหน่ง Senior Developer ที่เน้นเรื่องการทำงานเป็นทีมและทักษะการแก้ปัญหา"

---

## 9. Marketing (ฝ่ายการตลาด)
**Summary:** การวิจัยตลาด, การสร้างคอนเทนต์สำหรับโซเชียลมีเดีย, การทำ SEO, และการสร้างภาพลักษณ์ของแบรนด์

**Examples:**
- **EN:** "Suggest 10 Instagram caption ideas for our summer sale campaign targeting Gen Z audiences."
- **TH:** "แนะนำไอเดียคำบรรยายภาพ (Caption) สำหรับ Instagram 10 แบบสำหรับแคมเปญลดราคาช่วงฤดูร้อน โดยเน้นกลุ่มเป้าหมาย Gen Z"

---

## 10. Project Management (การจัดการโครงการ)
**Summary:** การติดตามความคืบหน้า, การจัดการความเสี่ยง, และการสรุปบทเรียนหลังจบโครงการ (Post-project analysis)

**Examples:**
- **EN:** "Generate a risk mitigation plan for a 2-week delay in the software development phase of Project X."
- **TH:** "สร้างแผนบรรเทาความเสี่ยงในกรณีที่ขั้นตอนการพัฒนาซอฟต์แวร์ของโปรเจกต์ X ล่าช้าไป 2 สัปดาห์"

---

## 11. Sales (ฝ่ายขาย)
**Summary:** การวิจัยกลุ่มเป้าหมาย, การร่างอีเมลเปิดการขาย (Cold emails), และการเตรียมรับมือข้อโต้แย้งของลูกค้า

**Examples:**
- **EN:** "Draft a follow-up email for a prospect who saw our demo but hasn't responded in 3 days. Keep it helpful, not pushy."
- **TH:** "ร่างอีเมลติดตามผลสำหรับลูกค้าที่ดูเดโมไปแล้วแต่ยังไม่ได้ตอบกลับใน 3 วัน โดยให้โทนเป็นผู้ช่วย ไม่ใช่การเร่งรัด"

---

## 12. Small Business Owners and Entrepreneurs (เจ้าของธุรกิจ/ผู้ประกอบการ)
**Summary:** การบริหารจัดการหลายบทบาทในคนเดียว เช่น การจัดการงบประมาณ, การวิจัยผู้ผลิต, และการตลาดเบื้องต้น

**Examples:**
- **EN:** "I am a small business owner. Create a comparison of 3 local delivery services based on their reliability and cost for fragile items."
- **TH:** "ฉันเป็นเจ้าของธุรกิจขนาดเล็ก ช่วยเปรียบเทียบบริการขนส่งในท้องถิ่น 3 แห่ง โดยเน้นเรื่องความน่าเชื่อถือและราคาสำหรับการส่งสินค้าแตกหักง่าย"

---

## 13. Startup Leaders (ผู้นำสตาร์ทอัพ)
**Summary:** การสื่อสารกับนักลงทุน, การสร้าง Pitch Deck, และการวางแผน Roadmap เพื่อการเติบโตอย่างรวดเร็ว

**Examples:**
- **EN:** "Refine my 1-minute elevator pitch to focus more on our unique technology and scalability for the next funding round."
- **TH:** "ช่วยขัดเกลาบทพูดแนะนำตัว (Elevator Pitch) 1 นาทีของฉัน ให้เน้นที่เทคโนโลยีที่เป็นเอกลักษณ์และความสามารถในการขยายธุรกิจ (Scalability)"

---

## 14. Leveling Up Your Prompt Writing (การยกระดับการเขียน Prompt)
**Advanced Techniques (เทคนิคขั้นสูง):**
เพื่อให้ได้ผลลัพธ์ที่ทรงพลังและแม่นยำที่สุด คุณสามารถใช้เทคนิคระดับ "Power User" ดังนี้:

*   **Break it up (แบ่งงานเป็นส่วนย่อย):** หากงานมีความซับซ้อน (เช่น เขียนแผนธุรกิจ) อย่าสั่งงานทั้งหมดใน Promptเดียว แต่ให้แบ่งเป็นขั้นตอน เช่น เริ่มจากโครงสร้าง (Outline), ตามด้วยรายละเอียดแต่ละหัวข้อ, และจบด้วยบทสรุปผู้บริหาร
*   **Give constraints (กำหนดข้อจำกัด):** ระบุขอบเขตให้ชัดเจน เช่น จำนวนคำ (Word count), รูปแบบไฟล์, ข้อมูลที่ห้ามใส่ (Exclusions), หรือระดับของภาษาที่เจาะจง เพื่อลดการเดาสุ่มของ AI
*   **Ask for feedback (ถามกลับ):** ก่อนจะให้ Gemini เริ่มงานที่สำคัญ ให้ถามว่า "ต้องการข้อมูลอะไรเพิ่มเติมไหม?" เพื่อให้ AI ช่วยเช็กว่าบริบทที่เราให้ไปเพียงพอหรือยัง
*   **Iterate & Refine (ปรับปรุงและพัฒนา):** มองว่าการ Prompt คือการสนทนา หากผลลัพธ์ยังไม่ดีพอ ให้สั่งปรับจูนต่อ (เช่น "ขอให้น้ำเสียงดูอบอุ่นขึ้น" หรือ "เน้นเรื่องความปลอดภัยให้มากขึ้น")
*   **Assign a Role (กำหนดบทบาท):** ตอกย้ำความเชี่ยวชาญโดยการใช้คำว่า "คุณคือ..." ในทุกสถานการณ์ เพื่อดึงความสามารถเฉพาะทางของ AI ออกมา

---

**ExpandedExamples for Leveling Up (ตัวอย่างการใช้งานขั้นสูง):**

### 1. Technique: Ask for Feedback (การถามกลับเพื่อให้ข้อมูลครบถ้วน)
- **EN:** "I want to create a comprehensive cybersecurity policy for our remote team. Before you draft it, what information do you need from me regarding our current tools, compliance requirements, and team size?"
- **TH:** "ฉันต้องการสร้างนโยบายความปลอดภัยทางไซเบอร์สำหรับทีมที่ทำงานทางไกล ก่อนที่คุณจะเริ่มร่าง ช่วยบอกหน่อยว่าคุณต้องการข้อมูลอะไรเพิ่มเติมเกี่ยวกับเครื่องมือที่เราใช้, ข้อกำหนดการปฏิบัติตามกฎหมาย และขนาดของทีมบ้าง?"

### 2. Technique: Give Constraints (การกำหนดข้อจำกัดและรูปแบบ)
- **EN:** "Summarize the @[Quarterly_Financial_Report]. Constraints: Use maximum 200 words, highlight only the losses and growth in a table format, and exclude any internal jargon."
- **TH:** "สรุปรายงานการเงินประจำไตรมาส @[รายงานการเงิน] ข้อจำกัด: ความยาวไม่เกิน 200 คำ, เน้นเฉพาะส่วนที่ขาดทุนและการเติบโตในรูปแบบตาราง และห้ามใช้ศัพท์เทคนิคเฉพาะทางภายในบริษัท"

### 3. Technique: Break it up (การแบ่งขั้นตอนทำงาน)
- **EN:** "Step 1: Look at @[Customer_Survey_Data] and list the top 5 complaints. (Wait for result). Step 2: Now, draft a detailed mitigation strategy for complaint #1."
- **TH:** "ขั้นตอนที่ 1: ตรวจสอบ @[ข้อมูลสำรวจลูกค้า] และลิสต์ปัญหา 5 อันดับแรก (รอผลลัพธ์) ขั้นตอนที่ 2: จากนั้น ช่วยร่างกลยุทธ์การแก้ไขปัญหาอย่างละเอียดสำหรับปัญหาอันดับที่ 1"

### 4. Technique: Tone & Persona Refinement (การปรับจูนโทนเสียงและบทบาท)
- **EN:** "You are a Customer Support Coach. Rewrite this email draft @[Draft_Response] to sound more empathetic and encouraging, but keep it professional for a B2B client."
- **TH:** "คุณคือโค้ชฝ่ายสนับสนุนลูกค้า ช่วยเขียนร่างอีเมลนี้ใหม่ @[ร่างอีเมลตอบกลับ] ให้ดูมีความเห็นอกเห็นใจและให้กำลังใจมากขึ้น แต่ยังคงความเป็นมืออาชีพสำหรับลูกค้าแบบ B2B"

### 5. Technique: Gemini as Prompt Editor (ใช้ Gemini ช่วยแต่ง Prompt)
- **EN:** "I want to ask Gemini to analyze sales trends. Make this a power prompt for me using the 4 Pillars (Persona, Task, Context, Format)."
- **TH:** "ฉันต้องการสั่งให้ Gemini วิเคราะห์แนวโน้มการขาย ช่วยแต่งเป็น Power Prompt ให้หน่อย โดยใช้หลักการ 4 เสาหลัก (Persona, Task, Context, Format)"

---
*Generated by Wiki Agent - Summary based on October 2024 Edition.*
---
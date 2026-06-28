---
type: source
aliases: []
tags: [source]
created: 2026-06-27
url: ""
file_path: ""
author: ""
---
# Give Me 10 Mins and I'll Save You Millions of Claude Tokens

## Summary
วิดีโอจาก Nate Herk อธิบายเกี่ยวกับการทำงานของ Prompt Caching ใน Claude Code เพื่อช่วยประหยัดจำนวน Token ที่ใช้ไปอย่างมหาศาล โดยเน้นที่การทำความเข้าใจค่าใช้จ่ายจริงของ Cache, พฤติกรรมที่ควรทำเพื่อหลีกเลี่ยงการใช้ Token สิ้นเปลือง, และสิ่งใดบ้างที่ทำให้ Cache ถูกลบ (Break cache) พร้อมแจก Token Dashboard ฟรี

## Key Takeaways
- Cached tokens มีราคาเพียง 10% ของ Input ปกติ ช่วยประหยัดค่าใช้จ่ายได้มาก
- Cache TTL (Time-to-Live) สำหรับ Claude subscriptions คือ 1 ชั่วโมง แต่ถ้าใช้ผ่าน API หรือ Subagents จะเหลือเพียง 5 นาที
- 3 พฤติกรรมเพื่อช่วยประหยัด Token: (1) อย่าปล่อย Session ไว้นานเกินไป (2) เริ่ม Session ใหม่เมื่อเปลี่ยนงานโดยใช้คำสั่ง /compact, /clear, หรือ Session Handoff (3) ใส่ไฟล์ยาวๆ ลงใน Project แทนการวางลงแชทตรงๆ
- สิ่งที่ทำให้ Cache หาย (Break cache): การเปลี่ยน Model กลางคัน (เช่น การใช้ Opus สำหรับ Plan และ Sonnet สำหรับ Execute) จะทำให้เปลี่ยน Prefix และต้องสร้าง Cache ใหม่อีกครั้ง

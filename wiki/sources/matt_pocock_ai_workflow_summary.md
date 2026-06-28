---
type: source
aliases: []
tags: [source]
created: 2026-06-28
url: "https://www.youtube.com/watch?v=-QFHIoCo-Ko&t=278s"
file_path: "/Users/spectrum/Resources/LLM-Wiki/raw/Full Walkthrough Workflow for AI Coding — Matt Pocock.md"
author: "[[ai_engineer|AI Engineer]]"
---
# Full Walkthrough Workflow for AI Coding — Matt Pocock

## Summary
ภาพรวมของเวิร์กชอปที่อธิบายถึงวงจรการพัฒนาซอฟต์แวร์โดยใช้ AI (AI-assisted development) ตั้งแต่การจัดการกับความต้องการที่คลุมเครือให้กลายเป็นแผนงานที่ชัดเจน ไปจนถึงกระบวนการให้ AI ช่วยเขียนโปรแกรมและทดสอบระบบ โดยหัวใจสำคัญคือการประยุกต์ใช้หลักการพื้นฐานทางวิศวกรรมซอฟต์แวร์ (Software Engineering) ดั้งเดิมมาใช้ร่วมกับ AI เพื่อควบคุมทิศทางการพัฒนา ออกแบบโครงสร้างโค้ดที่เหมาะสม และหลีกเลี่ยงข้อจำกัดของตัวแบบภาษา (LLMs)

## Key Takeaways
- **The Thesis of AI Engineering:** การเขียนโค้ดด้วย AI ไม่ได้หมายความว่าต้องทิ้งหลักการเดิม แต่พื้นฐานของ Software Engineering ยังคงสำคัญและใช้งานได้ดีมากกับ AI (เช่น การจับคู่เขียนโค้ดแบบ Pair Programming)
- **ข้อจำกัดของ LLM (Smart vs. Dumb Zone):** การป้อนข้อมูลให้ LLM จำนวนมากเกินไปในบริบทเดิมจะทำให้ AI เริ่มตัดสินใจแย่ลง (Dumb Zone) จึงควรแบ่งงานเป็นชิ้นเล็กๆ ที่พอดีกับช่วงแรกที่ AI ยังทำงานได้ดีที่สุด (Smart Zone) รวมถึงการล้างบริบท (Clear Context) กลับไปจุดเริ่มต้นดีกว่าการบีบอัดข้อมูล (Compacting)
- **The Grill Session เพื่อสร้างความเข้าใจที่ตรงกัน:** แทนที่จะรีบสร้างแผนงาน ควรใช้เทคนิคให้ AI ซักถามผู้ใช้ (Grill) อย่างละเอียด เพื่อให้เกิดความเข้าใจในการออกแบบที่ตรงกัน (Shared Design Concept) ก่อนที่จะสรุปเป็นเอกสาร Product Requirements Document (PRD)
- **Vertical Slices (Tracer Bullets):** การแตกงานให้ AI ไม่ควรทำแบบแบ่งตามเลเยอร์ของระบบ (Horizontal) แต่ควรแบ่งงานให้จบเป็นรายฟีเจอร์ในตัว (Vertical) เพื่อให้ AI สามารถทำงานได้อย่างอิสระและทดสอบได้จริง
- **Code is the Battleground:** ไม่ควรใช้แนวทาง "Specs-to-code" (เขียนแค่เอกสารและปล่อยให้ AI ทำโค้ดโดยไม่สนใจการออกแบบภายใน) นักพัฒนาต้องรักษาอำนาจในการออกแบบโครงสร้างโค้ดเบส (Codebase Architecture) เพราะโค้ดเบสที่ดีย่อมทำให้ AI ทำงานได้มีประสิทธิภาพยิ่งขึ้น 
- **ย้อนกลับไปอ่านหนังสือเก่าๆ:** หลักการออกแบบระบบและข้อคิดดีๆ จากหนังสือ Software Engineering ยุคก่อนหน้า AI ยังคงนำมาปรับใช้เป็นพื้นฐานได้เป็นอย่างดี

## Related Concepts
- [[thesis_of_ai_engineering]]
- [[ai_workflow_research_prototyping]]
- [[the_grill_session]]
- [[writing_the_prd]]
- [[slicing_work_into_issues]]
- [[implementation_with_ai_agents]]
- [[human_in_the_loop_review]]
- [[deployment_and_monitoring]]
- [[designing_codebases_for_ai]]

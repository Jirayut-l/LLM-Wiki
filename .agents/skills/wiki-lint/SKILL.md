---
name: wiki-lint
description: "Health check the Obsidian wiki vault. Scans for orphan pages, dead wikilinks, frontmatter gaps, and empty sections. Generates a read-only lint report. Triggers on: lint, health check, clean up wiki, check the wiki, wiki maintenance, find orphans, wiki audit."
---

# wiki-lint: Wiki Health Check (MVP)

Perform a health check on the wiki to maintain structural integrity. This is a **Read-only** operation. You must never automatically fix issues. Only generate a report.

**Trigger**: This skill runs strictly manually when the user requests a wiki check, lint, or audit.

---

## 1. Core Lint Checks

You must systematically scan the `wiki/` directory (using tools like `grep_search` and `list_dir`) and check for the following issues:

1. **Dead Links**: Wikilinks (e.g., `[[Page Name]]`) that reference a page that does not exist anywhere in the vault.
2. **Orphan Pages**: Wiki pages that have NO inbound wikilinks from any other page in the vault (excluding `index.md`).
3. **Frontmatter Gaps**: Pages missing required YAML frontmatter fields (e.g., `type`, `tags`).
4. **Empty Sections**: Markdown headings (`## Heading`) that have no content or text beneath them.
5. **Stale Index Entries**: Items listed in `wiki/index.md` that point to deleted or renamed pages.

---

## 2. Generating the Report

After scanning, compile your findings into a single report file. 
**Do NOT output the full report into the chat to save tokens.**

**Report Path**: `wiki/meta/lint-report-YYYY-MM-DD.md`

Use the following template for the report:

```markdown
---
type: meta
title: "Lint Report YYYY-MM-DD"
created: YYYY-MM-DD
tags: [meta, lint]
status: developing
---

# Lint Report: YYYY-MM-DD

## Summary
- Pages scanned: N
- Issues found: N

## Dead Links
- [[Missing Page]]: referenced in [[Source Page]] but does not exist.

## Orphan Pages
- [[Page Name]]: no inbound links found.

## Frontmatter Gaps
- [[Page Name]]: missing fields (e.g., tags, type).

## Empty Sections
- [[Page Name]]: section "## Details" has no content.

## Stale Index Entries
- [[Page Name]]: listed in index but file missing.
```

---

## 3. Post-Report Actions

Once the report is generated:
1. Provide a brief summary of the findings in the chat (e.g., "พบลิงก์เสีย 3 จุด และหน้า Orphan 2 หน้า").
2. สร้างลิงก์ให้ผู้ใช้กดไปดู Report ที่สร้างขึ้น: [lint-report](file:///Users/spectrum/Resources/LLM-Wiki/wiki/meta/lint-report-YYYY-MM-DD.md)
3. แจ้งผู้ใช้ให้ทราบว่านี่เป็นการสแกนอย่างเดียว (Read-only) ไม่ได้มีการแก้ไขไฟล์ใดๆ หากต้องการแก้จุดไหนสามารถสั่งเป็นรายเคสได้เลย

---

## 4. Constraints & Rules

- **Read-Only**: ห้ามแก้ไข (Auto-fix) ข้อบกพร่องใดๆ ที่เจอระหว่างรันเด็ดขาด เพื่อความปลอดภัยของข้อมูล
- **Scope**: สแกนเฉพาะไฟล์ในโฟลเดอร์ `wiki/` เท่านั้น ห้ามสแกนหรือยุ่งเกี่ยวกับโฟลเดอร์ `.raw/`
- **Thai Language**: พิมพ์สรุปโต้ตอบกับผู้ใช้เป็นภาษาไทย

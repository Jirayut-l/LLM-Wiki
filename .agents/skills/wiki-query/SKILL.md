---
name: wiki-query
description: "Answer questions using the Obsidian wiki vault. Reads hot cache first, then index, then relevant pages. Synthesizes answers with citations. Auto-files high quality questions back as wiki pages. Triggers on: what do you know about, query:, what is, explain, summarize, find in wiki, search the wiki, based on the wiki."
---

# wiki-query: Query the Wiki (MVP)

The wiki has already done the synthesis work. Read strategically, answer precisely based strictly on the wiki, and file high-quality answers back so the knowledge compounds.

**Trigger**: Runs when the user asks a question about the domain or explicitly triggers a query.

---

## 1. Retrieval Flow (Standard Mode)

To answer the user's question, you **MUST** follow this strict reading sequence to optimize tokens and ensure accuracy:

1. **Read `wiki/hot.md`**: Start here. It contains the most recent context. If it fully answers the question, stop reading and synthesize the answer.
2. **Read `wiki/index.md`**: If `hot.md` didn't have the answer, read the index to identify which pages might contain the answer. Scan the descriptions.
3. **Read Target Pages**: Select and read only **3-5 relevant pages** found in the index. Do not read the entire wiki.
4. **Synthesize**: Combine the information to form a coherent answer.

---

## 2. Strict Gap Handling (No Hallucinations)

- **Wiki Context ONLY**: You must answer using ONLY the information found in the wiki. Do not fabricate answers or bring in outside knowledge from your training data.
- **Identify Gaps**: If the wiki does not contain enough information to answer the question, state it explicitly: "ข้อมูลใน Wiki มีไม่เพียงพอที่จะตอบคำถามนี้"
- **Offer Ingestion**: Suggest that the user provide a new source file or URL so you can run the `wiki-ingest` skill to add this knowledge to the vault.

---

## 3. Answering & Auto-Filing

Evaluate the user's question. If the question is simple, trivial, or a quick lookup, just answer it in the chat.
If the question requires deep synthesis, analysis, or yields a highly valuable insight, you must **auto-file** the answer into the wiki to compound the knowledge.

**Filing Format**:
Create a new file in `wiki/questions/` (e.g., `wiki/questions/how-does-concept-x-work.md`):

```yaml
---
type: question
title: "[Short descriptive title]"
question: "[The exact query as asked]"
answer_quality: solid
created: YYYY-MM-DD
tags: [question]
related:
  - "[[Page referenced in answer]]"
sources:
  - "[[wiki/sources/relevant-source.md]]"
status: developing
---
```

Write the synthesized answer as the body of the markdown file.
Include in-line citations pointing to the source pages (e.g., `(อ้างอิง: [[Page Name]])`).

**Post-Filing Steps**:
If you filed a question, you must also:
1. Update `wiki/index.md` by adding a link to the new question under the `## Questions` section.
2. Update `wiki/log.md` with a new entry documenting that a query was answered and filed.

---

## 4. Constraints

- **Token Optimization**: Use file reading tools (`view_file`, `grep_search`) strategically.
- **Chat Responses**: Keep your chat responses concise. If you filed a long answer, provide a short summary in Thai in the chat and link to the newly created file.
- **Thai Language**: Always use Thai language when interacting with the user and when creating the answer pages.

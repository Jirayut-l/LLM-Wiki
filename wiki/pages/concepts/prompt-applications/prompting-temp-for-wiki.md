---
title: การเขียนพรอมต์สำหรับ Project LLM-WIki
tags:
  - concept
  - use-case
  - programming
source: wiki/pages/concepts/prompting-temp-for-wiki.md
date: 2026-05-15
---
# การเขียนพรอมต์สำหรับโปรแกรมเมอร์

  Prioritizing Tool Usage

  To get the best performance and save tokens when prompting an LLM to summarize an article from your  raw/  folder

  and ingest it into your wiki, you want a prompt that is highly structured, restricts the LLM from generating

  conversational fluff, and explicitly asks for the outputs in your Obsidian Wiki format.

  Here is a recommended prompt template you can use (or have me use on your behalf) when processing a new raw

  document.

  

  ### The Prompt Template

    You are an expert knowledge extraction assistant. I am providing you with a raw source document.

    Please analyze the text and extract the following components exactly as requested, without any conversational

  filler, to be ingested into my Obsidian wiki:

    1. SUMMARY PAGE (`wiki/pages/summaries/<kebab-case-title>.md`)

    Provide the content for the summary page, including the YAML frontmatter. Keep the summary dense and focus on

  actionable takeaways.

    ```yaml

    ---

    tags: [summary, <add-relevant-tags>]

    source: <source-name-or-url>

    date: <current-date>

    ---

  TL;DR: (1-2 sentences summarizing the core message)

  Key Takeaways: (3-5 concise bullet points)

  Main Arguments: (Brief outline of the author's logic)

  2. NEW ENTITIES & CONCEPTS

  List any significant new entities (people, organizations, tools) or concepts (frameworks, theories) introduced in

  this text that deserve their own wiki pages in  wiki/pages/entities/  or  wiki/pages/concepts/ . For each, provide

  a 1-sentence definition.

  3. EXISTING WIKI CONNECTIONS

  Suggest tags or existing concepts this document should be linked to (use  [[wikilinks]]  format).

  4. LOG ENTRY

  Provide a single line for the  wiki/log.md  file in this format:

  | YYYY-MM-DD | [INGEST] |  |  |

  

  

    ### Why this saves tokens and improves performance:

    1. **Zero-shot Structure**: By giving it the exact markdown headings and YAML frontmatter you want, you don't

  waste output tokens on the LLM trying to invent a format or writing things like *"Here is the summary of the

  article you requested..."*

    2. **Constrained Output**: Asking for "1-2 sentences" or "3-5 concise bullet points" prevents the model from

  generating a rambling, multi-paragraph essay that consumes output tokens.

    3. **Separation of Concerns**: It cleanly separates the summary from the entities/concepts, making it very easy

  for you (or me, as your Wiki Agent) to take the output and directly write it to the correct folders (`/summaries`,

  `/concepts`, `/entities`) without needing a secondary processing step.

  

    ### How to use this with me (Antigravity):

    If you want me to do this for you, you can simply say:

    *"Read `raw/my-article.pdf` and ingest it into the wiki."*

  

    Because I have your `GEMINI.md` rules memorized, I will automatically read the file, extract the concepts and

  summaries using a highly token-efficient method, and create/update the `.md` files in your `wiki/` directory while

  logging the action!
---
[[prompt-engineering-v7-summary|กลับสู่สรุปเทคนิค]] | [[index|กลับสู่สารบัญ]]

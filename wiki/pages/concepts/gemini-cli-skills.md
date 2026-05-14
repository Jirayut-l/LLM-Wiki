---
tags: [concept, gemini-cli, skills]
source: internal
date: 2026-05-14
---

# Gemini CLI Skills

## Overview
Gemini CLI Skills are specialized instruction sets and tool configurations that extend the capabilities of the Gemini CLI agent. They allow the agent to adopt expert personas or handle complex workflows (like wiki maintenance, code refactoring, or project planning) by following a defined set of procedures and using specialized resources.

## Architecture
A Gemini CLI skill typically consists of:
- **`SKILL.md`**: The primary document containing instructions, mandates, and operational guidelines for the skill.
- **Reference Documentation**: Supplemental files (e.g., in a `references/` folder) that provide examples, schemas, or function definitions.
- **Activation Logic**: Skills are activated via the `activate_skill` tool, which injects the skill's instructions into the agent's context.

## Integration in LLM Wiki
In the LLM Wiki, skills are managed in two layers:
1. **Raw Sources (`raw/skills/`)**: The actual implementation files for the skills. These are immutable and serve as the ground truth for the agent's behavior.
2. **Wiki Pages (`wiki/pages/skills/`)**: LLM-generated documentation and summaries of these skills, making them discoverable and understandable for human users and the agent alike.

## Key Examples
- [[skill-obsidian-markdown|Obsidian Markdown]]: Rules for OFM syntax.
- [[skill-obsidian-bases|Obsidian Bases]]: Managing structured data.
- [[skill-json-canvas|JSON Canvas]]: Visual knowledge mapping.

## Related
- [[llm-wiki-concept-summary|LLM Wiki Concept Summary]]
- [[index|Wiki Index]]

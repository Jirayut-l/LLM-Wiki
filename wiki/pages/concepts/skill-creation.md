---
tags: [concept, skill-creation, methodology]
source: internal
date: 2026-05-14
---

# Skill Creation

## Overview
Skill creation is the process of codifying domain expertise into reusable, machine-executable instruction sets for AI agents. In the context of the Gemini CLI, this involves authoring `SKILL.md` files that guide the agent through specific workflows and tool usage.

## Methodologies
- **Pattern Extraction**: Observing successful agent interactions and formalizing the winning steps.
- **Artifact Synthesis**: Converting internal documentation, schemas, and incident reports into agent-ready instructions.
- **Iterative Refinement**: Using execution traces to prune vague instructions and add "Gotchas."

## Core Principles
1. **High Signal-to-Noise**: Provide only the information the agent lacks. 
2. **Context Efficiency**: Utilize [[progressive-disclosure|Progressive Disclosure]] to keep the agent's context window lean.
3. **Fragility-Based Prescriptiveness**: Use rigid steps for fragile tasks (like migrations) and flexible goals for creative tasks (like code review).

## Design Patterns
- **Validation Loops**: Self-correction mechanisms.
- **Intermediate Plans**: Structured pre-execution validation.
- **Gotchas**: Documentation of non-obvious environment specificities.

## Related
- [[gemini-cli-skills|Gemini CLI Skills]]
- [[best-practices-for-skill-creators-summary|Best Practices for Skill Creators (Summary)]]
- [[index|Wiki Index]]

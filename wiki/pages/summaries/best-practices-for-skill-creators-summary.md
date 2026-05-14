---
tags: [summary, skill-creation, best-practices]
source: raw/Best practices for skill creators.md
date: 2026-05-14
---

# Best Practices for Skill Creators Summary

A comprehensive guide on authoring high-signal, well-calibrated agent skills that maximize utility while minimizing context overhead.

## Core Philosophies
- **Ground in Expertise**: Skills should capture project-specific patterns, API edge cases, and internal conventions, not generic LLM knowledge.
- **Spend Context Wisely**: Omit what the agent already knows. Focus on what it would get wrong without the skill.
- **Calibrate Control**: Match the prescriptiveness of instructions to the fragility of the task.

## Key Authoring Patterns
- **Gotchas**: List non-obvious facts and common pitfalls that defy reasonable assumptions.
- **Validation Loops**: Instruct the agent to validate its own work (using scripts or checklists) before finalizing.
- **Plan-Validate-Execute**: For complex or destructive tasks, require an intermediate validated plan.
- **Progressive Disclosure**: Keep the core `SKILL.md` lean (< 500 lines) and move detailed references to separate files, instructing the agent on when to load them.

## Iteration & Refinement
- **Extract from Tasks**: Build skills by extracting patterns from successful agent-user interactions.
- **Synthesize from Artifacts**: Use internal docs, schemas, and incident reports as source material.
- **Refine via Traces**: Read execution traces to identify where the agent wastes time or gets confused.

Related: [[skill-creation|Skill Creation]], [[gemini-cli-skills|Gemini CLI Skills]]

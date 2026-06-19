---
name: wiki-lint-fix
description: Fixes issues identified in the lint report systematically using an Orchestration Plan. Triggers on "fix lint", "run lint fix", "resolve lint errors".
---

# Wiki Lint Fix Skill

This skill is responsible for systematically resolving errors found in the wiki lint reports.

## Instructions

When the user triggers this skill:
1. Do not start fixing issues ad-hoc.
2. Read the standard workflow rules defined in `[Lint Fix Workflow](file:///Users/spectrum/Resources/LLM-Wiki/.agents/workflows/lint-fix.md)`.
3. Follow the workflow strictly, starting from Phase 1 (Finding the Report and Creating the Orchestration Plan).

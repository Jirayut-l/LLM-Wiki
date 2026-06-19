---
name: wiki-fold
description: "Rollup of wiki log entries into meta-pages. Triggers on: fold the log, run a fold, run wiki-fold, log rollup, roll up log entries."
---

# wiki-fold: Extractive Log Rollup (Trigger)

This skill serves as the **Entry Point** for performing a fold (rollup) of the wiki logs.

## Primary Instruction

When triggered by the user, **DO NOT** attempt to perform the fold steps manually or ad-hoc. 

Instead, you **MUST** immediately execute the Fold Workflow defined in:
`[fold.md](file:///Users/spectrum/Resources/LLM-Wiki/.agents/workflows/fold.md)`

Please read the workflow file and follow its 2-Step Process (Draft -> Commit) and checkpointing requirements strictly.

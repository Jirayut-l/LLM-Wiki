# Agent Rules for LLM-Wiki

This file contains project-scoped rules for all agents operating in this workspace.

## Orchestration Plan Progress Tracking

When executing workflows and working with an Orchestration Plan in the `plans/` directory:
- **Always update the plan inline**: You MUST use file editing tools (e.g. `replace_file_content`) to tick off tasks (`- [x]`) in the plan file immediately after completing each granular task or checkpoint. *(Exception: In the final Commit Phase, you may skip ticking the boxes if the phase succeeds, since the plan file will be deleted immediately after.)*
- **Main Agent as Sole Editor**: Only the Main Agent (Orchestrator) should edit the plan file. Subagents should report their completion back to the Main Agent, who will then aggregate results and tick off the checkboxes. This prevents concurrent file modification conflicts.
- **Do not leave `- [ ]` unticked**: Never assume the user knows you completed a task. Update the plan file to reflect your actual progress (except during successful Commit Phase cleanup).
- **Failure Handling**: If a granular task fails, mark it as failed (e.g., `- [!]` or add a brief note) and continue with the rest of the phase. Summarize all failures when you hit a Checkpoint. Do not pause the entire phase for a single task failure. If a failure occurs during the Commit Phase, ensure you record `- [x]` for what succeeded and `- [!]` for what failed before stopping.

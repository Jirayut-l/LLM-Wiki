---
tags: [summary, claude-code, best-practices, agentic-coding]
source: "[[raw/Best practices for Claude Code.md]]"
date: 2026-05-24
---
# Best practices for Claude Code

## TL;DR
Claude Code is an agentic coding environment where managing the context window is the primary constraint. Effective usage involves separating exploration from implementation, providing clear verification criteria, and structuring prompts and environments to maintain a clean and focused context.

## Key Takeaways
- **Verification is Crucial:** Provide Claude with clear ways to verify its work (e.g., tests, screenshots, error logs) to ensure functionality over just plausible-looking code.
- **Context Management:** The context window degrades as it fills. Use `/clear` between unrelated tasks, `/compact` to summarize history, and checkpoints to backtrack.
- **Structured Exploration:** Use "plan mode" or delegate investigation to subagents to avoid solving the wrong problem and cluttering the main context window.
- **Environment Configuration:** A concise, well-maintained `CLAUDE.md` is essential for setting project rules, while skills, hooks, and MCP servers extend Claude's capabilities deterministically.
- **Scalability:** Claude Code can be scaled horizontally using multiple parallel sessions or non-interactive mode for CI/CD pipelines.

## Main Arguments
- **Context is King:** The fundamental limit of agentic coding is context size. Most best practices (clearing, subagents, concise instructions) are strategies to optimize what is kept in context.
- **Explore Then Code:** Jumping straight to coding without exploring the codebase often leads to incorrect solutions.
- **Specificity in Prompts:** Precise instructions with explicit references (`@file`) and clear symptoms lead to fewer needed corrections.
- **Tight Feedback Loops:** Correcting Claude immediately when it strays, rather than letting failed attempts pile up in context, produces better solutions faster.
- **Tooling Over Text:** Using specific extensions like hooks, CLI tools, and `CLAUDE.md` provides more reliable direction than conversational prompting alone.

## Entities & Concepts
- **Concepts:** [[Context Window]], [[Plan Mode]], [[Auto Mode]], [[Sandboxing]], [[Hooks]], [[Subagents]], [[Skills]], [[MCP Servers]], [[Agent Teams]]
- **Entities:** [[Claude Code]]

---
tags:
  - concept
  - prompt-engineering
  - caching
source: "[[claude-code-prompt-caching-summary]]"
date: 2026-05-24
---
# Prompt Caching

**Prompt Caching** is a technique used in Large Language Models (LLMs) to reuse computation from previous roundtrips, significantly decreasing latency and cost for long-running sessions like AI agents.

## How it Works
Prompt caching relies on **prefix matching**. The LLM API caches everything from the start of the request up to a specific breakpoint. 
- If the beginning of a new request exactly matches a cached prefix, the model reuses the computation.
- **Rule of Thumb**: Any change anywhere in the prefix invalidates everything after it.

## Best Practices
To maximize cache hit rates, systems should be designed around the prefix-matching constraint:

1. **Static First, Dynamic Last**: Order your prompt components from the most stable (System Prompt, Tools) to the most variable (Conversation History).
2. **State Updates via Messages**: Instead of updating the system prompt when state changes, append a new message (e.g., `<system-reminder>`) to the conversation history.
3. **Stable Toolsets**: Never add or remove tools mid-conversation. Use state-transition tools (like `EnterPlanMode`) or deferred tool loading for large toolsets.
4. **Cache-Safe Forking**: When branching a conversation (e.g., for compaction/summarization), use the exact same system prompt and tools as the parent request to guarantee a cache hit.

> [!tip] 
> See [[claude-code-prompt-caching-summary|Lessons from building Claude Code]] for a detailed action plan on implementing these practices.

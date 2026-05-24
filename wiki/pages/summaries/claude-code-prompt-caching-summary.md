---
tags:
  - summary
  - prompt-engineering
  - agent-architecture
source: "[[Lessons from building Claude Code Prompt caching is everything.md]]"
date: 2026-05-24
---
# Lessons from building Claude Code: Prompt caching is everything

**Source**: `raw/Lessons from building Claude Code Prompt caching is everything.md`

This document outlines best practices for optimizing prompt caching in agentic products, specifically drawing from the development of Claude Code. A high cache hit rate significantly reduces latency and cost.

![[system-prompt-layout.png]]

## Core Concept
Prompt caching works by **prefix matching**. The API caches everything from the start of the request up to each `cache_control` breakpoint. Any change in the prefix invalidates the cache for everything that follows.

## Action Plan (Practical Steps)

1. **Order Prompts Strategically (Static to Dynamic)**
   - Place static content first and dynamic content last.
   - Recommended order:
     1. Static system prompt & Tools (globally cached)
     2. Project-specific context (e.g., `CLAUDE.md`)
     3. Session context
     4. Conversation messages

2. **Use Messages for Updates, Not System Prompts**
   - When information changes (e.g., time updates, file modifications), do not edit the system prompt.
   - Instead, pass the updated information via a user message or tool result in the agent's next turn (e.g., using a `<system-reminder>` tag).

3. **Keep Models Consistent Mid-Session**
   - Prompt caches are unique to models. Switching models (e.g., from Opus to Haiku) breaks the cache.
   - If a different model is needed, deploy a **subagent** to handle the specific task rather than changing the model in the main session.

4. **Never Add or Remove Tools Mid-Session**
   - Changing the toolset invalidates the cache. Keep all tools in the request at all times.
   - **State Transitions**: Use tools to change states (e.g., `EnterPlanMode` and `ExitPlanMode`) instead of swapping tools.
   - **Defer Tool Loading**: If there are too many tools, send lightweight tool stubs (with `defer_loading: true`). Let the model "discover" full tool schemas via a tool search tool when needed.

5. **Perform Cache-Safe Compaction (Forking)**
   - When the context window is full and summarization is needed, do not send a new bare-bones request.
   - Use the *exact same* system prompt, context, and tool definitions as the parent conversation. Prepend the history and append the compaction prompt as a new user message at the very end to reuse the parent's cached prefix.

6. **Monitor Cache Hit Rates**
   - Treat cache misses as incidents. Set up alerts for cache hit rates, as minor drops can drastically impact costs and performance.

---
**Related Concepts**:
- [[prompt-caching|Prompt Caching]]

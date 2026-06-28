# Orchestration Plan: Deduplicate and Standardize Source Files

**Target Scope**: `/wiki/sources` and `/index.md`
**Objective**: Rename source files to follow `snake_case.md` naming convention (no `source_` prefix, no spaces) and merge duplicate source files.

## Phase 1: Staging (Drafting)
- [ ] 1.1 Read and analyze `From Zero to Head of AI in 1 Year (as a regular person).md` and `source_from_zero_to_head_of_ai.md`.
- [ ] 1.2 Synthesize content from both files and create `plans/drafts/from_zero_to_head_of_ai.md`.
- [ ] 1.3 Read and analyze `How to Build Claude Subagents Better Than 99% of People.md` and `how_to_build_claude_subagents_source.md`.
- [ ] 1.4 Synthesize content from both files and create `plans/drafts/how_to_build_claude_subagents.md`.
- [ ] 1.5 Read `source_build_a_proactive_agent_workflow_with_claude_code.md` and copy its content to `plans/drafts/build_a_proactive_agent_workflow_with_claude_code.md`.
- [ ] 1.6 Read `Give Me 10 Mins and I'll Save You Millions of Claude Tokens.md` and copy its content to `plans/drafts/give_me_10_mins_and_ill_save_you_millions_of_claude_tokens.md`.
- [ ] 1.7 Read `index.md` and create a draft of updated index at `plans/drafts/index.md` pointing to the new standard filenames.

## Phase 2: User Verification Checkpoint
- [x] 2.1 Wait for user to review and approve the drafts in `plans/drafts/`.

## Phase 3: Commit
- [x] 3.1 Copy all `.md` files from `plans/drafts/` (except `index.md`) to `wiki/sources/`.
- [x] 3.2 Overwrite `index.md` with `plans/drafts/index.md`.
- [x] 3.3 Delete the 6 original non-compliant files from `wiki/sources/`.
- [x] 3.4 Append the operation log to `logs/log.md`.
- [x] 3.5 Update `hot.md` with Recent Changes.

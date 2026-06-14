# Glossary

- **Raw Source**: An immutable document (e.g., article, paper, note) provided by the user, strictly stored in the `raw/` directory. The LLM reads from these but never modifies them.
- **Wiki**: A persistent, structured collection of markdown files generated and maintained entirely by the LLM. It uses a **Flat Directory Structure** (e.g., all files in a `wiki/` folder or root), relying on Obsidian Properties (YAML frontmatter) such as `type: concept` or `type: entity` for categorization rather than nested folders.
- **Schema**: The rules and conventions that guide the LLM's behavior in maintaining the Wiki. (In this project, `CONTEXT.md` and related prompts serve as the Schema).
- **Ingest**: The process where a user prompts the LLM to read a new Raw Source from `raw/`, discuss takeaways, and structurally update the Wiki to reflect the new knowledge. Ingestion state is tracked exclusively via the presence of the source in `index.md` and its corresponding Wiki page, not by moving the raw file.
- **Index (`index.md`)**: A static, plain-text markdown file that catalogs everything in the Wiki. The Agent manually updates it on every ingest (instead of using dynamic plugins like Dataview) so that the Agent can read it quickly as a map of the knowledge base.
- **Log (`log.md`)**: A chronological record of all actions (Ingest, Query, Lint) performed by the Agent. It uses a detailed Audit Trace format (often utilizing tables for readability) to list exactly which Wiki pages were created or modified during an action. 
- **Log Rotation**: The process of archiving older log entries. When `log.md` exceeds 100 entries, the Agent will cut and paste the oldest logs into an archive file (e.g., `logs/archive-YYYY-MM.md`) to keep the main log readable while preserving history.
- **Hot Cache (`hot.md`)**: A lightweight memory file (approx. 500 words) located at the root. It acts as the Agent's short-term memory, summarizing the most recent context, work-in-progress (`Current Focus`), open decisions (`Decisions in Flight`), and recent changes. The Agent reads this file first before querying the full Wiki to reduce token usage and quickly regain context.
- **Agent**: The conversational LLM assistant that acts as the "programmer" or "maintainer" of the Wiki, operating alongside the user's IDE (Obsidian).
- **Page Template**: Every Wiki page must follow a strict structural template to ensure consistency. This includes YAML frontmatter (e.g., `type:`, `aliases:`), and standard headings such as `## Summary`, `## Related Concepts`, and `## Sources`. The Agent must adhere to this structure when creating or updating pages.
- **Skill**: A specialized tool or capability (e.g., `defuddle` for web scraping, `obsidian-cli` for vault operations) that the Agent can invoke to perform specific tasks within the repository.
- **Workflow**: A predefined sequence of steps or logic that the Agent follows to achieve a complex goal (e.g., the "Ingest Workflow" which orchestrates reading a source, invoking the `defuddle` skill, and formatting with the `obsidian-markdown` skill).
- **Orchestration Plan**: A markdown file (stored in the `plans/` directory) used to break down and track the execution of a complex task (like Ingestion) into distinct, trackable phases and checkpoints.
  - **Granular Task Breakdown**: The plan must break down the work for each Phase into the smallest, most detailed sub-tasks possible to enable task distribution and delegation to subagents.
  - **Single-File Scope Constraint**: A single task must never cover multiple files simultaneously. Each task must be scoped to explicitly target only one specific file.
- **Content Visualization**: When encountering complex or difficult concepts during page creation or Ingestion, the Agent should proactively use interactive elements, visualizations (e.g., Mermaid flowcharts, Comparison table), or tables to make the content easier for readers to understand. **Important:** Visualizations must supplement, not replace, comprehensive and detailed textual explanations. Do not reduce the depth or length of the text summary when adding visualizations.

# Agent Behavior Rules

- **Token Optimization & Output Muting**: Do not output all content into the chat to save tokens. Write it to a file (e.g., `plans/` or various `.md` files) instead and summarize briefly in the chat.
- **Raw File Protection**: Do not delete the original files in the `raw/` folder under any circumstances.
- **Thai Language Summary**: The summary should be in Thai only. If there are technical terms, please use their transliteration.

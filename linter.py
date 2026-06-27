import os
import re
import yaml

base_dir = "/Users/spectrum/Resources/LLM-Wiki"
wiki_dirs = ["wiki/concepts", "wiki/entities", "wiki/sources", "wiki/summarize"]
special_files = ["index.md", "hot.md", "logs/log.md"]

# 1. Gather all files
pages = {}
for d in wiki_dirs:
    dir_path = os.path.join(base_dir, d)
    if os.path.exists(dir_path):
        for f in os.listdir(dir_path):
            if f.endswith(".md"):
                name = f[:-3]
                pages[name] = os.path.join(dir_path, f)

for f in special_files:
    pages[f] = os.path.join(base_dir, f)

# Issues
dead_links = [] # (source, target)
orphans = []
frontmatter_gaps = []
empty_sections = []
invalid_sections = []
stale_index_entries = []

inbound_links = {p: set() for p in pages if not p.endswith(".md")}

required_fm = {
    "concept": ["type", "aliases", "tags", "created", "sources"],
    "entity": ["type", "aliases", "tags", "created", "sources"],
    "source": ["type", "aliases", "tags", "created", "author"], # url or file_path handled custom
    "summary": ["type", "aliases", "tags", "created", "sources"]
}

allowed_headings = {
    "concept": ["Summary", "Core Principles", "Related", "Questions to follow up"],
    "entity": ["Overview", "Key Characteristics", "Related", "Questions to follow up"],
    "source": ["Summary", "Key Takeaways", "Related Concepts"],
    "summary": ["Overview", "Key Insights", "Related Concepts"]
}

def check_file(name, path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find links
    links = re.findall(r'\[\[([^|\]]+)(?:\|[^\]]+)?\]\]', content)
    for target in links:
        # Resolve target base name
        t = target.strip()
        
        # Check dead links
        if t not in [p for p in pages if not p.endswith(".md")]:
            dead_links.append((name, t))
            if name == "index.md":
                stale_index_entries.append((name, t))
        else:
            if not name.endswith(".md"): # if it's from a wiki page
                inbound_links[t].add(name)

    if name.endswith(".md"):
        return # Skip frontmatter/section checks for index, hot, log

    # Parse frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    ptype = None
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1)) or {}
            ptype = fm.get("type")
            if ptype in required_fm:
                missing = []
                for req in required_fm[ptype]:
                    if req not in fm:
                        missing.append(req)
                if ptype == "source":
                    if "url" not in fm and "file_path" not in fm:
                        missing.append("url or file_path")
                if missing:
                    frontmatter_gaps.append((name, missing))
            else:
                frontmatter_gaps.append((name, ["type"]))
        except yaml.YAMLError:
            frontmatter_gaps.append((name, ["invalid yaml"]))
    else:
        frontmatter_gaps.append((name, ["all (no frontmatter)"]))

    # Sections check
    lines = content.split('\n')
    current_section = None
    section_content_lines = 0
    in_code_block = False

    def finalize_section(sec, sec_lines):
        if sec and sec_lines == 0:
            empty_sections.append((name, sec))

    for line in lines:
        if line.startswith("```"):
            in_code_block = not in_code_block
        if not in_code_block and (line.startswith("# ") or line.startswith("## ")):
            finalize_section(current_section, section_content_lines)
            
            # New section
            level = 1 if line.startswith("# ") else 2
            heading = line.strip("#").strip()
            current_section = line.strip()
            section_content_lines = 0

            # Valid heading check
            if level == 2 and ptype in allowed_headings:
                if heading not in allowed_headings[ptype]:
                    invalid_sections.append((name, line.strip()))
        else:
            # Check if line is not empty and not just comments
            text = re.sub(r'<!--.*?-->', '', line).strip()
            if text != '' and not text.startswith('<!--') and not text.endswith('-->'):
                if current_section:
                    section_content_lines += 1

    finalize_section(current_section, section_content_lines)

for name, path in pages.items():
    check_file(name, path)

for p in inbound_links:
    if len(inbound_links[p]) == 0:
        orphans.append(p)

print("Dead Links:")
for s, t in dead_links:
    print(f"- [[{t}]]: referenced in [[{s}]] but does not exist.")

print("\nOrphan Pages:")
for o in orphans:
    print(f"- [[{o}]]: no inbound links found.")

print("\nFrontmatter Gaps:")
for s, missing in frontmatter_gaps:
    print(f"- [[{s}]]: missing fields ({', '.join(missing)}).")

print("\nEmpty Sections:")
for s, sec in empty_sections:
    print(f"- [[{s}]]: section \"{sec}\" has no content.")

print("\nInvalid Sections:")
for s, sec in invalid_sections:
    print(f"- [[{s}]]: heading \"{sec}\" is not in the template.")

print("\nStale Index Entries:")
for s, t in stale_index_entries:
    print(f"- [[{t}]]: listed in index but file missing.")

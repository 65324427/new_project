import re

with open('course_materials/phase3_advanced/large_language_models/llm_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if the pattern matches the next section
next_section_pattern = r'^##\s+\d+\.'
next_section_match = re.search(next_section_pattern, content, re.MULTILINE)

if next_section_match:
    print(f"Found next section: {next_section_match.group()}")
    print(f"Position: {next_section_match.start()}")
    
    # Show context around the match
    start = max(0, next_section_match.start() - 20)
    end = min(len(content), next_section_match.end() + 20)
    print(f"Context: {repr(content[start:end])}")
else:
    print("No next section found!")
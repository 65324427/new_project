import re

with open('course_materials/phase3_advanced/large_language_models/llm_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all section headers
section_pattern = r'^##\s+\d+\.'
sections = list(re.finditer(section_pattern, content, re.MULTILINE))

print(f"Found {len(sections)} sections:")
for i, section in enumerate(sections):
    print(f"{i+1}. {section.group()} at position {section.start()}")
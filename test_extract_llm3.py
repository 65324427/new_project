import re

with open('course_materials/phase3_advanced/large_language_models/llm_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

section_title = '1. 大语言模型概述'

# Try to find the next section
next_section_pattern = r'^##\s+2\.'
next_section_match = re.search(next_section_pattern, content, re.MULTILINE)

if next_section_match:
    next_section_pos = next_section_match.start()
    print(f"Found next section at position: {next_section_pos}")
    print(f"Next section title: {next_section_match.group()}")
    
    # Now try to extract from section 1 to section 2
    start_pattern = rf'##\s+{re.escape(section_title)}'
    start_match = re.search(start_pattern, content)
    
    if start_match:
        start_pos = start_match.start()
        result = content[start_pos:next_section_pos]
        print(f"\nExtracted content length: {len(result)}")
        print(f"First 200 chars: {repr(result[:200])}")
else:
    print("Next section not found!")
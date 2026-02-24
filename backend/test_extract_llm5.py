import re

with open('course_materials/phase3_advanced/large_language_models/llm_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

section_title = '1. 大语言模型概述'

# Find the current section
start_pattern = rf'^##\s+{re.escape(section_title)}'
start_match = re.search(start_pattern, content, re.MULTILINE)

if start_match:
    start_pos = start_match.start()
    print(f"Found section at position: {start_pos}")
    
    # Find the next section with a different number
    # Extract the current section number
    current_num = re.search(r'(\d+)\.', section_title).group(1)
    next_num = str(int(current_num) + 1)
    
    # Pattern for next section
    next_section_pattern = rf'^##\s+{next_num}\.'
    next_section_match = re.search(next_section_pattern, content, re.MULTILINE)
    
    if next_section_match:
        end_pos = next_section_match.start()
        result = content[start_pos:end_pos]
        print(f"Extracted content length: {len(result)}")
        print(f"First 200 chars: {repr(result[:200])}")
    else:
        # If no next section, take till end
        result = content[start_pos:]
        print(f"Extracted content length (till end): {len(result)}")
        print(f"First 200 chars: {repr(result[:200])}")
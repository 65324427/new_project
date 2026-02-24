import re

with open('course_materials/phase3_advanced/large_language_models/llm_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

section_title = '1. 大语言模型概述'

# Try different patterns
patterns = [
    rf'##\s+{re.escape(section_title)}.*?(?=^##\s|$)',
    rf'##\s+{re.escape(section_title)}[\s\S]*?(?=^##\s|$)',
    rf'##\s+{re.escape(section_title)}.*?(?=##\s+|$)',
]

for i, pattern in enumerate(patterns):
    print(f"Pattern {i+1}: {pattern}")
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    if match:
        result = match.group(0)
        print(f"Match found! Length: {len(result)}")
        print(f"First 200 chars: {repr(result[:200])}")
    else:
        print("No match!")
    print("\n" + "="*50 + "\n")
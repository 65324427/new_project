import re

with open('course_materials/phase3_advanced/large_language_models/llm_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

section_title = '1. 大语言模型概述'
pattern = rf'##\s+{re.escape(section_title)}.*?(?=^##\s+\d+\.|$)'
match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

if match:
    result = match.group(0)
    print("Extracted content:")
    print(repr(result[:200]))
    print("\n" + "="*50 + "\n")
    print("First 500 characters:")
    print(result[:500])
else:
    print("No match found!")
import re

with open('course_materials/phase1_foundation/ai_overview/ai_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

section_title = '3. 不同背景学习者的职业路径规划'
pattern = rf'##\s+{re.escape(section_title)}.*?(?=##\s+|$)'
match = re.search(pattern, content, re.DOTALL)

if match:
    result = match.group(0)
    print("Extracted content:")
    print(repr(result))
    print("\n" + "="*50 + "\n")
    
    lines = result.split('\n')
    print("Number of lines:", len(lines))
    for i, line in enumerate(lines[:10]):
        print(f"Line {i}: {repr(line)}")
else:
    print("No match found!")
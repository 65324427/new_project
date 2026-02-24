import re

with open('course_materials/phase1_foundation/ai_overview/ai_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

section_title = '3. 不同背景学习者的职业路径规划'

print("Searching for section:", section_title)
print("\n" + "="*50 + "\n")

# Find the section start
start_pattern = rf'##\s+{re.escape(section_title)}'
start_match = re.search(start_pattern, content)

if start_match:
    start_pos = start_match.start()
    print(f"Found section at position: {start_pos}")
    print(f"Section title: {start_match.group()}")
    
    # Show what comes after the section title
    after_section = content[start_pos:start_pos+500]
    print("\nContent after section title (first 500 chars):")
    print(repr(after_section))
    
    # Now try the full pattern
    full_pattern = rf'##\s+{re.escape(section_title)}.*?(?=##\s+|$)'
    full_match = re.search(full_pattern, content, re.DOTALL)
    
    if full_match:
        result = full_match.group(0)
        print("\n" + "="*50 + "\n")
        print("Full match result:")
        print(repr(result))
    else:
        print("\n" + "="*50 + "\n")
        print("Full pattern did not match!")
else:
    print("Section not found!")
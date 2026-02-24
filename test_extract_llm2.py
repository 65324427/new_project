import re

with open('course_materials/phase3_advanced/large_language_models/llm_introduction.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section start
start_pattern = rf'##\s+1\. 大语言模型概述'
start_match = re.search(start_pattern, content)

if start_match:
    start_pos = start_match.start()
    print(f"Found section at position: {start_pos}")
    print(f"Section title: {start_match.group()}")
    
    # Show what comes after the section title
    after_section = content[start_pos:start_pos+500]
    print("\nContent after section title (first 500 chars):")
    print(repr(after_section))
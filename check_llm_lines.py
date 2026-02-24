import re

with open('course_materials/phase3_advanced/large_language_models/llm_introduction.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(0, 20):
    print(f"Line {i+1}: {repr(lines[i])}")
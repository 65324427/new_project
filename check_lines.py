import re

with open('course_materials/phase1_foundation/ai_overview/ai_introduction.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(124, 140):
    print(f"Line {i+1}: {repr(lines[i])}")
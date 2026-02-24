import re

with open('course_content3.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<div class="modal" id="modal(\d+)"[^>]*>.*?<h3>(.*?)</h3>'
matches = re.findall(pattern, content, re.DOTALL)

for modal_id, title in matches:
    if int(modal_id) >= 26:
        print(f"modal{modal_id}: {title}")
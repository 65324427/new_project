import re

content = '''## 3. 不同背景学习者的职业路径规划

### 3.1 零基础学习者

**学习路径**：
1. **基础阶段**（3-6个月）：
   - 学习Python编程
   - 掌握数学基础（线性代数、微积分、概率统计）
   - 了解AI基本概念

2. **进阶阶段**（6-12个月）：
   - 学习机器学习基础
   - 掌握深度学习框架
   - 完成小型项目

3. **专业阶段**（6-12个月）：
   - 深入学习特定领域（如大模型、计算机视觉）
   - 完成中型项目
   - 构建作品集

**推荐岗位**：
- AI助理
- 机器学习工程师（初级）
- AI产品经理

## 4. AI伦理与安全

### 4.1 AI伦理挑战'''

def extract_section_content(content, section_title):
    pattern = rf'##\s+{re.escape(section_title)}.*?(?=##\s+|$)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0)
    return None

result = extract_section_content(content, '3. 不同背景学习者的职业路径规划')
print("Extracted content:")
print(repr(result))
print("\n" + "="*50 + "\n")

def markdown_to_html(markdown_content):
    if not markdown_content:
        return '<p>本内容正在开发中，敬请期待...</p><p>点击右上角关闭按钮返回。</p>'
    
    html_lines = []
    lines = markdown_content.split('\n')
    
    in_list = False
    in_ordered_list = False
    
    for line in lines:
        stripped_line = line.strip()
        
        if not stripped_line:
            if in_list or in_ordered_list:
                html_lines.append('</ul>' if in_list else '</ol>')
                in_list = False
                in_ordered_list = False
            continue
        
        if stripped_line.startswith('## '):
            if in_list or in_ordered_list:
                html_lines.append('</ul>' if in_list else '</ol>')
                in_list = False
                in_ordered_list = False
            title = stripped_line[3:]
            html_lines.append(f'<h4>{title}</h4>')
        elif stripped_line.startswith('### '):
            if in_list or in_ordered_list:
                html_lines.append('</ul>' if in_list else '</ol>')
                in_list = False
                in_ordered_list = False
            title = stripped_line[4:]
            html_lines.append(f'<h5>{title}</h5>')
        elif stripped_line.startswith('#### '):
            if in_list or in_ordered_list:
                html_lines.append('</ul>' if in_list else '</ol>')
                in_list = False
                in_ordered_list = False
            title = stripped_line[5:]
            html_lines.append(f'<h6>{title}</h6>')
        elif stripped_line.startswith('- '):
            if not in_list:
                if in_ordered_list:
                    html_lines.append('</ol>')
                    in_ordered_list = False
                html_lines.append('<ul>')
                in_list = True
            text = stripped_line[2:]
            if text.startswith('**') and text.endswith('**'):
                text = text[2:-2]
            html_lines.append(f'<li>{text}</li>')
        elif stripped_line.startswith('1. ') or stripped_line.startswith('2. ') or stripped_line.startswith('3. ') or stripped_line.startswith('4. ') or stripped_line.startswith('5. '):
            if not in_ordered_list:
                if in_list:
                    html_lines.append('</ul>')
                    in_list = False
                html_lines.append('<ol>')
                in_ordered_list = True
            text = stripped_line[3:]
            if text.startswith('**') and text.endswith('**'):
                text = text[2:-2]
            html_lines.append(f'<li>{text}</li>')
        elif stripped_line.startswith('**') and stripped_line.endswith('**'):
            if in_list or in_ordered_list:
                html_lines.append('</ul>' if in_list else '</ol>')
                in_list = False
                in_ordered_list = False
            text = stripped_line[2:-2]
            html_lines.append(f'<p><strong>{text}</strong></p>')
        else:
            if in_list or in_ordered_list:
                html_lines.append('</ul>' if in_list else '</ol>')
                in_list = False
                in_ordered_list = False
            html_lines.append(f'<p>{stripped_line}</p>')
    
    if in_list:
        html_lines.append('</ul>')
    elif in_ordered_list:
        html_lines.append('</ol>')
    
    return '\n'.join(html_lines)

html_result = markdown_to_html(result)
print("HTML result:")
print(html_result)
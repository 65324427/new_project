import json
import re
from pathlib import Path

def read_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def extract_section_content(content, section_title):
    pattern = rf'##\s+{re.escape(section_title)}.*?(?=##\s+|$)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0)
    return None

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

def get_modal_content_mapping():
    course_materials_dir = Path('course_materials')
    
    mapping = {}
    
    ai_intro_file = course_materials_dir / 'phase1_foundation' / 'ai_overview' / 'ai_introduction.md'
    ai_intro_content = read_markdown_file(ai_intro_file)
    
    if ai_intro_content:
        mapping[4] = extract_section_content(ai_intro_content, '3. 不同背景学习者的职业路径规划')
        mapping[5] = extract_section_content(ai_intro_content, '4. AI伦理与安全')
    
    python_intro_file = course_materials_dir / 'phase1_foundation' / 'python_basics' / 'python_introduction.md'
    python_intro_content = read_markdown_file(python_intro_file)
    
    if python_intro_content:
        mapping[6] = extract_section_content(python_intro_content, '3. Python核心语法')
        mapping[7] = extract_section_content(python_intro_content, '4. 数据结构')
        mapping[8] = extract_section_content(python_intro_content, '5. 面向对象编程')
        mapping[9] = extract_section_content(python_intro_content, '6. 文件操作')
        mapping[10] = extract_section_content(python_intro_content, '7. 常用AI库')
    
    math_intro_file = course_materials_dir / 'phase1_foundation' / 'math_fundamentals' / 'math_introduction.md'
    math_intro_content = read_markdown_file(math_intro_file)
    
    if math_intro_content:
        mapping[11] = extract_section_content(math_intro_content, '2. 线性代数基础')
        mapping[12] = extract_section_content(math_intro_content, '3. 微积分基础')
        mapping[13] = extract_section_content(math_intro_content, '4. 概率统计基础')
        mapping[14] = extract_section_content(math_intro_content, '5. 信息论基础')
        mapping[15] = extract_section_content(math_intro_content, '6. 数学概念的直观理解')
    
    ml_intro_file = course_materials_dir / 'phase1_foundation' / 'ml_basics' / 'ml_introduction.md'
    ml_intro_content = read_markdown_file(ml_intro_file)
    
    if ml_intro_content:
        mapping[16] = extract_section_content(ml_intro_content, '1. 机器学习概述')
        mapping[17] = extract_section_content(ml_intro_content, '2. 线性回归')
        mapping[18] = extract_section_content(ml_intro_content, '4. 决策树')
        mapping[19] = extract_section_content(ml_intro_content, '6. 模型评估与选择')
        mapping[20] = extract_section_content(ml_intro_content, '7. 特征工程')
    
    dl_intro_file = course_materials_dir / 'phase2_skill_enhancement' / 'deep_learning_fundamentals' / 'deep_learning_introduction.md'
    dl_intro_content = read_markdown_file(dl_intro_file)
    
    if dl_intro_content:
        mapping[21] = extract_section_content(dl_intro_content, '1. 什么是深度学习？')
    
    dl_fb_file = course_materials_dir / 'phase2_skill_enhancement' / 'deep_learning_fundamentals' / 'forward_backward_propagation.md'
    dl_fb_content = read_markdown_file(dl_fb_file)
    
    if dl_fb_content:
        mapping[22] = extract_section_content(dl_fb_content, '1. 前向传播（Forward Propagation）')
    
    nn_basics_file = course_materials_dir / 'phase2_skill_enhancement' / 'deep_learning_fundamentals' / 'neural_network_basics.md'
    nn_basics_content = read_markdown_file(nn_basics_file)
    
    if nn_basics_content:
        mapping[23] = extract_section_content(nn_basics_content, '3. 激活函数')
        mapping[24] = extract_section_content(nn_basics_content, '4.3 梯度下降法')
        mapping[25] = extract_section_content(nn_basics_content, '5.1 过拟合')
    
    return mapping

def update_modal_in_html(html_file, modal_id, title, content):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    pattern = rf'<div class="modal" id="modal{modal_id}"[^>]*>.*?</div>\s*</div>'
    
    new_modal_html = f'''<div class="modal" id="modal{modal_id}" style="display: none;">
    <div class="modal-content">
        <span class="close" onclick="closeModal('modal{modal_id}')">&times;</span>
        <h3>{title}</h3>
        {markdown_to_html(content)}
    </div>
</div>'''
    
    html_content = re.sub(pattern, new_modal_html, html_content, flags=re.DOTALL)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    modal_titles = {
        4: '不同背景学习者的职业路径规划',
        5: 'AI伦理与安全',
        6: 'Python核心语法',
        7: '数据结构',
        8: '面向对象编程',
        9: '文件操作',
        10: '常用AI库（NumPy、Pandas、Matplotlib）',
        11: '线性代数基础（向量、矩阵、线性变换）',
        12: '微积分基础（导数、梯度、链式法则）',
        13: '概率统计基础（概率分布、贝叶斯定理、统计推断）',
        14: '信息论基础（熵、交叉熵、KL散度）',
        15: '数学概念的直观理解与AI应用',
        16: '机器学习概述',
        17: '线性回归',
        18: '决策树',
        19: '模型评估与选择',
        20: '特征工程',
        21: '深度学习概述',
        22: '前向传播与反向传播',
        23: '激活函数',
        24: '优化算法（SGD、Adam）',
        25: '模型正则化与防止过拟合',
    }
    
    content_mapping = get_modal_content_mapping()
    
    html_file = 'course_content3.html'
    
    updated_count = 0
    for modal_id, title in modal_titles.items():
        if modal_id in content_mapping and content_mapping[modal_id]:
            print(f'Updating modal{modal_id}: {title}')
            update_modal_in_html(html_file, modal_id, title, content_mapping[modal_id])
            updated_count += 1
        else:
            print(f'Skipping modal{modal_id}: {title} (no content found)')
    
    print(f'\nTotal updated: {updated_count} modals')

if __name__ == '__main__':
    main()
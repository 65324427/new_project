import re
from pathlib import Path

def read_markdown_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def extract_section_content(content, section_title):
    # Find the current section
    start_pattern = rf'^##\s+{re.escape(section_title)}'
    start_match = re.search(start_pattern, content, re.MULTILINE)
    
    if not start_match:
        return None
    
    start_pos = start_match.start()
    
    # Find the next section with a different number
    # Extract the current section number
    num_match = re.search(r'(\d+)\.', section_title)
    if num_match:
        current_num = num_match.group(1)
        next_num = str(int(current_num) + 1)
        
        # Pattern for next section
        next_section_pattern = rf'^##\s+{next_num}\.'
        next_section_match = re.search(next_section_pattern, content, re.MULTILINE)
        
        if next_section_match:
            end_pos = next_section_match.start()
            return content[start_pos:end_pos]
    
    # If no next section, take till end
    return content[start_pos:]

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
    
    # 大语言模型相关 (modal26-30)
    llm_file = course_materials_dir / 'phase3_advanced' / 'large_language_models' / 'llm_introduction.md'
    llm_content = read_markdown_file(llm_file)
    
    if llm_content:
        mapping[26] = extract_section_content(llm_content, '1. 大语言模型概述')
        mapping[27] = extract_section_content(llm_content, '2. Prompt Engineering技术')
        mapping[28] = extract_section_content(llm_content, '3. 模型微调方法')
        mapping[29] = extract_section_content(llm_content, '4. 大模型应用开发')
        mapping[30] = extract_section_content(llm_content, '5. 大模型评估指标')
    
    # 多模态AI相关 (modal31-35)
    multimodal_file = course_materials_dir / 'phase3_advanced' / 'multimodal_ai' / 'multimodal_introduction.md'
    multimodal_content = read_markdown_file(multimodal_file)
    
    if multimodal_content:
        mapping[31] = extract_section_content(multimodal_content, '1. 多模态AI概述')
        mapping[32] = extract_section_content(multimodal_content, '2. 文本-图像融合技术')
        mapping[33] = extract_section_content(multimodal_content, '3. 图像描述生成')
        mapping[34] = extract_section_content(multimodal_content, '4. 多模态模型评估')
        mapping[35] = extract_section_content(multimodal_content, '5. 多模态应用开发')
    
    # MLOps相关 (modal36-40)
    mlops_file = course_materials_dir / 'phase3_advanced' / 'mlops_deployment' / 'mlops_practice.md'
    mlops_content = read_markdown_file(mlops_file)
    
    if mlops_content:
        mapping[36] = extract_section_content(mlops_content, '1. 模型部署技术')
        mapping[37] = extract_section_content(mlops_content, '2. 模型监控与维护')
        mapping[38] = extract_section_content(mlops_content, '3. AI系统架构设计')
        mapping[39] = extract_section_content(mlops_content, '4. MLOps实践')
        mapping[40] = extract_section_content(mlops_content, '5. AI系统性能优化')
    
    # 高级AI技术 (modal41-44)
    advanced_ai_file = course_materials_dir / 'phase3_advanced' / 'advanced_ai_techniques' / 'advanced_ai.md'
    advanced_ai_content = read_markdown_file(advanced_ai_file)
    
    if advanced_ai_content:
        mapping[41] = extract_section_content(advanced_ai_content, '1. 强化学习基础')
        mapping[42] = extract_section_content(advanced_ai_content, '2. 图神经网络')
        mapping[43] = extract_section_content(advanced_ai_content, '3. 联邦学习')
        mapping[44] = extract_section_content(advanced_ai_content, '4. 自监督学习')
    
    # AI安全与隐私保护 (modal45)
    ai_security_file = course_materials_dir / 'phase3_advanced' / 'ai_security_privacy' / 'ai_security.md'
    ai_security_content = read_markdown_file(ai_security_file)
    
    if ai_security_content:
        mapping[45] = extract_section_content(ai_security_content, '1. AI安全概述')
    
    # 行业应用 (modal46-50)
    industry_ai_file = course_materials_dir / 'phase3_advanced' / 'industry_applications' / 'industry_ai.md'
    industry_ai_content = read_markdown_file(industry_ai_file)
    
    if industry_ai_content:
        mapping[46] = extract_section_content(industry_ai_content, '1. 金融科技AI应用')
        mapping[47] = extract_section_content(industry_ai_content, '2. 医疗健康AI应用')
        mapping[48] = extract_section_content(industry_ai_content, '3. 智能交通AI应用')
        mapping[49] = extract_section_content(industry_ai_content, '4. 智能制造AI应用')
        mapping[50] = extract_section_content(industry_ai_content, '5. 零售与营销AI应用')
    
    # 项目实践 (modal51-55)
    project_practice_file = course_materials_dir / 'phase3_advanced' / 'project_practice' / 'project_practice.md'
    project_practice_content = read_markdown_file(project_practice_file)
    
    if project_practice_content:
        mapping[51] = extract_section_content(project_practice_content, '1. 项目需求分析与设计')
        mapping[52] = extract_section_content(project_practice_content, '2. 数据处理与特征工程')
        mapping[53] = extract_section_content(project_practice_content, '3. 模型选择与训练')
        mapping[54] = extract_section_content(project_practice_content, '4. 模型评估与优化')
        mapping[55] = extract_section_content(project_practice_content, '5. 项目部署与文档编写')
    
    # 职业发展 (modal56-60)
    career_development_file = course_materials_dir / 'phase3_advanced' / 'career_development' / 'career_development.md'
    career_development_content = read_markdown_file(career_development_file)
    
    if career_development_content:
        mapping[56] = extract_section_content(career_development_content, '1. AI岗位简历优化')
        mapping[57] = extract_section_content(career_development_content, '2. 技术面试准备')
        mapping[58] = extract_section_content(career_development_content, '3. 算法题解题技巧')
        mapping[59] = extract_section_content(career_development_content, '4. 职业发展规划')
        mapping[60] = extract_section_content(career_development_content, '5. 行业趋势与发展方向')
    
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
    
    def replacer(match):
        return new_modal_html
    
    html_content = re.sub(pattern, replacer, html_content, flags=re.DOTALL)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    modal_titles = {
        26: '大语言模型概述',
        27: 'Prompt Engineering技术',
        28: '模型微调方法',
        29: '大模型应用开发',
        30: '大模型评估指标',
        31: '多模态AI概述',
        32: '文本-图像融合技术',
        33: '图像描述生成',
        34: '多模态模型评估',
        35: '多模态应用开发',
        36: '模型部署技术',
        37: '模型监控与维护',
        38: 'AI系统架构设计',
        39: 'MLOps实践',
        40: 'AI系统性能优化',
        41: '强化学习基础',
        42: '图神经网络',
        43: '联邦学习',
        44: '自监督学习',
        45: 'AI安全与隐私保护',
        46: '金融科技AI应用',
        47: '医疗健康AI应用',
        48: '智能交通AI应用',
        49: '智能制造AI应用',
        50: '零售与营销AI应用',
        51: '项目需求分析与设计',
        52: '数据处理与特征工程',
        53: '模型选择与训练',
        54: '模型评估与优化',
        55: '项目部署与文档编写',
        56: 'AI岗位简历优化',
        57: '技术面试准备',
        58: '算法题解题技巧',
        59: '职业发展规划',
        60: '行业趋势与发展方向',
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
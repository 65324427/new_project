// 生成缺失的模态框定义
const fs = require('fs');

// 读取现有的course_content3.html文件
const filePath = 'course_content3.html';
let content = fs.readFileSync(filePath, 'utf8');

// 已定义的模态框
const definedModals = [1, 2, 3];

// 需要定义的模态框范围
const startModal = 4;
const endModal = 60;

// 模态框标题映射
const modalTitles = {
    4: '不同背景学习者的职业路径规划',
    5: 'AI伦理与安全',
    6: 'Python核心语法',
    7: '数据结构',
    8: '面向对象编程',
    9: '文件操作与异常处理',
    10: '常用AI库（NumPy、Pandas、Matplotlib）',
    11: '线性代数基础（向量、矩阵、线性变换）',
    12: '微积分基础（导数、梯度、链式法则）',
    13: '概率统计基础（概率分布、贝叶斯定理、统计推断）',
    14: '信息论基础（熵、交叉熵、KL散度）',
    15: '数学概念的直观理解与AI应用',
    16: '机器学习概述',
    17: '线性回归与逻辑回归',
    18: '决策树与随机森林',
    19: '模型评估与调优',
    20: '特征工程基础',
    21: '神经网络基础',
    22: '前向传播与反向传播',
    23: '激活函数与损失函数',
    24: '优化算法（SGD、Adam）',
    25: '模型正则化与防止过拟合',
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
    60: '行业趋势与发展方向'
};

// 生成模态框定义
let modalDefinitions = '';
for (let i = startModal; i <= endModal; i++) {
    const title = modalTitles[i] || `模态框 ${i}`;
    modalDefinitions += `
<div class="modal" id="modal${i}" style="display: none;">
    <div class="modal-content">
        <span class="close" onclick="closeModal('modal${i}')">&times;</span>
        <h3>${title}</h3>
        <p>本内容正在开发中，敬请期待...</p>
        <p>点击右上角关闭按钮返回。</p>
    </div>
</div>`;
}

// 在文件末尾添加模态框定义
content += modalDefinitions;

// 写入文件
fs.writeFileSync(filePath, content, 'utf8');

console.log(`已生成 ${endModal - startModal + 1} 个模态框定义，从 modal${startModal} 到 modal${endModal}`);
console.log('文件已更新：', filePath);

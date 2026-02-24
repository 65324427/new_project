// UI修复脚本 - 添加缺失的函数

// 修复toggleFeature函数 - 用于正确关闭面板
function closePanel(feature) {
    console.log('Closing panel:', feature);
    
    const panelId = `${feature}-panel`;
    const buttonId = `${feature}-btn`;
    
    const panel = document.getElementById(panelId);
    const button = document.getElementById(buttonId);
    
    if (panel) {
        panel.classList.remove('show');
    }
    
    if (button) {
        button.classList.remove('active');
    }
}

// 重写toggleFeature函数以支持关闭功能
// 等待页面加载完成后执行，确保script.js已经加载
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded fired, enhancing toggleFeature');
    
    const originalToggleFeature = window.toggleFeature;
    
    window.toggleFeature = function(feature) {
        console.log('toggleFeature called with:', feature);
        
        const targetPanel = document.getElementById(`${feature}-panel`);
        
        if (targetPanel && targetPanel.classList.contains('show')) {
            console.log('Closing panel via toggleFeature:', feature);
            closePanel(feature);
        } else {
            console.log('Opening panel via toggleFeature:', feature);
            
            const panels = ['progress-panel', 'assessment-panel', 'community-panel', 'personalized-panel'];
            const buttons = ['progress-btn', 'assessment-btn', 'community-btn', 'personalized-btn'];
            
            panels.forEach(panelId => {
                const panel = document.getElementById(panelId);
                if (panel) {
                    panel.classList.remove('show');
                }
            });
            
            buttons.forEach(btnId => {
                const button = document.getElementById(btnId);
                if (button) {
                    button.classList.remove('active');
                }
            });
            
            const targetPanel = document.getElementById(`${feature}-panel`);
            const targetButton = document.getElementById(`${feature}-btn`);
            
            if (targetPanel) {
                targetPanel.classList.add('show');
            }
            
            if (targetButton) {
                targetButton.classList.add('active');
            }
            
            if (feature === 'progress') {
                if (typeof loadProgress === 'function') {
                    console.log('Calling loadProgress');
                    loadProgress();
                } else {
                    console.error('loadProgress function not found');
                }
            } else if (feature === 'assessment') {
                if (typeof loadAssessments === 'function') {
                    console.log('Calling loadAssessments');
                    loadAssessments();
                } else {
                    console.error('loadAssessments function not found');
                }
            } else if (feature === 'community') {
                if (typeof loadCommunityPosts === 'function') {
                    console.log('Calling loadCommunityPosts');
                    loadCommunityPosts();
                } else {
                    console.error('loadCommunityPosts function not found');
                }
            } else if (feature === 'personalized') {
                if (typeof loadPersonalizedPath === 'function') {
                    console.log('Calling loadPersonalizedPath');
                    loadPersonalizedPath();
                } else {
                    console.error('loadPersonalizedPath function not found');
                }
            }
        }
    };
    
    console.log('toggleFeature function has been enhanced');
});

// startQuiz函数 - 用于开始测试
function startQuiz(quizId) {
    console.log('Starting quiz:', quizId);
    
    // 隐藏测试列表
    const quizList = document.getElementById('quiz-list');
    if (quizList) {
        quizList.style.display = 'none';
    }
    
    // 显示测试容器
    const quizContainer = document.getElementById('quiz-container');
    if (quizContainer) {
        quizContainer.style.display = 'block';
    }
    
    // 根据quizId加载测试内容
    let testData = {};
    
    if (quizId === 'python-basics') {
        testData = {
            id: 'python-basics',
            title: 'Python基础测试',
            questions: [
                {
                    id: 1,
                    question: 'Python中，以下哪个不是内置数据类型？',
                    options: ['list', 'tuple', 'array', 'dict'],
                    correctAnswer: 'array'
                },
                {
                    id: 2,
                    question: '以下哪种方式可以创建一个空列表？',
                    options: ['list = []', 'list = list()', 'list = {}', 'A和B都对'],
                    correctAnswer: 'A和B都对'
                },
                {
                    id: 3,
                    question: 'Python中，以下哪个关键字用于定义函数？',
                    options: ['func', 'def', 'function', 'define'],
                    correctAnswer: 'def'
                },
                {
                    id: 4,
                    question: '以下代码的输出是什么？\nprint(3 * "Hello")',
                    options: ['HelloHelloHello', 'HelloHelloHelloHelloHelloHello', '3Hello', '错误'],
                    correctAnswer: 'HelloHelloHello'
                },
                {
                    id: 5,
                    question: 'Python中，以下哪种方式可以读取文件内容？',
                    options: ['with open("file.txt", "r") as f:\n    content = f.read()', 'open("file.txt", "r").read()', 'file = open("file.txt", "r")\ncontent = file.read()\nfile.close()', '以上三种方式都对'],
                    correctAnswer: '以上三种方式都对'
                }
            ]
        };
    } else if (quizId === 'ml-basics') {
        testData = {
            id: 'ml-basics',
            title: '机器学习基础测试',
            questions: [
                {
                    id: 1,
                    question: '以下哪个不是机器学习的类型？',
                    options: ['监督学习', '无监督学习', '强化学习', '深度学习'],
                    correctAnswer: '深度学习'
                },
                {
                    id: 2,
                    question: '以下哪个算法用于分类问题？',
                    options: ['线性回归', '逻辑回归', 'K-Means', 'PCA'],
                    correctAnswer: '逻辑回归'
                },
                {
                    id: 3,
                    question: '以下哪个是过拟合的表现？',
                    options: ['训练集准确率高，测试集准确率低', '训练集准确率低，测试集准确率高', '训练集和测试集准确率都高', '训练集和测试集准确率都低'],
                    correctAnswer: '训练集准确率高，测试集准确率低'
                },
                {
                    id: 4,
                    question: '以下哪个是常用的评估指标？',
                    options: ['准确率', '精确率', '召回率', '以上都是'],
                    correctAnswer: '以上都是'
                },
                {
                    id: 5,
                    question: '以下哪个算法用于聚类问题？',
                    options: ['决策树', '支持向量机', 'K-Means', '朴素贝叶斯'],
                    correctAnswer: 'K-Means'
                }
            ]
        };
    } else if (quizId === 'math-basics') {
        testData = {
            id: 'math-basics',
            title: '数学基础测试',
            questions: [
                {
                    id: 1,
                    question: '以下哪个是矩阵乘法的性质？',
                    options: ['交换律', '结合律', '分配律', 'B和C都对'],
                    correctAnswer: 'B和C都对'
                },
                {
                    id: 2,
                    question: '以下哪个是导数的几何意义？',
                    options: ['函数在某点的斜率', '函数在某点的面积', '函数在某点的值', '函数在某点的极限'],
                    correctAnswer: '函数在某点的斜率'
                },
                {
                    id: 3,
                    question: '以下哪个是概率的基本性质？',
                    options: ['概率值在0到1之间', '所有可能事件的概率之和为1', '不可能事件的概率为0', '以上都是'],
                    correctAnswer: '以上都是'
                },
                {
                    id: 4,
                    question: '以下哪个是向量的点积性质？',
                    options: ['交换律', '结合律', '分配律', 'A和C都对'],
                    correctAnswer: 'A和C都对'
                },
                {
                    id: 5,
                    question: '以下哪个是梯度的几何意义？',
                    options: ['函数增长最快的方向', '函数下降最快的方向', '函数的极值点', '函数的拐点'],
                    correctAnswer: '函数增长最快的方向'
                }
            ]
        };
    }
    
    // 渲染测试界面
    if (quizContainer && testData.questions) {
        quizContainer.innerHTML = `
            <h4>${testData.title}</h4>
            <div class="quiz-container">
                ${testData.questions.map((q, index) => `
                    <div class="question">
                        <div class="question-header">
                            <span class="question-number">问题 ${index + 1}/${testData.questions.length}</span>
                        </div>
                        <div class="question-text">${q.question.replace(/\n/g, '<br>')}</div>
                        <ul class="options">
                            ${q.options.map((option, optIndex) => `
                                <li class="option">
                                    <input type="radio" name="q${q.id}" value="${option}" id="q${q.id}_${optIndex}">
                                    <label for="q${q.id}_${optIndex}">${option.replace(/\n/g, '<br>')}</label>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                `).join('')}
                <div class="quiz-footer">
                    <div class="quiz-progress" id="quiz-progress">进度: 0/${testData.questions.length}</div>
                    <button class="submit-btn" onclick="submitQuiz('${quizId}')">提交答案</button>
                    <button class="cancel-btn" onclick="cancelQuiz('${quizId}')">取消</button>
                </div>
            </div>
        `;
        
        // 更新进度
        updateQuizProgress();
    }
}

// submitQuiz函数 - 用于提交测试答案
function submitQuiz(quizId) {
    console.log('Submitting quiz:', quizId);
    
    // 获取用户答案
    const testData = {
        'python-basics': {
            questions: [
                { id: 1, correctAnswer: 'array' },
                { id: 2, correctAnswer: 'A和B都对' },
                { id: 3, correctAnswer: 'def' },
                { id: 4, correctAnswer: 'HelloHelloHello' },
                { id: 5, correctAnswer: '以上三种方式都对' }
            ]
        },
        'ml-basics': {
            questions: [
                { id: 1, correctAnswer: '深度学习' },
                { id: 2, correctAnswer: '逻辑回归' },
                { id: 3, correctAnswer: '训练集准确率高，测试集准确率低' },
                { id: 4, correctAnswer: '以上都是' },
                { id: 5, correctAnswer: 'K-Means' }
            ]
        },
        'math-basics': {
            questions: [
                { id: 1, correctAnswer: 'B和C都对' },
                { id: 2, correctAnswer: '函数在某点的斜率' },
                { id: 3, correctAnswer: '以上都是' },
                { id: 4, correctAnswer: 'A和C都对' },
                { id: 5, correctAnswer: '函数增长最快的方向' }
            ]
        }
    };
    
    const quizData = testData[quizId];
    if (!quizData) {
        console.error('Quiz data not found:', quizId);
        return;
    }
    
    let correctCount = 0;
    const totalQuestions = quizData.questions.length;
    
    // 计算得分
    quizData.questions.forEach(q => {
        const selectedOption = document.querySelector(`input[name="q${q.id}"]:checked`);
        if (selectedOption && selectedOption.value === q.correctAnswer) {
            correctCount++;
        }
    });
    
    const score = Math.round((correctCount / totalQuestions) * 100);
    
    // 显示结果
    const quizContainer = document.getElementById('quiz-container');
    if (quizContainer) {
        quizContainer.innerHTML = `
            <div class="result-container">
                <div class="result-score">${score} 分</div>
                <div class="result-stats">
                    <div class="result-stat">
                        <div class="result-stat-value">${correctCount}</div>
                        <div class="result-stat-label">答对题数</div>
                    </div>
                    <div class="result-stat">
                        <div class="result-stat-value">${totalQuestions - correctCount}</div>
                        <div class="result-stat-label">答错题数</div>
                    </div>
                    <div class="result-stat">
                        <div class="result-stat-value">${score}%</div>
                        <div class="result-stat-label">正确率</div>
                    </div>
                </div>
                <div class="result-feedback">
                    <h5>测试完成</h5>
                    <p>您已完成${quizId === 'python-basics' ? 'Python基础' : quizId === 'ml-basics' ? '机器学习基础' : '数学基础'}测试</p>
                    <p>得分: ${score}分 (${correctCount}/${totalQuestions})</p>
                </div>
                <button class="retry-btn" onclick="retryQuiz('${quizId}')">重新测试</button>
                <button class="back-btn" onclick="cancelQuiz('${quizId}')">返回测试列表</button>
            </div>
        `;
    }
    
    // 保存测试结果
    const testResult = {
        quizId: quizId,
        score: score,
        correctCount: correctCount,
        totalQuestions: totalQuestions,
        completedAt: new Date().toLocaleString()
    };
    
    if (typeof isOnline === 'function' && isOnline()) {
        fetch('/api/assessments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(testResult)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Test result saved:', data);
        })
        .catch(error => {
            console.error('Error saving test result:', error);
            // 保存到本地存储
            const localResults = getFromLocalStorage('test_results') || [];
            localResults.push(testResult);
            saveToLocalStorage('test_results', localResults);
        });
    } else {
        // 保存到本地存储
        if (typeof getFromLocalStorage === 'function' && typeof saveToLocalStorage === 'function') {
            const localResults = getFromLocalStorage('test_results') || [];
            localResults.push(testResult);
            saveToLocalStorage('test_results', localResults);
        }
    }
}

// cancelQuiz函数 - 用于取消测试
function cancelQuiz(quizId) {
    console.log('Canceling quiz:', quizId);
    
    // 显示测试列表
    const quizList = document.getElementById('quiz-list');
    if (quizList) {
        quizList.style.display = 'block';
    }
    
    // 隐藏测试容器
    const quizContainer = document.getElementById('quiz-container');
    if (quizContainer) {
        quizContainer.style.display = 'none';
        quizContainer.innerHTML = '';
    }
}

// retryQuiz函数 - 用于重新测试
function retryQuiz(quizId) {
    console.log('Retrying quiz:', quizId);
    startQuiz(quizId);
}

// updateQuizProgress函数 - 用于更新测试进度
function updateQuizProgress() {
    const progressElement = document.getElementById('quiz-progress');
    if (progressElement) {
        const questions = document.querySelectorAll('.question');
        const answered = document.querySelectorAll('.question input[type="radio"]:checked');
        progressElement.textContent = `进度: ${answered.length}/${questions.length}`;
    }
}

// switchCommunityTab函数 - 用于切换社区标签
function switchCommunityTab(tab) {
    console.log('Switching to community tab:', tab);
    
    // 更新标签按钮状态
    const tabButtons = document.querySelectorAll('#community-panel .tab-btn');
    tabButtons.forEach(btn => {
        btn.classList.remove('active');
    });
    
    // 找到被点击的按钮并添加active类
    const clickedButton = Array.from(tabButtons).find(btn => 
        btn.textContent.includes(tab === 'posts' ? '讨论区' : '发布帖子')
    );
    if (clickedButton) {
        clickedButton.classList.add('active');
    }
    
    // 切换内容显示
    const postsTab = document.getElementById('posts-tab');
    const createTab = document.getElementById('create-tab');
    
    if (tab === 'posts') {
        if (postsTab) postsTab.style.display = 'block';
        if (createTab) createTab.style.display = 'none';
        // 重新加载帖子列表
        if (typeof loadCommunityPosts === 'function') {
            loadCommunityPosts();
        }
    } else if (tab === 'create') {
        if (postsTab) postsTab.style.display = 'none';
        if (createTab) createTab.style.display = 'block';
    }
}

// 页面加载完成后添加事件监听器
document.addEventListener('DOMContentLoaded', function() {
    console.log('UI修复脚本已加载');
    
    // 为所有单选按钮添加进度更新监听器
    document.addEventListener('change', function(event) {
        if (event.target.type === 'radio') {
            updateQuizProgress();
        }
    });
});

console.log('UI修复脚本已加载完成');

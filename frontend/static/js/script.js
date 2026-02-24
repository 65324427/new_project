// 模态框功能
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
        // 延迟刷新CodeMirror编辑器，确保在模态框显示后正确初始化
        setTimeout(() => {
            const editors = document.querySelectorAll('.CodeMirror');
            editors.forEach(editor => {
                editor.CodeMirror.refresh();
            });
        }, 100);
    }
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
    }
}

// 点击模态框外部关闭
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
}

// 功能面板切换
function toggleFeature(feature) {
    const panels = ['progress-panel', 'assessment-panel', 'community-panel', 'personalized-panel'];
    const buttons = ['progress-btn', 'assessment-btn', 'community-btn', 'personalized-btn'];
    
    panels.forEach(panelId => {
        const panel = document.getElementById(panelId);
        if (panel) {
            panel.style.display = 'none';
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
        targetPanel.style.display = 'block';
    }
    
    if (targetButton) {
        targetButton.classList.add('active');
    }
    
    // 加载对应功能的数据
    if (feature === 'progress') {
        loadProgress();
    } else if (feature === 'assessment') {
        loadAssessments();
    } else if (feature === 'community') {
        loadCommunityPosts();
    } else if (feature === 'personalized') {
        loadPersonalizedPath();
    }
}

// 学习进度功能
function loadProgress() {
    fetch('/api/progress')
        .then(response => response.json())
        .then(data => {
            updateProgressUI(data);
        })
        .catch(error => {
            console.error('Error loading progress:', error);
            // 尝试从本地存储加载
            const localData = getFromLocalStorage('progress_data');
            if (localData) {
                updateProgressUI(localData);
            } else {
                // 显示默认数据
                updateProgressUI({ totalProgress: 0, completedChapters: 0, learningTime: 0, lastLearned: null, chapters: [] });
            }
        });
}

function updateProgressUI(data) {
    const progressText = document.querySelector('.progress-text');
    const progressCircle = document.querySelector('.progress-circle .progress');
    const completedChapters = document.getElementById('completed-chapters');
    const learningTime = document.getElementById('learning-time');
    const lastLearned = document.getElementById('last-learned');
    const progressList = document.getElementById('progress-list');
    
    if (progressText) {
        progressText.textContent = `${data.totalProgress}%`;
    }
    
    if (progressCircle) {
        const radius = 65;
        const circumference = 2 * Math.PI * radius;
        const offset = circumference - (data.totalProgress / 100) * circumference;
        progressCircle.style.strokeDasharray = `${circumference} ${circumference}`;
        progressCircle.style.strokeDashoffset = offset;
    }
    
    if (completedChapters) {
        completedChapters.textContent = data.completedChapters;
    }
    
    if (learningTime) {
        learningTime.textContent = data.learningTime;
    }
    
    if (lastLearned) {
        if (data.lastLearned) {
            lastLearned.textContent = data.lastLearned;
        } else {
            lastLearned.textContent = '从未';
        }
    }
    
    if (progressList) {
        progressList.innerHTML = '';
        data.chapters.forEach(chapter => {
            const li = document.createElement('li');
            li.className = 'progress-item';
            li.innerHTML = `
                <div class="progress-item-header">
                    <span class="progress-item-title">${chapter.title}</span>
                    <span class="progress-item-percent">${chapter.progress}%</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-bar-fill" style="width: ${chapter.progress}%"></div>
                </div>
            `;
            progressList.appendChild(li);
        });
    }
}

function updateProgress() {
    const progressData = {
        totalProgress: Math.floor(Math.random() * 100),
        completedChapters: Math.floor(Math.random() * 20),
        learningTime: Math.floor(Math.random() * 100),
        lastLearned: new Date().toLocaleString(),
        chapters: [
            { title: 'AI概述与职业规划', progress: Math.floor(Math.random() * 100) },
            { title: '编程基础', progress: Math.floor(Math.random() * 100) },
            { title: '数学基础', progress: Math.floor(Math.random() * 100) },
            { title: '机器学习基础', progress: Math.floor(Math.random() * 100) }
        ]
    };
    
    if (isOnline()) {
        fetch('/api/progress', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(progressData)
        })
        .then(response => response.json())
        .then(data => {
            updateProgressUI(data);
            // 同时保存到本地存储
            saveToLocalStorage('progress_data', data);
        })
        .catch(error => {
            console.error('Error updating progress:', error);
            // 保存到本地存储，待网络恢复后同步
            saveToLocalStorage('progress_data', progressData);
            updateProgressUI(progressData);
        });
    } else {
        // 离线状态，保存到本地存储
        saveToLocalStorage('progress_data', progressData);
        updateProgressUI(progressData);
    }
}

// 评估测试功能
function loadAssessments() {
    fetch('/api/assessments')
        .then(response => response.json())
        .then(data => {
            updateAssessmentsUI(data);
        })
        .catch(error => {
            console.error('Error loading assessments:', error);
            // 尝试从本地存储加载
            const localData = getFromLocalStorage('assessments_data');
            if (localData) {
                updateAssessmentsUI(localData);
            } else {
                // 显示默认数据
                updateAssessmentsUI([]);
            }
        });
}

function updateAssessmentsUI(assessments) {
    const testList = document.getElementById('test-list');
    if (testList) {
        testList.innerHTML = '';
        
        const defaultTests = [
            {
                id: 1,
                title: 'Python基础测试',
                description: '测试您对Python基础语法和数据结构的掌握程度',
                difficulty: 'easy',
                questions: 5,
                duration: 15,
                completed: false
            },
            {
                id: 2,
                title: '机器学习基础测试',
                description: '测试您对机器学习基本概念和算法的理解',
                difficulty: 'medium',
                questions: 5,
                duration: 20,
                completed: false
            },
            {
                id: 3,
                title: '数学基础测试',
                description: '测试您对AI所需数学知识的掌握程度',
                difficulty: 'hard',
                questions: 5,
                duration: 25,
                completed: false
            }
        ];
        
        const testsToDisplay = assessments.length > 0 ? assessments : defaultTests;
        
        testsToDisplay.forEach(test => {
            const li = document.createElement('li');
            li.className = 'test-item';
            li.onclick = () => startTest(test.id);
            li.innerHTML = `
                <div class="test-item-header">
                    <span class="test-item-title">${test.title}</span>
                    <span class="test-item-difficulty difficulty-${test.difficulty}">
                        ${test.difficulty === 'easy' ? '简单' : test.difficulty === 'medium' ? '中等' : '困难'}
                    </span>
                </div>
                <div class="test-item-description">${test.description}</div>
                <div class="test-item-footer">
                    <span>${test.questions} 题 | ${test.duration} 分钟</span>
                    <span>${test.completed ? '已完成' : '未完成'}</span>
                </div>
            `;
            testList.appendChild(li);
        });
    }
}

function startTest(testId) {
    // 模拟测试数据
    const testData = {
        id: testId,
        title: testId === 1 ? 'Python基础测试' : testId === 2 ? '机器学习基础测试' : '数学基础测试',
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
    
    const quizContainer = document.getElementById('quiz-container');
    if (quizContainer) {
        quizContainer.innerHTML = `
            <h4>${testData.title}</h4>
            <div class="quiz-container">
                ${testData.questions.map((q, index) => `
                    <div class="question">
                        <div class="question-header">
                            <span class="question-number">问题 ${index + 1}/${testData.questions.length}</span>
                        </div>
                        <div class="question-text">${q.question}</div>
                        <ul class="options">
                            ${q.options.map((option, optIndex) => `
                                <li class="option">
                                    <input type="radio" name="q${q.id}" value="${option}" id="q${q.id}_${optIndex}">
                                    <label for="q${q.id}_${optIndex}">${option}</label>
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                `).join('')}
                <div class="quiz-footer">
                    <div class="quiz-progress">进度: 0/${testData.questions.length}</div>
                    <button class="submit-btn" onclick="submitTest(${testId})">提交答案</button>
                </div>
            </div>
        `;
    }
}

function submitTest(testId) {
    // 模拟测试结果
    const score = Math.floor(Math.random() * 51) + 50;
    const correctCount = Math.floor(score / 20);
    
    const resultContainer = document.getElementById('quiz-container');
    if (resultContainer) {
        resultContainer.innerHTML = `
            <div class="result-container">
                <div class="result-score">${score} 分</div>
                <div class="result-stats">
                    <div class="result-stat">
                        <div class="result-stat-value">${correctCount}</div>
                        <div class="result-stat-label">答对题数</div>
                    </div>
                    <div class="result-stat">
                        <div class="result-stat-value">${5 - correctCount}</div>
                        <div class="result-stat-label">答错题数</div>
                    </div>
                    <div class="result-stat">
                        <div class="result-stat-value">${Math.floor(score / 10)}</div>
                        <div class="result-stat-label">正确率(%)</div>
                    </div>
                </div>
                <div class="result-feedback">
                    <h5>答题反馈</h5>
                    <div class="feedback-item feedback-correct">
                        <div class="feedback-question">问题 1: Python中，以下哪个不是内置数据类型？</div>
                        <div class="feedback-your-answer">你的答案: array</div>
                        <div class="feedback-correct-answer">正确答案: array</div>
                    </div>
                    <div class="feedback-item feedback-incorrect">
                        <div class="feedback-question">问题 2: 以下哪种方式可以创建一个空列表？</div>
                        <div class="feedback-your-answer">你的答案: list = []</div>
                        <div class="feedback-correct-answer">正确答案: A和B都对</div>
                    </div>
                </div>
            </div>
        `;
    }
    
    // 保存测试结果
    const testResult = {
        testId: testId,
        score: score,
        correctCount: correctCount,
        totalQuestions: 5,
        completedAt: new Date().toLocaleString()
    };
    
    if (isOnline()) {
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
        const localResults = getFromLocalStorage('test_results') || [];
        localResults.push(testResult);
        saveToLocalStorage('test_results', localResults);
    }
}

// 社区互动功能
function loadCommunityPosts() {
    fetch('/api/community')
        .then(response => response.json())
        .then(data => {
            updateCommunityUI(data);
        })
        .catch(error => {
            console.error('Error loading community posts:', error);
            // 尝试从本地存储加载
            const localData = getFromLocalStorage('community_data');
            if (localData) {
                updateCommunityUI(localData);
            } else {
                // 显示默认数据
                updateCommunityUI([]);
            }
        });
}

function updateCommunityUI(posts) {
    const postList = document.getElementById('post-list');
    if (postList) {
        postList.innerHTML = '';
        
        const defaultPosts = [
            {
                id: 1,
                title: 'Python学习心得分享',
                content: 'Python是一门非常适合AI学习的语言，语法简洁，库丰富。建议大家多做实践项目来巩固知识。',
                author: '学习达人',
                createdAt: '2026-02-01',
                category: 'share',
                comments: [
                    {
                        id: 1,
                        author: '新手小白',
                        content: '谢谢分享，我会努力学习的！',
                        createdAt: '2026-02-02'
                    }
                ]
            },
            {
                id: 2,
                title: '机器学习算法疑问',
                content: '请问随机森林和决策树有什么区别？在什么情况下应该使用随机森林？',
                author: '求知者',
                createdAt: '2026-02-03',
                category: 'help',
                comments: []
            },
            {
                id: 3,
                title: '房价预测项目分享',
                content: '我完成了一个基于线性回归的房价预测项目，准确率达到了85%，大家有兴趣可以一起讨论。',
                author: '数据分析师',
                createdAt: '2026-02-04',
                category: 'project',
                comments: []
            }
        ];
        
        const postsToDisplay = posts.length > 0 ? posts : defaultPosts;
        
        postsToDisplay.forEach(post => {
            const li = document.createElement('li');
            li.className = 'post-item';
            li.innerHTML = `
                <div class="post-header">
                    <span class="post-title">${post.title}</span>
                    <span class="post-meta">${post.author} · ${post.createdAt}</span>
                </div>
                <div class="post-content">${post.content}</div>
                <div class="post-footer">
                    <span class="post-category">${post.category === 'share' ? '经验分享' : post.category === 'help' ? '问题求助' : post.category === 'project' ? '项目交流' : '综合讨论'}</span>
                    <div class="post-actions">
                        <button class="post-action" onclick="toggleComments(${post.id})">评论 (${post.comments ? post.comments.length : 0})</button>
                        <button class="post-action">点赞</button>
                    </div>
                </div>
                <div id="comments-${post.id}" class="comment-list" style="display: none;">
                    ${post.comments ? post.comments.map(comment => `
                        <li class="comment-item">
                            <div class="comment-header">
                                <span class="comment-author">${comment.author}</span>
                                <span class="comment-time">${comment.createdAt}</span>
                            </div>
                            <div class="comment-content">${comment.content}</div>
                        </li>
                    `).join('') : ''}
                    <div class="comment-form">
                        <textarea placeholder="写下你的评论..."></textarea>
                        <button onclick="addComment(${post.id})">发表评论</button>
                    </div>
                </div>
            `;
            postList.appendChild(li);
        });
    }
}

function toggleComments(postId) {
    const commentsContainer = document.getElementById(`comments-${postId}`);
    if (commentsContainer) {
        if (commentsContainer.style.display === 'none') {
            commentsContainer.style.display = 'block';
        } else {
            commentsContainer.style.display = 'none';
        }
    }
}

function addComment(postId) {
    const commentsContainer = document.getElementById(`comments-${postId}`);
    const textarea = commentsContainer.querySelector('textarea');
    const commentText = textarea.value.trim();
    
    if (commentText) {
        const newComment = {
            id: Date.now(),
            author: '当前用户',
            content: commentText,
            createdAt: new Date().toLocaleString()
        };
        
        const commentItem = document.createElement('li');
        commentItem.className = 'comment-item';
        commentItem.innerHTML = `
            <div class="comment-header">
                <span class="comment-author">${newComment.author}</span>
                <span class="comment-time">${newComment.createdAt}</span>
            </div>
            <div class="comment-content">${newComment.content}</div>
        `;
        
        const commentList = commentsContainer.querySelector('.comment-list');
        const commentForm = commentsContainer.querySelector('.comment-form');
        commentsContainer.insertBefore(commentItem, commentForm);
        
        textarea.value = '';
        
        // 保存评论
        if (isOnline()) {
            fetch(`/api/community/comments/${postId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newComment)
            })
            .then(response => response.json())
            .then(data => {
                console.log('Comment added:', data);
            })
            .catch(error => {
                console.error('Error adding comment:', error);
                // 保存到本地存储
                const localComments = getFromLocalStorage('local_comments') || {};
                if (!localComments[postId]) {
                    localComments[postId] = [];
                }
                localComments[postId].push(newComment);
                saveToLocalStorage('local_comments', localComments);
            });
        } else {
            // 保存到本地存储
            const localComments = getFromLocalStorage('local_comments') || {};
            if (!localComments[postId]) {
                localComments[postId] = [];
            }
            localComments[postId].push(newComment);
            saveToLocalStorage('local_comments', localComments);
        }
    }
}

function createPost() {
    const title = document.getElementById('post-title').value;
    const content = document.getElementById('post-content').value;
    const category = document.getElementById('post-category').value;
    
    if (title && content) {
        const newPost = {
            id: Date.now(),
            title: title,
            content: content,
            author: '当前用户',
            createdAt: new Date().toLocaleString(),
            category: category,
            comments: []
        };
        
        if (isOnline()) {
            fetch('/api/community/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newPost)
            })
            .then(response => response.json())
            .then(data => {
                console.log('Post created:', data);
                loadCommunityPosts();
                // 清空表单
                document.getElementById('post-title').value = '';
                document.getElementById('post-content').value = '';
            })
            .catch(error => {
                console.error('Error creating post:', error);
                // 保存到本地存储
                const localPosts = getFromLocalStorage('local_posts') || [];
                localPosts.push(newPost);
                saveToLocalStorage('local_posts', localPosts);
                // 清空表单
                document.getElementById('post-title').value = '';
                document.getElementById('post-content').value = '';
            });
        } else {
            // 保存到本地存储
            const localPosts = getFromLocalStorage('local_posts') || [];
            localPosts.push(newPost);
            saveToLocalStorage('local_posts', localPosts);
            // 清空表单
            document.getElementById('post-title').value = '';
            document.getElementById('post-content').value = '';
        }
    }
}

// 个性化学习路径功能
function loadPersonalizedPath() {
    // 模拟用户进度数据
    const userProgress = {
        totalProgress: 45,
        completedCourses: ['Python基础', '数学基础', '机器学习基础'],
        currentPhase: 2,
        learningStyle: 'visual',
        strengths: ['编程', '数学'],
        weaknesses: ['深度学习']
    };
    
    // 生成推荐课程
    const recommendedCourses = generateRecommendedCourses(userProgress);
    const learningInsights = generateLearningInsights(userProgress);
    
    // 显示推荐课程
    displayRecommendedCourses(recommendedCourses);
    
    // 显示学习洞察
    displayLearningInsights(learningInsights);
}

function generateRecommendedCourses(userProgress) {
    // 课程库
    const courseLibrary = [
        {
            id: 1,
            title: '深度学习基础',
            description: '学习深度学习的基本概念和原理，包括神经网络结构和训练方法',
            difficulty: 'medium',
            relevance: 0.9,
            reason: '基于您的学习进度，深度学习是下一阶段的核心内容'
        },
        {
            id: 2,
            title: '神经网络进阶',
            description: '深入学习神经网络的高级概念，包括卷积神经网络和循环神经网络',
            difficulty: 'hard',
            relevance: 0.7,
            reason: '作为深度学习的进阶内容，帮助您巩固基础'
        },
        {
            id: 3,
            title: 'Python高级编程',
            description: '学习Python的高级特性，包括装饰器、生成器和上下文管理器',
            difficulty: 'medium',
            relevance: 0.6,
            reason: '提升您的编程能力，为深度学习实践做准备'
        },
        {
            id: 4,
            title: '数据可视化',
            description: '学习如何使用Python库进行数据可视化，包括Matplotlib和Seaborn',
            difficulty: 'easy',
            relevance: 0.5,
            reason: '帮助您更好地理解和展示数据，提升分析能力'
        }
    ];
    
    // 根据用户进度和偏好排序课程
    return courseLibrary
        .sort((a, b) => b.relevance - a.relevance)
        .slice(0, 3);
}

function displayRecommendedCourses(courses) {
    const container = document.getElementById('recommended-courses');
    if (container) {
        container.innerHTML = '<h5>推荐课程</h5>';
        
        if (courses.length > 0) {
            courses.forEach(course => {
                const courseElement = document.createElement('div');
                courseElement.className = 'course-recommendation';
                courseElement.innerHTML = `
                    <div class="course-recommendation-header">
                        <span class="course-recommendation-title">${course.title}</span>
                        <span class="course-recommendation-score">${Math.round(course.relevance * 100)}% 匹配</span>
                    </div>
                    <div class="course-recommendation-description">${course.description}</div>
                    <div class="course-recommendation-reason">推荐理由: ${course.reason}</div>
                `;
                container.appendChild(courseElement);
            });
        } else {
            displayDefaultRecommendations(container);
        }
    }
}

function generateLearningInsights(userProgress) {
    // 生成学习洞察
    const insights = [
        {
            id: 1,
            title: '学习进度分析',
            description: `您已完成 ${userProgress.totalProgress}% 的课程内容，处于第 ${userProgress.currentPhase} 阶段。建议您继续专注于当前阶段的核心内容。`
        },
        {
            id: 2,
            title: '优势与劣势',
            description: `您在 ${userProgress.strengths.join('、')} 方面表现优秀，但在 ${userProgress.weaknesses.join('、')} 方面需要加强。建议针对性地进行练习。`
        },
        {
            id: 3,
            title: '学习建议',
            description: '根据您的学习风格，建议您多使用可视化资源来理解深度学习概念，同时加强实践项目的练习。'
        }
    ];
    
    return insights;
}

function displayLearningInsights(insights) {
    const container = document.getElementById('learning-insights');
    if (container) {
        container.innerHTML = '<h5>学习洞察</h5>';
        
        insights.forEach(insight => {
            const insightElement = document.createElement('div');
            insightElement.className = 'insight-item';
            insightElement.innerHTML = `
                <div class="insight-title">${insight.title}</div>
                <div class="insight-description">${insight.description}</div>
            `;
            container.appendChild(insightElement);
        });
    }
}

function displayDefaultRecommendations(container) {
    container.innerHTML = `
        <h5>推荐课程</h5>
        <div class="course-recommendation">
            <div class="course-recommendation-header">
                <span class="course-recommendation-title">深度学习基础</span>
                <span class="course-recommendation-score">高优先级</span>
            </div>
            <div class="course-recommendation-description">学习深度学习的基本概念和原理，包括神经网络结构和训练方法</div>
            <div class="course-recommendation-reason">推荐理由: 作为AI学习的核心内容，深度学习是您下一阶段的重点</div>
        </div>
        <div class="course-recommendation">
            <div class="course-recommendation-header">
                <span class="course-recommendation-title">Python高级编程</span>
                <span class="course-recommendation-score">中优先级</span>
            </div>
            <div class="course-recommendation-description">学习Python的高级特性，包括装饰器、生成器和上下文管理器</div>
            <div class="course-recommendation-reason">推荐理由: 提升您的编程能力，为深度学习实践做准备</div>
        </div>
    `;
}

// 离线学习支持
function isOnline() {
    return navigator.onLine;
}

function saveToLocalStorage(key, data) {
    try {
        localStorage.setItem(key, JSON.stringify(data));
        return true;
    } catch (error) {
        console.error('Error saving to localStorage:', error);
        return false;
    }
}

function getFromLocalStorage(key) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    } catch (error) {
        console.error('Error getting from localStorage:', error);
        return null;
    }
}

// 网络状态监听器
window.addEventListener('online', function() {
    console.log('网络已连接，开始同步数据...');
    // 同步本地存储的数据
    syncLocalData();
});

window.addEventListener('offline', function() {
    console.log('网络已断开，切换到离线模式...');
});

function syncLocalData() {
    // 同步本地存储的进度数据
    const localProgress = getFromLocalStorage('progress_data');
    if (localProgress) {
        fetch('/api/progress', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(localProgress)
        })
        .then(response => response.json())
        .then(data => {
            console.log('进度数据同步成功');
            // 清除本地存储的数据
            localStorage.removeItem('progress_data');
        })
        .catch(error => {
            console.error('进度数据同步失败:', error);
        });
    }
    
    // 同步本地存储的测试结果
    const localResults = getFromLocalStorage('test_results');
    if (localResults) {
        localResults.forEach(result => {
            fetch('/api/assessments', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(result)
            })
            .then(response => response.json())
            .then(data => {
                console.log('测试结果同步成功');
            })
            .catch(error => {
                console.error('测试结果同步失败:', error);
            });
        });
        // 清除本地存储的数据
        localStorage.removeItem('test_results');
    }
    
    // 同步本地存储的帖子
    const localPosts = getFromLocalStorage('local_posts');
    if (localPosts) {
        localPosts.forEach(post => {
            fetch('/api/community/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(post)
            })
            .then(response => response.json())
            .then(data => {
                console.log('帖子同步成功');
            })
            .catch(error => {
                console.error('帖子同步失败:', error);
            });
        });
        // 清除本地存储的数据
        localStorage.removeItem('local_posts');
    }
    
    // 同步本地存储的评论
    const localComments = getFromLocalStorage('local_comments');
    if (localComments) {
        Object.keys(localComments).forEach(postId => {
            localComments[postId].forEach(comment => {
                fetch(`/api/community/comments/${postId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(comment)
                })
                .then(response => response.json())
                .then(data => {
                    console.log('评论同步成功');
                })
                .catch(error => {
                    console.error('评论同步失败:', error);
                });
            });
        });
        // 清除本地存储的数据
        localStorage.removeItem('local_comments');
    }
}

// 代码执行功能
function executeCode() {
    const code = document.getElementById('code-editor').value;
    const output = document.getElementById('output');
    
    if (!code) {
        output.textContent = '请输入要执行的代码';
        return;
    }
    
    output.textContent = '执行中...';
    
    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            output.textContent = `错误: ${data.error}\n${data.stderr}`;
        } else {
            if (data.stdout) {
                output.textContent = data.stdout;
            } else {
                output.textContent = '代码执行成功，无输出结果';
            }
            if (data.stderr) {
                output.textContent += `\n警告: ${data.stderr}`;
            }
        }
    })
    .catch(error => {
        console.error('Error executing code:', error);
        output.textContent = `执行错误: ${error.message}`;
    });
}

// 初始化CodeMirror编辑器
let codeEditor;

window.onload = function() {
    // 初始化CodeMirror编辑器
    if (window.CodeMirror) {
        codeEditor = CodeMirror.fromTextArea(document.getElementById('code-editor'), {
            lineNumbers: true,
            mode: 'python',
            theme: 'monokai',
            indentUnit: 4,
            indentWithTabs: false,
            viewportMargin: Infinity
        });
    }
    
    // 检查网络状态
    if (!isOnline()) {
        console.log('当前处于离线模式，数据将保存到本地存储');
    }
};

// 页面加载完成后执行
window.addEventListener('DOMContentLoaded', function() {
    // 不再添加额外的事件监听器，因为按钮已经有onclick属性
    // 初始化功能面板
    // const featureButtons = document.querySelectorAll('.feature-nav button');
    // featureButtons.forEach(button => {
    //     button.addEventListener('click', function() {
    //         const feature = this.id.replace('-btn', '');
    //         toggleFeature(feature);
    //     });
    // });
    
    // 不再自动打开任何面板，让用户手动选择
    // toggleFeature('progress');
});

# AI课程学习平台 - 项目结构

## 项目概述

这是一个前后端分离的AI课程学习平台，提供完整的在线学习体验。

## 项目结构

```
new_project/
├── frontend/                 # 前端代码
│   ├── templates/           # HTML模板文件
│   │   ├── preview_all.html
│   │   ├── course_content1.html
│   │   ├── course_content2.html
│   │   ├── course_content3.html
│   │   ├── test_connection.html
│   │   └── ui_test.html
│   ├── static/              # 静态资源文件
│   │   ├── css/            # 样式文件
│   │   │   └── styles.css
│   │   └── js/             # JavaScript文件
│   │       ├── config.js
│   │       ├── script.js
│   │       ├── script_fixes.js
│   │       ├── progress_tracker.js
│   │       ├── user_manager.js
│   │       └── generate_modals.js
│   ├── course_materials/     # 课程材料
│   │   ├── phase1_foundation/
│   │   ├── phase2_skill_enhancement/
│   │   └── phase3_advanced/
│   ├── projects/             # 项目文件
│   ├── CODING_STANDARDS.md
│   ├── DASHBOARD.md
│   ├── PROJECT_LOG.md
│   ├── README.md
│   ├── TASKS.md
│   ├── UI_TEST_REPORT.md
│   ├── PERFORMANCE_OPTIMIZATION.md
│   ├── ai_course_prompt.md
│   └── course_syllabus.md
├── backend/                 # 后端代码
│   ├── app.py              # Flask应用主文件
│   ├── backend.py           # 原后端文件
│   ├── combined_server.py    # 组合服务器
│   ├── local_model_client.py # 本地模型客户端
│   ├── requirements.txt      # Python依赖
│   ├── tests/              # 测试文件
│   └── users.json          # 用户数据存储（自动生成）
└── .gitignore             # Git忽略文件
```

## 技术栈

### 前端
- **HTML5**: 页面结构
- **CSS3**: 样式设计
- **JavaScript**: 交互逻辑
- **CodeMirror**: 代码编辑器
- **LocalStorage**: 本地数据存储

### 后端
- **Flask**: Web框架
- **Flask-CORS**: 跨域支持
- **JSON**: 数据存储格式

## 核心功能

### 1. 用户管理
- 用户注册
- 用户登录
- 用户资料管理
- 用户设置（主题、语言、通知）

### 2. 学习进度跟踪
- 章节完成标记
- 学习时长统计
- 进度可视化
- 数据导入导出

### 3. 课程内容
- 结构化课程展示
- 模态框内容管理
- 响应式设计

### 4. 代码执行
- 在线Python代码编辑器
- 实时代码执行
- 代码结果展示

## API接口

### 用户相关
- `POST /api/users` - 用户注册、登录、更新
- `GET /api/users` - 获取用户列表

### 进度相关
- `GET /api/progress?userId={id}` - 获取用户进度
- `POST /api/progress` - 更新用户进度
- `PUT /api/progress` - 更新章节状态

### 健康检查
- `GET /api/health` - API健康检查

## 安装和运行

### 后端安装
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 前端运行
直接在浏览器中打开 `frontend/templates/preview_all.html`

## 开发规范

- 前端代码放在 `frontend/` 目录
- 后端代码放在 `backend/` 目录
- 静态资源放在 `frontend/static/` 目录
- 模板文件放在 `frontend/templates/` 目录
- 遵循CODING_STANDARDS.md中的编码规范

## 数据存储

### 用户数据
- 存储位置: `backend/users.json`
- 格式: JSON
- 包含: 用户信息、进度数据、设置、统计

### 本地存储
- 键名: 见 `frontend/static/js/config.js`
- 用途: 未登录用户的临时数据存储

## 未来改进

- [ ] 添加数据库支持（SQLite/PostgreSQL）
- [ ] 实现用户认证（JWT）
- [ ] 添加单元测试
- [ ] 实现CI/CD流程
- [ ] 添加Docker支持
- [ ] 实现用户权限管理
- [ ] 添加学习推荐算法
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
from pathlib import Path
from trae_ai import TraeAI
from trae_config import get_trae_config

app = Flask(__name__)
CORS(app)

# 配置
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / 'frontend'
STATIC_DIR = FRONTEND_DIR / 'static'
TEMPLATES_DIR = FRONTEND_DIR / 'templates'

app.config['STATIC_FOLDER'] = str(STATIC_DIR)
app.config['TEMPLATES_FOLDER'] = str(TEMPLATES_DIR)

# 测试模式配置
if os.environ.get('TESTING'):
    # 测试模式下使用相对路径
    STATIC_DIR = 'static'
    TEMPLATES_DIR = 'templates'
    app.config['STATIC_FOLDER'] = STATIC_DIR
    app.config['TEMPLATES_FOLDER'] = TEMPLATES_DIR
else:
    # 生产模式使用绝对路径
    app.config['STATIC_FOLDER'] = str(STATIC_DIR)
    app.config['TEMPLATES_FOLDER'] = str(TEMPLATES_DIR)

# 用户数据存储
USERS_FILE = BASE_DIR / 'backend' / 'users.json'

def load_users():
    if USERS_FILE.exists():
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# 路由
@app.route('/')
def index():
    return send_from_directory(TEMPLATES_DIR, 'preview_all.html')

@app.route('/test')
def test_page():
    return send_from_directory(TEMPLATES_DIR, 'test_functions.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

@app.route('/templates/<path:filename>')
def serve_templates(filename):
    return send_from_directory(TEMPLATES_DIR, filename)

@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    users = load_users()
    
    if request.method == 'GET':
        return jsonify({'success': True, 'users': list(users.values())})
    
    elif request.method == 'POST':
        data = request.json
        action = data.get('action')
        
        if action == 'register':
            return register_user(users, data)
        elif action == 'login':
            return login_user(users, data)
        elif action == 'update':
            return update_user(users, data)
        elif action == 'logout':
            return jsonify({'success': True, 'message': '登出成功'})
        
        return jsonify({'success': False, 'error': '未知操作'})

def register_user(users, data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    # 验证
    if not username or len(username) < 3:
        return jsonify({'success': False, 'errors': ['用户名至少需要3个字符']})
    
    if '@' not in email:
        return jsonify({'success': False, 'errors': ['请输入有效的邮箱地址']})
    
    if not password or len(password) < 6:
        return jsonify({'success': False, 'errors': ['密码至少需要6个字符']})
    
    # 检查用户名和邮箱是否已存在
    for user in users.values():
        if user.get('username') == username:
            return jsonify({'success': False, 'errors': ['用户名已被使用']})
        if user.get('email') == email:
            return jsonify({'success': False, 'errors': ['邮箱已被注册']})
    
    # 创建新用户
    import time
    user_id = f"user_{int(time.time())}_{username}"
    
    new_user = {
        'id': user_id,
        'username': username,
        'email': email,
        'password': hash_password(password),
        'createdAt': time.strftime('%Y-%m-%dT%H:%M:%S'),
        'lastLogin': None,
        'settings': {
            'theme': 'light',
            'notifications': True,
            'language': 'zh-CN'
        },
        'progress': {
            'totalProgress': 0,
            'completedSections': [],
            'sectionProgress': {},
            'totalTime': 0,
            'lastStudied': None,
            'sessions': []
        },
        'statistics': {
            'totalSessions': 0,
            'averageSessionTime': 0,
            'longestSession': 0,
            'streakDays': 0,
            'lastStudyDate': None
        }
    }
    
    users[user_id] = new_user
    save_users(users)
    
    return jsonify({'success': True, 'user': new_user})

def login_user(users, data):
    username_or_email = data.get('usernameOrEmail')
    password = data.get('password')
    
    for user_id, user in users.items():
        if user.get('username') == username_or_email or user.get('email') == username_or_email:
            if user.get('password') == hash_password(password):
                import time
                user['lastLogin'] = time.strftime('%Y-%m-%dT%H:%M:%S')
                users[user_id] = user
                save_users(users)
                return jsonify({'success': True, 'user': user})
            else:
                return jsonify({'success': False, 'error': '密码错误'})
    
    return jsonify({'success': False, 'error': '用户名或邮箱不存在'})

def update_user(users, data):
    user_id = data.get('userId')
    if user_id not in users:
        return jsonify({'success': False, 'error': '用户不存在'})
    
    user = users[user_id]
    
    # 更新进度
    if 'progress' in data:
        user['progress'] = data['progress']
    
    # 更新设置
    if 'settings' in data:
        user['settings'].update(data['settings'])
    
    users[user_id] = user
    save_users(users)
    
    return jsonify({'success': True, 'user': user})

def hash_password(password):
    hash_value = 0
    for char in password:
        hash_value = ((hash_value << 5) - hash_value) + ord(char)
        hash_value = hash_value & hash_value
    return str(hash_value)

@app.route('/api/progress', methods=['GET', 'POST', 'PUT'])
def handle_progress():
    if request.method == 'GET':
        user_id = request.args.get('userId')
        if not user_id:
            return jsonify({'success': False, 'error': '缺少用户ID'})
        
        users = load_users()
        if user_id not in users:
            return jsonify({'success': False, 'error': '用户不存在'})
        
        return jsonify({'success': True, 'progress': users[user_id].get('progress', {})})
    
    elif request.method == 'POST':
        data = request.json
        user_id = data.get('userId')
        progress = data.get('progress')
        
        if not user_id or not progress:
            return jsonify({'success': False, 'error': '缺少必要参数'})
        
        users = load_users()
        if user_id not in users:
            return jsonify({'success': False, 'error': '用户不存在'})
        
        users[user_id]['progress'] = progress
        save_users(users)
        
        return jsonify({'success': True, 'message': '进度更新成功'})
    
    elif request.method == 'PUT':
        data = request.json
        user_id = data.get('userId')
        section_id = data.get('sectionId')
        action = data.get('action')
        
        if not user_id or not section_id or not action:
            return jsonify({'success': False, 'error': '缺少必要参数'})
        
        users = load_users()
        if user_id not in users:
            return jsonify({'success': False, 'error': '用户不存在'})
        
        user = users[user_id]
        progress = user.get('progress', {})
        completed_sections = progress.get('completedSections', [])
        
        if action == 'complete':
            if section_id not in completed_sections:
                completed_sections.append(section_id)
        elif action == 'incomplete':
            if section_id in completed_sections:
                completed_sections.remove(section_id)
        
        progress['completedSections'] = completed_sections
        
        # 计算总进度
        total_sections = 60  # 假设有60个章节
        progress['totalProgress'] = int((len(completed_sections) / total_sections) * 100)
        
        users[user_id]['progress'] = progress
        save_users(users)
        
        return jsonify({'success': True, 'message': '章节状态更新成功'})

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy', 'message': 'API运行正常'})

# Trae AI 相关API端点
@app.route('/api/trae/generate-code', methods=['POST'])
def trae_generate_code():
    """
    Trae AI 代码生成接口
    """
    data = request.json
    prompt = data.get('prompt', '')
    language = data.get('language', 'python')
    context = data.get('context')
    max_tokens = data.get('max_tokens', 2000)
    
    trae_ai = TraeAI()
    result = trae_ai.generate_code(prompt, language, context, max_tokens)
    
    return jsonify(result)

@app.route('/api/trae/explain-code', methods=['POST'])
def trae_explain_code():
    """
    Trae AI 代码解释接口
    """
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'python')
    
    trae_ai = TraeAI()
    result = trae_ai.explain_code(code, language)
    
    return jsonify(result)

@app.route('/api/trae/optimize-code', methods=['POST'])
def trae_optimize_code():
    """
    Trae AI 代码优化接口
    """
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'python')
    optimization_type = data.get('optimization_type', 'performance')
    
    trae_ai = TraeAI()
    result = trae_ai.optimize_code(code, language, optimization_type)
    
    return jsonify(result)

@app.route('/api/trae/debug-code', methods=['POST'])
def trae_debug_code():
    """
    Trae AI 代码调试接口
    """
    data = request.json
    code = data.get('code', '')
    error_message = data.get('error_message')
    language = data.get('language', 'python')
    
    trae_ai = TraeAI()
    result = trae_ai.debug_code(code, error_message, language)
    
    return jsonify(result)

@app.route('/api/trae/chat', methods=['POST'])
def trae_chat():
    """
    Trae AI 对话接口
    """
    data = request.json
    message = data.get('message', '')
    conversation_history = data.get('conversation_history')
    model = data.get('model', 'gpt-4o')
    
    trae_ai = TraeAI()
    result = trae_ai.chat(message, conversation_history, model)
    
    return jsonify(result)

@app.route('/api/trae/analyze-content', methods=['POST'])
def trae_analyze_content():
    """
    Trae AI 课程内容分析接口
    """
    data = request.json
    content = data.get('content', '')
    analysis_type = data.get('analysis_type', 'completeness')
    
    trae_ai = TraeAI()
    result = trae_ai.analyze_course_content(content, analysis_type)
    
    return jsonify(result)

@app.route('/api/trae/generate-quiz', methods=['POST'])
def trae_generate_quiz():
    """
    Trae AI 测验生成接口
    """
    data = request.json
    topic = data.get('topic', '')
    difficulty = data.get('difficulty', 'medium')
    count = data.get('count', 5)
    
    trae_ai = TraeAI()
    result = trae_ai.generate_quiz_questions(topic, difficulty, count)
    
    return jsonify(result)

@app.route('/api/trae/suggest-path', methods=['POST'])
def trae_suggest_path():
    """
    Trae AI 学习路径推荐接口
    """
    data = request.json
    user_level = data.get('user_level', 'beginner')
    user_goals = data.get('user_goals', [])
    available_time = data.get('available_time', 10)
    
    trae_ai = TraeAI()
    result = trae_ai.suggest_learning_path(user_level, user_goals, available_time)
    
    return jsonify(result)

@app.route('/api/trae/config', methods=['GET', 'POST', 'PUT'])
def trae_config():
    """
    Trae AI 配置管理接口
    """
    config = get_trae_config()
    
    if request.method == 'GET':
        return jsonify({
            'success': True,
            'config': config.config
        })
    
    elif request.method == 'POST':
        data = request.json
        action = data.get('action')
        
        if action == 'set_api_key':
            api_key = data.get('api_key', '')
            success = config.set_api_key(api_key)
            return jsonify({'success': success})
        
        elif action == 'set_model':
            model_type = data.get('model_type', 'default')
            model_name = data.get('model_name', 'gpt-4o')
            success = config.set_model(model_type, model_name)
            return jsonify({'success': success})
        
        elif action == 'enable_feature':
            feature = data.get('feature', '')
            success = config.enable_feature(feature)
            return jsonify({'success': success})
        
        elif action == 'disable_feature':
            feature = data.get('feature', '')
            success = config.disable_feature(feature)
            return jsonify({'success': success})
        
        elif action == 'reset':
            success = config.reset_to_default()
            return jsonify({'success': success})
        
        return jsonify({'success': False, 'error': '未知操作'})

if __name__ == '__main__':
    # 确保必要的目录存在
    USERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # 初始化用户数据文件
    if not USERS_FILE.exists():
        save_users({})
    
    app.run(debug=False, host='0.0.0.0', port=5000)
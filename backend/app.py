from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json
from pathlib import Path

app = Flask(__name__)
CORS(app)

# 配置
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / 'frontend'
STATIC_DIR = FRONTEND_DIR / 'static'
TEMPLATES_DIR = FRONTEND_DIR / 'templates'

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

@app.route('/<path:filename>')
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

if __name__ == '__main__':
    # 确保必要的目录存在
    USERS_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # 初始化用户数据文件
    if not USERS_FILE.exists():
        save_users({})
    
    app.run(debug=True, host='0.0.0.0', port=5000)
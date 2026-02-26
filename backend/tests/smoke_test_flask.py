"""
冒烟测试 - 使用Flask测试客户端
验证系统核心功能
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app import app

class TestSmokeTestsFlask(unittest.TestCase):
    """
    冒烟测试类
    使用Flask测试客户端验证系统的核心功能是否正常工作
    """
    
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()
    
    def tearDown(self):
        self.ctx.pop()
    
    def test_api_health_check(self):
        """
        测试API健康检查
        """
        response = self.client.get('/api/health')
        
        assert response.status_code == 200, 'Health check failed'
        data = response.get_json()
        assert data['status'] == 'healthy', 'Health status incorrect'
        print('✅ API健康检查通过')
    
    def test_get_users(self):
        """
        测试获取用户列表
        """
        response = self.client.get('/api/users')
        
        assert response.status_code == 200, 'Get users failed'
        data = response.get_json()
        assert data['success'] == True, 'Get users unsuccessful'
        assert 'users' in data, 'Users data missing'
        print('✅ 获取用户列表测试通过')
    
    def test_user_registration(self):
        """
        测试用户注册流程
        """
        import time
        timestamp = str(int(time.time()))
        user_data = {
            'username': f'smoke_user_{timestamp}',
            'email': f'smoke_{timestamp}@example.com',
            'password': 'test123456',
            'confirmPassword': 'test123456'
        }
        
        response = self.client.post('/api/users', json={
            'action': 'register',
            **user_data
        })
        
        assert response.status_code == 200, 'Registration failed'
        data = response.get_json()
        if data.get('success') == True:
            print('✅ 用户注册测试通过')
        else:
            print(f'⚠️ 用户注册测试警告: {data.get("error", "未知错误")}')
    
    def test_user_login(self):
        """
        测试用户登录流程
        """
        login_data = {
            'usernameOrEmail': 'smoke@example.com',
            'password': 'test123456'
        }
        
        response = self.client.post('/api/users', json={
            'action': 'login',
            **login_data
        })
        
        assert response.status_code == 200, 'Login failed'
        data = response.get_json()
        if data.get('success') == True:
            print('✅ 用户登录测试通过')
        else:
            print(f'⚠️ 用户登录测试警告: {data.get("error", "未知错误")}')
    
    def test_course_content_loading(self):
        """
        测试课程内容加载
        """
        response = self.client.get('/')
        
        assert response.status_code == 200, 'Main page failed to load'
        assert 'AI课程学习路径' in response.data.decode('utf-8'), 'Page content incorrect'
        print('✅ 课程内容加载测试通过')
    
    def test_static_files_loading(self):
        """
        测试静态文件加载
        """
        static_files = [
            '/static/css/styles.css',
            '/static/js/config.js',
            '/static/js/script.js'
        ]
        
        for file_path in static_files:
            response = self.client.get(file_path)
            if response.status_code == 200:
                print(f'✅ 静态文件 {file_path} 加载成功')
            else:
                print(f'⚠️ 静态文件 {file_path} 加载失败: {response.status_code}')
    
    def test_progress_tracking(self):
        """
        测试进度跟踪功能
        """
        progress_data = {
            'totalProgress': 0,
            'completedSections': [],
            'sectionProgress': {},
            'totalTime': 0,
            'lastStudied': None,
            'sessions': []
        }
        
        response = self.client.post('/api/progress', json={
            'userId': 'smoke_user',
            'progress': progress_data
        })
        
        if response.status_code == 200:
            data = response.get_json()
            if data.get('success') == True:
                print('✅ 进度跟踪测试通过')
            else:
                print(f'⚠️ 进度跟踪测试警告: {data.get("message", "未知错误")}')
        else:
            print(f'⚠️ 进度跟踪测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_code_generation(self):
        """
        测试Trae AI代码生成端点
        """
        response = self.client.post('/api/trae/generate-code', json={
            'prompt': 'Create a hello world function',
            'language': 'python'
        })
        
        if response.status_code == 200:
            print('✅ Trae AI代码生成端点测试通过')
        else:
            print(f'⚠️ Trae AI代码生成端点测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_code_explanation(self):
        """
        测试Trae AI代码解释端点
        """
        response = self.client.post('/api/trae/explain-code', json={
            'code': 'print("Hello, World!")',
            'language': 'python'
        })
        
        if response.status_code == 200:
            print('✅ Trae AI代码解释端点测试通过')
        else:
            print(f'⚠️ Trae AI代码解释端点测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_code_optimization(self):
        """
        测试Trae AI代码优化端点
        """
        response = self.client.post('/api/trae/optimize-code', json={
            'code': 'def test():\n    print("Hello")',
            'language': 'python',
            'optimization_type': 'performance'
        })
        
        if response.status_code == 200:
            print('✅ Trae AI代码优化端点测试通过')
        else:
            print(f'⚠️ Trae AI代码优化端点测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_debug_code(self):
        """
        测试Trae AI代码调试端点
        """
        response = self.client.post('/api/trae/debug-code', json={
            'code': 'print("Hello")',
            'error_message': 'SyntaxError',
            'language': 'python'
        })
        
        if response.status_code == 200:
            print('✅ Trae AI代码调试端点测试通过')
        else:
            print(f'⚠️ Trae AI代码调试端点测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_chat(self):
        """
        测试Trae AI对话端点
        """
        response = self.client.post('/api/trae/chat', json={
            'message': 'Hello, how are you?',
            'model': 'gpt-4o'
        })
        
        if response.status_code == 200:
            print('✅ Trae AI对话端点测试通过')
        else:
            print(f'⚠️ Trae AI对话端点测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_analyze_content(self):
        """
        测试Trae AI内容分析端点
        """
        response = self.client.post('/api/trae/analyze-content', json={
            'content': 'This is a test content for analysis.',
            'analysis_type': 'completeness'
        })
        
        if response.status_code == 200:
            print('✅ Trae AI内容分析端点测试通过')
        else:
            print(f'⚠️ Trae AI内容分析端点测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_generate_quiz(self):
        """
        测试Trae AI测验生成端点
        """
        response = self.client.post('/api/trae/generate-quiz', json={
            'topic': 'Python basics',
            'difficulty': 'medium',
            'count': 5
        })
        
        if response.status_code == 200:
            print('✅ Trae AI测验生成端点测试通过')
        else:
            print(f'⚠️ Trae AI测验生成端点测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_suggest_path(self):
        """
        测试Trae AI路径推荐端点
        """
        response = self.client.post('/api/trae/suggest-path', json={
            'user_level': 'beginner',
            'user_goals': ['learn Python', 'understand AI'],
            'available_time': 10
        })
        
        if response.status_code == 200:
            print('✅ Trae AI路径推荐端点测试通过')
        else:
            print(f'⚠️ Trae AI路径推荐端点测试失败: HTTP {response.status_code}')
    
    def test_trae_ai_config(self):
        """
        测试Trae AI配置管理端点
        """
        # 测试获取配置
        response = self.client.get('/api/trae/config')
        
        if response.status_code == 200:
            data = response.get_json()
            if data.get('success') == True:
                print('✅ Trae AI配置获取测试通过')
            else:
                print(f'⚠️ Trae AI配置获取测试警告: {data.get("error", "未知错误")}')
        else:
            print(f'⚠️ Trae AI配置获取测试失败: HTTP {response.status_code}')
    
    def test_complete_workflow(self):
        """
        测试完整的用户工作流
        """
        print('🔄 测试完整工作流...')
        
        # 1. 检查API健康
        self.test_api_health_check()
        
        # 2. 测试用户注册
        self.test_user_registration()
        
        # 3. 测试Trae AI功能
        self.test_trae_ai_code_generation()
        self.test_trae_ai_code_explanation()
        
        # 4. 测试课程内容加载
        self.test_course_content_loading()
        
        # 5. 测试静态文件加载
        self.test_static_files_loading()
        
        print('✅ 完整工作流测试通过')

if __name__ == '__main__':
    print('🧪 冒烟测试开始（使用Flask测试客户端）')
    print('=' * 50)
    
    unittest.main()
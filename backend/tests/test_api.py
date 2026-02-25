import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

from app import app, load_users, save_users

class TestUserAPI(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.test_users = {
            'test_user_1': {
                'id': 'test_user_1',
                'username': 'testuser1',
                'email': 'test1@example.com',
                'password': '123456',
                'createdAt': '2024-01-01T00:00:00',
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
        }
    
    def tearDown(self):
        pass
    
    def test_health_check(self):
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['status'] == 'healthy')
        print('✅ 健康检查测试通过')
    
    def test_get_users(self):
        response = self.app.get('/api/users')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertIsInstance(data['users'], list)
        print('✅ 获取用户列表测试通过')
    
    def test_user_register_success(self):
        response = self.app.post('/api/users', json={
            'action': 'register',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123',
            'confirmPassword': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertIn('user', data)
        self.assertEqual(data['user']['username'], 'newuser')
        print('✅ 用户注册成功测试通过')
    
    def test_user_register_short_username(self):
        response = self.app.post('/api/users', json={
            'action': 'register',
            'username': 'ab',
            'email': 'test@example.com',
            'password': 'password123',
            'confirmPassword': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertFalse(data['success'])
        self.assertIn('errors', data)
        print('✅ 用户注册验证测试通过（用户名太短）')
    
    def test_user_register_invalid_email(self):
        response = self.app.post('/api/users', json={
            'action': 'register',
            'username': 'testuser',
            'email': 'invalid-email',
            'password': 'password123',
            'confirmPassword': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertFalse(data['success'])
        self.assertIn('errors', data)
        print('✅ 用户注册验证测试通过（邮箱格式错误）')
    
    def test_user_login_success(self):
        response = self.app.post('/api/users', json={
            'action': 'login',
            'usernameOrEmail': 'testuser1',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertIn('user', data)
        self.assertEqual(data['user']['username'], 'testuser1')
        print('✅ 用户登录成功测试通过')
    
    def test_user_login_wrong_password(self):
        response = self.app.post('/api/users', json={
            'action': 'login',
            'usernameOrEmail': 'testuser1',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertFalse(data['success'])
        self.assertIn('error', data)
        print('✅ 用户登录验证测试通过（密码错误）')
    
    def test_get_progress(self):
        response = self.app.get('/api/progress?userId=test_user_1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertIn('progress', data)
        print('✅ 获取进度测试通过')
    
    def test_update_progress(self):
        response = self.app.post('/api/progress', json={
            'userId': 'test_user_1',
            'progress': {
                'totalProgress': 50,
                'completedSections': ['section1', 'section2'],
                'sectionProgress': {},
                'totalTime': 120,
                'lastStudied': '2024-01-15T10:00:00',
                'sessions': []
            }
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        print('✅ 更新进度测试通过')
    
    def test_update_section_complete(self):
        response = self.app.put('/api/progress', json={
            'userId': 'test_user_1',
            'sectionId': 'section3',
            'action': 'complete'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        print('✅ 完成章节测试通过')
    
    def test_update_section_incomplete(self):
        response = self.app.put('/api/progress', json={
            'userId': 'test_user_1',
            'sectionId': 'section1',
            'action': 'incomplete'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        print('✅ 取消完成章节测试通过')

class TestFrontendRoutes(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def tearDown(self):
        pass
    
    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        print('✅ 主页路由测试通过')
    
    def test_test_page_route(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 200)
        print('✅ 测试页面路由通过')
    
    def test_static_file_route(self):
        response = self.app.get('/static/js/config.js')
        self.assertEqual(response.status_code, 200)
        print('✅ 静态文件路由测试通过')
    
    def test_template_file_route(self):
        response = self.app.get('/templates/preview_all.html')
        self.assertEqual(response.status_code, 200)
        print('✅ 模板文件路由测试通过')

class TestDataStorage(unittest.TestCase):
    
    def test_load_users(self):
        users = load_users()
        self.assertIsInstance(users, dict)
        print('✅ 加载用户数据测试通过')
    
    def test_save_users(self):
        test_data = {
            'test_id': {
                'username': 'test',
                'email': 'test@example.com'
            }
        }
        save_users(test_data)
        loaded = load_users()
        self.assertIn('test_id', loaded)
        print('✅ 保存用户数据测试通过')

def run_tests():
    print('=' * 50)
    print('🧪 AI课程学习平台 - 单元测试')
    print('=' * 50)
    print()
    
    suite = unittest.TestSuite()
    
    suite.addTests(unittest.makeSuite(TestUserAPI))
    suite.addTests(unittest.makeSuite(TestFrontendRoutes))
    suite.addTests(unittest.makeSuite(TestDataStorage))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    print('=' * 50)
    print('📊 测试结果统计')
    print('=' * 50)
    print(f'总测试数: {result.testsRun}')
    print(f'成功数: {result.testsRun - len(result.failures)}')
    print(f'失败数: {len(result.failures)}')
    print(f'成功率: {((result.testsRun - len(result.failures)) / result.testsRun * 100):.1f}%')
    
    if result.wasSuccessful():
        print('\n🎉 所有单元测试通过！')
        return 0
    else:
        print('\n⚠️  部分测试失败，请检查错误信息')
        print('\n失败的测试:')
        for test, traceback in result.failures:
            print(f'  - {test}: {traceback}')
        return 1

if __name__ == '__main__':
    sys.exit(run_tests())
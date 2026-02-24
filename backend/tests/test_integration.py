import os
import json
import unittest
import threading
import time
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from combined_server import run_server

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # 启动服务器线程
        self.server_thread = threading.Thread(target=run_server, args=(8002,))
        self.server_thread.daemon = True
        self.server_thread.start()
        
        # 等待服务器启动
        time.sleep(1)
        
        self.base_url = 'http://localhost:8002'
        self.test_user_id = 'integration_test_user'
    
    def tearDown(self):
        # 服务器线程会在测试结束后自动终止
        pass
    
    def test_complete_user_flow(self):
        """测试完整的用户流程：更新进度 -> 提交测验 -> 查看进度"""
        try:
            # 1. 更新课程进度
            progress_data = {
                'userId': self.test_user_id,
                'section': 'python-basics',
                'completed': True,
                'progress': 100,
                'timeSpent': 120
            }
            
            req = Request(
                f'{self.base_url}/api/progress',
                data=json.dumps(progress_data).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            
            response = urlopen(req)
            self.assertEqual(response.getcode(), 200)
            progress_result = json.loads(response.read().decode('utf-8'))
            self.assertTrue(progress_result.get('success'))
            
            # 2. 提交测验
            assessment_data = {
                'userId': self.test_user_id,
                'quizId': 'python-basics-quiz',
                'score': 85,
                'total': 100,
                'answers': {'q1': 'a', 'q2': 'b', 'q3': 'c'}
            }
            
            req = Request(
                f'{self.base_url}/api/assessments',
                data=json.dumps(assessment_data).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            
            response = urlopen(req)
            self.assertEqual(response.getcode(), 200)
            assessment_result = json.loads(response.read().decode('utf-8'))
            self.assertTrue(assessment_result.get('success'))
            
            # 3. 查看用户进度
            response = urlopen(f'{self.base_url}/api/progress')
            self.assertEqual(response.getcode(), 200)
            progress_data = json.loads(response.read().decode('utf-8'))
            self.assertIn(self.test_user_id, progress_data)
            user_progress = progress_data[self.test_user_id]
            self.assertIn('python-basics', user_progress['sections'])
            
            # 4. 查看测验结果
            response = urlopen(f'{self.base_url}/api/assessments')
            self.assertEqual(response.getcode(), 200)
            assessment_data = json.loads(response.read().decode('utf-8'))
            self.assertIn(self.test_user_id, assessment_data)
            user_assessments = assessment_data[self.test_user_id]
            self.assertGreater(len(user_assessments), 0)
            
        except HTTPError as e:
            self.fail(f'Integration test failed with status {e.code}')
    
    def test_community_integration(self):
        """测试社区功能集成：创建帖子 -> 添加评论 -> 查看社区"""
        try:
            # 1. 创建帖子
            post_data = {
                'author': 'Test User',
                'title': '测试帖子',
                'content': '这是一个测试帖子内容',
                'category': 'general'
            }
            
            req = Request(
                f'{self.base_url}/api/community/posts',
                data=json.dumps(post_data).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            
            response = urlopen(req)
            self.assertEqual(response.getcode(), 200)
            post_result = json.loads(response.read().decode('utf-8'))
            self.assertTrue(post_result.get('success'))
            post_id = post_result['post']['id']
            
            # 2. 添加评论
            comment_data = {
                'author': 'Commenter',
                'content': '这是一个测试评论'
            }
            
            req = Request(
                f'{self.base_url}/api/community/comments/{post_id}',
                data=json.dumps(comment_data).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            
            response = urlopen(req)
            self.assertEqual(response.getcode(), 200)
            comment_result = json.loads(response.read().decode('utf-8'))
            self.assertTrue(comment_result.get('success'))
            
            # 3. 查看社区数据
            response = urlopen(f'{self.base_url}/api/community')
            self.assertEqual(response.getcode(), 200)
            community_data = json.loads(response.read().decode('utf-8'))
            
            # 验证帖子存在
            posts = community_data.get('posts', [])
            test_post = next((p for p in posts if p['id'] == post_id), None)
            self.assertIsNotNone(test_post)
            self.assertEqual(test_post['title'], '测试帖子')
            
            # 验证评论存在
            comments = community_data.get('comments', {})
            post_comments = comments.get(str(post_id), [])
            self.assertGreater(len(post_comments), 0)
            
        except HTTPError as e:
            self.fail(f'Community integration test failed with status {e.code}')
    
    def test_code_execution_integration(self):
        """测试代码执行与课程内容的集成"""
        try:
            # 测试执行Python代码
            code_data = {
                'code': '''
# 测试基本Python功能
print("Hello, AI Course!")

# 测试数学运算
result = 2 + 2 * 3
print(f"计算结果: {result}")

# 测试条件语句
if result > 5:
    print("结果大于5")
else:
    print("结果小于等于5")
'''
            }
            
            req = Request(
                f'{self.base_url}/execute',
                data=json.dumps(code_data).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            
            response = urlopen(req)
            self.assertEqual(response.getcode(), 200)
            execution_result = json.loads(response.read().decode('utf-8'))
            
            # 验证执行结果
            stdout = execution_result.get('stdout', '')
            self.assertIn('Hello, AI Course!', stdout)
            self.assertIn('计算结果: 8', stdout)
            self.assertIn('结果大于5', stdout)
            self.assertEqual(execution_result.get('returncode'), 0)
            
        except HTTPError as e:
            self.fail(f'Code execution integration test failed with status {e.code}')

if __name__ == '__main__':
    unittest.main()

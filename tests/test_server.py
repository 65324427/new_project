import os
import json
import unittest
import threading
import time
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from combined_server import run_server

class TestServer(unittest.TestCase):
    def setUp(self):
        # 启动服务器线程
        self.server_thread = threading.Thread(target=run_server, args=(8001,))
        self.server_thread.daemon = True
        self.server_thread.start()
        
        # 等待服务器启动
        time.sleep(1)
        
        self.base_url = 'http://localhost:8001'
    
    def tearDown(self):
        # 服务器线程会在测试结束后自动终止
        pass
    
    def test_root_endpoint(self):
        # 测试根端点
        try:
            response = urlopen(f'{self.base_url}/')
            self.assertEqual(response.getcode(), 200)
            content_type = response.getheader('Content-Type')
            self.assertIn('text/html', content_type)
        except HTTPError as e:
            self.fail(f'Root endpoint failed with status {e.code}')
    
    def test_api_progress_get(self):
        # 测试获取进度API
        try:
            response = urlopen(f'{self.base_url}/api/progress')
            self.assertEqual(response.getcode(), 200)
            content_type = response.getheader('Content-Type')
            self.assertIn('application/json', content_type)
            
            # 解析响应
            data = json.loads(response.read().decode('utf-8'))
            self.assertIsInstance(data, dict)
        except HTTPError as e:
            self.fail(f'API progress GET failed with status {e.code}')
    
    def test_api_progress_post(self):
        # 测试更新进度API
        try:
            data = {
                'userId': 'test_user',
                'section': 'test_section',
                'completed': True,
                'progress': 100,
                'timeSpent': 60
            }
            
            req = Request(
                f'{self.base_url}/api/progress',
                data=json.dumps(data).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            
            response = urlopen(req)
            self.assertEqual(response.getcode(), 200)
            
            # 解析响应
            result = json.loads(response.read().decode('utf-8'))
            self.assertTrue(result.get('success'))
        except HTTPError as e:
            self.fail(f'API progress POST failed with status {e.code}')
    
    def test_execute_endpoint(self):
        # 测试代码执行端点
        try:
            data = {
                'code': 'print("Hello, World!")'
            }
            
            req = Request(
                f'{self.base_url}/execute',
                data=json.dumps(data).encode('utf-8'),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            
            response = urlopen(req)
            self.assertEqual(response.getcode(), 200)
            
            # 解析响应
            result = json.loads(response.read().decode('utf-8'))
            self.assertIn('stdout', result)
            self.assertIn('Hello, World!', result['stdout'])
        except HTTPError as e:
            self.fail(f'Execute endpoint failed with status {e.code}')
    
    def test_api_community_get(self):
        # 测试获取社区API
        try:
            response = urlopen(f'{self.base_url}/api/community')
            self.assertEqual(response.getcode(), 200)
            content_type = response.getheader('Content-Type')
            self.assertIn('application/json', content_type)
            
            # 解析响应
            data = json.loads(response.read().decode('utf-8'))
            self.assertIsInstance(data, dict)
            self.assertIn('posts', data)
            self.assertIsInstance(data['posts'], list)
        except HTTPError as e:
            self.fail(f'API community GET failed with status {e.code}')

if __name__ == '__main__':
    unittest.main()

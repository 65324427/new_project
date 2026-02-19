import os
import json
import unittest
import shutil
from combined_server import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        # 创建临时数据目录
        self.test_data_dir = 'test_data'
        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)
        os.makedirs(self.test_data_dir)
        
        # 创建新的DataManager实例
        self.data_manager = DataManager()
        # 修改实例的data_dir属性
        self.data_manager.data_dir = self.test_data_dir
        # 重新初始化数据文件
        self.data_manager._ensure_data_dir()
        self.data_manager._init_data_files()
    
    def tearDown(self):
        # 清理测试数据目录
        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)
    
    def test_ensure_data_dir(self):
        # 测试数据目录创建
        self.assertTrue(os.path.exists(self.test_data_dir))
    
    def test_init_data_files(self):
        # 测试数据文件初始化
        expected_files = ['progress.json', 'assessments.json', 'community.json']
        for filename in expected_files:
            filepath = os.path.join(self.test_data_dir, filename)
            self.assertTrue(os.path.exists(filepath))
            
            # 测试文件内容
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if filename == 'progress.json':
                    self.assertEqual(data, {})
                elif filename == 'assessments.json':
                    self.assertEqual(data, {})
                elif filename == 'community.json':
                    self.assertEqual(data, {'posts': [], 'comments': {}})
    
    def test_read_file(self):
        # 测试读取文件
        test_file = os.path.join(self.test_data_dir, 'test.json')
        test_data = {'key': 'value'}
        
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f)
        
        result = self.data_manager._read_file('test.json')
        self.assertEqual(result, test_data)
    
    def test_read_nonexistent_file(self):
        # 测试读取不存在的文件
        result = self.data_manager._read_file('nonexistent.json')
        self.assertEqual(result, {})
    
    def test_write_file(self):
        # 测试写入文件
        test_data = {'key': 'value'}
        self.data_manager._write_file('test_write.json', test_data)
        
        filepath = os.path.join(self.test_data_dir, 'test_write.json')
        self.assertTrue(os.path.exists(filepath))
        
        with open(filepath, 'r', encoding='utf-8') as f:
            result = json.load(f)
            self.assertEqual(result, test_data)

if __name__ == '__main__':
    unittest.main()

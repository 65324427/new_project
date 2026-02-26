"""
自动化测试脚本
自动执行GitHub skill测试并记录结果
"""

import subprocess
import sys
import os
from datetime import datetime

class TestRunner:
    """
    测试运行器
    """
    
    def __init__(self):
        self.test_results = []
        self.test_log_file = 'github_skills/test_results.log'
    
    def log_test(self, test_name, result, details=""):
        """
        记录测试结果
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] 测试: {test_name} - 结果: {result}\n"
        if details:
            log_entry += f"详情: {details}\n"
        log_entry += "-" * 50 + "\n"
        
        # 写入日志文件
        with open(self.test_log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        
        print(log_entry)
        self.test_results.append({
            'test_name': test_name,
            'result': result,
            'details': details,
            'timestamp': timestamp
        })
    
    def run_test(self, test_name, test_command, description=""):
        """
        运行单个测试
        """
        print(f"\n{'=' * 60}")
        print(f"运行测试: {test_name}")
        print(f"描述: {description}")
        print(f"{'=' * 60}\n")
        
        try:
            # 运行测试命令
            result = subprocess.run(
                test_command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            # 分析结果
            if result.returncode == 0:
                self.log_test(test_name, "通过", result.stdout)
                return True
            else:
                error_msg = result.stderr if result.stderr else "未知错误"
                self.log_test(test_name, "失败", error_msg)
                return False
                
        except subprocess.TimeoutExpired:
            self.log_test(test_name, "超时", "测试执行超过60秒")
            return False
        except Exception as e:
            self.log_test(test_name, "异常", str(e))
            return False
    
    def generate_summary(self):
        """
        生成测试摘要
        """
        print(f"\n{'=' * 60}")
        print("测试摘要")
        print(f"{'=' * 60}\n")
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results if r['result'] == '通过')
        failed_tests = total_tests - passed_tests
        
        print(f"总测试数: {total_tests}")
        print(f"通过: {passed_tests}")
        print(f"失败: {failed_tests}")
        print(f"成功率: {(passed_tests/total_tests*100):.1f}%")
        print(f"\n{'=' * 60}\n")
        
        # 写入摘要到日志文件
        with open(self.test_log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{'=' * 60}\n")
            f.write("测试摘要\n")
            f.write(f"{'=' * 60}\n")
            f.write(f"总测试数: {total_tests}\n")
            f.write(f"通过: {passed_tests}\n")
            f.write(f"失败: {failed_tests}\n")
            f.write(f"成功率: {(passed_tests/total_tests*100):.1f}%\n")
            f.write(f"\n{'=' * 60}\n")

def main():
    """
    主函数
    """
    runner = TestRunner()
    
    print("🧪 自动化测试开始")
    print("=" * 60)
    print()
    
    # 测试1: 运行Flask冒烟测试
    runner.run_test(
        test_name="Flask冒烟测试",
        test_command="cd backend/tests && python -m unittest smoke_test_flask -v",
        description="测试Flask应用的核心功能是否正常工作"
    )
    
    # 测试2: 检查Flask服务器状态
    runner.run_test(
        test_name="Flask服务器状态检查",
        test_command="netstat -ano | findstr :5000",
        description="检查Flask服务器是否在5000端口运行"
    )
    
    # 测试3: 检查Python环境
    runner.run_test(
        test_name="Python环境检查",
        test_command="python --version",
        description="检查Python版本是否满足要求"
    )
    
    # 测试4: 检查依赖安装
    runner.run_test(
        test_name="依赖检查",
        test_command="pip list",
        description="检查已安装的Python包"
    )
    
    # 测试5: 检查项目文件结构
    runner.run_test(
        test_name="项目结构检查",
        test_command="dir backend && dir frontend && dir github_skills",
        description="检查项目目录结构是否正确"
    )
    
    # 生成摘要
    runner.generate_summary()
    
    print("\n✅ 自动化测试完成！")
    print(f"测试日志已保存到: {runner.test_log_file}")
    print(f"\n{'=' * 60}\n")

if __name__ == '__main__':
    main()
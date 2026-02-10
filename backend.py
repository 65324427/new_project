from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import sys
import tempfile
import os

app = Flask(__name__)
CORS(app)  # 启用CORS支持，处理所有CORS相关的请求

@app.route('/execute', methods=['POST'])
def execute_code():
    """执行Python代码并返回结果"""
    try:
        # 获取代码
        code = request.json.get('code', '')
        if not code:
            return jsonify({'error': 'No code provided'}), 400
        
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file_name = f.name
        
        try:
            # 执行代码
            result = subprocess.run(
                [sys.executable, temp_file_name],
                capture_output=True,
                text=True,
                timeout=10  # 设置超时，防止无限循环
            )
            
            # 构建响应
            response = {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
            
            return jsonify(response)
        finally:
            # 清理临时文件
            if os.path.exists(temp_file_name):
                os.remove(temp_file_name)
                
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Code execution timed out', 'stdout': '', 'stderr': 'Execution timed out after 10 seconds', 'returncode': 1}), 408
    except Exception as e:
        return jsonify({'error': str(e), 'stdout': '', 'stderr': str(e), 'returncode': 1}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

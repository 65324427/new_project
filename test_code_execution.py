import json
import urllib.request

# 测试代码
code = '''# 基本数据类型示例

# 整数
age = 25
print(f"年龄: {age}, 类型: {type(age)}")

# 浮点数
temperature = 36.6
print(f"体温: {temperature}, 类型: {type(temperature)}")

# 布尔值
is_student = True
print(f"是否学生: {is_student}, 类型: {type(is_student)}")

# 字符串
name = "Alice"
print(f"姓名: {name}, 类型: {type(name)}")

# None类型
empty_value = None
print(f"空值: {empty_value}, 类型: {type(empty_value)}")

# 不同进制的整数
binary = 0b1010  # 二进制
octal = 0o12     # 八进制
hexadecimal = 0xA  # 十六进制
print(f"二进制 1010 = 十进制 {binary}")
print(f"八进制 12 = 十进制 {octal}")
print(f"十六进制 A = 十进制 {hexadecimal}")
'''

# 构建请求数据
data = {'code': code}
json_data = json.dumps(data).encode('utf-8')

# 发送请求
try:
    req = urllib.request.Request('http://localhost:8000/execute', data=json_data, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=10) as response:
        result = response.read().decode('utf-8')
        result_data = json.loads(result)
        print("执行结果:")
        print("stdout:")
        print(result_data.get('stdout', ''))
        print("stderr:")
        print(result_data.get('stderr', ''))
        print("returncode:")
        print(result_data.get('returncode', ''))
except Exception as e:
    print(f"错误: {str(e)}")

# Python编程基础

## 1. Python简介

Python是一种简单易学、功能强大的编程语言，已成为AI和数据科学领域的首选语言。它的主要特点包括：

- **简单易学**：语法简洁明了，可读性强
- **功能丰富**：拥有大量的第三方库
- **跨平台**：可在Windows、Mac、Linux等操作系统上运行
- **开源免费**：完全开源，社区活跃
- **面向对象**：支持面向对象编程范式

## 2. Python环境搭建

### 2.1 安装Python

- **Windows系统**：
  1. 访问Python官网（https://www.python.org/）
  2. 下载最新版本的Python安装包
  3. 运行安装包，勾选"Add Python to PATH"
  4. 点击"Install Now"完成安装

- **Mac系统**：
  1. 使用Homebrew安装：`brew install python`
  2. 或从官网下载安装包安装

- **Linux系统**：
  1. 使用包管理器安装，如Ubuntu：`sudo apt install python3`

### 2.2 验证安装

打开命令行终端，输入以下命令验证Python是否安装成功：

```bash
python --version  # 或 python3 --version
```

### 2.3 集成开发环境（IDE）

推荐使用以下IDE进行Python开发：

- **Visual Studio Code**：轻量级编辑器，插件丰富
- **PyCharm**：专业的Python IDE，功能强大
- **Jupyter Notebook**：交互式编程环境，适合数据分析

## 3. Python核心语法

### 3.1 基本数据类型

- **整数**：`1`, `2`, `3`
- **浮点数**：`1.0`, `2.5`, `3.14`
- **字符串**：`"Hello"`, `'World'`
- **布尔值**：`True`, `False`
- **None**：表示空值

### 3.2 变量和赋值

```python
# 变量赋值
x = 10
y = "Hello"
z = 3.14

# 多变量赋值
a, b, c = 1, 2, 3

# 增量赋值
x += 5  # 等价于 x = x + 5
```

### 3.3 控制流

#### 3.3.1 条件语句

```python
if x > 0:
    print("x是正数")
elif x < 0:
    print("x是负数")
else:
    print("x是零")
```

#### 3.3.2 循环语句

```python
# for循环
for i in range(5):
    print(i)

# while循环
count = 0
while count < 5:
    print(count)
    count += 1

# 循环控制
for i in range(10):
    if i == 5:
        break  # 跳出循环
    if i % 2 == 0:
        continue  # 跳过当前循环
    print(i)
```

### 3.4 函数

```python
# 定义函数
def greet(name):
    """打印问候信息"""
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

# 调用函数
result = greet("Alice")

# 默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 可变参数
def sum_numbers(*args):
    return sum(args)

# 关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### 3.5 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    print("无论是否发生异常，都会执行这里")
```

## 4. 数据结构

### 4.1 列表（List）

```python
# 创建列表
numbers = [1, 2, 3, 4, 5]

# 访问元素
print(numbers[0])  # 第一个元素
print(numbers[-1])  # 最后一个元素

# 切片
print(numbers[1:3])  # 从索引1到2的元素
print(numbers[:3])  # 前三个元素
print(numbers[2:])  # 从索引2开始的所有元素

# 修改列表
numbers.append(6)  # 添加元素
numbers.insert(0, 0)  # 插入元素
numbers.remove(3)  # 删除元素
numbers.pop()  # 弹出最后一个元素

# 列表推导式
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### 4.2 字典（Dictionary）

```python
# 创建字典
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 访问元素
print(person["name"])
print(person.get("age"))
print(person.get("country", "Unknown"))  # 提供默认值

# 修改字典
person["age"] = 31  # 更新值
person["country"] = "USA"  # 添加新键值对
person.pop("city")  # 删除键值对

# 遍历字典
for key, value in person.items():
    print(f"{key}: {value}")

# 字典推导式
squares = {x: x**2 for x in range(5)}
```

### 4.3 元组（Tuple）

```python
# 创建元组
point = (10, 20)

# 访问元素
print(point[0])

# 元组不可修改
# point[0] = 15  # 会引发错误

# 元组解包
x, y = point
print(x, y)
```

### 4.4 集合（Set）

```python
# 创建集合
fruits = {"apple", "banana", "cherry"}

# 添加元素
fruits.add("orange")

# 删除元素
fruits.remove("banana")  # 元素不存在会引发错误
fruits.discard("grape")  # 元素不存在不会引发错误

# 集合运算
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # 并集
print(a.intersection(b))  # 交集
print(a.difference(b))  # 差集

# 集合推导式
even_numbers = {x for x in range(10) if x % 2 == 0}
```

## 5. 面向对象编程

### 5.1 类的定义

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name}"
    
    def get_older(self, years):
        self.age += years
        return self.age
```

### 5.2 类的实例化

```python
# 创建实例
alice = Person("Alice", 30)

# 访问属性
print(alice.name)
print(alice.age)

# 调用方法
print(alice.greet())
alice.get_older(5)
print(alice.age)
```

### 5.3 继承

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self, subject):
        return f"{self.name} is studying {subject}"

# 创建学生实例
bob = Student("Bob", 20, "S12345")
print(bob.greet())  # 继承自Person的方法
print(bob.study("Math"))  # Student自己的方法
```

## 6. 文件操作

### 6.1 读取文件

```python
# 读取整个文件
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 逐行读取
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

### 6.2 写入文件

```python
# 写入文件（覆盖）
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("Python is awesome!\n")

# 追加文件
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("Adding new line.\n")
```

## 7. 常用AI库

### 7.1 NumPy

NumPy是用于科学计算的核心库，提供了强大的多维数组支持。

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# 数组操作
print(arr + 1)  # 元素级加法
print(arr * 2)  # 元素级乘法
print(np.dot(matrix, matrix))  # 矩阵乘法

# 统计函数
print(np.mean(arr))  # 平均值
print(np.median(arr))  # 中位数
print(np.std(arr))  # 标准差

# 随机数
random_arr = np.random.rand(5)  # 0-1之间的随机数
normal_arr = np.random.normal(0, 1, 5)  # 正态分布随机数
```

### 7.2 Pandas

Pandas是用于数据处理和分析的库，提供了DataFrame数据结构。

```python
import pandas as pd

# 创建DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "London", "Paris"]
}
df = pd.DataFrame(data)

# 查看数据
print(df.head())  # 前几行
print(df.info())  # 数据信息
print(df.describe())  # 统计摘要

# 选择数据
print(df["name"])
print(df.loc[0])  # 按标签选择
print(df.iloc[0])  # 按位置选择

# 过滤数据
print(df[df["age"] > 28])

# 读取数据
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# 写入数据
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

### 7.3 Matplotlib

Matplotlib是用于数据可视化的库。

```python
import matplotlib.pyplot as plt

# 折线图
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# 散点图
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# 直方图
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30)
plt.title("Histogram")
plt.show()
```

## 8. 实战练习

### 8.1 练习1：计算圆的面积

```python
import math

def calculate_circle_area(radius):
    """计算圆的面积"""
    if radius < 0:
        return "半径不能为负数"
    return math.pi * radius ** 2

# 测试函数
radius = 5
area = calculate_circle_area(radius)
print(f"半径为{radius}的圆的面积是: {area}")
```

### 8.2 练习2：生成斐波那契数列

```python
def fibonacci(n):
    """生成前n个斐波那契数"""
    sequence = [0, 1]
    if n <= 2:
        return sequence[:n]
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence

# 测试函数
n = 10
fib_sequence = fibonacci(n)
print(f"前{n}个斐波那契数是: {fib_sequence}")
```

### 8.3 练习3：统计单词频率

```python
def count_word_frequency(text):
    """统计文本中单词的频率"""
    # 转换为小写并分割单词
    words = text.lower().split()
    frequency = {}
    
    # 统计频率
    for word in words:
        # 移除标点符号
        word = word.strip(",.!?;:()[]'\"")
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

# 测试函数
text = "Hello world! Hello Python. Python is awesome."
frequency = count_word_frequency(text)
print("单词频率:")
for word, count in frequency.items():
    print(f"{word}: {count}")
```

### 8.4 练习4：数据可视化

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 创建示例数据
data = {
    "year": [2018, 2019, 2020, 2021, 2022, 2023],
    "ai_jobs": [10000, 15000, 25000, 40000, 60000, 85000],
    "salary": [150000, 180000, 220000, 250000, 280000, 320000]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 绘制折线图
plt.figure(figsize=(10, 6))

# 绘制AI岗位数量
plt.subplot(2, 1, 1)
plt.plot(df["year"], df["ai_jobs"], marker="o")
plt.title("AI岗位数量增长趋势")
plt.ylabel("岗位数量")

# 绘制平均薪资
plt.subplot(2, 1, 2)
plt.plot(df["year"], df["salary"], marker="s", color="r")
plt.title("AI岗位平均薪资增长趋势")
plt.xlabel("年份")
plt.ylabel("平均薪资")

plt.tight_layout()
plt.show()
```

## 9. 总结

Python是AI和数据科学领域的重要工具，掌握Python编程基础是学习AI的第一步。本章节介绍了Python的核心语法、数据结构、面向对象编程、文件操作以及常用的AI库。

通过本章节的学习，你应该能够：
- 搭建Python开发环境
- 编写基本的Python程序
- 使用Python的数据结构
- 处理文件和数据
- 使用NumPy、Pandas和Matplotlib进行数据处理和可视化

这些技能将为你后续学习机器学习和深度学习打下坚实的基础。

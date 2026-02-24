# Python基础练习题

## 1. 变量和数据类型

### 1.1 基础练习题

**Q1. 编写一个程序，将两个整数相加并输出结果。**

**输入示例：**
```python
a = 10
b = 20
```

**输出示例：**
```
30
```

**Q2. 编写一个程序，将字符串"Hello"和"World"连接起来并输出。**

**输入示例：**
```python
str1 = "Hello"
str2 = "World"
```

**输出示例：**
```
HelloWorld
```

**Q3. 编写一个程序，计算并输出列表[1, 2, 3, 4, 5]的和。**

**输入示例：**
```python
numbers = [1, 2, 3, 4, 5]
```

**输出示例：**
```
15
```

### 1.2 进阶练习题

**Q4. 编写一个程序，将字符串"Python is fun!"中的每个单词首字母大写并输出。**

**输入示例：**
```python
text = "Python is fun!"
```

**输出示例：**
```
Python Is Fun!
```

**Q5. 编写一个程序，将列表[3, 1, 4, 1, 5, 9, 2, 6, 5]去重并排序后输出。**

**输入示例：**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
```

**输出示例：**
```
[1, 2, 3, 4, 5, 6, 9]
```

**Q6. 编写一个程序，计算并输出字典{"a": 1, "b": 2, "c": 3}中所有值的和。**

**输入示例：**
```python
data = {"a": 1, "b": 2, "c": 3}
```

**输出示例：**
```
6
```

## 2. 控制流

### 2.1 基础练习题

**Q7. 编写一个程序，使用if-else语句判断一个数是正数、负数还是零。**

**输入示例：**
```python
num = 5
```

**输出示例：**
```
正数
```

**Q8. 编写一个程序，使用for循环输出1到10的所有偶数。**

**输出示例：**
```
2
4
6
8
10
```

**Q9. 编写一个程序，使用while循环计算1到100的和。**

**输出示例：**
```
5050
```

### 2.2 进阶练习题

**Q10. 编写一个程序，使用for循环和if语句找出列表[12, 34, 45, 67, 78, 89, 90]中大于60的数并输出。**

**输入示例：**
```python
numbers = [12, 34, 45, 67, 78, 89, 90]
```

**输出示例：**
```
67
78
89
90
```

**Q11. 编写一个程序，使用嵌套循环输出以下图案：**

```
*
**
***
****
*****
```

**Q12. 编写一个程序，使用break语句在循环中找到第一个大于50的数并输出，然后终止循环。**

**输入示例：**
```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
```

**输出示例：**
```
60
```

## 3. 函数

### 3.1 基础练习题

**Q13. 编写一个函数，计算两个数的乘积并返回结果。**

**函数签名：**
```python
def multiply(a, b):
    pass
```

**输入示例：**
```python
print(multiply(3, 4))
```

**输出示例：**
```
12
```

**Q14. 编写一个函数，判断一个数是否为质数。**

**函数签名：**
```python
def is_prime(n):
    pass
```

**输入示例：**
```python
print(is_prime(7))  # 输出: True
print(is_prime(4))  # 输出: False
```

**Q15. 编写一个函数，计算列表中所有元素的平均值。**

**函数签名：**
```python
def calculate_average(numbers):
    pass
```

**输入示例：**
```python
print(calculate_average([1, 2, 3, 4, 5]))
```

**输出示例：**
```
3.0
```

### 3.2 进阶练习题

**Q16. 编写一个函数，使用递归计算n的阶乘。**

**函数签名：**
```python
def factorial(n):
    pass
```

**输入示例：**
```python
print(factorial(5))  # 输出: 120
```

**Q17. 编写一个函数，接收可变数量的参数，返回它们的最大值。**

**函数签名：**
```python
def find_max(*args):
    pass
```

**输入示例：**
```python
print(find_max(1, 5, 3, 9, 2))  # 输出: 9
```

**Q18. 编写一个函数，接收一个字符串和一个整数n，返回该字符串重复n次的结果。**

**函数签名：**
```python
def repeat_string(s, n):
    pass
```

**输入示例：**
```python
print(repeat_string("Hello", 3))  # 输出: HelloHelloHello
```

## 4. 类和面向对象编程

### 4.1 基础练习题

**Q19. 编写一个Person类，包含name和age属性，以及一个greet方法，用于输出问候语。**

**类定义：**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass
```

**输入示例：**
```python
person = Person("Alice", 30)
person.greet()
```

**输出示例：**
```
Hello, my name is Alice and I am 30 years old.
```

**Q20. 编写一个Circle类，包含radius属性，以及计算面积和周长的方法。**

**类定义：**
```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        pass
    
    def calculate_circumference(self):
        pass
```

**输入示例：**
```python
circle = Circle(5)
print(circle.calculate_area())  # 输出: 78.53981633974483
print(circle.calculate_circumference())  # 输出: 31.41592653589793
```

### 4.2 进阶练习题

**Q21. 编写一个Student类，继承自Person类，添加student_id和grades属性，以及计算平均成绩的方法。**

**类定义：**
```python
class Student(Person):
    def __init__(self, name, age, student_id, grades):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades
    
    def calculate_average_grade(self):
        pass
```

**输入示例：**
```python
student = Student("Bob", 20, "S12345", [85, 90, 78, 92])
print(student.calculate_average_grade())  # 输出: 86.25
```

**Q22. 编写一个BankAccount类，包含balance属性，以及存款、取款和查询余额的方法。**

**类定义：**
```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        pass
    
    def withdraw(self, amount):
        pass
    
    def check_balance(self):
        pass
```

**输入示例：**
```python
account = BankAccount(100)
account.deposit(50)
print(account.check_balance())  # 输出: 150
account.withdraw(30)
print(account.check_balance())  # 输出: 120
```

## 5. 模块和包

### 5.1 基础练习题

**Q23. 编写一个程序，导入math模块，计算并输出9的平方根。**

**输出示例：**
```
3.0
```

**Q24. 编写一个程序，导入random模块，生成并输出一个1到100之间的随机整数。**

**输出示例：**
```
42  # 随机值
```

**Q25. 编写一个程序，导入datetime模块，输出当前日期和时间。**

**输出示例：**
```
2023-10-01 15:30:45  # 当前日期和时间
```

### 5.2 进阶练习题

**Q26. 编写一个自定义模块calculator.py，包含加法、减法、乘法和除法函数，然后在另一个程序中导入并使用这些函数。**

**calculator.py：**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
```

**使用示例：**
```python
import calculator

print(calculator.add(5, 3))  # 输出: 8
print(calculator.subtract(5, 3))  # 输出: 2
print(calculator.multiply(5, 3))  # 输出: 15
print(calculator.divide(5, 3))  # 输出: 1.6666666666666667
```

## 6. 文件操作

### 6.1 基础练习题

**Q27. 编写一个程序，将字符串"Hello, World!"写入到文件example.txt中。**

**Q28. 编写一个程序，读取文件example.txt的内容并输出。**

**Q29. 编写一个程序，读取文件numbers.txt中的数字（每行一个），计算它们的和并输出。**

**numbers.txt内容示例：**
```
10
20
30
40
50
```

**输出示例：**
```
150
```

### 6.2 进阶练习题

**Q30. 编写一个程序，读取文件students.txt中的学生信息（每行格式：姓名,年龄,成绩），计算平均成绩并输出。**

**students.txt内容示例：**
```
Alice,20,85
Bob,21,90
Charlie,19,78
```

**输出示例：**
```
84.33333333333333
```

**Q31. 编写一个程序，将字典{"name": "Alice", "age": 30, "city": "New York"}写入到文件data.json中，然后读取并输出。**

**输出示例：**
```
{'name': 'Alice', 'age': 30, 'city': 'New York'}
```

## 7. 异常处理

### 7.1 基础练习题

**Q32. 编写一个程序，使用try-except语句捕获除以零的异常并输出错误信息。**

**输入示例：**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
```

**输出示例：**
```
Error: Division by zero
```

**Q33. 编写一个程序，使用try-except语句捕获列表索引越界的异常并输出错误信息。**

**输入示例：**
```python
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Error: Index out of range")
```

**输出示例：**
```
Error: Index out of range
```

### 7.2 进阶练习题

**Q34. 编写一个程序，使用try-except-else-finally语句读取文件，处理可能的异常，并确保文件正确关闭。**

**Q35. 编写一个函数，使用try-except语句验证用户输入是否为整数，如果不是则提示用户重新输入。**

**函数签名：**
```python
def get_integer_input(prompt):
    pass
```

**输入示例：**
```python
age = get_integer_input("请输入您的年龄：")
print(f"您的年龄是：{age}")
```

**输入输出示例：**
```
请输入您的年龄：abc
错误：请输入有效的整数！
请输入您的年龄：25
您的年龄是：25
```

## 8. 综合练习题

**Q36. 编写一个程序，实现一个简单的计算器，支持加、减、乘、除操作。**

**功能要求：**
- 接收用户输入的两个数和操作符
- 执行相应的运算并输出结果
- 处理可能的异常（如除以零）

**输入输出示例：**
```
请输入第一个数：10
请输入操作符(+, -, *, /)：/
请输入第二个数：0
错误：除数不能为零！
```

**Q37. 编写一个程序，实现一个简单的猜数字游戏。**

**功能要求：**
- 生成一个1到100之间的随机数
- 让用户猜数字，直到猜对为止
- 提示用户猜的数字是太大还是太小
- 记录用户猜测的次数

**输入输出示例：**
```
猜数字游戏开始！我想了一个1到100之间的数字。
请猜一个数字：50
太大了！
请猜一个数字：25
太小了！
请猜一个数字：37
恭喜你，猜对了！你用了3次猜测。
```

**Q38. 编写一个程序，实现一个简单的学生管理系统。**

**功能要求：**
- 添加学生信息（姓名、年龄、成绩）
- 显示所有学生信息
- 根据姓名查找学生
- 计算所有学生的平均成绩

**输入输出示例：**
```
学生管理系统
1. 添加学生
2. 显示所有学生
3. 查找学生
4. 计算平均成绩
5. 退出
请选择操作：1
请输入姓名：Alice
请输入年龄：20
请输入成绩：85
学生添加成功！

学生管理系统
1. 添加学生
2. 显示所有学生
3. 查找学生
4. 计算平均成绩
5. 退出
请选择操作：2
姓名：Alice，年龄：20，成绩：85
```

**Q39. 编写一个程序，使用正则表达式验证邮箱地址的格式是否正确。**

**功能要求：**
- 接收用户输入的邮箱地址
- 使用正则表达式验证格式
- 输出验证结果

**输入输出示例：**
```
请输入邮箱地址：alice@example.com
邮箱地址格式正确！

请输入邮箱地址：alice.example.com
邮箱地址格式错误！
```

**Q40. 编写一个程序，使用列表推导式生成1到100之间的所有偶数，并输出结果。**

**输出示例：**
```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
```

## 9. 答案

### 1. 变量和数据类型

**Q1. 答案：**
```python
a = 10
b = 20
print(a + b)
```

**Q2. 答案：**
```python
str1 = "Hello"
str2 = "World"
print(str1 + str2)
```

**Q3. 答案：**
```python
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
```

**Q4. 答案：**
```python
text = "Python is fun!"
print(text.title())
```

**Q5. 答案：**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print(unique_numbers)
```

**Q6. 答案：**
```python
data = {"a": 1, "b": 2, "c": 3}
print(sum(data.values()))
```

### 2. 控制流

**Q7. 答案：**
```python
num = 5
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("零")
```

**Q8. 答案：**
```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

**Q9. 答案：**
```python
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(sum)
```

**Q10. 答案：**
```python
numbers = [12, 34, 45, 67, 78, 89, 90]
for num in numbers:
    if num > 60:
        print(num)
```

**Q11. 答案：**
```python
for i in range(1, 6):
    print("*" * i)
```

**Q12. 答案：**
```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
for num in numbers:
    if num > 50:
        print(num)
        break
```

### 3. 函数

**Q13. 答案：**
```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))
```

**Q14. 答案：**
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # 输出: True
print(is_prime(4))  # 输出: False
```

**Q15. 答案：**
```python
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(calculate_average([1, 2, 3, 4, 5]))
```

**Q16. 答案：**
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 输出: 120
```

**Q17. 答案：**
```python
def find_max(*args):
    if not args:
        return None
    max_val = args[0]
    for arg in args:
        if arg > max_val:
            max_val = arg
    return max_val

print(find_max(1, 5, 3, 9, 2))  # 输出: 9
```

**Q18. 答案：**
```python
def repeat_string(s, n):
    return s * n

print(repeat_string("Hello", 3))  # 输出: HelloHelloHello
```

### 4. 类和面向对象编程

**Q19. 答案：**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("Alice", 30)
person.greet()
```

**Q20. 答案：**
```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print(circle.calculate_area())  # 输出: 78.53981633974483
print(circle.calculate_circumference())  # 输出: 31.41592653589793
```

**Q21. 答案：**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id, grades):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = grades
    
    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

student = Student("Bob", 20, "S12345", [85, 90, 78, 92])
print(student.calculate_average_grade())  # 输出: 86.25
```

**Q22. 答案：**
```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"存款成功！当前余额：{self.balance}")
        else:
            print("存款金额必须大于0！")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"取款成功！当前余额：{self.balance}")
            else:
                print("余额不足！")
        else:
            print("取款金额必须大于0！")
    
    def check_balance(self):
        return self.balance

account = BankAccount(100)
account.deposit(50)
print(account.check_balance())  # 输出: 150
account.withdraw(30)
print(account.check_balance())  # 输出: 120
```

### 5. 模块和包

**Q23. 答案：**
```python
import math
print(math.sqrt(9))
```

**Q24. 答案：**
```python
import random
print(random.randint(1, 100))
```

**Q25. 答案：**
```python
import datetime
print(datetime.datetime.now())
```

**Q26. 答案：**
calculator.py：
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
```

使用示例：
```python
import calculator

print(calculator.add(5, 3))  # 输出: 8
print(calculator.subtract(5, 3))  # 输出: 2
print(calculator.multiply(5, 3))  # 输出: 15
print(calculator.divide(5, 3))  # 输出: 1.6666666666666667
```

### 6. 文件操作

**Q27. 答案：**
```python
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")
```

**Q28. 答案：**
```python
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

**Q29. 答案：**
```python
sum = 0
with open("numbers.txt", "r", encoding="utf-8") as f:
    for line in f:
        sum += int(line.strip())
print(sum)
```

**Q30. 答案：**
```python
grades = []
with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(",")
        grade = float(parts[2])
        grades.append(grade)
average = sum(grades) / len(grades)
print(average)
```

**Q31. 答案：**
```python
import json

data = {"name": "Alice", "age": 30, "city": "New York"}

# 写入文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取文件
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(loaded_data)
```

### 7. 异常处理

**Q32. 答案：**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
```

**Q33. 答案：**
```python
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Error: Index out of range")
```

**Q34. 答案：**
```python
try:
    with open("example.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print(f"Error: {str(e)}")
else:
    print("File read successfully")
finally:
    print("Operation completed")
```

**Q35. 答案：**
```python
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("错误：请输入有效的整数！")

age = get_integer_input("请输入您的年龄：")
print(f"您的年龄是：{age}")
```

### 8. 综合练习题

**Q36. 答案：**
```python
try:
    num1 = float(input("请输入第一个数："))
    operator = input("请输入操作符(+, -, *, /)：")
    num2 = float(input("请输入第二个数："))
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("除数不能为零！")
        result = num1 / num2
    else:
        print("错误：无效的操作符！")
        exit()
    
    print(f"结果：{result}")
except ZeroDivisionError as e:
    print(f"错误：{str(e)}")
except ValueError:
    print("错误：请输入有效的数字！")
except Exception as e:
    print(f"错误：{str(e)}")
```

**Q37. 答案：**
```python
import random

def guess_number():
    secret_number = random.randint(1, 100)
    guesses = 0
    print("猜数字游戏开始！我想了一个1到100之间的数字。")
    
    while True:
        try:
            guess = int(input("请猜一个数字："))
            guesses += 1
            
            if guess < secret_number:
                print("太小了！")
            elif guess > secret_number:
                print("太大了！")
            else:
                print(f"恭喜你，猜对了！你用了{guesses}次猜测。")
                break
        except ValueError:
            print("错误：请输入有效的整数！")

guess_number()
```

**Q38. 答案：**
```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class StudentManager:
    def __init__(self):
        self.students = []
    
    def add_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        grade = float(input("请输入成绩："))
        student = Student(name, age, grade)
        self.students.append(student)
        print("学生添加成功！")
    
    def show_all_students(self):
        if not self.students:
            print("没有学生信息！")
        else:
            for student in self.students:
                print(f"姓名：{student.name}，年龄：{student.age}，成绩：{student.grade}")
    
    def find_student(self):
        name = input("请输入要查找的学生姓名：")
        found = False
        for student in self.students:
            if student.name == name:
                print(f"姓名：{student.name}，年龄：{student.age}，成绩：{student.grade}")
                found = True
                break
        if not found:
            print("未找到该学生！")
    
    def calculate_average(self):
        if not self.students:
            print("没有学生信息！")
        else:
            total = sum(student.grade for student in self.students)
            average = total / len(self.students)
            print(f"所有学生的平均成绩：{average}")
    
    def run(self):
        while True:
            print("\n学生管理系统")
            print("1. 添加学生")
            print("2. 显示所有学生")
            print("3. 查找学生")
            print("4. 计算平均成绩")
            print("5. 退出")
            
            choice = input("请选择操作：")
            
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.show_all_students()
            elif choice == "3":
                self.find_student()
            elif choice == "4":
                self.calculate_average()
            elif choice == "5":
                print("退出系统！")
                break
            else:
                print("错误：无效的选择！")

if __name__ == "__main__":
    manager = StudentManager()
    manager.run()
```

**Q39. 答案：**
```python
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("请输入邮箱地址：")
if validate_email(email):
    print("邮箱地址格式正确！")
else:
    print("邮箱地址格式错误！")
```

**Q40. 答案：**
```python
even_numbers = [i for i in range(1, 101) if i % 2 == 0]
print(even_numbers)
```

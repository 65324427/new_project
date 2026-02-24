# 实践项目：房价预测

## 项目概述

房价预测是机器学习中的经典回归问题，也是初学者入门的理想项目。本项目将使用线性回归算法来预测房价，帮助你巩固所学的机器学习基础概念和技能。

## 数据描述

我们将使用一个简化的房价数据集，包含以下特征：

| 特征 | 描述 |
|------|------|
| area | 房屋面积（平方米） |
| bedrooms | 卧室数量 |
| bathrooms | 浴室数量 |
| stories | 楼层数量 |
| parking | 停车位数量 |
| price | 房价（万元） |

## 项目目标

1. 了解机器学习项目的完整工作流程
2. 掌握数据预处理和特征工程的基本方法
3. 实现线性回归算法进行房价预测
4. 评估模型性能并进行调优
5. 分析特征对房价的影响

## 项目步骤

### 步骤1：环境准备

首先，我们需要安装必要的Python库：

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 步骤2：数据准备

创建一个包含房价数据的CSV文件：

```python
import pandas as pd
import numpy as np

# 创建示例数据
np.random.seed(42)
data = {
    'area': np.random.randint(80, 300, 100),
    'bedrooms': np.random.randint(1, 5, 100),
    'bathrooms': np.random.randint(1, 4, 100),
    'stories': np.random.randint(1, 4, 100),
    'parking': np.random.randint(0, 3, 100)
}

# 生成房价（基于特征的线性组合加上噪声）
data['price'] = (
    0.5 * data['area'] +
    10 * data['bedrooms'] +
    8 * data['bathrooms'] +
    5 * data['stories'] +
    3 * data['parking'] +
    np.random.normal(0, 10, 100)
)

# 创建DataFrame并保存为CSV
df = pd.DataFrame(data)
df.to_csv('house_price_data.csv', index=False)
print('数据已生成并保存为 house_price_data.csv')
print('数据预览:')
print(df.head())
```

### 步骤3：数据探索与预处理

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载数据
df = pd.read_csv('house_price_data.csv')

# 数据基本信息
print('数据基本信息:')
print(df.info())
print('\n数据统计描述:')
print(df.describe())

# 数据可视化
plt.figure(figsize=(15, 10))

# 面积与房价的关系
plt.subplot(2, 3, 1)
sns.scatterplot(x='area', y='price', data=df)
plt.title('面积 vs 房价')

# 卧室数量与房价的关系
plt.subplot(2, 3, 2)
sns.boxplot(x='bedrooms', y='price', data=df)
plt.title('卧室数量 vs 房价')

# 浴室数量与房价的关系
plt.subplot(2, 3, 3)
sns.boxplot(x='bathrooms', y='price', data=df)
plt.title('浴室数量 vs 房价')

# 楼层数量与房价的关系
plt.subplot(2, 3, 4)
sns.boxplot(x='stories', y='price', data=df)
plt.title('楼层数量 vs 房价')

# 停车位数量与房价的关系
plt.subplot(2, 3, 5)
sns.boxplot(x='parking', y='price', data=df)
plt.title('停车位数量 vs 房价')

# 相关性热图
plt.subplot(2, 3, 6)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('特征相关性')

plt.tight_layout()
plt.show()

# 检查缺失值
print('\n缺失值检查:')
print(df.isnull().sum())
```

### 步骤4：特征工程

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 加载数据
df = pd.read_csv('house_price_data.csv')

# 分离特征和标签
X = df.drop('price', axis=1)
y = df['price']

# 特征缩放
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 查看缩放后的数据
print('缩放后的数据预览:')
print(pd.DataFrame(X_scaled, columns=X.columns).head())
```

### 步骤5：模型训练与评估

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# 加载数据
df = pd.read_csv('house_price_data.csv')

# 分离特征和标签
X = df.drop('price', axis=1)
y = df['price']

# 特征缩放
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
print(f'训练集大小: {X_train.shape[0]}')
print(f'测试集大小: {X_test.shape[0]}')

# 训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# 评估模型
mse_train = mean_squared_error(y_train, y_pred_train)
rmse_train = np.sqrt(mse_train)
r2_train = r2_score(y_train, y_pred_train)

mse_test = mean_squared_error(y_test, y_pred_test)
rmse_test = np.sqrt(mse_test)
r2_test = r2_score(y_test, y_pred_test)

print('\n模型评估结果:')
print(f'训练集 - MSE: {mse_train:.4f}, RMSE: {rmse_train:.4f}, R²: {r2_train:.4f}')
print(f'测试集 - MSE: {mse_test:.4f}, RMSE: {rmse_test:.4f}, R²: {r2_test:.4f}')

# 模型参数
print('\n模型参数:')
print(f'偏置项: {model.intercept_:.4f}')
for feature, coef in zip(X.columns, model.coef_):
    print(f'{feature}: {coef:.4f}')
```

### 步骤6：模型可视化

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 加载数据
df = pd.read_csv('house_price_data.csv')

# 分离特征和标签
X = df.drop('price', axis=1)
y = df['price']

# 特征缩放
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 训练模型
model = LinearRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 绘制预测值与实际值的对比
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.xlabel('实际房价（万元）')
plt.ylabel('预测房价（万元）')
plt.title('预测值与实际值的对比')
plt.grid(True)
plt.show()

# 绘制残差图
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('预测房价（万元）')
plt.ylabel('残差（万元）')
plt.title('残差图')
plt.grid(True)
plt.show()

# 特征重要性分析
feature_importance = np.abs(model.coef_)
sorted_indices = np.argsort(feature_importance)[::-1]

plt.figure(figsize=(10, 6))
plt.bar(range(X.shape[1]), feature_importance[sorted_indices], align='center')
plt.xticks(range(X.shape[1]), X.columns[sorted_indices], rotation=45)
plt.xlabel('特征')
plt.ylabel('重要性')
plt.title('特征重要性分析')
plt.tight_layout()
plt.show()
```

### 步骤7：模型调优

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# 加载数据
df = pd.read_csv('house_price_data.csv')

# 分离特征和标签
X = df.drop('price', axis=1)
y = df['price']

# 特征缩放
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 尝试不同的模型
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Lasso Regression': Lasso(alpha=0.1)
}

for name, model in models.items():
    # 交叉验证
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
    print(f'\n{name} 交叉验证结果:')
    print(f'平均R²: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}')
    
    # 训练模型
    model.fit(X_train, y_train)
    
    # 预测
    y_pred = model.predict(X_test)
    
    # 评估
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f'测试集评估结果:')
    print(f'MSE: {mse:.4f}, RMSE: {rmse:.4f}, R²: {r2:.4f}')

# 选择最佳模型
best_model = LinearRegression()
best_model.fit(X_train, y_train)

# 最终模型评估
y_pred_final = best_model.predict(X_test)
final_r2 = r2_score(y_test, y_pred_final)
print(f'\n最终模型R²分数: {final_r2:.4f}')
```

### 步骤8：预测新数据

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 加载数据
df = pd.read_csv('house_price_data.csv')

# 分离特征和标签
X = df.drop('price', axis=1)
y = df['price']

# 特征缩放
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 训练模型
model = LinearRegression()
model.fit(X_scaled, y)

# 新数据预测
new_houses = [
    {'area': 120, 'bedrooms': 3, 'bathrooms': 2, 'stories': 2, 'parking': 1},
    {'area': 180, 'bedrooms': 4, 'bathrooms': 3, 'stories': 2, 'parking': 2},
    {'area': 90, 'bedrooms': 2, 'bathrooms': 1, 'stories': 1, 'parking': 0}
]

new_houses_df = pd.DataFrame(new_houses)
print('新房屋数据:')
print(new_houses_df)

# 特征缩放
new_houses_scaled = scaler.transform(new_houses_df)

# 预测
predictions = model.predict(new_houses_scaled)

print('\n预测结果:')
for i, (house, price) in enumerate(zip(new_houses, predictions)):
    print(f'房屋 {i+1}: 面积 {house["area"]}㎡, {house["bedrooms"]}卧室, {house["bathrooms"]}浴室, {house["stories"]}层, {house["parking"]}车位')
    print(f'  预测房价: {price:.2f}万元')
    print()
```

## 项目总结

通过本项目，你应该已经掌握了以下技能：

1. **数据处理**：加载、探索和预处理数据
2. **特征工程**：理解特征与目标变量的关系，进行特征缩放
3. **模型训练**：实现线性回归算法并训练模型
4. **模型评估**：使用MSE、RMSE和R²等指标评估模型性能
5. **模型可视化**：绘制预测值与实际值的对比图、残差图和特征重要性图
6. **模型调优**：尝试不同的回归模型并选择最佳模型
7. **预测应用**：使用训练好的模型预测新数据

这些技能是机器学习项目的基础，将为你后续学习更复杂的算法和项目打下坚实的基础。

## 扩展思考

1. 如何处理更多的特征？例如，地理位置、建筑年份等
2. 如果特征之间存在非线性关系，应该如何处理？
3. 如何处理异常值对模型的影响？
4. 尝试使用其他回归算法，如决策树回归、随机森林回归，比较它们的性能
5. 如何提高模型的预测精度？

## 参考资料

- [Scikit-learn 文档](https://scikit-learn.org/stable/documentation.html)
- [Python 机器学习](https://book.douban.com/subject/30310984/)
- [Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow](https://book.douban.com/subject/33437381/)

# 机器学习练习题

## 1. 数据预处理

### 1.1 基础练习题

**Q1. 编写一个程序，使用pandas读取CSV文件并显示前5行数据。**

**输入示例：**
```python
import pandas as pd

# 读取CSV文件
df = pd.read_csv('data.csv')
# 显示前5行
print(df.head())
```

**Q2. 编写一个程序，使用pandas处理缺失值，将缺失值填充为列的平均值。**

**输入示例：**
```python
import pandas as pd
import numpy as np

# 创建包含缺失值的数据框
data = {'A': [1, 2, np.nan, 4, 5], 'B': [6, np.nan, 8, 9, 10]}
df = pd.DataFrame(data)
print("原始数据：")
print(df)

# 填充缺失值
filled_df = df.fillna(df.mean())
print("\n填充后的数据：")
print(filled_df)
```

**Q3. 编写一个程序，使用sklearn进行数据标准化（StandardScaler）。**

**输入示例：**
```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# 创建数据
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("原始数据：")
print(data)

# 标准化
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print("\n标准化后的数据：")
print(scaled_data)
```

### 1.2 进阶练习题

**Q4. 编写一个程序，使用pandas进行独热编码（One-Hot Encoding）。**

**输入示例：**
```python
import pandas as pd

# 创建包含分类变量的数据框
data = {'category': ['A', 'B', 'C', 'A', 'B']}
df = pd.DataFrame(data)
print("原始数据：")
print(df)

# 独热编码
encoded_df = pd.get_dummies(df, columns=['category'])
print("\n编码后的数据：")
print(encoded_df)
```

**Q5. 编写一个程序，使用sklearn进行数据分割，将数据分为训练集和测试集（比例为8:2）。**

**输入示例：**
```python
from sklearn.model_selection import train_test_split
import numpy as np

# 创建数据
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([0, 1, 0, 1, 0])

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("训练集特征：")
print(X_train)
print("训练集标签：")
print(y_train)
print("\n测试集特征：")
print(X_test)
print("测试集标签：")
print(y_test)
```

**Q6. 编写一个程序，使用pandas处理时间序列数据，提取年份、月份和日期。**

**输入示例：**
```python
import pandas as pd

# 创建时间序列数据
dates = pd.date_range('2023-01-01', periods=5)
data = {'date': dates, 'value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
print("原始数据：")
print(df)

# 提取时间组件
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
print("\n提取时间组件后的数据：")
print(df)
```

## 2. 监督学习

### 2.1 分类问题

**Q7. 编写一个程序，使用sklearn的KNN分类器对iris数据集进行分类。**

**输入示例：**
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 预测
y_pred = knn.predict(X_test)

# 评估
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率：{accuracy:.4f}")
```

**Q8. 编写一个程序，使用sklearn的逻辑回归对乳腺癌数据集进行分类。**

**输入示例：**
```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 加载数据集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
logreg = LogisticRegression(max_iter=10000)
logreg.fit(X_train, y_train)

# 预测
y_pred = logreg.predict(X_test)

# 评估
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率：{accuracy:.4f}")
print("\n分类报告：")
print(classification_report(y_test, y_pred))
```

**Q9. 编写一个程序，使用sklearn的决策树分类器对葡萄酒数据集进行分类。**

**输入示例：**
```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 加载数据集
wine = load_wine()
X = wine.data
y = wine.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

# 预测
y_pred = tree.predict(X_test)

# 评估
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率：{accuracy:.4f}")
```

### 2.2 回归问题

**Q10. 编写一个程序，使用sklearn的线性回归对波士顿房价数据集进行预测。**

**输入示例：**
```python
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 加载数据集
boston = load_boston()
X = boston.data
y = boston.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
lr = LinearRegression()
lr.fit(X_train, y_train)

# 预测
y_pred = lr.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"均方误差：{mse:.4f}")
print(f"R²评分：{r2:.4f}")
```

**Q11. 编写一个程序，使用sklearn的岭回归对糖尿病数据集进行预测。**

**输入示例：**
```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# 加载数据集
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# 预测
y_pred = ridge.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差：{mse:.4f}")
```

**Q12. 编写一个程序，使用sklearn的随机森林回归对自行车共享数据集进行预测。**

**输入示例：**
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 加载数据集
df = pd.read_csv('hour.csv')

# 准备特征和标签
X = df.drop(['cnt', 'dteday'], axis=1)
y = df['cnt']

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 预测
y_pred = rf.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差：{mse:.4f}")
```

## 3. 无监督学习

### 3.1 聚类

**Q13. 编写一个程序，使用sklearn的K-means对鸢尾花数据集进行聚类。**

**输入示例：**
```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 加载数据集
iris = load_iris()
X = iris.data

# 训练模型
kmeans = KMeans(n_clusters=3, random_state=42)
y_pred = kmeans.fit_predict(X)

# 可视化
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
plt.title('K-means Clustering on Iris Dataset')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()
```

**Q14. 编写一个程序，使用sklearn的层次聚类对葡萄酒数据集进行聚类。**

**输入示例：**
```python
from sklearn.datasets import load_wine
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# 加载数据集
wine = load_wine()
X = wine.data

# 层次聚类
linked = linkage(X, 'ward')

# 绘制 dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked, truncate_mode='lastp', p=12, leaf_rotation=45., leaf_font_size=15., show_contracted=True)
plt.title('Dendrogram for Wine Dataset')
plt.xlabel('Sample index')
plt.ylabel('Euclidean distance')
plt.show()

# 训练模型
agg = AgglomerativeClustering(n_clusters=3)
y_pred = agg.fit_predict(X)
print(f"聚类结果：{y_pred}")
```

### 3.2 降维

**Q15. 编写一个程序，使用sklearn的PCA对鸢尾花数据集进行降维（降至2维）并可视化。**

**输入示例：**
```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# PCA降维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 可视化
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.title('PCA on Iris Dataset')
plt.xlabel('First principal component')
plt.ylabel('Second principal component')
plt.show()

# 查看解释方差比
print(f"解释方差比：{pca.explained_variance_ratio_}")
print(f"累计解释方差：{sum(pca.explained_variance_ratio_):.4f}")
```

**Q16. 编写一个程序，使用sklearn的t-SNE对MNIST数据集进行降维（降至2维）并可视化。**

**输入示例：**
```python
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 加载数据集
digits = load_digits()
X = digits.data
y = digits.target

# 随机选择部分样本以加快计算
import numpy as np
np.random.seed(42)
indices = np.random.choice(range(len(X)), 500)
X_subset = X[indices]
y_subset = y[indices]

# t-SNE降维
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_subset)

# 可视化
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_subset, cmap='tab10')
plt.title('t-SNE on MNIST Dataset')
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.colorbar()
plt.show()
```

## 4. 模型评估与调优

### 4.1 模型评估

**Q17. 编写一个程序，使用sklearn的交叉验证评估KNN分类器的性能。**

**输入示例：**
```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 创建模型
knn = KNeighborsClassifier(n_neighbors=3)

# 交叉验证
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
print(f"交叉验证准确率：{scores}")
print(f"平均准确率：{scores.mean():.4f}")
print(f"准确率标准差：{scores.std():.4f}")
```

**Q18. 编写一个程序，使用sklearn的混淆矩阵和ROC曲线评估分类模型的性能。**

**输入示例：**
```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt

# 加载数据集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
logreg = LogisticRegression(max_iter=10000)
logreg.fit(X_train, y_train)

# 预测
y_pred = logreg.predict(X_test)
y_pred_proba = logreg.predict_proba(X_test)[:, 1]

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print("混淆矩阵：")
print(cm)

# ROC曲线
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
```

### 4.2 模型调优

**Q19. 编写一个程序，使用sklearn的GridSearchCV对KNN分类器进行超参数调优。**

**输入示例：**
```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 定义参数网格
param_grid = {'n_neighbors': [1, 3, 5, 7, 9, 11]}

# 创建模型
knn = KNeighborsClassifier()

# 网格搜索
grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# 最佳参数
print(f"最佳参数：{grid_search.best_params_}")
print(f"最佳交叉验证准确率：{grid_search.best_score_:.4f}")

# 使用最佳参数评估模型
best_knn = grid_search.best_estimator_
test_accuracy = best_knn.score(X_test, y_test)
print(f"测试集准确率：{test_accuracy:.4f}")
```

**Q20. 编写一个程序，使用sklearn的RandomizedSearchCV对随机森林分类器进行超参数调优。**

**输入示例：**
```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
import numpy as np

# 加载数据集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 定义参数分布
param_dist = {
    'n_estimators': np.arange(10, 201, 10),
    'max_depth': np.arange(1, 11),
    'min_samples_split': np.arange(2, 11),
    'min_samples_leaf': np.arange(1, 6)
}

# 创建模型
rf = RandomForestClassifier(random_state=42)

# 随机搜索
random_search = RandomizedSearchCV(
    rf, param_distributions=param_dist, n_iter=100, cv=5, scoring='accuracy', random_state=42
)
random_search.fit(X_train, y_train)

# 最佳参数
print(f"最佳参数：{random_search.best_params_}")
print(f"最佳交叉验证准确率：{random_search.best_score_:.4f}")

# 使用最佳参数评估模型
best_rf = random_search.best_estimator_
test_accuracy = best_rf.score(X_test, y_test)
print(f"测试集准确率：{test_accuracy:.4f}")
```

## 5. 综合练习题

**Q21. 编写一个程序，完成一个完整的机器学习工作流程，包括数据加载、预处理、模型训练、评估和调优。**

**功能要求：**
- 加载一个数据集（如糖尿病数据集）
- 数据预处理（标准化）
- 分割数据为训练集和测试集
- 训练多个模型（如线性回归、岭回归、随机森林回归）
- 评估模型性能
- 选择最佳模型

**输入示例：**
```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 加载数据集
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 数据预处理
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 训练多个模型
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}

# 评估模型
results = {}
for name, model in models.items():
    # 训练
    model.fit(X_train, y_train)
    # 预测
    y_pred = model.predict(X_test)
    # 评估
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[name] = {'MSE': mse, 'R2': r2}
    print(f"{name}:")
    print(f"  MSE: {mse:.4f}")
    print(f"  R2: {r2:.4f}")

# 选择最佳模型
best_model_name = min(results, key=lambda x: results[x]['MSE'])
print(f"\n最佳模型：{best_model_name}")
print(f"最佳模型MSE：{results[best_model_name]['MSE']:.4f}")
print(f"最佳模型R2：{results[best_model_name]['R2']:.4f}")
```

**Q22. 编写一个程序，使用管道（Pipeline）和网格搜索对鸢尾花数据集进行分类。**

**输入示例：**
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建管道
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

# 定义参数网格
param_grid = {
    'svm__C': [0.1, 1, 10, 100],
    'svm__kernel': ['linear', 'rbf', 'poly'],
    'svm__gamma': ['scale', 'auto']
}

# 网格搜索
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# 最佳参数
print(f"最佳参数：{grid_search.best_params_}")
print(f"最佳交叉验证准确率：{grid_search.best_score_:.4f}")

# 使用最佳模型评估
test_accuracy = grid_search.score(X_test, y_test)
print(f"测试集准确率：{test_accuracy:.4f}")
```

**Q23. 编写一个程序，使用集成学习方法（如投票分类器）对乳腺癌数据集进行分类。**

**输入示例：**
```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report

# 加载数据集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建基础模型
model1 = LogisticRegression(max_iter=10000)
model2 = DecisionTreeClassifier(random_state=42)
model3 = SVC(probability=True, random_state=42)

# 创建投票分类器
voting_clf = VotingClassifier(
    estimators=[
        ('logreg', model1),
        ('tree', model2),
        ('svm', model3)
    ],
    voting='soft'  # 使用概率进行投票
)

# 训练模型
voting_clf.fit(X_train, y_train)

# 评估基础模型
for name, model in [('Logistic Regression', model1), ('Decision Tree', model2), ('SVM', model3)]:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name}准确率：{accuracy:.4f}")

# 评估投票分类器
y_pred = voting_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n投票分类器准确率：{accuracy:.4f}")
print("\n分类报告：")
print(classification_report(y_test, y_pred))
```

## 6. 答案

### 1. 数据预处理

**Q1. 答案：**
```python
import pandas as pd

# 读取CSV文件
df = pd.read_csv('data.csv')
# 显示前5行
print(df.head())
```

**Q2. 答案：**
```python
import pandas as pd
import numpy as np

# 创建包含缺失值的数据框
data = {'A': [1, 2, np.nan, 4, 5], 'B': [6, np.nan, 8, 9, 10]}
df = pd.DataFrame(data)
print("原始数据：")
print(df)

# 填充缺失值
filled_df = df.fillna(df.mean())
print("\n填充后的数据：")
print(filled_df)
```

**Q3. 答案：**
```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# 创建数据
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("原始数据：")
print(data)

# 标准化
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
print("\n标准化后的数据：")
print(scaled_data)
```

**Q4. 答案：**
```python
import pandas as pd

# 创建包含分类变量的数据框
data = {'category': ['A', 'B', 'C', 'A', 'B']}
df = pd.DataFrame(data)
print("原始数据：")
print(df)

# 独热编码
encoded_df = pd.get_dummies(df, columns=['category'])
print("\n编码后的数据：")
print(encoded_df)
```

**Q5. 答案：**
```python
from sklearn.model_selection import train_test_split
import numpy as np

# 创建数据
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = np.array([0, 1, 0, 1, 0])

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("训练集特征：")
print(X_train)
print("训练集标签：")
print(y_train)
print("\n测试集特征：")
print(X_test)
print("测试集标签：")
print(y_test)
```

**Q6. 答案：**
```python
import pandas as pd

# 创建时间序列数据
dates = pd.date_range('2023-01-01', periods=5)
data = {'date': dates, 'value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
print("原始数据：")
print(df)

# 提取时间组件
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
print("\n提取时间组件后的数据：")
print(df)
```

### 2. 监督学习

**Q7. 答案：**
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 预测
y_pred = knn.predict(X_test)

# 评估
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率：{accuracy:.4f}")
```

**Q8. 答案：**
```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 加载数据集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
logreg = LogisticRegression(max_iter=10000)
logreg.fit(X_train, y_train)

# 预测
y_pred = logreg.predict(X_test)

# 评估
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率：{accuracy:.4f}")
print("\n分类报告：")
print(classification_report(y_test, y_pred))
```

**Q9. 答案：**
```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 加载数据集
wine = load_wine()
X = wine.data
y = wine.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

# 预测
y_pred = tree.predict(X_test)

# 评估
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率：{accuracy:.4f}")
```

**Q10. 答案：**
```python
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 加载数据集
boston = load_boston()
X = boston.data
y = boston.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
lr = LinearRegression()
lr.fit(X_train, y_train)

# 预测
y_pred = lr.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"均方误差：{mse:.4f}")
print(f"R²评分：{r2:.4f}")
```

**Q11. 答案：**
```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# 加载数据集
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# 预测
y_pred = ridge.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差：{mse:.4f}")
```

**Q12. 答案：**
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 加载数据集
df = pd.read_csv('hour.csv')

# 准备特征和标签
X = df.drop(['cnt', 'dteday'], axis=1)
y = df['cnt']

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 预测
y_pred = rf.predict(X_test)

# 评估
mse = mean_squared_error(y_test, y_pred)
print(f"均方误差：{mse:.4f}")
```

### 3. 无监督学习

**Q13. 答案：**
```python
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 加载数据集
iris = load_iris()
X = iris.data

# 训练模型
kmeans = KMeans(n_clusters=3, random_state=42)
y_pred = kmeans.fit_predict(X)

# 可视化
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', marker='X')
plt.title('K-means Clustering on Iris Dataset')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()
```

**Q14. 答案：**
```python
from sklearn.datasets import load_wine
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# 加载数据集
wine = load_wine()
X = wine.data

# 层次聚类
linked = linkage(X, 'ward')

# 绘制 dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked, truncate_mode='lastp', p=12, leaf_rotation=45., leaf_font_size=15., show_contracted=True)
plt.title('Dendrogram for Wine Dataset')
plt.xlabel('Sample index')
plt.ylabel('Euclidean distance')
plt.show()

# 训练模型
agg = AgglomerativeClustering(n_clusters=3)
y_pred = agg.fit_predict(X)
print(f"聚类结果：{y_pred}")
```

**Q15. 答案：**
```python
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# PCA降维
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 可视化
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.title('PCA on Iris Dataset')
plt.xlabel('First principal component')
plt.ylabel('Second principal component')
plt.show()

# 查看解释方差比
print(f"解释方差比：{pca.explained_variance_ratio_}")
print(f"累计解释方差：{sum(pca.explained_variance_ratio_):.4f}")
```

**Q16. 答案：**
```python
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 加载数据集
digits = load_digits()
X = digits.data
y = digits.target

# 随机选择部分样本以加快计算
import numpy as np
np.random.seed(42)
indices = np.random.choice(range(len(X)), 500)
X_subset = X[indices]
y_subset = y[indices]

# t-SNE降维
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_subset)

# 可视化
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_subset, cmap='tab10')
plt.title('t-SNE on MNIST Dataset')
plt.xlabel('t-SNE 1')
plt.ylabel('t-SNE 2')
plt.colorbar()
plt.show()
```

### 4. 模型评估与调优

**Q17. 答案：**
```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 创建模型
knn = KNeighborsClassifier(n_neighbors=3)

# 交叉验证
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
print(f"交叉验证准确率：{scores}")
print(f"平均准确率：{scores.mean():.4f}")
print(f"准确率标准差：{scores.std():.4f}")
```

**Q18. 答案：**
```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt

# 加载数据集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
logreg = LogisticRegression(max_iter=10000)
logreg.fit(X_train, y_train)

# 预测
y_pred = logreg.predict(X_test)
y_pred_proba = logreg.predict_proba(X_test)[:, 1]

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
print("混淆矩阵：")
print(cm)

# ROC曲线
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
```

**Q19. 答案：**
```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 定义参数网格
param_grid = {'n_neighbors': [1, 3, 5, 7, 9, 11]}

# 创建模型
knn = KNeighborsClassifier()

# 网格搜索
grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# 最佳参数
print(f"最佳参数：{grid_search.best_params_}")
print(f"最佳交叉验证准确率：{grid_search.best_score_:.4f}")

# 使用最佳参数评估模型
best_knn = grid_search.best_estimator_
test_accuracy = best_knn.score(X_test, y_test)
print(f"测试集准确率：{test_accuracy:.4f}")
```

**Q20. 答案：**
```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
import numpy as np

# 加载数据集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 定义参数分布
param_dist = {
    'n_estimators': np.arange(10, 201, 10),
    'max_depth': np.arange(1, 11),
    'min_samples_split': np.arange(2, 11),
    'min_samples_leaf': np.arange(1, 6)
}

# 创建模型
rf = RandomForestClassifier(random_state=42)

# 随机搜索
random_search = RandomizedSearchCV(
    rf, param_distributions=param_dist, n_iter=100, cv=5, scoring='accuracy', random_state=42
)
random_search.fit(X_train, y_train)

# 最佳参数
print(f"最佳参数：{random_search.best_params_}")
print(f"最佳交叉验证准确率：{random_search.best_score_:.4f}")

# 使用最佳参数评估模型
best_rf = random_search.best_estimator_
test_accuracy = best_rf.score(X_test, y_test)
print(f"测试集准确率：{test_accuracy:.4f}")
```

### 5. 综合练习题

**Q21. 答案：**
```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 加载数据集
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# 数据预处理
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 训练多个模型
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}

# 评估模型
results = {}
for name, model in models.items():
    # 训练
    model.fit(X_train, y_train)
    # 预测
    y_pred = model.predict(X_test)
    # 评估
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[name] = {'MSE': mse, 'R2': r2}
    print(f"{name}:")
    print(f"  MSE: {mse:.4f}")
    print(f"  R2: {r2:.4f}")

# 选择最佳模型
best_model_name = min(results, key=lambda x: results[x]['MSE'])
print(f"\n最佳模型：{best_model_name}")
print(f"最佳模型MSE：{results[best_model_name]['MSE']:.4f}")
print(f"最佳模型R2：{results[best_model_name]['R2']:.4f}")
```

**Q22. 答案：**
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

# 加载数据集
iris = load_iris()
X = iris.data
y = iris.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建管道
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

# 定义参数网格
param_grid = {
    'svm__C': [0.1, 1, 10, 100],
    'svm__kernel': ['linear', 'rbf', 'poly'],
    'svm__gamma': ['scale', 'auto']
}

# 网格搜索
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# 最佳参数
print(f"最佳参数：{grid_search.best_params_}")
print(f"最佳交叉验证准确率：{grid_search.best_score_:.4f}")

# 使用最佳模型评估
test_accuracy = grid_search.score(X_test, y_test)
print(f"测试集准确率：{test_accuracy:.4f}")
```

**Q23. 答案：**
```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, classification_report

# 加载数据集
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建基础模型
model1 = LogisticRegression(max_iter=10000)
model2 = DecisionTreeClassifier(random_state=42)
model3 = SVC(probability=True, random_state=42)

# 创建投票分类器
voting_clf = VotingClassifier(
    estimators=[
        ('logreg', model1),
        ('tree', model2),
        ('svm', model3)
    ],
    voting='soft'  # 使用概率进行投票
)

# 训练模型
voting_clf.fit(X_train, y_train)

# 评估基础模型
for name, model in [('Logistic Regression', model1), ('Decision Tree', model2), ('SVM', model3)]:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name}准确率：{accuracy:.4f}")

# 评估投票分类器
y_pred = voting_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n投票分类器准确率：{accuracy:.4f}")
print("\n分类报告：")
print(classification_report(y_test, y_pred))
```

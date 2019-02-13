# -*- coding: utf-8 -*-
import pandas as pd
# 这里会报经过方法在后面版本已经被修改，但是我还没有好的合适的新方法
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
# 逻辑回归，自动建模
fileName = './bankloan.xls'
data = pd.read_excel(fileName)
# 取前8列
x = data.iloc[:, :8].values
# 取最后一列
y = data.iloc[:, 8].values

print(x)
print(y)
# 建立随机逻辑回归模型，筛选变量
rlr = RLR()
# 训练模型
rlr.fit(x, y)
# 获取特征筛选结果
rlr.get_support(indices=True)
print(rlr.get_support(indices=True))
print("通过随机逻辑回归模型筛选特征结果")
print('有效特征为: %s' % ','.join(data.columns[rlr.get_support(indices=True)]))
# 筛选好特征
x = data[data.columns[rlr.get_support(indices=True)]].values
# 建立逻辑回归模型
lr = LR(solver='liblinear')
# 训练模型
lr.fit(x, y)
print("逻辑回归模型训练结束")
print('平均准确率为： %s' % lr.score(x, y))

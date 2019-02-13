# -*- coding: utf-8 -*-
# 使用K-Means算法聚类消费行为特征数据

import numpy as np
import pandas as pd

# 销量及其他属性数据
inputFile = './consumption_data.xls'
# 聚类的类别
k = 3
# 离散点阈值
threshold = 2
# 聚类最大循环次数
iteration = 500
# 读取数据
data = pd.read_excel(inputFile, index_col='Id')
# 数据标准化
data_zs = 1.0*(data - data.mean())/data.std()

from sklearn.cluster import KMeans

# 分为k类，并发数4
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
model.fit(data_zs)
# 标准化数据及其类别
# 每个样本对应的类别
r = pd.concat([data_zs, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + [u'聚类类别']

norm = []
for i in range(k):
    norm_tmp = r[['R', 'F', 'M']][r[u'聚类类别'] == i]-model.cluster_centers_[i]
    # 求出绝对距离
    norm_tmp = norm_tmp.apply(np.linalg.norm, axis=1)
    # 求相对距离并添加
    norm.append(norm_tmp/norm_tmp.median())
# 合并
norm = pd.concat(norm)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 正常点
norm[norm <= threshold].plot(style='go')
# 离群点
discrete_points = norm[norm > threshold]
discrete_points.plot(style='ro')
# 离群点做标记
for i in range(len(discrete_points)):
  id = discrete_points.index[i]
  n = discrete_points.iloc[i]
  plt.annotate('(%s, %0.2f)' % (id, n), xy=(id, n), xytext=(id, n))

plt.xlabel(u'编号')
plt.ylabel(u'相对距离')
plt.show()

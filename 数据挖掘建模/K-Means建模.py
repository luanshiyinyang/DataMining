# -*- coding: utf-8 -*-
# 使用K-Means算法聚类消费行为特征数据
import pandas as pd
from sklearn.cluster import KMeans
inputFile = './consumption_data.xls'
outputFile = './data_type.xls'
# 类别数目
k = 3
# 聚类最大循环次数
iteration = 500
data = pd.read_excel(inputFile, index_col='Id')
# 标准化数据
data_zs = 1.0*(data - data.mean())/data.std()
model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
# 开始聚类
model.fit(data_zs)
# 统计各个类别的数目
r1 = pd.Series(model.labels_).value_counts()
# 找出聚类中心
r2 = pd.DataFrame(model.cluster_centers_)
# 横向连接（0是纵向），得到聚类中心对应的类别下的数目
r = pd.concat([r2, r1], axis=1)
# 重命名表头
r.columns = list(data.columns) + [u'类别数目']
print(r)

# 详细输出原始数据及其类别
# 详细输出每个样本对应的类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + [u'聚类类别']
r.to_excel(outputFile)


def density_plot(data):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    p = data.plot(kind='kde', linewidth=2, subplots=True, sharex=False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.legend()
    return plt


pic_output = './pd_'
for i in range(k):
  density_plot(data[r[u'聚类类别'] == i]).savefig(u'%s%s.png' % (pic_output, i))

from sklearn.manifold import TSNE

tsne = TSNE()
# 进行数据降维
tsne.fit_transform(data_zs)
# 转换数据格式
tsne = pd.DataFrame(tsne.embedding_, index=data_zs.index)

import matplotlib.pyplot as plt
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()

# -*- coding: utf-8 -*-
"""
聚类离散化，最后结果的格式为：
      1           2           3           4
A     0    0.178698    0.257724    0.351843
An  240  356.000000  281.000000   53.000000
...
即(0, 0.178698]有240个，(0.178698, 0.257724]有356个，依此类推其他项。
"""
import pandas as pd
from sklearn.cluster import KMeans

dataFile = './data/data.xls'
resultFile = './data/data_processed.xls'
label = {u'肝气郁结证型系数': 'A', u'热毒蕴结证型系数': 'B', u'冲任失调证型系数': 'C', u'气血两虚证型系数': 'D', u'脾胃虚弱证型系数': 'E', u'肝肾阴虚证型系数': 'F'}
k = 4  # 需要进行的聚类类别数

# 读取数据并进行聚类分析
data = pd.read_excel(dataFile)  # 读取数据
keys = list(label.keys())
result = pd.DataFrame()

if __name__ == '__main__':
    for i in range(len(keys)):
        # 调用k-means算法，进行聚类离散化
        print(u'正在进行“{}”的聚类...'.format(keys[i]))
        kmodel = KMeans(n_clusters=k, n_jobs=4)
        kmodel.fit(data[[keys[i]]].as_matrix())
        r1 = pd.DataFrame(kmodel.cluster_centers_, columns=[label[keys[i]]])
        r2 = pd.Series(kmodel.labels_).value_counts()
        r2 = pd.DataFrame(r2, columns=[label[keys[i]] + 'n'])
        r = pd.concat([r1, r2], axis=1).sort_values(label[keys[i]])
        r.index = [1, 2, 3, 4]
        # 这两句代码将原来的聚类中心改为边界点
        r[label[keys[i]]] = r[label[keys[i]]].rolling(2).mean()
        r[label[keys[i]]][1] = 0.0
        result = result.append(r.T)
    # 以Index排序，即以A,B,C,D,E,F顺序排
    result = result.sort_index()
    result.to_excel(resultFile)
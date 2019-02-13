#- *- coding: utf-8 -*-
# 主成分分析 降维
import pandas as pd
from sklearn.decomposition import PCA

inputFile = './principal_component.xls'
outputFile = './dimention_reducted.xls'
data = pd.read_excel(inputFile, header=None)
pca = PCA()
pca.fit(data)
# 返回模型的各个特征向量
pca.components_
# 返回各个成分各自的方差百分比
pca.explained_variance_ratio_
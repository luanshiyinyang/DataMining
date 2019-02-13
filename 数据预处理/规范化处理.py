# -*- coding: utf-8 -*-
# 数据规范化
import pandas as pd
import numpy as np

datafile = './normalization_data.xls'
# 无表头的excel文件
data = pd.read_excel(datafile, header=None)
# 最小-最大规范化
print((data - data.min())/(data.max() - data.min()) )
# 零-均值规范化
print((data - data.mean())/data.std())
# 小数定标规范化
print(data/10**np.ceil(np.log10(data.abs().max())))
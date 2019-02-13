# -*- coding: utf-8 -*-
import pandas as pd
catering_sale = './catering_sale_all.xls'
data = pd.read_excel(catering_sale, index_col="日期")
# 计算相关系数矩阵
print(data.corr())
# 计算指定对象与其他之间的相关系数
print(data.corr()['百合酱蒸凤爪'])
# 计算两者之间的相关系数
print(data['百合酱蒸凤爪'].corr(data['翡翠蒸香茜饺']))
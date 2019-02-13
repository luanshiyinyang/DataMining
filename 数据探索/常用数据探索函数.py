# -*- coding: utf-8 -*-
import pandas as pd
source = './test.xlsx'
data = pd.read_excel(source, index_col='ID')
print("打印数据类型")
print(type(data))
data_0 = data["A"]
print("打印数据类型")
print(type(data_0))
# 求和
print("求和")
print(data.sum())
print(data_0.sum())
print("计算算数平均数")
# 计算算数平均数
print(data.mean())
print(data_0.mean())
# 计算方差
print("计算方差")
print(data.var())
print(data_0.var())
# 计算标准差
print("计算标准差")
print(data.std())
print(data_0.std())
# 计算相关系数
print("计算相关系数")
# method为计算方法，可选为pearson,kendall,spearman
print(data.corr(method='pearson'))
print(data["A"].corr(data["B"]))
# 计算协方差矩阵
print("计算协方差矩阵")
print(data.cov())
print(data.loc[101].cov(data.loc[102]))
# 计算阶矩
print("计算阶矩")
print(data.skew())
print(data_0.kurt())
# 基本统计量
print("基本统计量")
print(data.describe())
print(type(data.describe()))
print(data.describe().loc["mean"])
# -*- coding:utf-8 -*-
# 导入数据分析库和绘图库
import pandas as pd
import matplotlib.pyplot as plt
# 指定数据来源（本地）
catering_sale = './catering_sale.xls'
# 读取数据，指定日期列为索引
data = pd.read_excel(catering_sale, index_col="日期")
# 这里与运算必须这样使用
data = data[(data["销量"] > 400) & (data["销量"] < 5000)]
statistics = data.describe()
# 极差
statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
# 变异系数
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
# 四分位数间距
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']
print(statistics)
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

dish_profit = './catering_dish_profit.xls'
data = pd.read_excel(dish_profit, index_col="菜品名")
data = data[u'盈利'].copy()
# 参数修改，降序排列
data.sort_values(ascending=False)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
data.plot(kind='bar')
plt.ylabel("盈利（元）")
p = 1.0 * data.cumsum() / data.sum()
p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.ylabel("盈利（比例）")
plt.show()
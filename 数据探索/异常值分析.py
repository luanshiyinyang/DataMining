# -*- coding:utf-8 -*-
# 导入数据分析库和绘图库
import pandas as pd
import matplotlib.pyplot as plt
# 指定数据来源（本地）
catering_sale = './catering_sale.xls'
# 读取数据，指定日期列为索引
data = pd.read_excel(catering_sale, index_col="日期")
print("数据量")
print(len(data))
print("显示数据大致分析情况")
print(data.describe())

# 配置plt显示
# 显示中文，不加为方框
# 显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 建立图像，类似MATLAB中的figure
plt.figure()
# 绘制箱型图
p = data.boxplot(return_type='dict')
# 异常值数据
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
# 进行排序，修改原对象
y.sort()

for i in range(len(x)):
    if i > 0:
        # xy为注释坐标点，xytext为注释文字的位置
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.08, y[i]))
plt.show()

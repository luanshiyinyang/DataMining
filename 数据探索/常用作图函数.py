import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 显示中文，不加为方框
plt.rcParams['font.sans-serif'] = ['SimHei']
# 显示负号
plt.rcParams['axes.unicode_minus'] = False
# 创建图像区域，指定比例（可以不指定）
plt.figure(figsize=(8, 6))

# 绘制线性图
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.plot(x, y, 'bp--')
plt.show()
# 也可以直接用DataFrame或者Series调用plot方法，指定绘图类型（kind），默认index为横坐标
plt.figure()
data = pd.DataFrame([[1, 2, 3], [2, 3, 4]])
data.plot(kind='line', )
plt.show()

# 饼图
plt.figure()
labels = ["A", "B", "C", "D"]
sizes = [15, 30, 45, 10]
colors = ['yellow', 'green', 'lightskyblue', 'lightcoral']
explode = [0, 0.1, 0, 0]
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()

# 条形图
plt.figure()
x = np.random.randn(1000)
plt.hist(x, 10)
plt.show()

# 箱型图
plt.figure()
D = pd.DataFrame([x, x+1]).T
D.plot(kind='box')
plt.show()

# 误差条形图
error = np.random.randn(10)
y = pd.Series(np.sin(np.arange(10)))
y.plot(yerr=error)
plt.figure()
plt.show()


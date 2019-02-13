import pandas as pd
from scipy.interpolate import lagrange

inputFile = './catering_sale.xls'
outputFile = './sales.xls'

data = pd.read_excel(inputFile)
# 异常值置为空
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None

# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5


def ployinterp_column(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i], j)
data.to_excel(outputFile)
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz
# 使用ID3决策树算法预测销量高低
inputFile = './sales_data.xls'
data = pd.read_excel(inputFile, index_col=u"序号")
# 用1表示“好、是、高”三个属性，-1拜师其反面
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].values.astype(int)
y = data.iloc[:, 3].values.astype(int)
dtc = DTC(criterion='entropy')
dtc.fit(x, y)
# 训练之后表头丢失
x = pd.DataFrame(x)
x.columns = ['天气', '是否周末', '是否促销']
y = pd.DataFrame(y)
y.columns = ['销量']
with open("tree.dot", 'w', encoding='utf-8') as f:
    f = export_graphviz(dtc, feature_names=x.columns, out_file=f)

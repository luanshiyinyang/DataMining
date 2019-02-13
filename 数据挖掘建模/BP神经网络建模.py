# -*- coding: utf-8 -*-
# 使用神经网络算法预测销量
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation
inputFile = './sales_data.xls'
data = pd.read_excel(inputFile, index_col=u'序号')
# 字符串数值化
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = 0
x = data.iloc[:, :3].values.astype(int)
y = data.iloc[:, 3].values.astype(int)
model = Sequential()
model.add(Dense(input_dim=3, units=10))
# 指定激活函数
model.add(Activation('relu'))
model.add(Dense(input_dim=10, units=1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam')
# 编译模型，由于是二元分类，所以指定损失函数为binary_crossentropy,以及模式为binary
# 常见损失函数还有mean_squaed_error,categorical_crossentropy
# 求解方法指定adam，还有sgd，rmsprop可选
model.fit(x, y, epochs=1000, batch_size=10)
yp = model.predict_classes(x).reshape(len(y))
# 导入自定义模块
from cm_plot import *
cm_plot(y, yp).show()

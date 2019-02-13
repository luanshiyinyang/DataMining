# -*- coding: utf-8 -*-
"""
利用神经网络挖掘建模
"""
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

inputFile1 = 'data/train_neural_network_data.xls'
inputFile2 = 'data/test_neural_network_data.xls'
testoutputfile = 'data/test_output_data.xls'
data_train = pd.read_excel(inputFile1)
data_test = pd.read_excel(inputFile2)
y_train = data_train.iloc[:, 4].as_matrix()
x_train = data_train.iloc[:, 5:17].as_matrix()
y_test = data_test.iloc[:, 4].as_matrix()
x_test = data_test.iloc[:, 5:17].as_matrix()

# 建模
model = Sequential()
# 添加输入层、隐藏层的连接
model.add(Dense(input_dim=11, units=17))
# 以Relu函数为激活函数
model.add(Activation('relu'))
# 添加隐藏层、隐藏层的连接
model.add(Dense(input_dim=17, units=10))
# 以Relu函数为激活函数
model.add(Activation('relu'))
# 添加隐藏层、输出层的连接
model.add(Dense(input_dim=10, units=1))
# 以sigmoid函数为激活函数
model.add(Activation('sigmoid'))
# 编译模型，损失函数为binary_crossentropy，用adam法求解
model.compile(loss='binary_crossentropy', optimizer='adam')

model.fit(x_train, y_train, epochs=100, batch_size=1)
model.save_weights('data/net.model')

r = pd.DataFrame(model.predict_classes(x_test), columns=['预测结果'])
pd.concat([data_test.iloc[:, :5], r], axis=1).to_excel(testoutputfile)
rst = model.predict(x_test)
print(rst)
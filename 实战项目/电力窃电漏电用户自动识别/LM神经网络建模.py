# -*- coding: utf-8 -*-
"""
使用LM神经网络进行建模分析
"""
import pandas as pd
import matplotlib.pyplot as plt
from random import shuffle
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from cm_plot import *
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

def getDataSet(fileName):
    data = pd.read_excel(fileName)
    data = data.values
    # 随机打乱
    shuffle(data)
    rawData = data[:, :3]
    rawLabel = data[:, 3]
    trainData, testData, trainLabel, testLabel = train_test_split(rawData, rawLabel, test_size=0.2)

    def modeling(trainData, trainLabel, testData, testLabel):
        '''
        构建LM神经网络
        :return:
        '''
        netFile = 'net.model'
        net = Sequential()
        # 添加输入层（3结点）到隐藏层（10结点）的连接
        net.add(Dense(input_dim=3, units=10))
        # 隐藏层使用relu激活函数
        net.add(Activation('relu'))
        # 添加隐藏层（10结点）到输出层（1结点）的连接
        net.add(Dense(input_dim=10, units=1))
        # 输出层使用sigmoid激活函数
        net.add(Activation('sigmoid'))
        net.compile(loss='binary_crossentropy', optimizer='adam')
        # 循环1000次训练模型
        net.fit(trainData, trainLabel, epochs=1000, batch_size=1)

        # 本地化模型
        net.save_weights(netFile)

        # 训练集数据回判
        # keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n*1维数组，而不是通常的1*n
        rst = net.predict_classes(trainData).reshape(len(trainData))
        # 输出混淆矩阵
        cm = confusion_matrix(trainLabel, rst)
        print('训练集混淆矩阵', cm)

        # 测试集预测
        rst_test = net.predict_classes(testData).reshape(len(testData))
        cm2 = confusion_matrix(testLabel, rst_test)
        print('测试集混淆矩阵', cm2)
        rst2 = net.predict(testData).reshape(len(testData))
        fpr, tpr, thresholds = roc_curve(testLabel, rst2, pos_label=1)
        #
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.plot(fpr, tpr, linewidth=2, label='ROC of LM')
        plt.title("LM神经网络分类结果")
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.ylim(0, 1.05)
        plt.xlim(0, 1.05)
        plt.legend(loc=4)
        plt.show()

    modeling(trainData, trainLabel, testData, testLabel)


if __name__ == '__main__':
    getDataSet('./data/model.xls')

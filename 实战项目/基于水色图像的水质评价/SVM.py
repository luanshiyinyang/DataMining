# -*- coding: utf-8 -*-
import pandas as pd
from numpy.random import shuffle
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split


def getDataSet(fileName):
    # 取得原数据切分落地
    data = pd.read_csv(fileName, encoding='gbk')
    data = data.values
    # 随机打乱
    shuffle(data)
    label = data[:, :1]
    dataSet = data[:, 2:]
    # 这里依然遵循机器学习最原始的82开分配训练集和测试集
    trainData, testData, trainLabel, testLabel = train_test_split(dataSet, label, test_size=0.2)
    # 这里参数过多就直接定义一个内部函数

    def dataAdjust(trainData, testData, trainLabel, testLabel):
        # 数据区间过于接近，经过数据探索不难得知需要扩大数据范围，经过分析可以进行*30操作
        x_train = trainData[:, :]*30
        y_train = trainLabel[:, :].astype(int)
        x_test = testData[:, :]*30
        y_test = testLabel[:, :].astype(int)
        return x_train, y_train, x_test, y_test
    a, b, c, d = dataAdjust(trainData, testData, trainLabel, testLabel)
    return a, b, c, d


def modeling(x_train, y_train, x_test, y_test):
    # 建立模型
    model = svm.SVC()
    model.fit(x_train, y_train)
    # 预测数据生成混淆矩阵
    # 首先预测训练集，成为回判
    cm_train = metrics.confusion_matrix(y_train, model.predict(x_train))
    # 再预测测试集
    cm_test = metrics.confusion_matrix(y_test, model.predict(x_test))
    pd.DataFrame(cm_train, index=range(1, 6), columns=range(1, 6)).to_excel('训练集回判预测混淆矩阵.xls')
    pd.DataFrame(cm_test, index=range(1, 6), columns=range(1, 6)).to_excel('测试集预测混淆矩阵.xls')


if __name__ == '__main__':
    inputFile = './data/moment.csv'
    a, b, c, d = getDataSet(inputFile)
    modeling(a, b, c, d)
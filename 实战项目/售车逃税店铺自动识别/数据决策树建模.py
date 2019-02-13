# -*- coding: utf-8 -*-
"""
使用决策树进行建模估计
"""
import matplotlib.pyplot as plt
import pandas as pd
from random import shuffle


def getDataSet(fileName):
    data = pd.read_excel(fileName).iloc[:, 1:]
    data = data.values
    # 随机打乱
    shuffle(data)
    rawData = data[:, :11]
    rawLabel = data[:, 11].astype(int)
    from sklearn.model_selection import train_test_split
    trainData, testData, trainLabel, testLabel = train_test_split(rawData, rawLabel, test_size=0.2)

    def modeling(trainData, trainLabel, testData, testLabel):
        from sklearn.tree import DecisionTreeClassifier
        clf = DecisionTreeClassifier()
        clf.fit(trainData, trainLabel)

        # 回判训练集，输出混淆矩阵
        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(trainLabel, clf.predict(trainData))
        print(cm)

        # 预测测试集，输出ROC曲线
        from sklearn.metrics import roc_curve
        fpr, tpr, thresholds = roc_curve(testLabel, clf.predict_proba(testData)[:, 1], pos_label=1)
        plt.rcParams['font.sans-serif'] = ['Simhei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.clf()
        plt.plot(fpr, tpr, linewidth=2, label='ROC of CART', color='blue')
        plt.title('CART决策树分类结果')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.ylim(0, 1.05)
        plt.xlim(0, 1.05)
        plt.legend(loc=4)
        plt.show()
    modeling(trainData, trainLabel, testData, testLabel)
    return None


if __name__ == '__main__':
    dataFile = './data/sales_data_processed.xls'
    getDataSet(dataFile)
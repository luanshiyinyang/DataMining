# -*- coding: utf-8 -*-
"""
使用决策树建模数据预估
"""
import matplotlib.pyplot as plt
import pandas as pd
from random import shuffle
import pydotplus
from sklearn.externals.six import StringIO
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split

feathersName = None


def getDataSet(fileName):
    data = pd.read_excel(fileName)
    global feathersName
    # 提取特征名
    feathersName = data.columns[:3].values
    data = data.values
    # 随机打乱
    shuffle(data)
    # 设置训练集数据量为总数据的80%
    rawData = data[:, :3]
    rawLabel = data[:, 3]
    trainData, testData, trainLabel, testLabel = train_test_split(rawData, rawLabel, test_size=0.2)
    return trainData, testData, trainLabel, testLabel


def modeling(trainData, trainLabel, testData, testLabel):
    # 构建CART决策树模型
    clf = tree.DecisionTreeClassifier(max_depth=5)
    clf.fit(trainData, trainLabel)

    # 本地落地模型
    from sklearn.externals import joblib
    joblib.dump(clf, 'tree.pkl')

    # 可视化决策树
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    dot_data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data, feature_names=feathersName, class_names=str(clf.classes_),
                         filled=True, rounded=True, special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("tree.pdf")

    # 利用模型回判测试集,输出预测结果混淆矩阵
    cm = metrics.confusion_matrix(trainLabel, clf.predict(trainData))
    print(cm)

    # 利用模型预测测试集，输出ROC曲线
    from sklearn.metrics import roc_curve
    fpr, tpr, thresholds = roc_curve(testLabel, clf.predict_proba(testData)[:, 1], pos_label=1)
    plt.plot(fpr, tpr, linewidth=2, label='ROC of CART', color='green')
    plt.title("CART决策树分类结果")
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.ylim(0, 1.05)
    plt.xlim(0, 1.05)
    plt.legend(loc=4)
    plt.show()


if __name__ == '__main__':
    a, b, c, d = getDataSet('./data/model.xls')
    modeling(a, c, b, d)
# -*- coding:UTF-8 -*-
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
import pydotplus
from sklearn.externals.six import StringIO


def getDataSet(fileName):
    # 读取数据
    data = pd.read_csv(fileName)
    dataSet = []
    for item in data.values:
        dataSet.append(list(item[:5]))
    label = list(data['K'])
    return dataSet, label


def divide(dataSet, labels):
    '''
    分类数据，按比例拆开
    :param dataSet:
    :param labels:
    :return:
    '''
    train_data, test_data, train_label, test_label = train_test_split(dataSet, labels, test_size=0.2)
    return train_data, test_data, train_label, test_label


if __name__ == '__main__':
    data, label = getDataSet('./data/data_standard.csv')
    train_data, test_data, train_label, test_label = divide(data, label)
    clf = tree.DecisionTreeClassifier(max_depth=5)
    clf = clf.fit(train_data, train_label)
    # 可视化
    dataLabels = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC', ]
    data_list = []
    data_dict = {}
    for each_label in dataLabels:
        for each in data:
            data_list.append(each[dataLabels.index(each_label)])
        data_dict[each_label] = data_list
        data_list = []
    lenses_pd = pd.DataFrame(data_dict)
    print(lenses_pd.keys())
    dot_data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data, feature_names=lenses_pd.keys(),
                         class_names=clf.classes_, filled=True, rounded=True, special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("tree.pdf")
    from cm_plot import *
    cm_plot(test_label, clf.predict(test_data)).show()
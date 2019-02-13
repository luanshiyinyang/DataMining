# -*- coding: UTF-8 -*-
'''
使用K-Means进行聚类
'''
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


def leida(data, kmodel):
    '''
    画出雷达图
    :return:
    '''
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    labels = data.columns
    print(labels)
    k = 5
    plot_data = kmodel.cluster_centers_
    color = ['b', 'g', 'r', 'c', 'y']
    angles = np.linspace(0, 2*np.pi, k, endpoint=False)
    plot_data = np.concatenate((plot_data, plot_data[:, [0]]), axis=1)
    angles = np.concatenate((angles, [angles[0]]))
    fig = plt.figure()
    # polar参数
    ax = fig.add_subplot(111, polar=True)
    for i in range(len(plot_data)):
        # 画线
        ax.plot(angles, plot_data[i], 'o-', color=color[i], label=u'客户群'+str(i), linewidth=2)
    ax.set_rgrids(np.arange(0.01, 3.5, 0.5), np.arange(-1, 2.5, 0.5), fontproperties="SimHei")
    ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
    plt.legend(loc=4)
    plt.show()


if __name__ == '__main__':
    inputfile = './data/data_standard.csv'
    k = 5
    # 读取数据并进行聚类分析
    data = pd.read_csv(inputfile, encoding='utf-8')
    # 调用k-means算法，进行聚类分析
    # n_jobs是并行数，一般等于CPU数较好
    kmodel = KMeans(n_clusters=k, n_jobs=4)
    kmodel.fit(data)
    # 查看聚类中心
    kmodel.cluster_centers_
    # 查看各样本对应的类别
    kmodel.labels_
    leida(data, kmodel)

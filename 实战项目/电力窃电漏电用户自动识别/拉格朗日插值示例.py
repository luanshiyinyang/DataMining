# -*- coding: utf-8 -*-
"""
由于有些函数使用已经被官方修改，本模块有警告但是使用无妨
"""
import pandas as pd
from scipy.interpolate import lagrange


def lagrange_insert_column(s, n, k=5):
    '''
    自定义列向量插值函数（这里是纵向数据插值，对比值是纵向的，必然使用列向量插值函数）
    :param s: 列向量
    :param n: 插值位置
    :param k: 前后取值个数，默认5个数据
    :return:
    '''
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
    # 取出相关值，如果存在空数据直接剔除
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


if __name__ == '__main__':
    inputFile = './data/missing_data.xls'
    outputFile = './missing_data_processed.xls'
    # 读入数据
    data = pd.read_excel(inputFile, header=None)
    # 逐个元素判断是否需要插值
    for i in data.columns:
        for j in range(len(data)):
            if (data[i].isnull())[j]:
                data[i][j] = lagrange_insert_column(data[i], j)
    # 输出数据为插值之后的表格
    data.to_excel(outputFile, header=None, index=False)
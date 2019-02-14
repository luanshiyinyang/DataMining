# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd


def gaikuo():
    '''
    原始数据概括性度量
    :return:
    '''
    inputfile = 'data/data1.csv'
    data = pd.read_csv(inputfile)
    # 依次计算最小值、最大值、均值、标准差
    r = [data.min(), data.max(), data.mean(), data.std()]
    # 计算相关系数矩阵
    r = pd.DataFrame(r, index=['Min', 'Max', 'Mean', 'STD']).T
    # 保留两位小数
    np.round(r, 2)
    print(r)


def correlation():
    '''
    原始数据求解Pearson相关系数
    :return:
    '''
    inputfile = 'data/data1.csv'
    data = pd.read_csv(inputfile)
    np.round(data.corr(method='pearson'), 2)
    print(data)


if __name__ == '__main__':
    # gaikuo()
    correlation()
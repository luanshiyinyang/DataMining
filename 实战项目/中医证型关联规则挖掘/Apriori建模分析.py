# -*- coding: utf-8 -*-
"""
利用Apriori算法进行关联规则分析
"""
import pandas as pd
from apriori import *

if __name__ == '__main__':
    # 根据离散化处理的文件
    inputFile = './data/apriori.txt'
    data = pd.read_csv(inputFile, header=None, dtype=object)
    print('\n转换原始数据至0-1矩阵...')
    # 转换0-1矩阵的过渡函数
    ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])
    b = map(ct, data.values)
    # 实现矩阵转换，空值用0填充
    data = pd.DataFrame(list(b)).fillna(0)
    # 删除中间变量b，节省内存
    del b
    # 最小支持度
    support = 0.06
    # 最小置信度
    confidence = 0.75
    ms = '---'
    print('\n开始搜索关联规则...')
    find_rule(data, support, confidence, ms)


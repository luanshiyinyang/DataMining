# -*- coding: utf-8 -*-
"""
对数据基本探索
返回缺失值个数和最值
"""
import pandas as pd
if __name__ == '__main__':
    dataFile = './data/air_data.csv'
    resultFile = './data/explore.xls'
    data = pd.read_csv(dataFile, encoding='utf-8')
    # percentiles指定分位数
    explore = data.describe(percentiles=[], include='all').T
    # 手动补上空值数目
    explore['null'] = len(data) - explore['count']
    explore = explore[['null', 'max', 'min']]
    # 重命名表头
    explore.columns = [u'空值数', u'最大值', u'最小值']
    explore.to_excel(resultFile, encoding='utf-8')
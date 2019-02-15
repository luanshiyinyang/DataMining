# -*- coding: utf-8 -*-
import pandas as pd


def standard():
    '''
    数据标准化到[0,1]
    :return:
    '''
    filename = 'data/business_circle.xls'
    standardizedfile = 'data/standardized.xls'
    data = pd.read_excel(filename, index_col=u'基站编号')
    data = (data - data.min())/(data.max() - data.min())
    data = data.reset_index()
    data.to_excel(standardizedfile, index=False)


if __name__ == '__main__':
    standard()
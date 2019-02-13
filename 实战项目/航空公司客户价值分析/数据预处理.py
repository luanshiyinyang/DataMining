# -*- coding: utf-8 -*-
"""
进行了数据清洗，属性规约，数据变换等基本预处理操作
"""
import pandas as pd


def clean():
    '''
    数据清洗，去除空记录
    :param fileName:
    :return:
    '''
    cleanedFile = './data/data_cleaned.csv'
    data = pd.read_csv(dataFile, encoding='utf-8')
    # 非空保留
    data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]
    # 只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
    index1 = data['SUM_YR_1'] != 0
    index2 = data['SUM_YR_2'] != 0
    index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)
    data = data[index1 | index2 | index3]
    data.to_csv(cleanedFile)


def change(fileName):
    '''
    取出需要的属性列
    :param fileName:
    :return:
    '''
    changedFile = './data/data_changed.csv'
    data = pd.read_csv(fileName, encoding='utf-8')
    data = data[['LOAD_TIME', 'FFP_DATE', 'LAST_TO_END', 'FLIGHT_COUNT', 'avg_discount', 'SEG_KM_SUM', 'LAST_TO_END']]
    data.to_csv(changedFile, encoding='utf-8')


def LRFMC(fileName):
    '''
    经过计算得到我的指标数据
    :param fileName:
    :return:
    '''
    data = pd.read_csv(fileName)
    data2 = pd.DataFrame(columns=['L', 'R', 'F', 'M', 'C'])
    time_list = []
    import datetime
    for i in range(len(data['LOAD_TIME'])):
        str1 = data['LOAD_TIME'][i].split('/')
        str2 = data['FFP_DATE'][i].split('/')
        temp = datetime.datetime(int(str1[0]), int(str1[1]), int(str1[2])) - datetime.datetime(int(str2[0]), int(str2[1]), int(str2[2]))
        time_list.append(temp.days)
    data2['L'] = pd.Series(time_list)
    data2['R'] = data['LAST_TO_END']
    data2['F'] = data['FLIGHT_COUNT']
    data2['M'] = data['SEG_KM_SUM']
    data2['C'] = data['avg_discount']
    data2.to_csv('./data/data_changed2.csv', encoding='utf-8')


def standard():
    '''
    标准差标准化
    :return:
    '''
    data = pd.read_csv('./data/data_changed2.csv', encoding='utf-8').iloc[:, 1:]
    zscoredfile = './data/data_standard.csv'
    # 简洁的语句实现了标准化变换，类似地可以实现任何想要的变换
    data = (data - data.mean(axis=0)) / (data.std(axis=0))
    data.columns = ['Z' + i for i in data.columns]
    data.to_csv(zscoredfile, index=False)


if __name__ == '__main__':
    dataFile = './data/air_data.csv'
    clean()
    change('./data/data_cleaned.csv')
    LRFMC('./data/data_changed.csv')
    standard()

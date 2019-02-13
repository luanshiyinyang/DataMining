# -*- coding:UTF-8 -*
import pandas as pd


def attrStatute():
    '''
    属性规约
    :return:
    '''
    rawData = pd.read_excel('data/original_data.xls').drop(columns=["热水器编号","有无水流", "节能模式"])
    return rawData


def valueStatute():
    '''
    数值规约
    :return:
    '''
    data = pd.read_excel('data/water_heater.xls')
    newData = data[data['开关机状态'].isin(['关']) & data['水流量'].isin([0])]
    return newData


def divideEvent():
    '''
    事件划分
    :return:
    '''
    # 阈值设置为4分钟
    threshold = pd.Timedelta('4 min')
    inputFile = 'data/water_heater.xls'
    outputFile = 'data/dividesequence.xls'
    data = pd.read_excel(inputFile)
    data['发生时间'] = pd.to_datetime(data['发生时间'], format='%Y%m%d%H%M%S')
    # 只保留水流量大于0的记录
    data = data[data['水流量'] > 0]
    # 将原数据的发生时间做一阶差分，得到一个时间差值的dataframe
    d = data['发生时间'].diff() > threshold
    # 累计求和编号数据
    data['事件编号'] = d.cumsum() + 1
    data.to_excel(outputFile)


if __name__ == '__main__':
    # attrStatute().to_excel("data/water_heater.xls")
    # valueStatute().to_excel("data/water_heater2.xls")z
    divideEvent()
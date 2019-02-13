# -*- coding: utf-8 -*-
"""
在1-9分钟进行阈值寻优
"""
import numpy as np
import pandas as pd


def event_num(ts):
    '''
    得到事件数目
    :param ts:
    :return:
    '''
    d = data[u'发生时间'].diff() > ts
    return d.sum() + 1


if __name__ == '__main__':
    inputfile = 'data/water_heater.xls'
    # 使用以后四个点的平均斜率
    n = 4
    threshold = pd.Timedelta(minutes=5)
    data = pd.read_excel(inputfile)
    data[u'发生时间'] = pd.to_datetime(data[u'发生时间'], format='%Y%m%d%H%M%S')
    data = data[data[u'水流量'] > 0]
    dt = [pd.Timedelta(minutes=i) for i in np.arange(1, 9, 0.25)]
    # 定义阈值列
    h = pd.DataFrame(dt, columns=[u'阈值'])
    # 计算每个阈值对应的事件数
    h[u'事件数'] = h[u'阈值'].apply(event_num)
    # 计算每两个相邻点对应的斜率
    h[u'斜率'] = h[u'事件数'].diff()/0.25
    # 采用后n个的斜率绝对值平均作为斜率指标
    h[u'斜率指标'] = pd.DataFrame(h[u'斜率'].abs()[len(h)-n:]).rolling(2).mean()
    ts = h[u'阈值'][h[u'斜率指标'].idxmin() - n]
    if ts > threshold:
        ts = pd.Timedelta(minutes=4)
    print(ts)

# -*- coding:utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine


def chunkCount():
    '''
    访问数据库并进行分块统计
    :return:
    '''
    engine = create_engine('mysql+pymysql://root:155155@127.0.0.1:3306/data?charset=utf8')
    sql = pd.read_sql('all_gzdata', engine, chunksize=10000)
    # 逐块统计
    counts = [i['fullURLId'].value_counts() for i in sql]
    # 合并统计结果，把相同的统计项合并（即按index分组并求和）
    counts = pd.concat(counts).groupby(level=0).sum()
    # 重新设置index，将原来的index作为counts的一列。
    counts = counts.reset_index()
    # 重新设置列名，主要是第二列，默认为0
    counts.columns = ['index', 'num']
    # 提取前三个数字作为类别id
    counts['type'] = counts['index'].str.extract('(\d{3})')
    # 按类别合并
    counts_ = counts[['type', 'num']].groupby('type').sum()
    # 降序排列
    print(counts_.sort_values('num', ascending=False))


def count107Main():
    def count107(i):
        '''
        统计107类别的情况
        :param i:
        :return:
        '''
        j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy()
        # 添加空列
        j['type'] = None
        j['type'][j['fullURL'].str.contains('info/.+?/')] = u'知识首页'
        j['type'][j['fullURL'].str.contains('info/.+?/.+?')] = u'知识列表页'
        j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')] = u'知识内容页'
        return j['type'].value_counts()
    engine = create_engine('mysql+pymysql://root:155155@127.0.0.1:3306/data?charset=utf8')
    sql = pd.read_sql('all_gzdata', engine, chunksize=10000)
    # 逐块统计
    # 合并统计结果
    counts2 = [count107(i) for i in sql]
    counts2 = pd.concat(counts2).groupby(level=0).sum()
    print(counts2)


def countTime():
    '''
    统计点击次数
    :return:
    '''
    engine = create_engine('mysql+pymysql://root:155155@127.0.0.1:3306/data?charset=utf8')
    sql = pd.read_sql('all_gzdata', engine, chunksize=10000)
    c = [i['realIP'].value_counts() for i in sql]
    # 分块统计各个IP的出现次数
    # 合并统计结果，level=0表示按index分组
    count3 = pd.concat(c).groupby(level=0).sum()
    # Series转为DataFrame
    count3 = pd.DataFrame(count3)
    # 添加一列，全为1
    count3[1] = 1
    # 统计各个“不同的点击次数”分别出现的次数
    count3_ = count3.groupby('realIP').sum()
    print(count3_)


if __name__ == '__main__':
    # chunkCount()
    # count107Main()
    countTime()

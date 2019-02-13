# -*- coding:utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:155155@127.0.0.1:3306/data?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)


def clean():
    '''
    清洗数据
    :return:
    '''
    for i in sql:
        # 只要网址列
        d = i[['realIP', 'fullURL']]
        # 只要含有.html的网址
        d = d[d['fullURL'].str.contains('\.html')].copy()
        # 保存到数据库的cleaned_gzdata表中（如果表不存在则自动创建）
        d.to_sql('cleaned_gzdata', engine, index=False, if_exists='append')


def change():
    '''
    数据变换
    :return:
    '''
    # 逐块变换并去重
    for i in sql:
        d = i.copy()
        # 将下划线后面部分去掉，规范为标准网址
        d['fullURL'] = d['fullURL'].str.replace('_\d{0,2}.html', '.html')
        # 删除重复记录
        d = d.drop_duplicates()
        # 保存
        d.to_sql('changed_gzdata', engine, index=False, if_exists='append')


def split():
    '''
    网址分类
    :return:
    '''
    for i in sql:
        d = i.copy()
        # 复制一列
        d['type_1'] = d['fullURL']
        # 将含有ask、askzt关键字的网址的类别一归为咨询（后面的规则就不详细列出来了，实际问题自己添加即可）
        d['type_1'][d['fullURL'].str.contains('(ask)|(askzt)')] = 'zixun'
        # 保存
        d.to_sql('splited_gzdata', engine, index=False, if_exists='append')


if __name__ == '__main__':
    # clean()
    # change()
    split()
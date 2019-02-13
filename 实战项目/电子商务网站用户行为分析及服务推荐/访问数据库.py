# -*- coding:utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine


def linkDatabase():
    '''
    用create_engine建立连接，连接地址的意思依次为“数据库格式（mysql）+程序名（pymysql）+账号密码@地址端口/数据库名（test）”，最后指定编码为utf8；
all_gzdata是表名，engine是连接数据的引擎，chunksize指定每次读取1万条记录。这时候sql是一个容器，未真正读取数据。
    :return:
    '''
    engine = create_engine('mysql+pymysql://root:155155@127.0.0.1:3306/data?charset=utf8')
    sql = pd.read_sql('all_gzdata', engine, chunksize=10000)
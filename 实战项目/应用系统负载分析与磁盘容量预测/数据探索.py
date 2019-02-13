# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
def draw():
    data = pd.read_excel('data/discdata.xls')
    str1 = 'C:\\'
    str2 = 'D:\\'
    dataC = data[(data['DESCRIPTION'] == '磁盘已使用大小') & (data['ENTITY'] == str1)]
    dataD = data[(data['DESCRIPTION'] == '磁盘已使用大小') & (data['ENTITY'] == str2)]
    dataC.plot(y='VALUE')
    dataD.plot(y='VALUE')
    plt.show()


if __name__ == '__main__':
    draw()
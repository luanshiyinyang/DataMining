# -*- coding:UTF-8 -*-
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('./data/data.csv')
    data.drop(['MEMBER_NO'], axis=1, inplace=True)
    data.describe().to_csv('./data/data_explored.csv')
    data.to_excel('./data/data.xls')


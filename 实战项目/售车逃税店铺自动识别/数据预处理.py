import pandas as pd
import numpy as np


def getDataSet():


    def autoNorm(dataSet):
        '''
        数值的不同范围影响很大，归一是必须的
        :param dataSet: 归一化之前的数据集
        :return: 归一化后的数据集
        '''
        # 获得数据的最小值
        minVals = dataSet.min(0)
        maxVals = dataSet.max(0)
        # 最大值和最小值的范围
        ranges = maxVals - minVals
        # shape(dataSet)返回dataSet的矩阵行列数
        normDataSet = np.zeros(np.shape(dataSet))
        # 返回dataSet的行数
        m = dataSet.shape[0]
        # 原始值减去最小值
        normDataSet = dataSet - np.tile(minVals, (m, 1))
        # 除以最大和最小值的差,得到归一化数据
        normDataSet = normDataSet / np.tile(ranges, (m, 1))
        # 返回归一化数据结果,数据范围,最小值
        return normDataSet, ranges, minVals

    data = pd.read_excel('./data/sales_data.xls', index_col=u"纳税人编号")
    # 去掉无关因素,取出需要数据列
    data = data.iloc[:, 2:15]
    print(data)
    # 数值化
    for i in range(1, len(data) + 1):
        if data['输出'][i] == u"正常":
            data['输出'][i] = 1
        else:
            data['输出'][i] = 0
    A, B, C = autoNorm(data.values)
    df = pd.DataFrame(A)
    df.to_excel('./data/sales_data_processed.xls')


if __name__ == '__main__':
    getDataSet()

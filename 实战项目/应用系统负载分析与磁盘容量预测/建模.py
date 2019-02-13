# -*- coding:utf-8 -*-
import pandas as pd



def stationarityTest():
    '''
    平稳性检验
    :return:
    '''
    discfile = 'data/discdata_processed.xls'
    predictnum = 5

    data = pd.read_excel(discfile)
    data = data.iloc[: len(data) - predictnum]
    # 平稳性检验
    from statsmodels.tsa.stattools import adfuller as ADF
    diff = 0
    adf = ADF(data['CWXT_DB:184:D:\\'])
    while adf[1] > 0.05:
        diff = diff + 1
        adf = ADF(data['CWXT_DB:184:D:\\'].diff(diff).dropna())

    print(u'原始序列经过%s阶差分后归于平稳，p值为%s' % (diff, adf[1]))


def whitenoiseTest():
    '''
    白噪声检验
    :return:
    '''
    discfile = 'data/discdata_processed.xls'
    data = pd.read_excel(discfile)
    data = data.iloc[: len(data) - 5]
    # 白噪声检验
    from statsmodels.stats.diagnostic import acorr_ljungbox
    [[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'], lags=1)
    if p < 0.05:
        print(u'原始序列为非白噪声序列，对应的p值为：%s' % p)
    else:
        print(u'原始该序列为白噪声序列，对应的p值为：%s' % p)
    [[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'].diff().dropna(), lags=1)
    if p < 0.05:
        print(u'一阶差分序列为非白噪声序列，对应的p值为：%s' % p)
    else:
        print(u'一阶差分该序列为白噪声序列，对应的p值为：%s' % p)


def findOptimalpq():
    '''
    得到模型参数
    :return:
    '''
    discfile = 'data/discdata_processed.xls'
    data = pd.read_excel(discfile, index_col='COLLECTTIME')
    data = data.iloc[: len(data) - 5]
    xdata = data['CWXT_DB:184:D:\\']

    from statsmodels.tsa.arima_model import ARIMA

    # 定阶
    # 一般阶数不超过length/10
    pmax = int(len(xdata) / 10)
    qmax = int(len(xdata) / 10)
    # bic矩阵
    bic_matrix = []
    for p in range(pmax + 1):
        tmp = []
        for q in range(qmax + 1):
            try:
                tmp.append(ARIMA(xdata, (p, 1, q)).fit().bic)
            except:
                tmp.append(None)
        bic_matrix.append(tmp)

    bic_matrix = pd.DataFrame(bic_matrix)
    # 先用stack展平，然后用idxmin找出最小值位置。
    p, q = bic_matrix.stack().astype('float64').idxmin()
    print(u'BIC最小的p值和q值为：%s、%s' % (p, q))


def arimaModelCheck():
    '''
    模型检验
    :return:
    '''
    discfile = 'data/discdata_processed.xls'
    # 残差延迟个数
    lagnum = 12

    data = pd.read_excel(discfile, index_col='COLLECTTIME')
    data = data.iloc[: len(data) - 5]
    xdata = data['CWXT_DB:184:D:\\']
    # 建立ARIMA(0,1,1)模型
    from statsmodels.tsa.arima_model import ARIMA
    # 建立并训练模型
    arima = ARIMA(xdata, (0, 1, 1)).fit()
    # 预测
    xdata_pred = arima.predict(typ='levels')
    # 计算残差
    pred_error = (xdata_pred - xdata).dropna()

    from statsmodels.stats.diagnostic import acorr_ljungbox
    # 白噪声检验
    lb, p = acorr_ljungbox(pred_error, lags=lagnum)
    # p值小于0.05，认为是非白噪声。
    h = (p < 0.05).sum()
    if h > 0:
        print(u'模型ARIMA(0,1,1)不符合白噪声检验')
    else:
        print(u'模型ARIMA(0,1,1)符合白噪声检验')


def calErrors():
    '''
    误差计算
    :return:
    '''
    # 参数初始化
    file = 'data/predictdata.xls'
    data = pd.read_excel(file)

    # 计算误差
    abs_ = (data[u'预测值'] - data[u'实际值']).abs()
    mae_ = abs_.mean()  # mae
    rmse_ = ((abs_ ** 2).mean()) ** 0.5
    mape_ = (abs_ / data[u'实际值']).mean()

    print(u'平均绝对误差为：%0.4f，\n均方根误差为：%0.4f，\n平均绝对百分误差为：%0.6f。' % (mae_, rmse_, mape_))


if __name__ == '__main__':
    # stationarityTest()
    # whitenoiseTest()
    # findOptimalpq()
    arimaModelCheck()
    calErrors()

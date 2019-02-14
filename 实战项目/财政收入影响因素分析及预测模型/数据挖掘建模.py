# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from GM11 import GM11


def adaptiveLasso():
    '''
    Adaptive-Lasso变量选择模型
    :return:
    '''
    inputfile = 'data/data1.csv'
    data = pd.read_csv(inputfile)
    # 导入AdaptiveLasso算法，要在较新的Scikit-Learn才有。
    from sklearn.linear_model import LassoLars
    model = LassoLars()
    model.fit(data.iloc[:, 0:13], data['y'])
    print(model.coef_)


def huise():
    '''
    地方财政收入灰色预测
    :return:
    '''
    inputfile = 'data/data1.csv'
    outputfile = 'data/data1_GM11.xls'
    data = pd.read_csv(inputfile)
    data.index = range(1994, 2014)

    data.loc[2014] = None
    data.loc[2015] = None
    l = ['x1', 'x2', 'x3', 'x4', 'x5', 'x7']
    for i in l:
        f = GM11(data[i][np.arange(1994, 2014)].values)[0]
        # 2014年预测结果
        data[i][2014] = f(len(data) - 1)
        # 2015年预测结果
        data[i][2015] = f(len(data))
        data[i] = data[i].round(2)

    data[l + ['y']].to_excel(outputfile)
    print(data)


def yuce():
    '''
    地方财政收入神经网络预测模型
    :return:
    '''
    inputfile = 'data/data1_GM11.xls'  # 灰色预测后保存的路径
    outputfile = 'data/revenue.xls'  # 神经网络预测后保存的结果
    modelfile = 'data/1-net.model'  # 模型保存路径
    data = pd.read_excel(inputfile)
    feature = ['x1', 'x2', 'x3', 'x4', 'x5', 'x7']  # 特征所在列

    data_train = data.loc[range(1994, 2014)].copy()  # 取2014年前的数据建模
    data_mean = data_train.mean()
    data_std = data_train.std()
    data_train = (data_train - data_mean) / data_std  # 数据标准化
    x_train = data_train[feature].values  # 特征数据
    y_train = data_train['y'].values  # 标签数据

    from keras.models import Sequential
    from keras.layers.core import Dense, Activation

    model = Sequential()  # 建立模型
    model.add(Dense(input_dim=6, units=12))
    model.add(Activation('relu'))  # 用relu函数作为激活函数，能够大幅提供准确度
    model.add(Dense(input_dim=12, units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')  # 编译模型
    model.fit(x_train, y_train, nb_epoch=10000, batch_size=16)  # 训练模型，学习一万次
    model.save_weights(modelfile)  # 保存模型参数

    # 预测，并还原结果。
    x = ((data[feature] - data_mean[feature]) / data_std[feature]).values
    data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']
    data.to_excel(outputfile)

    import matplotlib.pyplot as plt  # 画出预测结果图
    p = data[['y', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])
    plt.show()


def adaptiveLasso2():
    '''
    Adaptive-Lasso变量选择
    :return:
    '''

    inputfile = 'data/data2.csv'  # 输入的数据文件
    data = pd.read_csv(inputfile)  # 读取数据
    # 导入AdaptiveLasso算法，新版本已经删除
    from sklearn.linear_model import AdaptiveLasso
    model = AdaptiveLasso(gamma=1)
    model.fit(data.iloc[:, 0:6], data['y'])
    model.coef_  # 各个特征的系数


def huise2():
    '''
    增值税灰色预测
    :return:
    '''
    inputfile = 'data/data2.csv'  # 输入的数据文件
    outputfile = 'data/data2_GM11.xls'  # 灰色预测后保存的路径
    data = pd.read_csv(inputfile)  # 读取数据
    data.index = range(1999, 2014)

    data.loc[2014] = None
    data.loc[2015] = None
    l = ['x1', 'x3', 'x5']
    for i in l:
        f = GM11(data[i][np.arange(1999, 2014)].values)[0]
        data[i][2014] = f(len(data) - 1)  # 2014年预测结果
        data[i][2015] = f(len(data))  # 2015年预测结果
        data[i] = data[i].round(6)  # 保留六位小数
    data[l + ['y']].to_excel(outputfile)  # 结果输出
    print(data)


def yuce2():
    '''
    增值税神经网络预测模型
    :return:
    '''
    inputfile = 'data/data2_GM11.xls'  # 灰色预测后保存的路径
    outputfile = 'data/VAT.xls'  # 神经网络预测后保存的结果
    modelfile = 'data/2-net.model'  # 模型保存路径
    data = pd.read_excel(inputfile)  # 读取数据
    feature = ['x1', 'x3', 'x5']  # 特征所在列

    data_train = data.loc[np.arange(1999, 2014)].copy()  # 取2014年前的数据建模
    data_mean = data_train.mean()
    data_std = data_train.std()
    data_train = (data_train - data_mean) / data_std  # 数据标准化
    x_train = data_train[feature].values  # 特征数据
    y_train = data_train['y'].values  # 标签数据

    from keras.models import Sequential
    from keras.layers.core import Dense, Activation

    model = Sequential()  # 建立模型
    model.add(Dense(input_dim=3, units=6))
    model.add(Activation('relu'))  # 用relu函数作为激活函数，能够大幅提供准确度
    model.add(Dense(input_dim=6, units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')  # 编译模型
    model.fit(x_train, y_train, nb_epoch=10000, batch_size=16)  # 训练模型，学习一万次
    model.save_weights(modelfile)  # 保存模型参数

    # 预测，并还原结果。
    x = ((data[feature] - data_mean[feature]) / data_std[feature]).values
    data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']
    data[u'y_pred'] = data[u'y_pred'].round(2)
    data.to_excel(outputfile)

    import matplotlib.pyplot as plt  # 画出预测结果图
    p = data[['y', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])
    plt.show()



def adaptiveLasso3():
    '''
    Adaptive-Lasso变量选择
    :return:
    '''
    inputfile = 'data/data3.csv'  # 输入的数据文件
    data = pd.read_csv(inputfile)  # 读取数据

    # 导入AdaptiveLasso算法，要在较新的Scikit-Learn才有。
    from sklearn.linear_model import AdaptiveLasso
    model = AdaptiveLasso(gamma=1)
    model.fit(data.iloc[:, 0:10], data['y'])
    model.coef_  # 各个特征的系数


def huise3():
    '''
    营业税灰色预测
    :return:
    '''
    inputfile = 'data/data3.csv'  # 输入的数据文件
    outputfile = 'data/data3_GM11.xls'  # 灰色预测后保存的路径
    data = pd.read_csv(inputfile)  # 读取数据
    data.index = range(1999, 2014)

    data.loc[2014] = None
    data.loc[2015] = None
    l = ['x3', 'x4', 'x6', 'x8']
    for i in l:
        f = GM11(data[i][np.arange(1999, 2014)].values)[0]
        data[i][2014] = f(len(data) - 1)  # 2014年预测结果
        data[i][2015] = f(len(data))  # 2015年预测结果
        data[i] = data[i].round()  # 取整

    data[l + ['y']].to_excel(outputfile)  # 结果输出
    print(data)


def yuce3():
    '''
    营业税神经网络预测模型
    :return:
    '''
    inputfile = 'data/data3_GM11.xls'  # 灰色预测后保存的路径
    outputfile = 'data/sales_tax.xls'  # 神经网络预测后保存的结果
    modelfile = 'data/3-net.model'  # 模型保存路径
    data = pd.read_excel(inputfile)  # 读取数据
    feature = ['x3', 'x4', 'x6', 'x8']  # 特征所在列

    data_train = data.loc[range(1999, 2014)].copy()  # 取2014年前的数据建模
    data_mean = data_train.mean()
    data_std = data_train.std()
    data_train = (data_train - data_mean) / data_std  # 数据标准化
    x_train = data_train[feature].values  # 特征数据
    y_train = data_train['y'].values  # 标签数据

    from keras.models import Sequential
    from keras.layers.core import Dense, Activation

    model = Sequential()  # 建立模型
    model.add(Dense(input_dim=4, units=8))
    model.add(Activation('relu'))  # 用relu函数作为激活函数，能够大幅提供准确度
    model.add(Dense(input_dim=8, units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')  # 编译模型
    model.fit(x_train, y_train, nb_epoch=10000, batch_size=16)  # 训练模型，学习一万次
    model.save_weights(modelfile)  # 保存模型参数

    # 预测，并还原结果。
    x = ((data[feature] - data_mean[feature]) / data_std[feature]).values
    data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']
    data[u'y_pred'] = data[u'y_pred'].round(2)
    data.to_excel(outputfile)

    import matplotlib.pyplot as plt  # 画出预测结果图
    p = data[['y', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])
    plt.show()


def adaptiveLasso4():
    '''
    Adaptive-Lasso变量选择
    :return:
    '''
    inputfile = 'data/data4.csv'  # 输入的数据文件
    data = pd.read_csv(inputfile)  # 读取数据

    # 导入AdaptiveLasso算法，要在较新的Scikit-Learn才有。
    from sklearn.linear_model import AdaptiveLasso
    model = AdaptiveLasso(gamma=1)
    model.fit(data.iloc[:, 0:10], data['y'])
    model.coef_  # 各个特征的系数


def huise4():
    '''
    企业所得税灰色预测
    :return:
    '''
    inputfile = 'data/data4.csv'  # 输入的数据文件
    outputfile = 'data/data4_GM11.xls'  # 灰色预测后保存的路径
    data = pd.read_csv(inputfile)  # 读取数据
    data.index = range(2002, 2014)

    data.loc[2014] = None
    data.loc[2015] = None
    l = ['x1', 'x2', 'x3', 'x4', 'x6', 'x7', 'x9', 'x10']
    for i in l:
        f = GM11(data[i][np.arange(2002, 2014)].values)[0]
        data[i][2014] = f(len(data) - 1)  # 2014年预测结果
        data[i][2015] = f(len(data))  # 2015年预测结果
        data[i] = data[i].round(2)  # 保留两位小数
    data[l + ['y']].to_excel(outputfile)  # 结果输出
    print(data)


def yuce4():
    '''
    企业所得税神经网络预测模型
    :return:
    '''
    inputfile = 'data/data4_GM11.xls'  # 灰色预测后保存的路径
    outputfile = 'data/enterprise_income.xls'  # 神经网络预测后保存的结果
    modelfile = 'data/4-net.model'  # 模型保存路径
    data = pd.read_excel(inputfile)  # 读取数据
    feature = ['x1', 'x2', 'x3', 'x4', 'x6', 'x7', 'x9', 'x10']  # 特征所在列

    data_train = data.loc[range(2002, 2014)].copy()  # 取2014年前的数据建模
    data_mean = data_train.mean()
    data_std = data_train.std()
    data_train = (data_train - data_mean) / data_std  # 数据标准化
    x_train = data_train[feature].values  # 特征数据
    y_train = data_train['y'].values  # 标签数据

    from keras.models import Sequential
    from keras.layers.core import Dense, Activation

    model = Sequential()  # 建立模型
    model.add(Dense(input_dim=8, units=6))
    model.add(Activation('relu'))  # 用relu函数作为激活函数，能够大幅提供准确度
    model.add(Dense(input_dim=6, units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')  # 编译模型
    model.fit(x_train, y_train, nb_epoch=5000, batch_size=16)  # 训练模型，学习五千次
    model.save_weights(modelfile)  # 保存模型参数

    # 预测，并还原结果。
    x = ((data[feature] - data_mean[feature]) / data_std[feature]).values
    data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']
    data[u'y_pred'] = data[u'y_pred'].round()
    data.to_excel(outputfile)

    import matplotlib.pyplot as plt  # 画出预测结果图
    p = data[['y', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])
    plt.show()


def adaptiveLasso5():
    '''
    Adaptive-Lasso变量选择
    :return:
    '''
    inputfile = 'data/data5.csv'  # 输入的数据文件
    data = pd.read_csv(inputfile)  # 读取数据

    # 导入AdaptiveLasso算法，要在较新的Scikit-Learn才有。
    from sklearn.linear_model import AdaptiveLasso
    model = AdaptiveLasso(gamma=1)
    model.fit(data.iloc[:, 0:7], data['y'])
    model.coef_  # 各个特征的系数


def huise5():
    '''
    个人所得税灰色预测
    :return:
    '''
    inputfile = 'data/data5.csv'  # 输入的数据文件
    outputfile = 'data/data5_GM11.xls'  # 灰色预测后保存的路径
    data = pd.read_csv(inputfile)  # 读取数据
    data.index = range(2000, 2014)

    data.loc[2014] = None
    data.loc[2015] = None
    l = ['x1', 'x4', 'x5', 'x7']
    for i in l:
        f = GM11(data[i][np.arange(2000, 2014)].values)[0]
        data[i][2014] = f(len(data) - 1)  # 2014年预测结果
        data[i][2015] = f(len(data))  # 2015年预测结果
        data[i] = data[i].round()  # 取整

    data[l + ['y']].to_excel(outputfile)  # 结果输出
    print(data)


def yuce5():
    '''
    个人所得税神经网络预测模型
    :return:
    '''
    inputfile = 'data/data5_GM11.xls'  # 灰色预测后保存的路径
    outputfile = 'data/personal_Income.xls'  # 神经网络预测后保存的结果
    modelfile = 'data/5-net.model'  # 模型保存路径
    data = pd.read_excel(inputfile)  # 读取数据
    feature = ['x1', 'x4', 'x5', 'x7']  # 特征所在列

    data_train = data.loc[range(2000, 2014)].copy()  # 取2014年前的数据建模
    data_mean = data_train.mean()
    data_std = data_train.std()
    data_train = (data_train - data_mean) / data_std  # 数据标准化
    x_train = data_train[feature].values  # 特征数据
    y_train = data_train['y'].values  # 标签数据

    from keras.models import Sequential
    from keras.layers.core import Dense, Activation

    model = Sequential()  # 建立模型
    model.add(Dense(input_dim=4, units=8))
    model.add(Activation('relu'))  # 用relu函数作为激活函数，能够大幅提供准确度
    model.add(Dense(input_dim=8, units=1))
    model.compile(loss='mean_squared_error', optimizer='adam')  # 编译模型
    model.fit(x_train, y_train, nb_epoch=15000, batch_size=16)  # 训练模型，学习一万五千次
    model.save_weights(modelfile)  # 保存模型参数

    # 预测，并还原结果。
    x = ((data[feature] - data_mean[feature]) / data_std[feature]).values
    data[u'y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']
    data[u'y_pred'] = data[u'y_pred'].round()
    data.to_excel(outputfile)

    import matplotlib.pyplot as plt  # 画出预测结果图
    p = data[['y', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])
    plt.show()


def huise6():
    '''
    政府性基金收入灰色预测
    :return:
    '''
    x0 = np.array([3152063, 2213050, 4050122, 5265142, 5556619, 4772843, 9463330])
    f, a, b, x00, C, P = GM11(x0)
    print(u'2014年、2015年的预测结果分别为：\n%0.2f万元和%0.2f万元' % (f(8), f(9)))
    print(u'后验差比值为：%0.4f' % C)
    p = pd.DataFrame(x0, columns=['y'], index=range(2007, 2014))
    p.loc[2014] = None
    p.loc[2015] = None
    p['y_pred'] = [f(i) for i in range(1, 10)]
    p['y_pred'] = p['y_pred'].round(2)
    p.index = pd.to_datetime(p.index, format='%Y')

    import matplotlib.pylab as plt
    p.plot(style=['b-o', 'r-*'], xticks=p.index)
    plt.show()


if __name__ == '__main__':
    # adaptiveLasso()
    # huise()
    # yuce()
    # adaptiveLasso2()
    # huise2()
    # yuce2()
    # adaptiveLasso3()
    # huise3()
    # yuce3()
    # adaptiveLasso4()
    # huise4()
    # yuce4()
    # adaptiveLasso5()
    # huise5()
    # yuce5()
    huise6()

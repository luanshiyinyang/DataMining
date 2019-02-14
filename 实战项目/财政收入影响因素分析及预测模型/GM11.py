# -*- coding: utf-8 -*-
import numpy as np


def GM11(x0):
  '''
  自定义灰色预测函数
  :param x0:
  :return:
  '''
  # 1-AGO序列
  x1 = x0.cumsum()
  # 紧邻均值（MEAN）生成序列
  z1 = (x1[:len(x1)-1] + x1[1:])/2.0
  z1 = z1.reshape((len(z1), 1))
  B = np.append(-z1, np.ones_like(z1), axis = 1)
  Yn = x0[1:].reshape((len(x0)-1, 1))
  # 计算参数
  [[a],[b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Yn)
  # 还原值
  f = lambda k: (x0[0]-b/a)*np.exp(-a*(k-1))-(x0[0]-b/a)*np.exp(-a*(k-2))
  delta = np.abs(x0 - np.array([f(i) for i in range(1,len(x0)+1)]))
  C = delta.std()/x0.std()
  P = 1.0*(np.abs(delta - delta.mean()) < 0.6745*x0.std()).sum()/len(x0)
  # 返回灰色预测函数、a、b、首项、方差比、小残差概率
  return f, a, b, x0[0], C, P
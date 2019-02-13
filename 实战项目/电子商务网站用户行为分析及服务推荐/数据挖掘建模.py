# -*- coding：utf-8-*-
import numpy as np


def Jaccard(a, b):
    '''
    自定义杰卡德相似系数函数，只对0-1矩阵有效
    :param a:
    :param b:
    :return:
    '''
    return 1.0 * (a * b).sum() / (a + b - a * b).sum()


class Recommender():
    # 相似度矩阵
    sim = None

    def similarity(self, x, distance):
        '''
        计算相似度矩阵的函数
        :param x:
        :param distance:
        :return:
        '''
        y = np.ones((len(x), len(x)))
        for i in range(len(x)):
            for j in range(len(x)):
                y[i, j] = distance(x[i], x[j])
        return y

    def fit(self, x, distance=Jaccard):
        '''
        训练函数
        :param x:
        :param distance:
        :return:
        '''
        self.sim = self.similarity(x, distance)

    def recommend(self, a):
        '''
        推荐函数
        :param a:
        :return:
        '''
        return np.dot(self.sim, a) * (1 - a)
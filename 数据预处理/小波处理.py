# -*- coding: utf-8 -*-
import pywt
from scipy.io import loadmat
# 利用小波分析进行特征分析
inputFile = './leleccum.mat'
# mat是MATLAB专用格式，需要用loadmat读取它
mat = loadmat(inputFile)
signal = mat['leleccum'][0]
coeffs = pywt.wavedec(signal, 'bior3.7', level=5)
# 返回结果为level+1个数字，第一个数组为逼近系数数组，后面的依次是细节系数数组

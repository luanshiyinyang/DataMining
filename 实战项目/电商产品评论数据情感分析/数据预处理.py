# -*- coding: utf-8 -*-
import pandas as pd
import jieba


def cleanSame():
    '''
    去重
    :return:
    '''
    inputfile = 'data/meidi_jd.txt'  # 评论文件
    outputfile = 'data/meidi_jd_process_1.txt'  # 评论处理后保存路径
    data = pd.read_csv(inputfile, encoding='utf-8', header=None)
    l1 = len(data)
    data = pd.DataFrame(data[0].unique())
    l2 = len(data)
    data.to_csv(outputfile, index=False, header=False, encoding='utf-8')
    print(u'删除了%s条评论。' % (l1 - l2))


def cleanPrefix():
    '''
    删除前缀评分
    :return:
    '''
    # 参数初始化
    inputfile1 = 'data/meidi_jd_process_end_负面情感结果.txt'
    inputfile2 = 'data/meidi_jd_process_end_正面情感结果.txt'
    outputfile1 = 'data/meidi_jd_neg.txt'
    outputfile2 = 'data/meidi_jd_pos.txt'

    data1 = pd.read_csv(inputfile1, encoding='utf-8', header=None, engine='python')  # 读入数据
    data2 = pd.read_csv(inputfile2, encoding='utf-8', header=None, engine='python')

    data1 = pd.DataFrame(data1[0].str.replace('.*?\d+?\\t ', ''))  # 用正则表达式修改数据
    data2 = pd.DataFrame(data2[0].str.replace('.*?\d+?\\t ', ''))

    data1.to_csv(outputfile1, index=False, header=False, encoding='utf-8')  # 保存结果
    data2.to_csv(outputfile2, index=False, header=False, encoding='utf-8')


def cut():
    '''
    分词
    :return:
    '''
    # 参数初始化
    inputfile1 = 'data/meidi_jd_neg.txt'
    inputfile2 = 'data/meidi_jd_pos.txt'
    outputfile1 = 'data/meidi_jd_neg_cut.txt'
    outputfile2 = 'data/meidi_jd_pos_cut.txt'

    data1 = pd.read_csv(inputfile1, encoding='utf-8', header=None)  # 读入数据
    data2 = pd.read_csv(inputfile2, encoding='utf-8', header=None)

    mycut = lambda s: ' '.join(jieba.cut(s))  # 自定义简单分词函数
    data1 = data1[0].apply(mycut)  # 通过“广播”形式分词，加快速度。
    data2 = data2[0].apply(mycut)

    data1.to_csv(outputfile1, index=False, header=False, encoding='utf-8')  # 保存结果
    data2.to_csv(outputfile2, index=False, header=False, encoding='utf-8')


if __name__ == '__main__':
    # cleanSame()
    # cleanPrefix()
    cut()
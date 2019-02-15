# -*- coding: utf-8 -*-
import pandas as pd


def LDA():
    '''
    LDA主题分析
    :return:
    '''
    # 参数初始化
    negfile = 'data/meidi_jd_neg_cut.txt'
    posfile = 'data/meidi_jd_pos_cut.txt'
    stoplist = 'data/stoplist.txt'

    neg = pd.read_csv(negfile, encoding='utf-8', header=None)  # 读入数据
    pos = pd.read_csv(posfile, encoding='utf-8', header=None)
    stop = pd.read_csv(stoplist, encoding='utf-8', header=None, sep='tipdm', engine='python')
    # sep设置分割词，由于csv默认以半角逗号为分割词，而该词恰好在停用词表中，因此会导致读取出错
    # 所以解决办法是手动设置一个不存在的分割词，如tipdm。
    stop = [' ', ''] + list(stop[0])  # Pandas自动过滤了空格符，这里手动添加

    neg[1] = neg[0].apply(lambda s: s.split(' '))  # 定义一个分割函数，然后用apply广播
    neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop])  # 逐词判断是否停用词，思路同上
    pos[1] = pos[0].apply(lambda s: s.split(' '))
    pos[2] = pos[1].apply(lambda x: [i for i in x if i not in stop])

    from gensim import corpora, models

    # 负面主题分析
    neg_dict = corpora.Dictionary(neg[2])  # 建立词典
    neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]]  # 建立语料库
    neg_lda = models.LdaModel(neg_corpus, num_topics=3, id2word=neg_dict)  # LDA模型训练
    for i in range(3):
        neg_lda.print_topic(i)  # 输出每个主题
        print(neg_lda.print_topic(i))

    # 正面主题分析
    pos_dict = corpora.Dictionary(pos[2])
    pos_corpus = [pos_dict.doc2bow(i) for i in pos[2]]
    pos_lda = models.LdaModel(pos_corpus, num_topics=3, id2word=pos_dict)
    for i in range(3):
        neg_lda.print_topic(i)  # 输出每个主题
        print(pos_lda.print_topic(i))


if __name__ == '__main__':
    LDA()
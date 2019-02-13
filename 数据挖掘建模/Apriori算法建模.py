# -*- coding: utf-8 -*-
# 使用Apriori算法挖掘菜品订单关联规则
from __future__ import print_function
import pandas as pd
from apriori import *

inputFile = './menu_orders.xls'
outputFile = './apriori_rules.xls'
data = pd.read_excel(inputFile, header=None)

print(u'\n转换原始数据至0-1矩阵...')
# 转换0-1矩阵的过渡函数
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])
# 用map方式执行
b = map(ct, data.values)
# 实现矩阵转换，空值用0填充
data = pd.DataFrame(list(b)).fillna(0)
print(u'\n转换完毕。')
# 删除中间变量b，节省内存
del b
# 最小支持度
support = 0.2
# 最小置信度
confidence = 0.5
# 连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符
ms = '---'
# 保存结果
find_rule(data, support, confidence, ms).to_excel(outputFile)
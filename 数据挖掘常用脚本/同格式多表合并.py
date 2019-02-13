import pandas as pd
inputFile1 = r'MOCK_DATA (0).csv'
# 这里读取要保留第一个表头
data = pd.read_csv(inputFile1, header=None)[:]
print(data)
inputFile = r'MOCK_DATA (zcnb).csv'
for i in range(1, 30):
    zc = inputFile.replace('zcnb', str(i))
    # 这里读取不记录表头，否则拼接会多表头重复
    data2 = pd.read_csv(zc, header=None)[1:]
    # 不能用“+”号，表示矩阵加运算
    data = pd.concat([data, data2], axis=0)
data.to_csv("rst.csv", index=None)
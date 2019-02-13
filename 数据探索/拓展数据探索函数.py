import pandas as pd
import matplotlib.pyplot as plt
data = pd.Series(range(2, 9))
# 累计计算
print("累计计算")
print(data.cumsum())
print(data.cumprod())
print(data.cummax())
print(data.cummin())
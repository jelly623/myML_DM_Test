# __*__ coding: utf-8 __*__

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key':['b','b','a','c','a','a','b'],
                    "data1":range(7)})
df2 = pd.DataFrame({"key":["a",'b','d'],
                    "data2":range(3)})

print df1
print df2
# 如果没有指定按照那一列进行数据合并，则默认采取相同的列名字进行合并
print pd.merge(df1,df2)
print pd.merge(df1,df2, left_on="data1", right_on='data2')

df3 = pd.DataFrame({'lkey':['b','b','a','c','a','a','b'],
                    "data1":range(7)})
df4 = pd.DataFrame({"rkey":["a",'b','d'],
                    "data2":range(3)})

#索引的使用
left1 = pd.DataFrame({'key':['a','b','a','a','b','c'],
                    "value":range(6)})
right1 = pd.DataFrame({"group_val":[3.5,7],
                    "index":['a', 'b']})
print left1
print right1
# pd.merge(left1, right1, left_on='key',right_index=True)

# 清除掉重复的数据
data = pd.DataFrame({'k1':['one'] * 3 + ['two'] * 4,
                     'k2':[1,1,2,3,3,4,4]})
# map的用法
my_data = pd.DataFrame({"name":["daijitao","fengshuting"],
                        "age":["22","22"]})
flag = {"daijitao":"nan","fengshuting":"nv"}
my_data["gender"] = my_data["name"].map(str.lower).map(flag)
print my_data

#正态分布数据
np.random.seed(12345)
data = pd.DataFrame(np.random.randn(1000,4)) # 代表1000行 4列数据
print data
val = "aditjjitaojijij"
print val.count("ji0") # 子串的出现次数
print val.index("j")
print val.find("j")
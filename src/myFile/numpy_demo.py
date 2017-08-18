# __*__ coding: utf-8 __*__

import numpy as np
import pandas as pd

data1 = [1,2,3,4,5,6]
arr1 = np.array(data1)
print arr1.ndim
print arr1.shape
print np.arange(15)
# 数组和标量之间的运算
arr = np.array([[1,2,3,4],[5,6,7,8]])
print arr * arr

arr = np.arange(10)
print np.sqrt(arr)
print np.exp(arr)

# points = np.arange(-5,5,0.01)
# np.save("D:/test",points) # 数据的保存
my_data = np.load("D:/test.npy") # numpy 数据的下载
print "====================="
points = np.arange(4)
print "==============="
print points
print points.cumsum(0) # 0是按行累计 1是按列累加

# 创建数组
data = np.arange(1,2,0.1)
# linspace函数通过指定开始值、终值和元素个数来创建一维数组，可以通过endpoint关键字指定
# 是否包括终值，缺省设置是包括终值:
# data = np.arange(0,1,linspace = 12)
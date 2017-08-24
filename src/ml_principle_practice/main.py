# __*__ coding:utf-8 __*__
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math

# 测试数据集-二维list
dataSet = [[-0.017612,14.053064],[-1.395634 ,4.662541],[-0.752157 ,6.538620],
           [-1.322371 ,7.152853],[0.423363 ,11.054677],[0.406704 ,7.067335],
           [0.667394 ,12.741452], [-2.460150 ,6.866805],[0.569411 ,9.548755],
           [-0.026632 ,10.427743],[0.850433 ,6.920334],[1.347183 ,13.175500],
           [1.176813 ,3.167020],[-1.781871 ,9.097953]]
# 把 dataSet 转为 numpy矩阵
dataMatTemp = mat(dataSet)
print type(dataMatTemp)
dataMat = dataMatTemp.T #进行转置
print dataMat[0]
print dataMat[1]
print "======================"

plt.scatter(dataMat[0], dataMat[1],c="red", marker='o')
# plt.show()
# X = np.linspace(-2,2,100)
# print X
#
# Y = 2.8 * X + 9
# plt.plot(X ,Y)
# plt.show()

my_list = [i for i in range(10)]
print my_list
# 转换为矩阵
listMat = np.mat(my_list)
print 10 * listMat

# 3行 5列
myZeros = np.zeros((3,5))
print myZeros
myOnes = np.ones((3,5))
print myOnes
print np.random.rand(3,5) # 随机数
mymatrix2 = 1.5* np.ones([3,3])
mymatrix = np.mat( [[1,2,3],[4,5,6],[7,8,9]])
print "==========================="
print multiply(mymatrix2, mymatrix) # 矩阵相乘
print "内积："
print np.dot(mymatrix2, mymatrix) # 矩阵的内积
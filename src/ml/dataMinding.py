# _*_ coding:utf-8 _*_

# page 22 python数据挖掘入门与实践
# http://archive.ics.uci.edu/ml/datasets/Ionosphere
# print os.path.expanduser("~") 用户主目录
import numpy as np
import csv

data_filename = "C:\\Users\\daijitao\\data\\ionosphere.data"
X = np.zeros((351,34),dtype='float')
y = np.zeros((351,), dtype='bool') #1行

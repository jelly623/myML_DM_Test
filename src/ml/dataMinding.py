# _*_ coding:utf-8 _*_

# page 22 python数据挖掘入门与实践
# http://archive.ics.uci.edu/ml/datasets/Ionosphere
# print os.path.expanduser("~") 用户主目录
import numpy as np
import csv

data_filename = "C:\\Users\\daijitao\\data\\ionosphere.data"
X = np.zeros((351,34),dtype='float')
y = np.zeros((351,), dtype='bool') #1行

with open(data_filename, "r") as input_file:
    """ 读取文件 """
    reader = csv.reader(input_file)
    # for j in enumerate(reader):
    #     """ 本质上是一个个的元祖 """
    #     print j
    for i, row in enumerate(reader):
        print "row: ", row
        data = [float(datum) for datum in row[:-1]]
        X[i] = data
        # 读取类别值，‘g' is good, float:1.0
        y[i] = row[-1] == 'g'

from sklearn.cross_validation import train_test_split
# 训练集 测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=14)
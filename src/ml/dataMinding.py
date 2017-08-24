# _*_ coding:utf-8 _*_

# page 22 python数据挖掘入门与实践
# http://archive.ics.uci.edu/ml/datasets/Ionosphere
# print os.path.expanduser("~") 用户主目录
import numpy as np
import csv

data_filename = "C:\\Users\\daijitao\\data\\ionosphere.data"
X = np.zeros((351, 34), dtype='float')
y = np.zeros((351,), dtype='bool')  # 1行

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

'''
K 近邻算法的应用
'''
from sklearn.cross_validation import train_test_split

# 训练集 测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=14)
from sklearn.neighbors import KNeighborsClassifier

# 获取估计器, 默认K = 5
estimator = KNeighborsClassifier()
# 用估计器进行训练
estimator.fit(X_train, y_train)
y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100
print "The accuracy is {0:.1f}%".format(accuracy)  # 打印准确率

# 进行K折交叉验证
from sklearn.cross_validation import cross_val_score

scores = cross_val_score(estimator, X, y, scoring='accuracy')
average_accuracy = np.mean(scores) * 100
print("The average accuracy is {0:.1f}%".format(average_accuracy))

avg_scores = []
all_scores = []
parameter_values = list(range(1, 21))  # Include 20
for n_neighbors in parameter_values:
    """ 参数调优吧"""
    estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
    scores = cross_val_score(estimator, X, y, scoring='accuracy')
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)

# 绘图
from matplotlib import pyplot as plt
# plt.plot(parameter_values, avg_scores, '-o')
# plt.show()
# print "end"

"""数据的规范化"""
print "数据的规范化"
X_broken = np.array(X)
X_broken[:,::2] /= 10 # [行，列]



estimator = KNeighborsClassifier()
original_scores = cross_val_score(estimator, X, y, scoring='accuracy')
print "=========================="
print np.mean(original_scores)
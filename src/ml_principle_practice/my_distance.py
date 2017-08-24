# __*__ coding:utf-8 __*__

import numpy as np

data = np.mat([i for i in range(0,10)])
data2 = np.mat([i for i in range(10, 20)])
print data #row
print data2 # lie


def ou_distance(a, b):
    '''  计算欧氏距离 '''
    return np.sqrt( (a-b) * ((a-b).T))

def manhatun_distance():
    """曼哈顿距离 """
    pass

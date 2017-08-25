# __*__ coding:utf-8 __*__

import numpy as np
from numpy import *


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

featuremat = mat([[88.5,96.8,104.1,111.3,117.7,124.0,130.0,135.4,140.2,145.3,151.9,159.5,165.9,169.8,171.6,
                   172.3,172.7],[12.54,14.65,16.64,18.98,21.26,24.06,27.33,30.46,33.74,37.69,42.49,48.08,53.37,
                                 57.08,59.35,60.68,61.40]])
print featuremat

import sys
import os
import jieba

# 设置utf-8环境
reload(sys)
sys.setdefaultencoding('utf-8')

seg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=False) #默认的结巴分词
print "DefalutMode: ", " ".join(seg_list)

seg_list = jieba.cut("小明1995年毕业于北京清华大学", cut_all=True) # 全切分
print "All Mode: ", "/".join(seg_list)

#搜索引擎模式
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print "search mode: ","/ ".join(seg_list)

def save_file(save_path, content):
    """ 保存文件 """
    fp = open(save_path, "wb")
    fp .write(content)

def read_file(path):
    """读取文件"""
    fp = open(path, "rb")
    content = fp.read()
    fp.close()
    return content
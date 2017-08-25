# _*_ coding:utf-8 _*_

from numpy import *
#导入图像处理库
from PIL import Image, ImageDraw, ImageFont
from skimage import transform as tf
from matplotlib import pyplot as plt
import numpy as np


def luojisidi(x, L=1, k=1):
    """逻辑斯蒂函数"""
    temp = k * x
    return L / (1 + exp(-temp))

x = [i for i in range(1,10)]
y = [luojisidi(i) for i in x]

# plt.plot(x, y)
# plt.show()

def create_captcha(text, shear=0, size=(100, 24)):
    im = Image.new("L", size, "black")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(r"E:\data\Coval-Black.otf", 22)
    draw.text((2, 2), text, fill=1, font=font)
    image = np.array(im)
    affine_tf = tf.AffineTransform(shear=shear)
    image = tf.warp(image, affine_tf)
    return image / image.max()



image = create_captcha("GENE", shear=0.5)
plt.imshow(image, cmap='Greys')
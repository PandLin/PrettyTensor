#coding:utf-8
import matplotlib.pyplot as plt
import tensorflow as tf
import  numpy as np
from  sklearn.metrics import confusion_matrix #混淆矩阵
import time
from datetime import  timedelta
import math
import prettytensor as pt

#载入数据MNIST
from tensorflow.examples.tutorials.mnist import input_data
data = input_data.read_data_sets('./MNIST/',one_hot=True)

print("Size of")
print("- Training-set:\t\t{}".format(len(data.train.labels)))
print("- Test-set:\t\t{}".format(len(data.test.labels)))
print("- Validation-set:\t{}".format(len(data.validation.labels)))

#我们也需要测试数据集类别数字的整型值，用下面的方法来计算。
#data.test.cls = np.argmax(data.test.labels, axis=0)

#数据维度，常量定义

# We know that MNIST images are 28 pixels in each dimension.
img_size = 28
# Images are stored in one-dimensional arrays of this length.
img_size_flat = img_size * img_size
# Tuple with height and width of images used to reshape arrays.
img_shape = (img_size, img_size)
# Number of colour channels for the images: 1 channel for gray-scale.
num_channels = 1
# Number of classes, one class for each of 10 digits.
num_classes = 10

#绘制图片的帮助函数
#这个函数用来在3x3的栅格中画9张图像，然后在每张图像下面写出真实类别和预测类别。
def plot_images(images,cls_true,cls_pred=None):
    assert  len(images) == len(cls_true) == 9

    #create figure with 3*3 sub-plots.
    fig,axes = plt.subplots(3,3)
    fig.subplots_adjust()




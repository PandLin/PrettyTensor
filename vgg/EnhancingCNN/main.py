#coding:utf-8

import cifar10,cifar10_input
import tensorflow as tf
import numpy as np
import time


max_steps = 3000
batch_size = 128
data_dir =  '/tmp/cifar10_data/cifar-10-batches-bin'

def variable_with_wight_loss(shape,stddev,wl):
    var = tf.Variable(yf.truncated_normal(shape,stddev=stddev))
    #'wl' is used to control the size of L2 loss
    if wl is not None:
        weight_loss = tf.multiply(tf.nn.l2_loss(var),wl,name='weight_loss')
        tf.add_to_collection('losses',weight_loss)
    return var

image
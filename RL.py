import tensorflow as tf
import cv2
import pong
import numpy as np
import random
from collections import deque


#Defining hyperparameters
ACTIONS = 3
#Defining the LEARNING RATE
GAMMA = 0.99
#Update the gradient or training time
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05
#How many frames to anneal epsilon
EXPLORE = 500000
OBSERVE = 50000
REPLAY_MEMORY = 50000
#Batch size
batch = 100

#Create TF graph
def createGraph():

    #First convolutional layer and BIAS vector
    #creates an empty tensor with all elements set to zero with a shape
    W_conv1 = tf.Variable(tf.zeros([8, 8, 4, 32]))  
    b_conv1 = tf.Variable(tf.zeros([32]))

    #Second convolutional layer
    W_conv2 = tf.Variable([4, 4 32, 64]) 
    b_conv2 = tf.Variable([64])

    #Third convolutional layer
    W_conv3 = tf.Variable(tf.zeros([3, 3, 64, 64]))
    b_conv3 = tf.Variable(tf.zeros([64]))

    #Fouth convolutional layer
    W_fc4 = tf.Variable(tf.zeros([784, ACTIONS]))
    b_fc4 = tf.Variable(tf.zeros([784]))

    #Last layer
    W_fc5 = td.Variable(tf.zeros([784, ACTIONS]))
    b_fc5 = tf.Variable(tf.zeros([ACTIONS]))


    #Input for pixel data
    s = tf.placeholder("float", [None, 84, 84, 4])

    #Computes rectified linear unit activation function on a 2-D convolution given 4-D input and filter tensors
    conv1 = tf.nn.relu(tf.nn.conv2d(s, W_conv1, strides = [1, 4, 4, 1], padding = "VALID") + b_conv1)

    conv2 = tf.nn.relu(tf.nn.conv2d(conv1, W_conv2, strides = [1, 2, 2, 1], padding = "VALID") + b_conv2)

    conv3 = tf.nn.relu(tf.nn.conv2d(conv2, W_conv3, strides = [1, 1, 1, 1], padding = "VALID") + b_conv3)

    conv3_flat = tf.reshape(conv3, [-1, 3136])

    fc4 = tf.nn.relu(tf.matmul(conv3_flat, W_fc4) + b_fc4)
    
    fc5 = tf.matmul(fc4, W_fc5) + b_fc5

    return s, fc5

def main():

    #Create session
    sess = tf.InteractiveSession()
    #Input layer and output layer
    inp, out = createGraph()
    tainGraph(inp, out, sess)

if __name__ = "__main__":
    main()
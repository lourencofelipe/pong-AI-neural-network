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
    b_fc5 = tf.Variable(tf.zeros([784]))

    #Last layer
    W_fc5 = td.Variable(tf.zeros([784, ACTIONS]))
    b_fc5 = tf.Variable(tf.zeros([ACTIONS]))
    


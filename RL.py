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



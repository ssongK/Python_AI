import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import models,layers
print(tf.__version__)

import cv2

def test1():
  img = cv2.imread("Day2/1.jpg") # 3차원 데이터
  print(type(img),img.shape)
  cv2.imshow("my",img)
  cv2.waitKey(0) # 무한 대기
  cv2.destroyAllWindows()
  
test1()
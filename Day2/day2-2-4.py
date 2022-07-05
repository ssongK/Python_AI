import numpy as np
import cv2
from tensorflow.keras import datasets

def test1():
    (x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
    # print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

    img = x_train[0]
    # print(img.shape,img)
    cv2.imwrite("1.png",img)

    img1 = x_train[1]
    # print(img.shape,img)

    cv2.imwrite("2.png",img1)
    print(y_train[:20])
    
test1()

def test2():
    (x_train, y_train), (x_test, y_test) = datasets.fashion_mnist.load_data()
    print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

    img = x_train[0]
    cv2.imwrite("1.png",img)
    print(y_train[0])

    img1 = x_train[1]
    cv2.imwrite("2.png",img1)
    print(y_train[1])

test2()

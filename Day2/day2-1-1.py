import random
import numpy as np
import matplotlib.pyplot as plt

def test1():
    x = [[0,0], # 센싱 데이터
         [0,1],
         [1,0],
         [1,1]]
    y = [0,0,0,1] # 라벨
    w = [random.random(),random.random(),random.random()] # 가중치
    print(w)
    for j in range(50):
        print(j,'------------------------')
        for i in range(len(x)):
            # print(x[i])
            net = x[i][0]*w[0] + x[i][1]*w[1] + 1*w[2] 
            if net>0:
                y_pre = 1
            else:
                y_pre = 0
            print(x[i],net,y_pre)
            
            # w = w + 0.01*(y-y_pre)*x
            w[0] = w[0] + 0.01*(y[i]-y_pre) * x[i][0]
            w[1] = w[1] + 0.01*(y[i]-y_pre) * x[i][1]
            w[2] = w[2] + 0.01*(y[i]-y_pre) * 1
test1()
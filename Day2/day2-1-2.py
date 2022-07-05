import random

def test1():
    x = [[0,0],
         [0,1],
         [1,0],
         [1,1]]
    y = [0,1,1,1]
    # 파라미터(컴퓨터가 지정) / 하이퍼파라미터(사람이 지정)
    w = [random.random(),random.random(),random.random()]
    for epoch in range(100):
        print(epoch,'--------------------')
        for i in range(len(x)):
            net = x[i][0]*w[0] + x[i][1]*w[1] + 1*w[2]
            
            if net>0:
                act = 1
            else: 
                act = 0
            
            loss = y[i] - act
            
            w[0] = w[0] + 0.01*loss*x[i][0]
            w[1] = w[1] + 0.01*loss*x[i][1]
            w[2] = w[2] + 0.01*loss*1
            
            print(x[i],act,y[i])
test1()
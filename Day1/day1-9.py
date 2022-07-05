"""
30명의 회원
3개 항목(국,영,수)에 대한 시험 점수
개인별 총점 및 평균
"""

import numpy as np

def average():
    data = np.random.randint(1,101,(30,3))
    print(data,data.shape)
    
    sum = data[:,0]+data[:,1]+data[:,2]
    sum = sum.reshape(30,-1)
    avg = sum/3
    avg = avg.reshape(30,-1)
    
    print(sum,sum.shape)
    print(avg,avg.shape)
    
    data = np.concatenate([data,sum,avg],axis=1)
    print(data)
    
average()

def test1():
    data = np.random.randint(1,10,(5,2))
    print(data,data.shape)
    print('-----------------------')
    
    data1 = np.random.randint(50,60,(5,3))
    print(data1,data1.shape)
    print('-----------------------')

    data3 = np.concatenate([data,data1],axis=1)
    print(data3,data3.shape)
    
# test1()


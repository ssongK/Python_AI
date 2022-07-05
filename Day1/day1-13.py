"""
성적 처리 프로그램
인원 : 200

평균
총점
과목분석
총점분석
"""

import numpy as np
import matplotlib.pyplot as plt

def test1():
    data = np.random.randint(0, 101, (200, 7))
    d1 = data[:, 0] + data [:, 1] + data [:, 1]
    d2 = d1 // 3
    dd1 = d1.reshape(-1, 1)
    dd2 = d2.reshape(-1, 1)
    result = np.concatenate([data, dd1, dd2], axis=1)
    print(result)
    
    y1 = plt.axes()
    y1.plot(data[:, 0], 'r', label='kor')
    y1.plot(data[:, 1], 'b', label='eng')
    y1.plot(data[:, 2], 'g', label='mat')
    y1.legend()
    y2 = y1.twinx()
    y2.plot(dd1[:, 0], 'g', label="1 score")
    y2.plot(dd2[:, 0], 'r', label="2 score")
    y2.legend()
    plt.grid()
    plt.title('Subject Analysis')
    plt.show()
    
    plt.plot(data[:, 0], 'ro')
    plt.title('kor score')
    plt.grid()
    plt.show()
    
    plt.plot(data[:, 1], 'go')
    plt.title('Eng score')
    plt.grid()
    plt.show()
    
    plt.plot(data[:, 2], 'bo')
    plt.title('Mat score')
    plt.grid()
    plt.show()
    
    plt.plot(dd1[:, 0], 'yo')
    plt.title('sum score')
    plt.grid()
    plt.show()
    
    plt.plot(dd2[:, 0], 'ro')
    plt.title('average score')
    plt.grid()
    plt.show()
    
    plt.boxplot([data[:, 0], data[:, 1], data[:, 2]], labels=['kor', 'eng', 'mat'])
    plt.title('Average of three subjects')
    plt.show()
    

test1()
import numpy as np
import matplotlib.pyplot as plt

def test1():
    data1 = np.random.randint(0,10,(20,))
    print(data1,data1.shape) 
    print('-------------------------------')
    
    data2 = np.random.rand(20,)
    print(data2,data2.shape)
    
    plt.plot(data1)
    plt.plot(data2)
    plt.show()
    
    y1 = plt.axes()
    y1.plot(data1,'r')
    y2 = y1.twinx()
    y2.plot(data2,'b')
    plt.show()
    
# test1()

def test2():
    data1 = np.random.randint(0,101,(30,3))
    print(data1,data1.shape)
    print('-------------------------------')
    
    data2 = np.random.rand(30,2)
    print(data2,data2.shape)
    print('-------------------------------')
    
    a = plt.axes()
    a.plot(data1[:,0],'r',label="kor")
    a.legend()
    
    b = a.twinx()
    b.plot(data2[:,0],'b',label="data B")
    b.legend()
    
    plt.grid()
    plt.show()
    
# test2()

def test3():
    data1 = np.random.randint(0,10,(10,))
    print(data1,data1.shape)
    print('-------------------------------')
    
    data2 = np.random.randn(10,)
    print(data2,data2.shape)
    
    _,y1 = plt.subplots() # _는 사용하지 않음 anonymous value
    y1.plot(data1,'r',label="data1")
    y2 = y1.twinx()
    y2.plot(data2,'g',label="data2")
    
    y1.legend(loc="upper left")
    y2.legend(loc="upper right")
    plt.show()
    
# test3()

def test4():
    data1 = np.random.randint(0,101,(30,))
    print(data1,data1.shape)
    print('-------------------------------')

    data2 = np.random.randint(0,101,(30,))
    print(data2,data2.shape)
    print('-------------------------------')
    
    plt.plot(data1,'r',label="A class")
    plt.plot(data2,'b',label="B class")
    
    plt.grid()
    plt.legend()
    plt.show()
    
    plt.boxplot([data1,data2],labels=["A class","B class"])
    plt.show()
    
test4()


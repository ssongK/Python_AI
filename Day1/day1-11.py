import numpy as np
import matplotlib.pyplot as plt

def test1():
    data = np.random.randint(0,101,(100,5))
    print(data,data.shape)
    
    x_data = data[:,0]
    y_data = data[:,-1]
    
    plt.plot(x_data,y_data,'r>',label='A score') # 색깔 뒤에 o,x,> 등의 마커 사용 가능
    plt.grid()
    plt.legend()
    plt.show()
    
# test1()

def test2():
    data = np.random.rand(50,3)
    print(data,data.shape)
    
    data1 = data[:,0]
    plt.plot(data1,'g',label="score")
    plt.title("Score")
    plt.grid()
    plt.legend()
    plt.show()
    
    plt.plot(data[:,0],data[:,1],'rx',label="f0,f1")
    plt.plot(data[:,0],data[:,2],'bo',label="f0,f2")
    plt.grid()
    plt.legend()
    plt.show()
    
# test2()

def test3():
    data = np.random.randint(0,101,(100,3))
    plt.plot(data[:,0],'y',label="kor")
    plt.plot(data[:,1],'b',label="eng")
    plt.plot(data[:,2],'g',label="math")
    plt.grid()
    plt.legend()
    plt.show()
    
    plt.plot(data[:,0],data[:,1],'y')
    plt.show()
    
test3()
import numpy as np
import matplotlib.pyplot as plt

def test1():
    data = np.random.randint(0,10,(2,3,4))
    print(data, data.shape)
    print('----------------------------')
    
    data1 = data[0]
    print(data1,data1.shape)
    
# test1()

def test2():
    data = np.random.randint(0,10,(10,))
    print(data, data.shape)
    
    plt.plot(data,"g")
    plt.show()
    
# test2()

def test3():
    data = np.random.randint(0,100,(20,))    
    data1 = np.random.randint(0,100,(30,))
    plt.plot(data,"g",label="A반 성적")
    plt.plot(data1,"b",label="B반 성적")
    plt.legend()
    plt.show()
    
# test3()

def test4():
    data1 = np.random.randint(0,101,(50,))
    data2 = np.random.randint(0,101,(50,))
    data3 = np.random.randint(0,101,(50,))
    
    plt.plot(data1,"b")
    plt.show()
    plt.plot(data2,"g")
    plt.show()
    plt.plot(data3,"y")
    plt.show()
    
    plt.plot(data1,"b",label="A score")
    plt.plot(data2,"g",label="B scroe")
    plt.plot(data3,"y",label="C scroe")
    plt.legend()
    plt.show()
    
test4()
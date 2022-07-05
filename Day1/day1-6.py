import numpy as np
def test1():
    data = np.random.randint(0,10,(2,5))
    print(data,data.shape)
    print('----------------------------------')
    
    data1 = data.T
    print(data1,data1.shape)
    print('----------------------------------')
    
# test1()
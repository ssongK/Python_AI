import numpy as np

def test1():
    # input : 3, hidden : 6, output : 1 
    x = np.array([[0,0,1], #(4,3)
                  [0,1,1],
                  [1,0,1],
                  [1,1,1]])
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])#(4,1)
    print(x,x.shape)
    print('--------------')
    print(y,y.shape)
    
    weight0 = np.random.random((3,6)) #(3,6)
    print(weight0.shape)
    weight1 = np.random.random((6,1)) #(6,1)
    print(weight1.shape)
    print('--------------')
    
    for i in range(100):
        # 정방향 계산
        net1 = x @ weight0 #(4,3) @ (3,6) = (4,6)
        print(net1, net1.shape)
        print('--------------')
        act1 = 1 / (1+np.exp(-net1)) #(4,6)
        print(act1.shape)
        
        act1[:,-1] = 1.0 # bias 조정
        
        net2 = act1 @ weight1 # (4,6) @ (6,1) = (4,1)
        print(net2,net2.shape)
        print('--------------')
        act2 = 1 / (1+np.exp(-net2)) #(4,1)
        print(act2,act2.shape)
        print('==============')
        
        act2_error = act2 - y #(4,1) - (4,1) = (4,1)
        t = act2*(1-act2) #(4,1) * (4,1) = (4,1)
        act2_delta = act2_error*t
        print(act2_delta,act2_delta.shape)
        print('--------------')
        
        weight1 = weight1 - 0.2*(act1.T@act2_delta) #(6,4) @ (4,1) = (6,1)
        
        act1_error = act2_delta @ weight1.T #(4,1) @ (1,6) = (4,6)
        t = act1*(1-act1)
        act1_delta = act1_error*t #(4,6) * (4,6) = (4,6)
        
        weight0 = weight0 - 0.2*(x.T@act1_delta) #(3,4) @ (4,6) = (3,6)
        
        print(x)
        print(y)
        print(act2)
        
test1()
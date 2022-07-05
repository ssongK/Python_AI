import random
def test1():
    data = [1,3,5,7]
    
    for i in range(4):
        a = data[i]
        print(a)
    print()
    
    for i in range(len(data)):
        a = data[i]
        print(a)
    print()
    
    for v in data:
        print(v)
    print()
    
    for i,v in enumerate(data):
        print(i,v)
    print()

test1()
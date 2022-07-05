# 10부터 20사이의 숫자 중에 7개를 선택해 출력한다.
# 단, 중복은 없어야 한다.
import random
import re

def test1():
    list = []
    while(len(list)<8):
        j = random.randint(10,20)
        if j not in list:
            list.append(j)
    print(list)

# test1()


def test2():
    a = [1,3,5]
    b = [2,3,7]
    
    strike = 0
    ball = 0    
    
    for i in range(len(a)):
        if a[i]==b[i]:
            strike += 1
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[i] and i != j:
                ball += 1
    print(a,b)
    print("strike : ",strike)
    print("ball : ",ball)
            
# test2()
def getinput():
    userdata = []
    while len(userdata) < 3:
        a = input(len(userdata)+1,"숫자 입력>>")
        if a not in userdata:
            userdata.append(a)
    return userdata

def getdata():
    data = []
    while len(data)<3 :
        a = random.randint(0,9)
        if a not in data:
            data.append(a)
    return data

def getsb(data1,data2):
    s = 0
    b = 0
    for i in range(len(data1)):
        if data1[i] == data2[i]:
            s += 1
        elif data1[i] in data2:
            b += 1
    return s,b

def test3():
    data1 = getinput()
    data2 = getdata()
    s,b = getsb(data1,data2)
    print(data1)
    print(data2)
    print("strike : ",s)
    print("ball : ",b)
    
test3()
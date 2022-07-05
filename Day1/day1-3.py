import random

def getcom():
# 0~9사이 중복없이 3개 선택
    data = []
    while len(data)<3:
        a = random.randint(0,9)
        if a not in data:
            data.append(a)
    
    return data

def getplayer():
# 0~9사이 중복없이 3개 입력
    data = []
    while len(data)<3:
        a = (int)(input("0~9 >> "))
        if a not in data:
            data.append(a)
        else:
            print("중복된 입력 값!")
        
    return data

def getsb(com,player):
# s,b 계산해서 리턴
    s = 0
    b = 0
    for i in range(len(com)):
        if com[i] == player[i]:
            s += 1
        elif com[i] in player:
            b += 1
            
    return s,b


def game():
    com = getcom()
    
    for i in range(5):
        player = getplayer()
        s,b = getsb(com,player)
        print("strike : ",s,", ball :",b)
        if s == 3 :
            print("You win!")
            print(com)
            return
    print("You lost")
    print(com)

game()
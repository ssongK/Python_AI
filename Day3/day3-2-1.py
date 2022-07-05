# pip install djitellopy
# import djitellopy
from djitellopy import Tello

def test1():
    drone = Tello()
    drone.connect()
    
    power = drone.get_battery()
    print("power : ",power)
    
    if power<30 :
        print("에너지가 부족합니다")
        return
    
    drone.end()
    
# test1()

def test2():
    drone = Tello()
    drone.connect()
    power = drone.get_battery()
    if power<30:
        print("낮은 에너지입니다.")
        return
    
    while True:
        power = drone.get_battery()
        if power<30:
            print("저젼력입니다")
            break
        
        print("power : ",power)
        cmd = input("명령어를 넣어주세요?")
        
        if cmd == "end":
            print("프로그램을 종료하겠습니다.")
            break
        elif cmd == "takeoff":
            drone.takeoff()
        elif cmd == "land":
            drone.land()
        elif cmd == "forward":
            drone.move_forward(30)
        elif cmd == "left":
            drone.move_left(20)
        elif cmd == "lclock":
            drone.rotate_clockwise(90)
        elif cmd == "rclock":
            drone.rotate_counter_clockwise(90)
        elif cmd == "back":
            drone.move_back(30)
        else:
            print("unknown command")
    
    drone.end()
    
test2()
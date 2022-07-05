import time
from threading import Thread
from djitellopy import Tello

def myWork(name,count):
    print("start my work",name)
    for i in range(count):
        print(name,i)
        time.sleep(1)
    print("end my work",name)

def main():
    print("start main")
    
    # myWork("aaa",10)
    my = Thread(target=myWork,args=["aaa",10])
    my.start()
    myWork("bbb",5)
    my.join()
    
    print("end main")

# main()

def myTakeoff(drone):
    drone.takeoff()

def test1():
    drone = Tello()
    drone.connect()
    
    # drone.takeoff()
    my = Thread(target=myTakeoff,args=[drone])
    my.start()
    
    for i in range(20):
        print("main",i)
        time.sleep(1)
    
    my.join()    
    
    print("착륙합니다")
    drone.land()
    
    drone.end()
    
test1()
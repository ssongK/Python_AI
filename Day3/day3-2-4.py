import time
import cv2
from djitellopy import Tello

def test1():
    drone = Tello()
    drone.connect()
    
    power = drone.get_battery()
    print("power : ",power)
    
    drone.streamon()
    time.sleep(3)
    
    while True:
        cmd = input("명령어를 넣어주세요")
        if cmd == "show":
            img = drone.get_frame_read().frame
            print(type(img),img.shape)
            
            cv2.imwrite("t1.png",img)
            
            img = cv2.resize(img,(32,32))
            cv2.imshow("test",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        elif cmd == "bye":
            break
        else:
            print("unknown command")
    
    drone.streamoff()
    drone.end()
    
test1()
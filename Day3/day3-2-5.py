import time
import cv2 
from djitellopy import Tello
from threading import Thread

def test1():
    drone = Tello()
    drone.connect()
    
    power = drone.get_battery
    print("power : ",power)
    
    drone.streamon()
    time.sleep(3)
    
    while True:
        img = drone.get_frame_read().frame
        img = cv2.resize(img,(120,120))
        cv2.imshow("120*120",img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    
    cv2.destroyAllWindows()
    
    drone.streamoff()
    drone.end()
test1()

def myCamera():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
    # for i in range(2):
        a,img = cap.read()
        if not a:
            print("error")
            break
        print(img.shape)
        # img = cv2.flip(img,0)
        img = cv2.resize(img,(120,120))
        cv2.imwrite("t1.png",img)
        cv2.imshow("test",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
# myCamera()
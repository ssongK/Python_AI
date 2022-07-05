from djitellopy import Tello
import time

def test1():
    
    drone = Tello()
    drone.connect()
    
    drone.enable_mission_pads()
    drone.set_mission_pad_detection_direction(1)
    
    power = drone.get_battery()
    print("power : ",power)
    
    for i in range(20):
        print(i)
        pad_id = drone.get_mission_pad_id()
        print(pad_id)
        if pad_id == 3:
            print("mission pad ok")
            break
        time.sleep(1)
        
    
    
    drone.disable_mission_pads()    
    drone.end()
    
test1()

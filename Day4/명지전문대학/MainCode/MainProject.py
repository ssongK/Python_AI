from djitellopy import Tello
from threading import Thread
import time
import cv2
import numpy as np
from keras.models import load_model

def droneConnect(drone):
    drone.connect()
    drone.streamon()
    time.sleep(3) #3초 대기를 주지 않으면 오류가 발생할 수 있음

    while True:
        img = drone.get_frame_read().frame
        cv2.imshow("Show", img)
        img = cv2.resize(img, (64,64))
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        max_output_value = 255   # 출력 픽셀 강도의 최대값
        neighborhood_size = 99
        subtract_from_mean = 10
        image_binarized = cv2.adaptiveThreshold(img, max_output_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, neighborhood_size, subtract_from_mean)

        cv2.imwrite("1.jpg", image_binarized)

        Key = cv2.waitKey(1)
        if Key == ord("q"):
            break

    cv2.destroyAllWindows()
    drone.streamoff()
    drone.end()

def flyController(drone):
    drone.connect()
    power = drone.get_battery()

    if power<30:
        print("에너지가 부족함")
    else:
        while True:
            if power<30:
                print("에너지가 부족함")
                break
            print("현재 배터리 잔량 :", power)
            print("이륙 착륙 앞쪽 뒷쪽 우측 좌측 시계 반시계 종료")
            print("[5]  [.]  [8]  [2]  [6]  [4] [86] [42] [exit]")
            cmd = input("명령어를 넣어주세요 >> ")
            
            if cmd=="end":
                print("프로그램을 종료하겠습니다.")
                break
            elif cmd=="5":
                drone.takeoff() #올라가기
            elif cmd==".":
                drone.land() #내려오기
            elif cmd=="8":
                drone.move_forward(50) #앞으로 이동
            elif cmd=="2":
                drone.move_back(50) #뒤로 이동
            elif cmd=="4":
                drone.move_left(20) #왼쪽으로 이동
            elif cmd=="6":
                drone.move_right(20) #오른쪽으로 이동
            elif cmd=="86":
                drone.rotate_clockwise(90) #시계방향
            elif cmd=="42":
                drone.rotate_counter_clockwise(90) #반시계방향
            elif cmd=="exit":
                break
            else:
                print("알수없는 명령어!")

def droneControll(data, drone):
    if data == 0:
        drone.rotate_clockwise(90) #시계방향
        time.sleep(2)
        drone.move_forward(80) #앞으로 이동
    elif data == 1:
        drone.rotate_counter_clockwise(90) #반시계방향
        time.sleep(2)
        drone.move_forward(80) #앞으로 이동
    elif data == 2:
        drone.move_up(30) #30cm 올라가기
        time.sleep(2)
    elif data == 3:
        drone.land() #착륙
        time.sleep(2)


def main():
    model = load_model('C://Users//Monta//Desktop//Language//pythonAI//Day4//Model//2022-07-01-02-Model//MyoungJiAI_sub.h5')
    
    drone = Tello()
    videoRun = Thread(target=droneConnect, args=[drone])
    videoRun.start()
    time.sleep(10)

    cntList = [0, 0, 0, 0] # 리스트 초기화
    drone.takeoff()
    time.sleep(3)
    while True:
        data = np.ndarray(shape=(1, 64, 64, 3), dtype=np.float32)
        image = cv2.imread('1.jpg')
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array

        prediction = model.predict(data)
        list = ["right","left","up","down"]
        index=np.argmax(prediction)

        cntList[index] += 1
        print("index = ",list[index], "List = ",cntList, "배터리 :",drone.get_battery())
        
        if cntList[0] == 3:
            droneControll(0, drone)
            cntList = [0, 0, 0, 0]
        elif cntList[1] == 3:
            droneControll(1, drone)
            cntList = [0, 0, 0, 0]
        elif cntList[2] == 3:
            droneControll(2, drone)
            cntList = [0, 0, 0, 0]
        elif cntList[3] == 3:
            droneControll(3, drone)
            break

        time.sleep(2)
    
    videoRun.join()
    time.sleep(3)
    drone.end()

main()
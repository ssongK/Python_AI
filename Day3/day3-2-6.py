from djitellopy import Tello
from threading import Thread
import time
import cv2

def test01(drone):
    drone.connect()
    drone.streamon()
    time.sleep(3) #3초 대기를 주지 않으면 오류가 발생할 수 있음

    while True:
        img = drone.get_frame_read().frame
        img = cv2.resize(img, (120,120))
        cv2.imshow("120*120", img)
        Key = cv2.waitKey(1)
        if Key == ord("q"):
            break

    cv2.destroyAllWindows()
    drone.streamoff()
    drone.end()

# test01()

def test02(drone):
    drone.connect()
    power = drone.get_battery()

    if power<30:
        print("에너지가 부족함")
    else:
        while True:
            if power<30:
                print("에너지가 부족함")
                break
            print("이륙 착륙 앞쪽 뒷쪽 우측 좌측 시계 반시계")
            print("[5]  [.]  [8]  [2]  [6]  [4] [86] [42] ")
            cmd = input("명령어를 넣어주세요 >> ")
            
            if cmd=="end":
                print("프로그램을 종료하겠습니다.")
                break
            elif cmd=="5":
                drone.takeoff() #올라가기
            elif cmd==".":
                drone.land() #내려오기
            elif cmd=="8":
                drone.move_forward(20) #앞으로 이동
            elif cmd=="2":
                drone.move_back(20) #뒤로 이동
            elif cmd=="4":
                drone.move_left(20) #왼쪽으로 이동
            elif cmd=="6":
                drone.move_right(20) #오른쪽으로 이동
            elif cmd=="86":
                drone.rotate_clockwise(90) #시계방향
            elif cmd=="42":
                drone.rotate_counter_clockwise(90) #반시계방향
            else:
                print("알수없는 명령어!")
#test02()


def main():
    drone = Tello()
    videoRun = Thread(target=test01, args=[drone])
    
    flyRun = Thread(target=test02, args=[drone])

    videoRun.start()
    time.sleep(10)
    flyRun.start()
    time.sleep(1)

    videoRun.join()
    flyRun.join()

    drone.land()
    time.sleep(3)
    drone.end()

main()
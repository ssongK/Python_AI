import cv2

def test1():
    img = cv2.imread("Day2/1.jpg")
    print(img.shape)
    cv2.imshow("my",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# test1()

def test2():
    img = cv2.imread("Day2/1.jpg")
    print(img.shape)
    
    img1 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    print(img.shape)
    
    # cv2.imshow("ds",img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    cv2.imwrite("Day2/1a.png",img1)
    
# test2()

def test3():
    img = cv2.imread("Day2/1.jpg")
    print(img.shape)
    w,h,_ = img.shape
    print(w,h)
    
    w = int(w*0.5)
    h = int(h*0.5)
    print(w,h)
    
    img1 = cv2.resize(img,(w,h))
    print(img1.shape)
    
    cv2.imshow("ds",img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# test3()

# 인터넷에서 이미지 파일 구할것 -> 그레이 이미지로 변경 -> 크기를 절반으로 줄이고 출력
def test4():
    img = cv2.imread("Day2/2.jpg")
    img1 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    print(img1.shape)
    
    w,h = img1.shape
    w = int(w*0.5)
    h = int(h*0.5)
    
    img1 = cv2.resize(img1,(w,h))
    
    cv2.imshow("my",img)
    cv2.imshow("ds",img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
test4()
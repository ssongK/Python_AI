import numpy as np
import cv2

def test1():
    img = cv2.imread("Day2/data/2.jpg")
    print(img.shape)
    
    cv2.imshow("color",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    print(img2.shape)
    
    cv2.imshow("HSV",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# test1()

import os
def my_make_data():
    path = "Day2/data"
    file_list = os.listdir(path)
    print(file_list)
    
    data = []
    
    for i in range(len(file_list)):
        file_path = path + "/" + file_list[i]
        # print(file_path)
        img = cv2.imread(file_path,0)
        print(file_path,img.shape)
        
        img = cv2.resize(img,(320,240))
        print(img.shape)
        img = img.tolist()
        data.append(img)
        
    data = np.array(data)
    print(data.shape)
    
    return data
        
my_make_data()
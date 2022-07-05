import cv2
import os

path = "C://Users//Monta//Desktop//Language//pythonAI//Day4//NewData"

folder_list = os.listdir(path)
print(folder_list)

for i in range(len(folder_list)):
    file_path = path + "/" + folder_list[i]
    file_name = os.listdir(file_path)
    print(i,file_path)
    
    for j in range(len(file_name)):
        full_file_path = file_path + "/" + file_name[j]
        print(full_file_path)
        img = cv2.imread(full_file_path)
        
        # img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        # max_output_value = 255   # 출력 픽셀 강도의 최대값
        # neighborhood_size = 99
        # subtract_from_mean = 4
        # img = cv2.adaptiveThreshold(img,        
        #                             max_output_value,
        #                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        #                             cv2.THRESH_BINARY,
        #                             neighborhood_size,
        #                             subtract_from_mean)
        img = cv2.resize(img,(64,64))
        cv2.imwrite(f"small{j}.jpg",img)
        print(f"small{j}.jpg")

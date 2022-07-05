import numpy as np
import cv2
from tensorflow.keras import applications
from tensorflow.keras import models,layers
import os

def get_XY(path):
    x = []
    y = []
    
    folder_list = os.listdir(path)
    print(folder_list)
    
    for i in range(len(folder_list)):
        file_path = path + "/" + folder_list[i]
        file_name = os.listdir(file_path)
        # print(i,file_path)
        
        for j in range(len(file_name)):
            full_file_path = file_path + "/" + file_name[j]
            # print(full_file_path)
            img = cv2.imread(full_file_path)
            img = cv2.resize(img,(32,32))
            x.append(img)
            y.append(i)
            
    return np.array(x),np.array(y)

def getData():
    path = "Day3/data/train"
    x_train,y_train = get_XY(path)
    print(x_train.shape,y_train.shape)
    
    path = "Day3/data/train"
    x_test,y_test = get_XY(path)
    
    return (x_train,y_train),(x_test,y_test)

def makeModel():
    resnet50 = applications.resnet50.ResNet50(
        include_top=False,
        weights="imagenet",
        input_shape=(32,32,3),
    )
    resnet50.trainable = False
    
    model = models.Sequential()
    model.add(resnet50)
    model.add(layers.Flatten())
    model.add(layers.Dense(1024,activation="relu"))
    model.add(layers.Dense(5,activation="softmax"))
    
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])
    print(model.summary())

    return model

def doLearn():
    (x_train,y_train),(x_test,y_test) = getData()
    
    model = makeModel()
    
doLearn()

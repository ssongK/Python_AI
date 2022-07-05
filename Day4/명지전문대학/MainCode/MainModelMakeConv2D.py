import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
from tensorflow.keras import applications
from tensorflow.keras import models, layers
from keras.callbacks import ModelCheckpoint, EarlyStopping

def get_XY(path):
    x = []
    y = []
    folder_list = os.listdir(path)

    #파일의 경로를 가져오는 알고리즘
    for i in range(len(folder_list)):
        file_path = path + "/" + folder_list[i]
        file_name = os.listdir(file_path)
        # print(i,"|", file_path)
        for j in range(len(file_name)):
            full_file_path = file_path + "/" + file_name[j]
            # print(full_file_path)
            img = cv2.imread(full_file_path)
            img = cv2.resize(img, (64,64))
            x.append(img)
            y.append(i)
    
    return np.array(x), np.array(y)

def getData():
    #기본 파일 경로
    path = "Day4/mainData/train" #변경
    x_train, y_train = get_XY(path)
    print(x_train.shape, y_train.shape)

    path = "Day4/mainData/test" #변경
    x_test, y_test = get_XY(path)
    print(x_test.shape, y_test.shape)

    return (x_train, y_train), (x_test, y_test)
#getData()

def makeModel():
    
    model = models.Sequential()
    
    model.add(layers.Conv2D(32,(3,3),activation="relu",input_shape=(64,64,3)))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64,(3,3),activation="relu"))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64,(3,3),activation="relu"))
    model.add(layers.MaxPooling2D((2,2)))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(512, activation="relu")) 
    model.add(layers.Dense(256, activation="relu"))
    model.add(layers.Dense(128, activation="relu"))
    model.add(layers.Dense(4, activation="softmax"))
    
    
    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["acc"])
    
    print(model.summary())

    return model

def doLearn():
    (x_train, y_train), (x_test, y_test) = getData()
    
    # earlystopping = EarlyStopping(monitor='val_loss', # 모니터 기준 설정 (val loss) 
    #                               mode='min',
    #                               patience=10         # 10회 Epoch동안 개선되지 않는다면 종료
    #                              )
    
    checkpoint = ModelCheckpoint("MyoungJiAI_sub.h5",      # file명을 지정합니다
                                monitor='val_loss',   # val_loss 값이 개선되었을때 호출됩니다
                                verbose=1,            # 로그를 출력합니다
                                save_best_only=True,  # 가장 best 값만 저장합니다
                                mode='auto'           # auto는 알아서 best를 찾습니다. min/max
                                )

    model = makeModel()

    log = model.fit(x_train, y_train,
                    epochs=2000, batch_size=16,
                    validation_split=0.2,
                    callbacks=[checkpoint]
                    )
    
    model.save("MyoungJiAI.h5")

    loss_h = log.history["loss"]
    acc_h = log.history["acc"]
    val_loss = log.history["val_loss"]
    val_acc = log.history["val_acc"]
    
    y1 = plt.axes()
    y1.plot(loss_h,'r',label="loss_h")
    y1.plot(val_loss,'y',label="val_loss")
    y1.legend(loc="upper left")
    
    y2 = y1.twinx()
    y2.plot(acc_h,'b',label="acc_h")
    y2.plot(val_acc,'g',label="val_acc")
    y2.legend(loc="upper right")
    plt.show()

doLearn()
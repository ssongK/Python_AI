import numpy as np
import cv2
from tensorflow.keras import datasets
from tensorflow.keras import models,layers

def getData():
    (x_train,y_train),(x_test,y_test) = datasets.mnist.load_data()
    x_train = x_train / 255.0
    x_test = x_test / 255.0
    return (x_train,y_train),(x_test,y_test) 

def makeModel():
    model = models.Sequential()
    model.add(layers.Conv2D(32,(3,3),activation="relu",input_shape=(28,28,3)))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Conv2D(16,(3,3),activation="relu"))

    model.add(layers.Flatten())
    model.add(layers.Dense(64,activation="relu"))
    model.add(layers.Dense(10,activation="softmax"))

    model.compile(loss = "sparse_categorical_crossentropy",
                    optimizer = "adam",
                    metrics = ["accuracy"])
    print(model.summary)
    
    return model

def doRun():
    (x_train,y_train),(x_test,y_test) = getData()
    model = makeModel()
    
    log = model.fit(x_train, y_train,
                    epochs = 3, batch_size = 16)
    
    model.save("my.h5")

    score = model.evaluate(x_test, y_test) # evaluate(문제, 답)
    print(score)

doRun()
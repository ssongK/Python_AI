import numpy as np
import cv2
from tensorflow.keras import models,layers
from tensorflow.keras import datasets

def getData():
    (x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
    print(x_train.shape)

    x_train = x_train.reshape(-1,28*28)
    print(x_train.shape)  

    x_test = x_test.reshape(-1,28*28)

    return (x_train, y_train), (x_test, y_test)

getData()

def makeModel():
# input : (28*28,) / output : (10,)
    model = models.Sequential()
    model.add(layers.Dense(200,activation="relu",input_shape=(28*28,)))
    model.add(layers.Dense(100,activation="relu"))
    model.add(layers.Dense(10,activation="softmax"))
    model.compile(loss="sparse_categorical_crossentropy",
                    optimizer="adam",
                    metrics=["accuracy"])
    print(model.summary())
    return model

makeModel()

def doRun():
    (x_train, y_train), (x_test, y_test) = getData()
    model = makeModel()
    log = model.fit(x_train,y_train,
                    epochs=2,batch_size=16)
    model.save("my1.h5")

doRun()
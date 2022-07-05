import numpy as np
import cv2
from tensorflow.keras import datasets,models,layers

def getData():
    (x_train,y_train),(x_test,y_test) = datasets.fashion_mnist.load_data()
    print(x_train.shape)
    return (x_train,y_train),(x_test,y_test) 

getData()
    
def makeModel():
    model = models.Sequential()
    model.add(layers.Conv2D(32,(3,3),activation="relu",input_shape=(28,28,1)))
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
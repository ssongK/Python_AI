import numpy as np
import cv2
from tensorflow.keras import datasets
from tensorflow.keras import models,layers

def getData(): 
    (x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
    
    x_train = x_train.reshape(-1, 28 * 28)
    x_test = x_test.reshape(-1, 28 * 28)

    return (x_train, y_train), (x_test, y_test)

def makeModel() :
    model = models.Sequential()
    model.add(layers.Dense(1000, activation = "relu", input_shape = (28 * 28, )))
    model.add(layers.Dense(500, activation= "relu"))
    model.add(layers.Dense(10, activation = "softmax"))
    
    model.compile(loss = "sparse_categorical_crossentropy",
                    optimizer = "adam",
                    metrics = ["accuracy"])
    print(model.summary)

    return model

def doRun() :
    (x_train, y_train), (x_test, y_test) = getData()
    model = makeModel()
    
    log = model.fit(x_train, y_train,
                    epochs = 3, batch_size = 16)
    
    model.save("my2.h5")

    score = model.evaluate(x_test, y_test) # evaluate(문제, 답)
    print(score)

    loss_h = log.history["loss"]
    acc_h = log.history["accuracy"]
    print(loss_h,acc_h)

doRun()

def makeData():
    (x_train,y_train),(x_test,y_test) = datasets.mnist.load_data()
    img = x_test[0]
    cv2.imwrite("1.png",img)

makeData()

def doPredict():
    x = cv2.imread("1.png",0)
    x = x.reshape(-1,(28*28))
    print(x.shape)
    x = [x]
    model = models.load_model("my2.h5")
    y_pre = model.predict(x)
    y_pre = np.argmax(y_pre)
    print(y_pre)

doPredict()
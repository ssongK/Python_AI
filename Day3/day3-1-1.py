import numpy as np
import cv2
from tensorflow.keras import datasets
from tensorflow.keras import applications

from tensorflow.keras import models,layers

def changeData(data,size=(32,32)):
  ans = []
  for i in range(len(data)):
    img = data[i]
    cv2.imwrite("t.png",img)
    img = cv2.imread("t.png")
    img = cv2.resize(img,size)
    ans.append(img)

  ans = np.array(ans)
  return ans



def getData():
    (x_train,y_train),(x_test,y_test) = datasets.mnist.load_data()
    print(x_train.shape,y_train.shape)
    x_train = changeData(x_train)
    x_test = changeData(x_test)
    print(x_train.shape)
    print(x_test.shape)
    return (x_train,y_train),(x_test,y_test)

def makeModel():
    vgg16 = applications.VGG16(include_top=False,input_shape=(32,32,3))
    vgg16.trainable = False
    
    model = models.Sequential()
    model.add(vgg16)
    
    model.add(layers.Flatten())
    model.add(layers.Dense(256,activation="relu"))
    model.add(layers.Dense(10,activation="softmax"))
    
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])
    
    print(model.summary())

    return model

def doLearn():
    (x_train,y_train),(x_test,y_test) = getData()
    model = makeModel()

    log = model.fit(x_train,y_train,
                    epochs=2,batch_size=16)
    
    model.save("my.h5")
    score = model.evaluate(x_test,y_test)
    print(score)

doLearn()
"""
비만도(BMI) = 몸무게(kg) / 키(m)**2
1   1.83    86
2   1.76    74
3   1.69    59
4   1.86    95
5   1.77    80
6   1.78    68
7   1.65    60

BMI > 27 => 비만
"""
    
import numpy as np

def checkBMI():
    w = [86,74,59,95,80,68,60]
    h = [1.83,1.76,1.69,1.86,1.77,1.78,1.65]
    wdata = np.array(w)
    hdata = np.array(h)
    bmi = wdata / hdata ** 2
    bmi = np.where(bmi>27,'비만','정상')
    
    print("몸무게 : ",wdata)
    print("키 : ",hdata)
    print(bmi)
    
checkBMI()

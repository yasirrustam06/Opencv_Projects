import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while True:
    ret,Image=cap.read()
    Gray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(Gray)

    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(Gray, invertedblur, scale=256.0)


    cv2.imshow("sketch",sketch)
    cv2.imshow("Gray",Gray)
    cv2.waitKey(1)
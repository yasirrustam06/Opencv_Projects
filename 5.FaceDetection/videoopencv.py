import cv2
import numpy as np
cap=cv2.VideoCapture(0)

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
    cv2.imshow("Image",img)
    cv2.waitKey(1)




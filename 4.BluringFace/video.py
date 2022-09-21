import cv2
import numpy as np

cap=cv2.VideoCapture(0)

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray,1.1,1)
    for x,y,w,h in faces:
        blur_face = img[y:y + h, x:x + w]
        blur_face = cv2.GaussianBlur(blur_face, (23, 23), 30)

        img[y:y + blur_face.shape[0], x:x + blur_face.shape[1]] = blur_face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        cv2.imshow("Image",img)

        cv2.waitKey(1)

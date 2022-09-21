import cv2
import numpy as np

img=cv2.imread('Father-Daughter.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces=cascade.detectMultiScale(gray,1.1,1)
for x,y,w,h in faces:
    blur_face = img[y:y + h, x:x + w]
    blur_face = cv2.GaussianBlur(blur_face, (23, 23), 30)


    img[y:y + blur_face.shape[0], x:x + blur_face.shape[1]] = blur_face



    cv2.imshow("Image",img)
    cv2.waitKey(0)



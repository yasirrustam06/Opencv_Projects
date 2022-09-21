import cv2
import numpy as np
img=cv2.imread('face.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces=cascade.detectMultiScale(gray,1.1,4)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



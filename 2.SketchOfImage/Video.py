import cv2
import numpy as np


cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
   # preprocessing Image--------------->
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    invertGray=255-gray
    Gaussian=cv2.GaussianBlur(src=gray,ksize=(3,3),sigmaY=1,sigmaX=1)
    invert_Gaussian=255-Gaussian
    Sketched_Image=cv2.divide(src1=gray,src2=invert_Gaussian,scale=256.0)




    cv2.imshow("Image",img)
    cv2.imshow("Sketched_Image",Sketched_Image)
    cv2.waitKey(1)
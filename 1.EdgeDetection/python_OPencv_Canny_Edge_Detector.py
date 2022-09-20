import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    # Gray Scale Image
    Gray_Image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Gaussian BLurring For removing the noise from an image
    Gaussian_Image=cv2.GaussianBlur(src=Gray_Image,ksize=(3,3),sigmaX=0,sigmaY=1)


    # Now applying the Canny Edge Detector For Edge Detection
    Canny_Edged_Image=cv2.Canny(image=Gaussian_Image,threshold1=100,threshold2=200)

    cv2.imshow("Canny_Edged_Detected_Image",Canny_Edged_Image)
    cv2.imshow("Gaussian_Image",Gaussian_Image)
    # cv2.imshow("Gray_Image",Gray_Image)
    cv2.waitKey(1)

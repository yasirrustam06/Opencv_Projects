import cv2
import numpy as np


cap=cv2.VideoCapture(0)



while True:
    ret,Image=cap.read()

    gray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)

    _,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoured_Image = cv2.drawContours(Image, contours, -1, (0, 255, 0), 2)


    cv2.imshow("gray",gray)
    cv2.imshow('contoured_Image',contoured_Image)
    cv2.waitKey(1)





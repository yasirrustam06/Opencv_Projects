import cv2
# img=cv2.imread('edgee.jpg')
# cv2.imshow("Origian_Image",img)


cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()




    # change intp gray scale image
    #-----------------------------------------
    gray_Img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray_sacled_Image",gray_Img)
    #----------------------------------------------
    # Applying the Gaussian Blur

    Gaussin_Image=cv2.GaussianBlur(gray_Img,(3,3),1)
    cv2.imshow("Gaussian_Image",Gaussin_Image)
    #-----------------------
    #Appluing sobble Filter for calculating the deriavtive of an image fo edge detection
    sobelx=cv2.Sobel(src=Gaussin_Image,ddepth=cv2.CV_64F,dx=1,dy=0,ksize=5)
    sobely=cv2.Sobel(src=Gaussin_Image,ddepth=cv2.CV_64F,dx=0,dy=1,ksize=5)
    #  applying combined
    sobelXY=cv2.Sobel(src=Gaussin_Image,ddepth=cv2.CV_64F,dx=1,dy=1,ksize=5)
    cv2.imshow("Sobel_Edged_Image",sobelXY)



    cv2.waitKey(1)











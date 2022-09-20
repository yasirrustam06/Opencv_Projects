import cv2
import numpy as np
Image=cv2.imread('person.jpg')

#----------------------------------->

# gray _Image
Gray_Image=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
# invert Gray Image
Inverted_Gray=255 - Gray_Image
#----------------------------->
# Gauaain_Blur Image
Gaussian_Image=cv2.GaussianBlur(src=Gray_Image,ksize=(3,3),sigmaX=1,sigmaY=1)
#Invert Gaussian_Blur Image
Inverted_Gaussian_Image=255 - Gaussian_Image

#--------------------------->
#      Creating the Pencil Sketches Of Given Images

Sketched_Image=cv2.divide(src1=Gray_Image,src2=Inverted_Gaussian_Image,scale=256.0)

cv2.imshow("Sketched_Image",Sketched_Image)
cv2.imshow("Gray_scale_Imag",Gray_Image)

cv2.waitKey(0)
cv2.destroyAllWindows()






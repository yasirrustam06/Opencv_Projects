import cv2
Image=cv2.imread("thumbs_up_down.jpg")
gray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)


# create a binary thresholded image
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)




# draw all contours
contoured_Image = cv2.drawContours(Image, contours, -1, (0, 255, 0), 2)


cv2.imshow("Image",contoured_Image)
# cv2.imshow("Gray",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

#First openCV program to play with
import cv2

img1 = cv2.imread(r"C:\Users\Tuts\Pictures\sunset.jpg",0)
img1 = cv2.resize(img1,(1280,720))
cv2.imshow('Image', img1)
cv2.waitkey(0)
cv2.destroyAllWindows()

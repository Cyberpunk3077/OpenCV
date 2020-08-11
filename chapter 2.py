import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

print(img.shape)

imgResize = cv2.resize(img,(640,480))
imgCropped = img[0:200,200:500]

cv2.imshow("Cropped image",imgCropped)
cv2.waitKey(0)
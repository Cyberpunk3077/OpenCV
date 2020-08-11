import numpy as np
import cv2

img = cv2.imread("Resources/falling-poker-playing-cards-of-aces-vector-18818709.jpg")
width,height = 250,350
pts1 = np.float32([[331,70],[527,60],[491,299],[694,270]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Output", imgOutput)
cv2.waitKey(0)
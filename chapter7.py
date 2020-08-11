import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue max","TrackBars",172,179,empty)
cv2.createTrackbar("Sat min","TrackBars",114,255,empty)
cv2.createTrackbar("Sat max","TrackBars",255,255,empty)
cv2.createTrackbar("Val min","TrackBars",169,179,empty)
cv2.createTrackbar("Val max","TrackBars",255,255,empty)

while True:
    img = cv2.imread("Resources/05da3b6087826d375547b7b87799360f.jpg")
    imgResized = cv2.resize(img,(640,480))
    imgHSV = cv2.cvtColor(imgResized,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat max","TrackBars")
    v_min = cv2.getTrackbarPos("Val min","TrackBars")
    v_max = cv2.getTrackbarPos("Val max","TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(imgResized,imgResized,mask=mask)

    cv2.imshow("Original",imgResized)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)
import cv2

width,height = 640,480
cap = cv2.VideoCapture(0)

cap.set(3,width)
cap.set(4,height)
cap.set(10,130)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

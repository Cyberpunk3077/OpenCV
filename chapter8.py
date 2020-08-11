import cv2

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),4)
            peri = cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objCor==3:
                objectType = "Tri"
            elif objCor==4:
                aspectRatio = w/h
                if 0.95<aspectRatio<1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor>4:
                objectType = "Circle"
            else:
                objectType = "None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,0),1)


img = cv2.imread("Resources/original-3785610-1.jpg")
imgResize = cv2.resize(img,(300,300))
imgContour = imgResize.copy()
imgGray = cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

#cv2.imshow("Original",imgResize)
#cv2.imshow("Gray",imgGray)
#cv2.imshow("Blur",imgBlur)
#cv2.imshow("Canny",imgCanny)
cv2.imshow("Contour",imgContour)
cv2.waitKey(0)
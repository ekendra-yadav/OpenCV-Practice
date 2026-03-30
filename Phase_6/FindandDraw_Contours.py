import cv2

image = cv2.imread("Phase_6\Screenshot 2026-03-30 113459.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
contours,heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,contours,-1,(0, 255, 0),3)

cv2.imshow("Contour Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
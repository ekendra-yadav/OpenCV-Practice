import cv2

img = cv2.imread("Phase_5\c0d80a5d314d69658afa0e82a0d9357b.jpg",cv2.IMREAD_GRAYSCALE)

ret,thresh_img = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

cv2.imshow("Original Image",img)
cv2.imshow("Thresholded Image",thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

image = cv2.imread("Phase_4\c0d80a5d314d69658afa0e82a0d9357b.jpg")
resize = cv2.resize(image,(600,600))

blurred = cv2.medianBlur(resize,11)
resize_blur = cv2.resize(blurred,(600,600))

cv2.imshow("Original Image", resize)
cv2.imshow("Median Blurred Image",resize_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
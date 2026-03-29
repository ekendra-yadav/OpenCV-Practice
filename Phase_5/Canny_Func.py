import cv2
img = cv2.imread("Phase_5\c0d80a5d314d69658afa0e82a0d9357b.jpg",cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img,50,150)

cv2.imshow("Original Image",img)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
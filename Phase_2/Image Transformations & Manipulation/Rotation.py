import cv2
image = cv2.imread("Phase_1\Ekendra Yadav Profile.jpeg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

if image is None:
    print("Image not Found!")
else:
    (h,w) = gray.shape[:2]
    center = ((w//2),(h//2))
    M = cv2.getRotationMatrix2D(center,90,1.0)
    rotated = cv2.warpAffine(gray,M,(w,h))
    cv2.imshow("Original Image",gray)
    cv2.imshow("Rotated Image",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
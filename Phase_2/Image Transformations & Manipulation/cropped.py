import cv2
image = cv2.imread("Phase_1\Ekendra Yadav Profile.jpeg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

if image is None:
    print("Image not Found!")
else:
    cropped_image = gray[100:550, 50:600]
    cv2.imshow("Original Image",gray)
    cv2.imshow("Cropped Image",cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
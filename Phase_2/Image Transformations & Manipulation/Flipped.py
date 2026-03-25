import cv2
image = cv2.imread("Phase_1\Ekendra Yadav Profile.jpeg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resize = cv2.resize(gray,(500,500))

if image is None:
    print("Image not Found!")
else:
    flipped_horizontal = cv2.flip(resize,1)
    flipped_vertical = cv2.flip(resize,0)
    flipped_both = cv2.flip(resize,-1)
    cv2.imshow("Original Image",resize)
    cv2.imshow("Flipped Horizontal",flipped_horizontal)
    cv2.imshow("Flipped Vertical",flipped_vertical)
    cv2.imshow("Flipped Both",flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
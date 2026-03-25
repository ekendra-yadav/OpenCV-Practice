import cv2
image = cv2.imread("Phase_2\Basic Image Drawing Techniques\Ekendra Yadav Profile.jpeg")

if image is None:
    print("Image not found!")
else:
    print("Image Loaded")
    pt1 = (50,100)
    pt2 = (300,100)
    color = (255,0,0)
    thickness = 4
    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("Line Drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
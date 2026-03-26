import cv2
image = cv2.imread("Phase_2\Basic Image Drawing Techniques\Ekendra Yadav Profile.jpeg")

if image is None:
    print("Image not found!")
else:
    print("Image Found!")

    pt1 = (250,200)
    pt2 = (600,400)
    color = (255,0,0)
    thickness = 2
    
    cv2.rectangle(image,pt1,pt2,color,thickness)
    
    cv2.imshow("Rectangle Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import cv2
image = cv2.imread("Phase_2\Basic Image Drawing Techniques\Ekendra Yadav Profile.jpeg")

if image is None:
    print("Image not found!")
else:
    print("Image found!")
    
    cv2.circle(image,center=(350,380),radius=150,color=(255,0,0),thickness=2)
    cv2.imshow("Circle Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
import cv2
image = cv2.imread("Phase_2\Basic Image Drawing Techniques\Ekendra Yadav Profile.jpeg")

if image is None:
    print("Image not found!")
else:
    print("Image Found!")
    cv2.putText(image,"Hello I'm Ekendra",org=(250,150),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.2,color=(250,0,0),thickness=3)
    cv2.imshow("Adding Text",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
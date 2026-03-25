import cv2
image = cv2.imread("Ekendra Yadav Profile.jpeg")
if image is not None:
    print("Image Loaded Succesfully")
else:
    print("Error: Could Load the Image")
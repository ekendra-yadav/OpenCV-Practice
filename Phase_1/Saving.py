import cv2
image = cv2.imread("Ekendra Yadav Profile.jpeg")

if image is not None:
    success = cv2.imwrite("Output_image.jpeg",image)
    if success:
        print("Image saved sucessfully as 'Output_image.jpeg'")
    else:
        print("Failed to save")
else:
    print("Could not load the image")
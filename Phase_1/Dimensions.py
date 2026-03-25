import cv2
image = cv2.imread("Phase_1\Ekendra Yadav Profile.jpeg")

if image is not None:
    h,w,c = image.shape
    print(f"Image Loaded\nHeight: {h}\nWidth: {w}\nChannel: {c}")
else:
    print("Could not load the image")
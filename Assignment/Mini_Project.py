'''
import cv2  # import the library

image = cv2.imread("Assignment\Apple.png")   # Read or Load the image 

cv2.imshow("Windows Title",image)  # Display the image
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Outpu_image.png",image)  # Save the image 

image.shape  # Dimension of the image (height,width,channel if (BGR) || height,width if (Grayscale))

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)  # Grayscale conversion 
'''



# import cv2
# location = input("Enter the location of image: ")
# image = cv2.imread(location)


# permit = input("Do you want to see(SH) the picture or save the picture(SV): ").upper()
# if (permit=="SH"):
#     if image is not None:
#         gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#         cv2.imshow("Grayscale Image",gray)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     else:
#         print("Could not load the image")
# elif(permit=="SV"):
#     success = cv2.imwrite("Assignment\Saved.png",image)
#     if success:
#         print("Image is Saved Sucessfully as 'Saved.png'")
#     else:
#         print("Failed to save")
# else:
#     print("Invalid input")



import cv2
image_location = input("Enter image location: ")
if image_location is not None:
    image = cv2.imread(image_location)
    print("Image loaded successfully")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    print("Error: Image not found")

userchoice = input("Show or Save? ")
user_choice = userchoice.lower()
if user_choice=="show":
    cv2.imshow("Gray image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif user_choice=="save":
    file_name = input("Enter file name: ")
    success = cv2.imwrite(file_name, gray)
    if success:
        print("Image saved successfully")
    else:
        print("Error: Failed to save image")
else:
    print("Make a valid choice") 
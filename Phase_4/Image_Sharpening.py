import cv2
import numpy as np

# Use / for paths to avoid escape sequence errors
image = cv2.imread("Phase_4/couple-before-02.jpg")

if image is None:
    print("Error: Image could not load. Check the file name and path.")
else:
    # 1. Resize first for consistent display
    resize = cv2.resize(image, (600, 600))

    # 2. Define the kernel with proper commas
    sharpen_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    # 3. Apply the filter
    sharpened = cv2.filter2D(resize, -1, sharpen_kernel)

    # 4. Display results
    cv2.imshow("Original Image (Resized)", resize)
    cv2.imshow("Sharpened Image", sharpened)

    print("Sharpening applied successfully!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
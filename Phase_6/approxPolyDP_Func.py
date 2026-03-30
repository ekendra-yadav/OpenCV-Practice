import cv2

# Use r"" to avoid the path errors we discussed earlier
img = cv2.imread(r"Phase_6\2D-Shapes-06.png")

if img is None:
    print("Error: Image not found.")
else:
    # 1. Pre-process to remove noise
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) # Smooths the jagged edges
    
    # 2. Threshold (Using INV if the shape is darker than background)
    _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)

    # 3. Find Contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        
        # 4. IGNORE TINY NOISE: Only look at the big triangle
        if area > 1000:
            # Increased epsilon to 0.02 for better simplification
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            corners = len(approx)

            if corners == 3:
                shape_name = "Triangle"
            elif corners == 4:
                shape_name = "Rectangle"
            elif corners == 5:
                shape_name = "Pentagon"
            elif corners == 8:
                shape_name = "Hexagon"
            elif corners > 8:
                shape_name = "Circle"
            else:
                shape_name = "Invalid Shape"

            # Draw only the simplified 'approx' shape
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)
            
            # Label at the first point of the approximation
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 10
            cv2.putText(img, shape_name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

    cv2.imshow("Clean Contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
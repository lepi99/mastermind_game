import cv2
import numpy as np
def getSubImage(rect, src):
    # Get center, size, and angle from rect
    center, size, theta = rect
    # Convert to int
    center, size = tuple(map(int, center)), tuple(map(int, size))
    # Get rotation matrix for rectangle
    M = cv2.getRotationMatrix2D( center, theta, 1)
    # Perform rotation on src image
    dst = cv2.warpAffine(src, M, (src.shape[0],src.shape[1]))
    out = cv2.getRectSubPix(dst, size, center)
    return out
# Load the image
#image = cv2.imread("images/Mastermind_cover1.jpg")
image = cv2.imread("../images/Mastermind_cover2.jpg")
#image = cv2.imread("images/Mastermind_cover3.jpg")
#image = cv2.imread("images/Mastermind_cover4.jpg")
#image = cv2.imread("../images/Mastermind_cover5.jpg")
#image = cv2.imread("../images/mastermind-wooden-2-player-game-kubiya.webp")

# Convert the image to grayscale
#gray = image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Apply Gaussian blur to reduce noise
#blurred = image
#blurred = cv2.GaussianBlur(gray, (11, 11), 0)
blurred = cv2.medianBlur(gray, 11)
#blurred = cv2.bilateralFilter(gray, 11, 77, 77)

# Detect edges using Canny edge detection
edges = cv2.Canny(blurred, 50, 60)  # Adjust the thresholds here
cv2.imshow("Circle Detection cont", edges)
cv2.waitKey(0)
# Find contours in the edged image
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
#contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)


# Initialize a list to store circle information
circles_info = []

# Iterate through detected contours
for contour in contours:
    # Fit an ellipse to the contour (assuming it's a circle)
    if len(contour) >= 10:
        ellipse = cv2.fitEllipse(contour)

        # Extract ellipse information: center, axes lengths (major and minor), and angle
        center, axes, angle = ellipse

        # Calculate the diameter of the circle (average of major and minor axes)
        print(axes)
        diameter = int((axes[0] + axes[1]) / 2.0)

        # Filter out non-circular shapes based on aspect ratio
        min_axis_length = min(axes)
        if min_axis_length > 0:
            aspect_ratio = max(axes) / min_axis_length
            if aspect_ratio < 2:
                # Store circle information as a tuple (center, diameter)
                circles_info.append((center, diameter))

# Calculate the average diameter for each circle
average_diameters = {}

# Iterate through detected circles and calculate the average diameter
for _, diameter in circles_info:
    # Find circles with similar diameters
    similar_diameters = [d for _, d in circles_info if abs(d - diameter) <10]

    # Calculate the average diameter
    average_diameter = sum(similar_diameters) / len(similar_diameters)

    # Store the average diameter with the diameter value as the key
    average_diameters[average_diameter] = similar_diameters
print(average_diameters)

# Draw the circles and their average diameters on the original image
for center, diameter in circles_info:
    # Convert the center coordinates to integers
    if (diameter > 20 and diameter < 35) or (diameter > 11 and diameter < 18):
        center = (int(center[0]), int(center[1]))

        # Draw the circle
        cv2.circle(image, center, int(diameter / 2), (0, 255, 0), 2)

        # Calculate the topmost point on the circle
        topmost_point = center[1] - int(diameter / 2)

        # Find the corresponding average diameter
        for avg_diameter, similar_diameters in average_diameters.items():
            if diameter in similar_diameters:
                # Draw the average diameter as text next to the circle
                aa=0
                cv2.putText(image, f"Diameter: {avg_diameter:.2f}", (center[0], topmost_point),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                break

# Display the image with circles and average diameters
cv2.imshow("Circle Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

###### work on this to just get the previous filtered circles
edges = cv2.Canny(image, 50, 60)
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
contours = np.vstack(contours).squeeze()
rect = cv2.minAreaRect(contours)
# Extract subregion
out = getSubImage(rect, edges)
# Save image
cv2.imwrite('out.jpg', out)
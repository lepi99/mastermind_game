import cv2
#import numpy as np

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

img = cv2.imread('images/mastermind-wooden-2-player-game-kubiya.webp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
blurred = cv2.medianBlur(gray, 11)
edges = cv2.Canny(blurred, 50, 60)
# Find some contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
# Get rotated bounding box
rect = cv2.minAreaRect(contours[3])
# Extract subregion
out = getSubImage(rect, edges)
# Save image
cv2.imwrite('out.jpg', out)
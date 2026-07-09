import cv2
import numpy as np

# ==========================================
# Load Packaging Image
# ==========================================

image = cv2.imread("images/package.jpg")

# Check if image exists
if image is None:
    print("Error: Packaging image not found.")
    exit()

print("Packaging image loaded successfully.")

# ==========================================
# Rotate Image 90° Clockwise
# ==========================================

height, width = image.shape[:2]

center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(
    center,
    -90,          # Clockwise rotation
    1.0
)

rotated = cv2.warpAffine(
    image,
    rotation_matrix,
    (width, height)
)

print("Image rotated successfully.")

# ==========================================
# Crop Lower-Right Quadrant
# ==========================================

h, w = rotated.shape[:2]

cropped = rotated[h//2:h, w//2:w]

print("Lower-right quadrant cropped.")

# ==========================================
# Flip Horizontally
# ==========================================

flipped = cv2.flip(cropped, 1)

print("Image flipped horizontally.")

# ==========================================
# Apply Gaussian Blur
# ==========================================

blurred = cv2.GaussianBlur(
    flipped,
    (5,5),
    0
)

print("Gaussian Blur applied.")

# ==========================================
# Canny Edge Detection
# ==========================================

edges = cv2.Canny(
    blurred,
    100,
    200
)

print("Canny Edge Detection completed.")

# ==========================================
# Display Images
# ==========================================

cv2.imshow("Rotated Image", rotated)

cv2.imshow("Cropped Image", cropped)

cv2.imshow("Flipped Image", flipped)

cv2.imshow("Label Edges", edges)

# ==========================================
# Save Edge Image
# ==========================================

cv2.imwrite("label_edges.jpg", edges)

print("\nEdge image saved as label_edges.jpg")

# ==========================================
# Wait and Close
# ==========================================

cv2.waitKey(0)

cv2.destroyAllWindows()
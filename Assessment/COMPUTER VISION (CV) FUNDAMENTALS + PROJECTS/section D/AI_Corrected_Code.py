import cv2

# Load image
image = cv2.imread("food.jpg")

# Fix: Check if image exists
if image is None:
    print("Error: Image not found.")
    exit()

# Resize
image = cv2.resize(image, (300,300))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian Blur
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Canny Edge Detection
edges = cv2.Canny(blur, 100, 200)

# Count edge pixels
edge_count = cv2.countNonZero(edges)

print("Total Edge Pixels:", edge_count)

# Convert edge image to BGR
edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Display images
combined = cv2.hconcat([image, edges_bgr])

cv2.imshow("Food Image Processing", combined)

# Save result
cv2.imwrite("ai_edge_output.jpg", edges)

print(f"Saved as ai_edge_output.jpg (Edge Pixels: {edge_count})")

cv2.waitKey(0)

cv2.destroyAllWindows()
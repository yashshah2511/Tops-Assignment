import cv2

# ==========================================
# Load Food Image
# ==========================================

image = cv2.imread("images/food.jpg")

# ==========================================
# Check if Image Exists
# ==========================================

if image is None:
    print("Error: Food image not found.")
    exit()

print("Food image loaded successfully.")

# ==========================================
# Print Image Properties
# ==========================================

height, width, channels = image.shape

print("\nImage Properties")
print("-" * 30)
print("Height :", height)
print("Width  :", width)
print("Channels :", channels)

# ==========================================
# Convert to Grayscale
# ==========================================

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ==========================================
# Display Images
# ==========================================

cv2.imshow("Original Food Image", image)

cv2.imshow("Grayscale Food Image", gray)

# ==========================================
# Save Grayscale Image
# ==========================================

cv2.imwrite("grayscale_food.jpg", gray)

print("\nImage saved successfully as grayscale_food.jpg")

# ==========================================
# Wait & Close Windows
# ==========================================

cv2.waitKey(0)

cv2.destroyAllWindows()
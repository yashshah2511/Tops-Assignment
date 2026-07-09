import cv2
import numpy as np

# ==========================================
# Load Image
# ==========================================

image = cv2.imread("images/menu.jpg")

# Check if image exists
if image is None:
    print("Error: Menu image not found.")
    exit()

print("Menu image loaded successfully.")

# ==========================================
# Resize Image
# ==========================================

resized = cv2.resize(
    image,
    (256, 256),
    interpolation=cv2.INTER_AREA
)

print("Image resized to 256 x 256.")

# ==========================================
# Split BGR Channels
# ==========================================

blue, green, red = cv2.split(resized)

# ==========================================
# Calculate Average Intensities
# ==========================================

blue_avg = np.mean(blue)
green_avg = np.mean(green)
red_avg = np.mean(red)

print("\nAverage Pixel Intensities")
print("-" * 35)
print(f"Blue  : {blue_avg:.2f}")
print(f"Green : {green_avg:.2f}")
print(f"Red   : {red_avg:.2f}")

# ==========================================
# Display Images
# ==========================================

cv2.imshow("Resized Menu Image", resized)

cv2.imshow("Blue Channel", blue)

cv2.imshow("Green Channel", green)

cv2.imshow("Red Channel", red)

# ==========================================
# Find Dominant Channel
# ==========================================

channels = {
    "Blue": blue_avg,
    "Green": green_avg,
    "Red": red_avg
}

dominant = max(channels, key=channels.get)

print("\nSummary")
print("-" * 35)
print(f"The {dominant} channel has the highest average intensity.")
print(f"This suggests that {dominant.lower()} is the dominant colour in the dish.")

# ==========================================
# Wait and Close
# ==========================================

cv2.waitKey(0)

cv2.destroyAllWindows()
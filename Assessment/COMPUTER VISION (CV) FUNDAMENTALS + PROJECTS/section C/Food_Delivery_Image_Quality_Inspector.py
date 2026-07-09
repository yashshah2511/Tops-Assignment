import cv2
import numpy as np
import os

# ==========================================
# Global Variables
# ==========================================

image = None
image_path = ""

# ==========================================
# Display Menu
# ==========================================

def show_menu():

    print("\n" + "=" * 55)
    print(" Food Delivery Image Quality Inspector")
    print("=" * 55)

    print("1. Load & Inspect Image")

    print("2. Resize and Analyse Colour Channels")

    print("3. Apply Transformation Pipeline")

    print("4. Run Edge-Based Quality Scan")

    print("5. Exit")
    
    
    
# ==========================================
# Option 1 - Load & Inspect Image
# ==========================================

def load_and_inspect():

    global image
    global image_path

    image_path = input("\nEnter image path: ").strip()

    image = cv2.imread(image_path)

    if image is None:
        print("\nError: Unable to load image.")
        return

    print("\nImage loaded successfully.")

    # Image properties
    height, width, channels = image.shape

    print("\nImage Properties")
    print("-" * 30)
    print(f"Height   : {height}")
    print(f"Width    : {width}")
    print(f"Channels : {channels}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)

    # Save grayscale image
    filename = os.path.splitext(os.path.basename(image_path))[0]

    save_name = filename + "_gray.jpg"

    cv2.imwrite(save_name, gray)

    print(f"\nGrayscale image saved as: {save_name}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()




# ==========================================
# Option 2 - Resize & Analyse Colour Channels
# ==========================================

def resize_and_analyse():

    global image

    if image is None:
        print("\nPlease load an image first (Option 1).")
        return

    # Resize image
    resized = cv2.resize(
        image,
        (256, 256),
        interpolation=cv2.INTER_AREA
    )

    print("\nImage resized to 256 x 256.")

    # Split channels
    blue, green, red = cv2.split(resized)

    # Average intensities
    blue_avg = np.mean(blue)
    green_avg = np.mean(green)
    red_avg = np.mean(red)

    print("\nAverage Pixel Intensities")
    print("-" * 35)
    print(f"Blue  : {blue_avg:.2f}")
    print(f"Green : {green_avg:.2f}")
    print(f"Red   : {red_avg:.2f}")

    # Display images
    cv2.imshow("Resized Image", resized)
    cv2.imshow("Blue Channel", blue)
    cv2.imshow("Green Channel", green)
    cv2.imshow("Red Channel", red)

    cv2.waitKey(0)
    cv2.destroyAllWindows()




# ==========================================
# Option 3 - Transformation Pipeline
# ==========================================

def transformation_pipeline():

    global image

    if image is None:
        print("\nPlease load an image first (Option 1).")
        return

    # Get rotation angle
    angle = float(input("\nEnter rotation angle (degrees): "))

    height, width = image.shape[:2]

    center = (width // 2, height // 2)

    # Rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0
    )

    # Rotate image
    rotated = cv2.warpAffine(
        image,
        rotation_matrix,
        (width, height)
    )

    # ======================================
    # Crop Central 60%
    # ======================================

    crop_width = int(width * 0.60)
    crop_height = int(height * 0.60)

    start_x = (width - crop_width) // 2
    start_y = (height - crop_height) // 2

    cropped = rotated[
        start_y:start_y + crop_height,
        start_x:start_x + crop_width
    ]

    # ======================================
    # Flip Horizontally
    # ======================================

    flipped = cv2.flip(cropped, 1)

    # ======================================
    # Display Results
    # ======================================

    cv2.imshow("Rotated Image", rotated)

    cv2.imshow("Cropped Image", cropped)

    cv2.imshow("Flipped Image", flipped)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

    print("\nTransformation pipeline completed successfully.")




# ==========================================
# Option 4 - Edge-Based Quality Scan
# ==========================================

def edge_quality_scan():

    global image

    if image is None:
        print("\nPlease load an image first (Option 1).")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Canny Edge Detection
    edges = cv2.Canny(
        blurred,
        100,
        200
    )

    # Count edge pixels
    edge_pixels = cv2.countNonZero(edges)

    print("\nEdge Analysis")
    print("-" * 30)
    print(f"Total Edge Pixels : {edge_pixels}")

    # Quality Verdict
    if edge_pixels > 5000:
        verdict = "High texture (good detail)"
    else:
        verdict = "Low texture (may need re-shoot)"

    print(f"Quality Verdict : {verdict}")

    # Display edge image
    cv2.imshow("Edge-Based Quality Scan", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()







# ==========================================
# Main Program
# ==========================================

while True:

    show_menu()

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        load_and_inspect()

    elif choice == "2":
        resize_and_analyse()

    elif choice == "3":
        transformation_pipeline()

    elif choice == "4":
        edge_quality_scan()

    elif choice == "5":

        print("\nThank you for using the system.")

        break

    else:

        print("\nInvalid Choice.")
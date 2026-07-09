import cv2

# ==========================================
# Load Haar Cascade Classifier
# ==========================================

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ==========================================
# Open Webcam
# ==========================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to access the webcam.")
    exit()

print("Webcam started successfully.")
print("Press 'S' to save a snapshot.")
print("Press 'Q' to quit.")

# ==========================================
# Webcam Loop
# ==========================================

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(80, 80)
    )

    # Draw rectangle and text
    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Agent Detected",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # Show webcam
    cv2.imshow("Delivery Agent Verifier", frame)

    key = cv2.waitKey(1) & 0xFF

    # Save snapshot
    if key == ord("s"):

        cv2.imwrite("agent_snapshot.jpg", frame)

        print("Snapshot saved as agent_snapshot.jpg")

    # Quit
    elif key == ord("q"):

        print("Program terminated.")

        break

# ==========================================
# Release Resources
# ==========================================

cap.release()

cv2.destroyAllWindows()
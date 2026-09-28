import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Draw line on webcam feed
    cv2.line(frame, (100, 100), (500, 300), (255, 0, 0), 3)

    # Display webcam feed
    cv2.imshow("Webcam Feed", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()
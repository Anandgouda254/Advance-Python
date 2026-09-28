import cv2

# Read the image
image = cv2.imread("Advance Python A1 Q1.py.png")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Display OpenCV version
print("OpenCV Version:", cv2.__version__)

# Display image information
print("Image Shape:", image.shape)
print("Image Height:", image.shape[0])
print("Image Width:", image.shape[1])
print("Number of Channels:", image.shape[2])

# Resize the image
resized = cv2.resize(image, (500, 400))

# Convert the image to grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)
cv2.imshow("Grayscale Image", gray)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
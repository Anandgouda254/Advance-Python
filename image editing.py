import cv2

# Load image
image = cv2.imread("j.bat.png")

if image is None:
    print("Error: Image not found!")
    exit()

while True:
    print("\n===== IMAGE EDITOR =====")
    print("1. Original Image")
    print("2. Grayscale")
    print("3. Blur")
    print("4. Edge Detection")
    print("5. Rotate 90°")
    print("6. Resize (25%)")
    print("7. Save Current Image")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        edited = image.copy()

    elif choice == 2:
        edited = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    elif choice == 3:
        edited = cv2.GaussianBlur(image, (15, 15), 0)

    elif choice == 4:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edited = cv2.Canny(gray, 100, 200)

    elif choice == 5:
        edited = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    elif choice == 6:
        edited = cv2.resize(image, None, fx=0.5, fy=0.5)

    elif choice == 7:
        cv2.imwrite("edited_image.jpg", edited)
        print("Image saved as edited_image.jpg")
        continue

    elif choice == 8:
        break

    else:
        print("Invalid Choice!")
        continue

    cv2.imshow("Edited Image", edited)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.destroyAllWindows()
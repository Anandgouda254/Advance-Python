
import cv2
import numpy as np

# Create a white image
img = np.ones((500, 700, 3), dtype=np.uint8) * 255

drawing = False
ix, iy = -1, -1

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = img.copy()
            cv2.rectangle(temp, (ix, iy), (x, y), (255, 0, 0), 2)
            cv2.imshow("Draw Rectangle", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
        cv2.imshow("Draw Rectangle", img)

# Create window
cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

while True:
    cv2.imshow("Draw Rectangle", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cv2.destroyAllWindows()

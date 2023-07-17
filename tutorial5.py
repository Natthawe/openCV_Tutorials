import cv2
import numpy as np

cam = cv2.VideoCapture('/dev/video2')

while True:
    success, frame = cam.read()

    width = int(cam.get(3))
    height = int(cam.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 90, 90])
    upper_blue = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Frame", result)
    cv2.imshow("Mask", mask)


    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()   
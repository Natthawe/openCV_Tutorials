import cv2
import numpy as np

cam = cv2.VideoCapture('/dev/video2')

while True:
    success, frame = cam.read()

    width = int(cam.get(3))
    height = int(cam.get(4))

    line = cv2.line(frame, (0,0), (width, height), (255,0,0), 10) # cv2.line(source_image, start_line, end_line, color, thicknesspixel))
    line = cv2.line(line, (0,height), (width, 0), (0,255,0), 10) # cv2.line(source_image, start_line, end_line, color, thickness(pixel))
    line = cv2.rectangle(line, (10,10), (200,150), (0,0,255), -1) #cv2.rectangle(source_image, start_center_position, end_radius_position, color, thickness(-1 to fill))
    line = cv2.circle(line, (320,240), 30, (255,255,255), -1) #cv2.circle(source_image, center_position, radius, color, thickness(-1 to fill))

    font = cv2.FONT_HERSHEY_COMPLEX
    line = cv2.putText(line, 'You are Smart!', (190, height-15), font, 1, (150,100,0), 2, cv2.LINE_AA) # cv2.putText(source_image, 'text', center_position, font, font_size, color, thickness, LINE_TYPE)

    cv2.imshow("Frame", line)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()   
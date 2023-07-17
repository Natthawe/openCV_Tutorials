import cv2
import numpy as np

# cam = cv2.VideoCapture('video/sample.mp4') #for video
cam = cv2.VideoCapture(0) #for webcam #640x480

while True:
    success, frame = cam.read() # ret = working or not, frame = nmupy array of image

    width = int(cam.get(3)) # convert decimal to int, 3 = width 
    height = int(cam.get(4)) # convert decimal to int, 4 = height

    image = np.zeros(frame.shape, np.uint8)

    half_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    image[:height//2, :width//2] = cv2.rotate(half_frame, cv2.ROTATE_180)   #top left
    image[height//2:, :width//2] = half_frame   #bottom left
    image[:height//2, width//2:] = cv2.rotate(half_frame, cv2.ROTATE_180)   #top right
    image[height//2:, width//2:] = half_frame   #bottom right


    cv2.imshow('Video Capture', image)

    if cv2.waitKey(1) == ord('q'): # 1 = 1 millisecond
        break

cam.release()
cv2.destroyAllWindows()    
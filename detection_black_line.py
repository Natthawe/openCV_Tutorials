import cv2
import time
import numpy as np

dispW=1280
dispH=720
fps=0
pos=(0,30)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1
weight=2
myColor=(0,0,255)
# cam = cv2.VideoCapture('/dev/video2')
cam = cv2.VideoCapture(0)


while True:
    tStart = time.time()
    s, frame = cam.read()
    # print(frame.shape)
    # frameGRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.putText(frameGRAY, str(int(fps))+' FPS', pos, font, height, myColor, weight)  
    # print(frameGRAY)
    cv2.putText(frame, str(int(fps)), pos, font, height, myColor, weight)  

    # filter black line
    low_b = np.uint8([100, 100, 100])
    high_b = np.uint8([0, 0, 0])
    mask = cv2.inRange(frame, high_b, low_b)   

    # draw contours around black line
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_NONE)

    # find black line max Area
    if len(contours) > 0:
        # Use the max function to find the largest shape.
        c = max(contours, key=cv2.contourArea)

        # need to find the center of the contour and for this we use the moments methods will get x,y position of the center of the shape.
        M = cv2.moments(c)
        if M["m00"] !=0 :
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("CX : "+str(cx)+"  CY : "+str(cy))

        if cx >= 512:
            print("Turn Right!")

        if 384 <= cx < 512:
            print("Turn a little Right!") 

        if 256 <= cx < 384:
            print("On Track!")                        

        if 180 <= cx < 256:
            print("Turn a little Left!") 

        if cx <= 180:
            print("Turn Left!") 
            
        cv2.circle(frame, (cx,cy), 10, (255,255,255), -1)

    else:
        print("Don't see the line")


    cv2.drawContours(frame, contours, -1, (0, 255, 0), 5)  
    cv2.drawContours(frame, c, -1, (0,0,255), 3)  
    cv2.imshow("MASK", mask)
    cv2.imshow("FRAME", frame)

    if cv2.waitKey(1) == ord('q'):
        break

    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = .9*fps + .1*(1/loopTime)

cam.release()
cv2.destroyAllWindows()

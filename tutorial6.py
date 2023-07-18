import cv2
import numpy as np

img = cv2.imread("assets/aaa.jpg")
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(gray, 100, 0.5, 10)
#print(corners)

#convert corner to int
corners = np.int0(corners)

for corner in corners:
    # print(corners)
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 5, (0,0,255), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corners1 = tuple(corners[i][0])
        corners2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), (np.random.randint(0,255,size=3))))
        cv2.line(img, corners1, corners2, color, 1)

cv2.imshow("Frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

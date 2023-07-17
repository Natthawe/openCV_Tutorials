import cv2

# -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

# Read Image
img = cv2.imread('assets/aaa.jpg', 0)

#Resize
# img = cv2.resize(img, (1280,720))
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#Rotating
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

#Write Image
cv2.imwrite('assets/tutorial1.jpg', img)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
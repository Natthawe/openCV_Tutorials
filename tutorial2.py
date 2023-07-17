import cv2
import random

img = cv2.imread('assets/ocean.jpg', -1) #(427, 640, 3)

# print(img)
# print(img[0]) #first row of image
# print(img[0][0:100]) #pixel at 0-100 of first column of image
# print(img[0][100]) #want to 1 pixel of column

# print(type(img))
# print(img.shape) #(397, 612, 3) is mean (height of image(rows), width of image(column), (channels)color area of image / Pixel)

# loop 100 column 
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]


tag = img[80:180, 360:460] #img[coppy rows(y) desired pixel , coppy column(x) desired pixel]
img[0:100, 0:100] = tag #[rows(y), column(x)]

cv2.imshow('Frame', img)        
cv2.waitKey(0)
cv2.destroyAllWindows()

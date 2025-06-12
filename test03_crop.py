import cv2

image = cv2.imread("data/02.jpeg")

crop = image[10:320, 58:377]

cv2.imshow("crop",crop)

cv2.waitKey()
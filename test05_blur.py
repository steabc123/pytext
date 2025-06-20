import cv2

image = cv2.imread("data/plane.jpg")

gauss = cv2.GaussianBlur(image, (5, 5), 0)  # 高斯滤波
median = cv2.medianBlur(image, 5)   # 中值滤波器

cv2.imshow("image", image)
cv2.imshow("gauss", gauss)
cv2.imshow("median", median)



cv2.waitKey()

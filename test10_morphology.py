import cv2
import numpy as np

gray = cv2.imread("data/opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(gray, 200, 256, cv2.THRESH_BINARY_INV)  # 反向阈值

kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(binary, kernel)   # 利用kernel 腐蚀binary图像
dilation = cv2.dilate(binary, kernel)  # 膨胀,利用相同的内核

cv2.imshow("binary", binary)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.waitKey()

import cv2
import  numpy as np

gray = cv2.imread("data/opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)  # 拉普拉斯算子
canny = cv2.Canny(gray, 100, 200)  # canny算法


cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny",canny)

cv2.waitKey()

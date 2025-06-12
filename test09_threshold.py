import cv2
import numpy as np


gray = cv2.imread("data/bookpage.jpg", cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)  # ret是使用的实际阈值
binary_adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115 ,1)  # 自适应阈值算法
ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # 大津法



cv2.imshow("gray", gray)
cv2.imshow("binary", binary)
cv2.imshow("binary_adaptive", binary_adaptive)
cv2.imshow("binary_otsu", binary_otsu)

cv2.waitKey()

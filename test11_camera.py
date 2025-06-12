import cv2
import numpy as np


capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()  # ret表示是否读取成功，是bool类型
    cv2.imshow("camera", frame)

    key = cv2.waitKey(1)  # 等待键盘输入1ms
    if key != -1:
        break

capture.release()  # 释放capture指针

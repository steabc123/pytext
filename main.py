import cv2
import numpy

print(cv2.getVersionString())

image = cv2.imread("data/bus.jpg")
h, w, _ = image.shape

print(image.shape)
#image1 = cv2.resize(image,(w*0.5,h*0.5), interpolation=cv2.INTER_NEAREST)
image1 = cv2.resize(image,dsize=(w,h), dst=None, fx=0, fy=0, interpolation=cv2.INTER_NEAREST)


cv2.imshow("image1",image1)
cv2.waitKey(0)
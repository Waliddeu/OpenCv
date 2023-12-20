import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Reading Images
img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)

# # This reads colours as RGB
# plt.imshow(img)
# plt.show()

# BGR to grascale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Gray', hsv)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('RGB', lab)

# HSV to BGR
gray2bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
hsv2bgr = cv.cvtColor(gray2bgr, cv.COLOR_BGR2HSV)
cv.imshow('GRAY2HSV', hsv2bgr)

cv.waitKey(0)
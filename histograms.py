import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Reading Images
img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 100, img.shape[0]//2), 250, 255, -1)
# cv.imshow('Mask', mask)

# # masked = cv.bitwise_and(img, img, mask=mask)
# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Masked Image', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

# # Gray Histogram
# gray_hist = cv.calcHist([gray],[0], mask, [256], [0,256])

# plt.figure()
# plt.title('Gray Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# if pixels')
# plt.xlim([0,256])
# plt.plot(gray_hist)
# plt.show()
plt.figure()
plt.title('Colour Histogram')

colors = ('b','r','g')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)


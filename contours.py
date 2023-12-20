import cv2 as cv
import numpy as np

# Reading Images

img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)


# Converting an image in grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayCat', gray)

# Bluring the image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade 
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny', canny)

# Threshold (Binarising an image) balck & white
ret, thresh = cv.threshold(gray, 125, 255 , cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Contouring is finding the boundering of the picture, better to use it with canny instead of Thresh. 
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} conttour(s) found!')

# Drawing in the blank image created above. 
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)

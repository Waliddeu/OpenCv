import cv2 as cv

# Reading Images
img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Threshold (Binarising an image) balck & white
# threshold, thresh = cv.threshold(gray, 125, 255 , cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# # Threshold (Binarising an image) balck & white (INVERSE)
# threshold, thresh_inv = cv.threshold(gray, 125, 255 , cv.THRESH_BINARY_INV)
# cv.imshow('Thresh', thresh_inv)

adaptive_thresholding = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,5)
cv.imshow('Thresh', adaptive_thresholding)


cv.waitKey(0)
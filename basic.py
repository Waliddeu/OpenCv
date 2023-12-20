import cv2 as cv

# Reading Images
img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)

# Converting an image in grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayCat', gray)

# Blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade 
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding the image
eroded = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize the image
resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

# Cropp the image
cropped = img[50:690,500:1100]
cv.imshow('Resized', cropped)

cv.waitKey()

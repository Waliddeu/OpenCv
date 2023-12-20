import cv2 as cv
import numpy as np

# Reading Images

img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)
blank = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('BLUE', blue)
cv.imshow('GREEN', green)
cv.imshow('RED', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)


cv.waitKey(0)
import cv2 as cv
import numpy as np

# Reading Images
img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)

# Translating
def translate(img, x,y): 
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (height/2, width/2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat,dimensions)

rotated = rotate(img, 45, None)
cv.imshow('Rotated', rotated)







cv.waitKey(0)

import cv2 as cv
import numpy as np

# Initializing the blank window
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1.paint the image in a certain colour
blank[100:300, 300:400] = 31,3,98
cv.imshow('Red', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (255,0,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (255,0,0), thickness=-1)
cv.imshow('Circle', blank)

# 3. Draw a line
cv.line(blank, (0,0), (blank.shape[1],blank.shape[0]), (255,0,0), thickness=3)
cv.imshow('Line', blank)

# Write a text on an image
cv.putText(blank, 'Walid', (225,225), cv.FONT_HERSHEY_DUPLEX, 1.0, (255,255,255) , 2)
cv.imshow('Text', blank)

cv.waitKey(0)
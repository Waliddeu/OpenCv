import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/person.png')
# cv.imshow('Person', img)

# img_resized = rescaleFrame(img)
# cv.imshow('Person-resized', img_resized)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
print(f'number of faces found is = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('face_detected', img) 

cv.waitKey(0)
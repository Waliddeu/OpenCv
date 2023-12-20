import cv2 as cv

# Rescale a Video

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

# Change resolution for live videos

def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)    
# Reading Images

img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)
img_resized = rescaleFrame(img)
cv.imshow('Cat-resized', img_resized)

# Reading Videos

capture = cv.VideoCapture('dog-video.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Video', frame)
#     cv.imshow('Video-resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
    
# capture.release()
# cv.destryAllWindows()

cv.waitKey(0)

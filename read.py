import cv2 as cv

# Reading Images

img = cv.imread('Photos/cat-large.png')
cv.imshow('Cat', img)

# Reading Videos

capture = cv.VideoCapture('dog-video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destryAllWindows()
cv.waitKey(0)




    
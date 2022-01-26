import cv2 as cv
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
# import RPi.GPIO as GPIO
import time

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')
print('Loaded xml files')

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCap = PiRGBArray(camera, size=(640, 480))

time.sleep(0.2)

for frame in camera.capture_continuous(rawCap, format='bgr', use_video_port=True):
    image = frame.array
    cv.imshow('frame', image)
    key = cv.waitKey(1) & 0xFF
    
    rawCap.truncate(0)
    
    if key == ord('q'):
        break

# cap = cv.VideoCapture(cv.CAP_V4L2)  try 0 or -1 for camera
print('Capture object created')
while True:
#     ret, frame = cap.read()
    camera.capture(rawCap, format='bgr')
    image = rawCap.array
    try:
        None
    except cv.error:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print(faces, len(faces))
    if len(faces) != 0:
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(gray, 1.8, minNeighbors=20)
            for (sx, sy, sw, sh) in smiles:
                cv.rectangle(frame, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    cv.line(image, (320, 260), (320, 220), (0, 255, 0), 2)
    cv.line(image, (300, 240), (340, 240), (0, 255, 0), 2)
    cv.imshow('POGGERS', image)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

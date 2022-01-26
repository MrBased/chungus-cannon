import cv2 as cv
import numpy as np
import RPi.GPIO as GPIO
import time

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')
print('Loaded xml files')

# servoPIN = 17
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servoPIN, GPIO.OUT)
# p = GPIO.PWM(servoPIN, 50)
# p.start(5)

cap = cv.VideoCapture(cv.CAP_V4L2)  # try 0 or -1 for camera
print('Capture object created')
while True:
    ret, frame = cap.read()
#     print('Read frame')
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
    cv.line(frame, (320, 260), (320, 220), (0, 255, 0), 2)
    cv.line(frame, (300, 240), (340, 240), (0, 255, 0), 2)
    cv.imshow('POGGERS', frame)
#     print(frame.shape)
    if cv.waitKey(1) == ord('q'):
        break
# p.stop()
# GPIO.cleanup()
cap.release()
cv.destroyAllWindows()

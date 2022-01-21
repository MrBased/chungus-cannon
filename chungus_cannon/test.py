import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

cap = cv.VideoCapture(0)  # try 0 or -1 for camera
while True:
    ret, frame = cap.read()
    try:
        None
    except cv.error:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(gray, 1.8, minNeighbors=20)
        for (sx, sy, sw, sh) in smiles:
            cv.rectangle(frame, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    cv.imshow('POGGERS', frame)
    print(frame.shape)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

import cv2 as cv
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
servo_x = GPIO.PWM(11, 50)
current_cycle = 0
servo_x.start(current_cycle)


face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')
print('Loaded xml files')

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCap = PiRGBArray(camera, size=(640, 480))
center = (320, 240)

time.sleep(0.2)
try:
    for frame in camera.capture_continuous(rawCap, format='bgr', use_video_port=True):
        image = frame.array
        
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) != 0:
            for (x, y, w, h) in faces:
                cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.line(image, (int(x + w / 2), y + h), (int(x + w / 2), y), (0, 255, 0), 1)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = image[y:y + h, x:x + w]
                target_coord = (int(x + w / 2), int(y + h / 2))
                smiles = smile_cascade.detectMultiScale(gray, 1.8, minNeighbors=20)
                
                if len(smiles) == 0:
                    if target_coord[0] < center[0] - 10 and not current_cycle == 12:
                        current_cycle += 0.5
                        servo_x.ChangeDutyCycle(current_cycle)
                        time.sleep(0.05)
                        servo_x.ChangeDutyCycle(0)
                    if target_coord[0] > center[0] + 10 and not current_cycle == 0:
                        current_cycle -= 0.5
                        servo_x.ChangeDutyCycle(current_cycle)
                        time.sleep(0.05)
                        servo_x.ChangeDutyCycle(0)
                else:
                    for (sx, sy, sw, sh) in smiles:
                        cv.rectangle(image, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
        cv.line(image, (320, 260), (320, 220), (0, 255, 0), 1)
        cv.line(image, (300, 240), (340, 240), (0, 255, 0), 1)
        
        
        
        cv.imshow('frame', image)
        key = cv.waitKey(1) & 0xFF
        
        rawCap.truncate(0) # clears stream

        if key == ord('q'):
            break
finally:
    cv.destroyAllWindows()
    servo_x.stop()
    GPIO.cleanup()
    print('Clean')

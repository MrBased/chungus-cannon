import cv2 as cv
import numpy as np
# from fer import FER


class ChungusCannon:

    def __init__(self):
        print('Chungus Cannon online')
        self.cap = cv.VideoCapture(cv.CAP_V4L2)  # res: (640, 480), center: (320, 240)
        # self.emotion_detector = FER()
        # self.camera_init()

    def camera_init(self):
        while True:
            _, frame = self.cap.read()
            try:
                None
            except cv.error:
                print('Could not read frame')
                break
#             emos = self.emotion_detector.detect_emotions(frame)
#             top_emo = self.emotion_detector.top_emotion(frame)
#             print(top_emo, frame.shape)
#             self.draw_face_box(frame, emos)
            self.draw_crosshair(frame)
            cv.imshow('Eye of the Chungus', frame)
            print('HOLA')
            if cv.waitKey(1) == ord('q'):
                self.terminate()

#     def draw_face_box(self, input_image, result):
#         try:
#             bounding_box = result[0]["box"]
#             cv.rectangle(input_image, (
#               bounding_box[0], bounding_box[1]), (
#               bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
#                 (0, 0, 255), 2,)
#             cv.circle(input_image,
#                       (int(bounding_box[0] + bounding_box[2] / 2),
#                        int(bounding_box[1] + bounding_box[3] / 2)), 15,
#                       (0, 0, 255), 2)
#         except IndexError:
#             None


    def draw_crosshair(self, input_image):
        cv.line(input_image, (320, 260), (320, 220), (0, 255, 0), 2)
        cv.line(input_image, (300, 240), (340, 240), (0, 255, 0), 2)

    def terminate(self):
        self.cap.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    # obs = ChungusCannon()
    cap = cv.VideoCapture(-1)
    while True:
        _, frame = cap.read()
        try:
            None
        except cv.error:
            print('Could not read frame')
            break
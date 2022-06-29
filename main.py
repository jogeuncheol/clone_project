"""
create: 2022-06-25
edit:   2022-06-26
author: github.com/jogeuncheol
"""

import mediapipe as mp
import cv2

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


# For static images:
def static_images():
    IMAGE_FILES = ['image/01.jpg', 'image/02.jpg']
    with mp_face_detection.FaceDetection(
            model_selection=1,
            min_detection_confidence=0.5
    ) as face_detection:
        for idx, file in enumerate(IMAGE_FILES):
            image = cv2.imread(file)
            # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
            results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Draw face detections of each face.
            if not results.detections:
                continue
            annotated_image = image.copy()
            for detection in results.detections:
                print('Nose tip:')
                print(mp_face_detection.get_key_point(
                    detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
                mp_drawing.draw_detection(annotated_image, detection)
            # cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
            cv2.imshow('image', annotated_image)
            cv2.waitKey(0)


def web_cam():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("web cam is not ready")
        return -1
    while True:
        read_return, image = cam.read()
        if not read_return:
            break
        with mp_face_detection.FaceDetection(
                model_selection=1,
                min_detection_confidence=0.5
        ) as face_detection:
            # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
            results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Draw face detections of each face.
            if not results.detections:
                continue
            annotated_image = image.copy()
            for detection in results.detections:
                print('Nose tip:')
                print(mp_face_detection.get_key_point(
                    detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
                mp_drawing.draw_detection(annotated_image, detection)
            # cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
            cv2.imshow('image', annotated_image)
            # cv2.waitKey(0)
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cam.release()


def set_roi():
    pass


def flow_face():
    pass


def main():
    # static_images()
    web_cam()
    return 0


if __name__ == '__main__':
    main()

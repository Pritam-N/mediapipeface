import cv2
import mediapipe as mp

class FaceDetector():
    def __init__(self) -> None:
        self.mpfacedetect = mp.solutions.face_detection
        self.mpdraw = mp.solutions.drawing_utils
        self.drawspec = self.mpdraw.DrawingSpec(thickness=1, circle_radius=1)

    def faceDetect(self, img):
        with self.mpfacedetect.FaceDetection(
            min_detection_confidence=0.5) as fd:
            self.imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            self.results = fd.process(self.imgrgb)

            if self.results.detections:
                annotated_image = img.copy()
                for detection in self.results.detections:
                    self.mpdraw.draw_detection(annotated_image, detection)
                    return annotated_image

            return img


def main(path='PATHTOVIDEO', iswebcam=0):
    if iswebcam:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(path)

    detector = FaceDetector()
    while cap.isOpened():
        success, img = cap.read()
        
        if not success:
            if iswebcam:
                continue
            break

        annoted = detector.faceDetect(img)

        cv2.imshow("Image", annoted)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
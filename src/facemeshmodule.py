import mediapipe as mp
import cv2

class FaceMeshDetector:
    def __init__(self,
                staticmode = False, 
                max_num_faces=2, 
                mindetectioconfidence=0.5,
                mintrackconfidence=0.5) -> None:
        self.staticmode = staticmode
        self.max_num_faces = max_num_faces
        self.mindetectioconfidence = mindetectioconfidence
        self.mintrackconfidence = mintrackconfidence

        self.mpdraw = mp.solutions.drawing_utils

        self.mpfacemesh = mp.solutions.face_mesh
        self.facemesh = self.mpfacemesh.FaceMesh(self.staticmode, 
                                                self.max_num_faces, 
                                                self.mindetectioconfidence,
                                                self.mintrackconfidence)
        self.drawspec = self.mpdraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):
        self.imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.facemesh.process(self.imgrgb)
        faces = []

        if self.result.multi_face_landmarks:
            
            for facelandmarks in self.result.multi_face_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img, facelandmarks, self.mpfacemesh.FACE_CONNECTIONS, 
                                    self.drawspec, self.drawspec)
                
                face = []
                for lm in facelandmarks.landmark:
                    ih, iw, ic = img.shape
                    x,y = int(lm.x*iw), int(lm.y*ih)
                    face.append([x,y])

                faces.append(face)
        return img, faces

def main(path='PATHTOVIDEO', iswebcam=0):
    if iswebcam:
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(path)

    detector = FaceMeshDetector()
    while cap.isOpened():
        success, img = cap.read()

        if not success:
            if iswebcam:
                continue
            break

        img, faces = detector.findFaceMesh(img)

        cv2.imshow("Image", img)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
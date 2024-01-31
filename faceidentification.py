import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from insightface.app import FaceAnalysis
from create_face_bank import CreatFaceBank


class FaceIdentification():
    def __init__(self):
        self.model = None
        self.input = None
        self.results = None
        self.face_bank = None

    def load_model(self):
        self.model = FaceAnalysis(providers=["CPUExecutionProvider"], name="buffalo_s")
        self.model.prepare(ctx_id=0, det_size=(640, 640))

    def load_image(self, img_path):
        self.input = cv2.imread(img_path)
        self.input = cv2.cvtColor(self.input, cv2.COLOR_BGR2RGB)

    def load_face_bank(self):
        self.results = self.model.get(self.input)
        self.face_bank = np.load("face_bank.npy", allow_pickle=True)

    def face_identifier(self):
        threshold = 25
        for result in self.results:
            cv2.rectangle(self.input, (int(result.bbox[0]), int(result.bbox[1])), (int(result.bbox[2]), int(result.bbox[3])), (0, 0, 255), 1)

            for person in self.face_bank:
                face_bank_person_embedding = person["embedding"]
                new_person_embedding = result["embedding"]

                dist = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding)**2))
        
                if dist<threshold:
                    cv2.putText(self.input, person["name"], (int(result.bbox[0]), int(result.bbox[1] - 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1, cv2.LINE_AA)
                    break

            else:
                cv2.putText(self.input, "Unknown", (int(result.bbox[0]), int(result.bbox[1] - 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1, cv2.LINE_AA)

        plt.imshow(self.input)
        plt.show()
import os
import cv2
import numpy as np
from insightface.app import FaceAnalysis


class CreatFaceBank():
    def __init__(self):
        self.model = None
        self.face_bank_path = None

    def creation_model(self):
        self.model = FaceAnalysis(providers=["CPUExecutionProvider"], name="buffalo_s")
        self.model.prepare(ctx_id=0, det_size=(640, 640))

    def creation_facebank(self):
        self.face_bank_path = "./face_bank/"
        face_bank = []

        for person_name in os.listdir(self.face_bank_path):
            file_path = os.path.join(self.face_bank_path, person_name)
            if os.path.isdir(file_path):
                for image_name in os.listdir(file_path):
                    if image_name != ".DS_Store":
                        image_path = os.path.join(file_path, image_name)
                        print(image_path)
                        image = cv2.imread(image_path)
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                        result = self.model.get(image)

                        if len(result)>1:
                            print("Warning: There are more than one person in this image!!")
                            continue

                        # print(len(result))

                        embedding = result[0]["embedding"]
                        my_dict = {"name": person_name, "embedding": embedding}
                        face_bank.append(my_dict)


        np.save("face_bank.npy", face_bank)

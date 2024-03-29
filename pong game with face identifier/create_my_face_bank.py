import os
import cv2
import numpy as np
from insightface.app import FaceAnalysis

app = FaceAnalysis(providers=["CPUExecutionProvider"], name="buffalo_s")
app.prepare(ctx_id=0, det_size=(640, 640))

my_face_bank_path = "pong game with face identifier/my_face_bank"
my_face_bank = []

for person_name in os.listdir(my_face_bank_path):
    file_path = os.path.join(my_face_bank_path, person_name)
    if os.path.isdir(file_path):
        for image_name in os.listdir(file_path):
            if image_name != ".DS_Store":
                image_path = os.path.join(file_path, image_name)
                print(image_path)
                image = cv2.imread(image_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                result = app.get(image)

                if len(result)>1:
                    print("Warning: There are more than one person in this image!!")
                    continue

                    # print(len(result))

                    embedding = result[0]["embedding"]
                    my_dict = {"name": person_name, "embedding": embedding}
                    my_face_bank.append(my_dict)


np.save("pong game with face identifier/my_face_bank.npy", my_face_bank)
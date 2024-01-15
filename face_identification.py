import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
from insightface.app import FaceAnalysis

parser = argparse.ArgumentParser()
parser.add_argument("--image", type=str, help="Path of the inferential image")

arg = parser.parse_args()

img_path = arg.image

face_bank = np.load("face_bank.npy", allow_pickle=True )

app = FaceAnalysis(providers=["CPUExecutionProvider"], name="buffalo_s")
app.prepare(ctx_id=0, det_size=(640, 640))

#input = cv2.imread(img_path)
input = cv2.imread("Inputs/a2.jpg")
input = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)

results = app.get(input)
print(len(results))

threshold = 25

for result in results:
    cv2.rectangle(input, (int(result.bbox[0]), int(result.bbox[1])), (int(result.bbox[2]), int(result.bbox[3])), (0, 255, 0), 2)

    for person in face_bank:
        face_bank_person_embedding = person["embedding"]
        new_person_embedding = result["embedding"]

        dist = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding)**2))
        
        if dist<threshold:
            cv2.putText(input, person["name"], (int(result.bbox[0]), int(result.bbox[1] - 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1, cv2.LINE_AA)
            break

    else:
        cv2.putText(input, "Unknown", (int(result.bbox[0]), int(result.bbox[1] - 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1, cv2.LINE_AA)

plt.imshow(input)
plt.show()
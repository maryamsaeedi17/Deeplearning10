import cv2
import numpy as np
import argparse
from insightface.app import FaceAnalysis

parser = argparse.ArgumentParser()
parser.add_argument("--image1", type=str)
parser.add_argument("--image2", type=str)

args = parser.parse_args()

img1_path = args.image1
img2_path = args.image2

app = FaceAnalysis(providers=["CPUExecutionProvider"], name="buffalo_s")
app.prepare(ctx_id=0, det_size=(640, 640))

img1 = cv2.imread(img1_path)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

result1 = app.get(img1)
embedding1 = result1[0]["embedding"]


img2 = cv2.imread(img2_path)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

result2 = app.get(img2)
embedding2 = result2[0]["embedding"]

dist = np.sqrt(np.sum((embedding1 - embedding2)**2))

if dist<22:
    print("Same Person")
else:
    print("Diffrent Persons")

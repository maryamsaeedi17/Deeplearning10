import cv2
import arcade
import numpy as np
from insightface.app import FaceAnalysis
from ponggame import Game

app = FaceAnalysis(providers=["CPUExecutionProvider"], name="buffalo_s")
app.prepare(ctx_id=0, det_size=(640, 640))

my_face_bank = np.load("my_face_bank.npy", allow_pickle=True)

cap = cv2.VideoCapture(0)
_, frame = cap.read()

rows = frame.shape[0]
cols = frame.shape[1]

while True:
    _, input_image = cap.read()
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    input_image = cv2.cvtColor(input_image, cv2.COLOR_HSV2BGR)
    results = app.get(input_image)

    threshold = 25

    for result in results:
        cv2.rectangle(input_image, (int(result.bbox[0]), int(result.bbox[1])), (int(result.bbox[2]), int(result.bbox[3])), (0, 0, 255), 1)

        for person in my_face_bank:
            face_bank_person_embedding = person["embedding"]
            new_person_embedding = result["embedding"]

            distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding) **2))
            if distance<threshold:
                cv2.putText(input_image, person["name"], (int(result.bbox[0]), int(result.bbox[1]) - 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.4, (0, 255, 0), 1, cv2.LINE_AA)
                print("Welcome!!")
                game = Game()
                arcade.run()
                break
        else:
            cv2.putText(input_image,"Unknown", (int(result.bbox[0]), int(result.bbox[1]) - 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.4, (255, 0, 0), 1, cv2.LINE_AA)
            print("Sorry! It is forbidden for you..")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cap.release()
cv2.destroyAllWindows()
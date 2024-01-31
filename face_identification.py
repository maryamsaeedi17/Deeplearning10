import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
from insightface.app import FaceAnalysis
from create_face_bank import CreatFaceBank
from faceidentification import FaceIdentification

parser = argparse.ArgumentParser()
parser.add_argument("--image", type=str, help="Path of the inferential image")
parser.add_argument('--update', type=str, help='Directory involved new images')

args = parser.parse_args()

img_path = args.image

if args.update:
    CreatFaceBank.creation_facebank()

FaceIdentifier = FaceIdentification()

FaceIdentifier.load_model()
FaceIdentifier.load_image(img_path)
FaceIdentifier.load_face_bank()
FaceIdentifier.face_identifier()
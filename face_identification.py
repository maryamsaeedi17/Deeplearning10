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


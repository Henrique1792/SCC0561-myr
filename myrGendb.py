import random
import numpy as np
import sys
import pickle
import cv2
import os

from myrAnalyse import extractDescriptors

def generateDict():
    content = []
    bagOFeatures = []
    db_names = os.listdir("db")
    images = []

    for i in range(0, 10):
        images.append(random.choice(db_names))

    for reference in images:
        content.append([reference, 1.0])
        _, descriptor = extractDescriptors(reference)
        bagOFeatures = bagOFeatures + list(descriptor)

    bagOFeatures = np.float32(bagOFeatures)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 1.0)

    ret, label, center = cv2.kmeans(bagOFeatures, 10, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    pickle.dump(center,open("dict.pkl", "wb"))

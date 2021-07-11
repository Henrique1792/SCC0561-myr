import random
import numpy as np
import pickle
import cv2
import os

# get descriptor from img `imgName`
def extractDescriptors(imgName):
    # load imgName
    img = cv2.imread('db/'+imgName)
    if img is None:
        print('db/'+imgName+'not Found!')
        return []

    # convert img to grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ORB extrator
    orb = cv2.ORB_create()
    kp, des = orb.detectAndCompute(grayscale, None)

    return kp, des

def genHistogram(img):
    inImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hist = cv2.calcHist(inImg, [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

def generateDict():
    content = []
    bagOFeatures = []
    db_names = os.listdir("dict")
    images = []

    for image in db_names:
        images.append(image)

    for reference in images:
        content.append([reference, 1.0])
        _, descriptor = extractDescriptors(reference)
        bagOFeatures = bagOFeatures + list(descriptor)

    bagOFeatures = np.float32(bagOFeatures)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 1.0)
    ret, label, center = cv2.kmeans(bagOFeatures, 10, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    pickle.dump(center,open("dict.pkl", "wb"))

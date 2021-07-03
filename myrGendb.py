import random
import numpy as np
import sys
import os

from myrAnalyse import extractDescriptors



def generateDict():
    content = []
    bagOFeatures = []
    db_names = os.listdir("db")

    for i in range(0, 10):
        reference = random.choice(db_names)
        content.append([reference, 1.0])
        descriptor = extractDescriptors(reference[0])
        bagOFeatures = bagOFeatures + descriptor.tolist()

    bagOFeatures = np.float32(bagOFeatures)
    criteria = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 1.0)

    ret, label, center = cv2.kmeans(bagOFeatures, 10, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Here we need to do YAML dump of data
    #for elements in reference:
    #    with open('dict.txt', 'w') as dictFile:
    #        print(content, file=dictFile)


    #dbFile.close()

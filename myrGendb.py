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
        descriptor = extractDescriptors(reference)

    for elements in reference:
        print(content, file=dbFile)

    dbFile = open('db.txt', "w")

    dbFile.close()

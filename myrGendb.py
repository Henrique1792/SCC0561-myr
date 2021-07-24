import random
import numpy as np
import pickle
import cv2
import os
import pylab as pl
import joblib


from scipy.cluster.vq import vq, kmeans
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score

#get imglist from path
def imglist(path):
    return [os.path.join(path, f) for f in os.listdir(path)]

# get descriptor from img `imgName`
def extract_characteristcs(imgName):
    # load imgName
    img = cv2.imread(imgName)
    if img is None:
        print(imgName+'not Found!')
        return []

    # convert img to grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ORB extraction
    orb = cv2.ORB_create(50)
    kp, des = orb.detectAndCompute(grayscale, None)

    return kp, des

# generate dict using db/dict/class folders
def generateDict():
    dict_path = "db/dict"
    dict_names = os.listdir(dict_path)
    bagOFeatures = []
    images = []
    image_paths = []
    image_classes = []
    dict_descriptors = []
    class_id = 0
    k = 200

    for dict_name in dict_names:
        dir = os.path.join(dict_path, dict_name)
        class_path = imglist(dir)
        image_paths+=class_path
        image_classes+=[class_id]*len(class_path)
        class_id+=1

    for image_path in image_paths:
        print(image_path)
        _, descriptor = extract_characteristcs(image_path)
        dict_descriptors.append((image_path, descriptor))

    stack_descriptors = dict_descriptors[0][1]

    for image_path, descriptor in dict_descriptors[1:]:
        stack_descriptors = np.vstack((stack_descriptors, descriptor))

    descriptors_float = stack_descriptors.astype(float)

    voc, variance = kmeans(descriptors_float, k, 1)

    features = np.zeros((len(image_paths),k), "float32")

    for i in range(len(image_paths)):
        words, distance = vq (dict_descriptors[i][1], voc)
        for w in words:
            features[i][w] += 1

    # normalization
    nbr_occurences = np.sum( (features > 0) * 1, axis = 0)
    idf = np.array(np.log((1.0*len(image_paths)+1) / (1.0*nbr_occurences + 1)), 'float32')

    stdSlr = StandardScaler().fit(features)
    features = stdSlr.transform(features)
 
    clf = LinearSVC(max_iter=10000)  #Default of 100 is not converging
    clf.fit(features, np.array(image_classes))
 
    joblib.dump((clf, dict_names, stdSlr, k, voc), "bovw_myr.pkl", compress=3)


# classify imgs under db/test/class folders
def myr_classify():

    clf, classes_names, stdSlr, k, voc = joblib.load("bovw_myr.pkl")
    test_path = 'db/test'

    testing_names = os.listdir(test_path)

    image_paths = []
    image_classes = []
    class_id = 0
    test_descriptors = []

    for testing_name in testing_names:
        dir = os.path.join(test_path, testing_name)
        class_path = imglist(dir)
        image_paths+=class_path
        image_classes+=[class_id]*len(class_path)
        class_id+=1

    for image_path in image_paths:
        _, descriptor = extract_characteristcs(image_path)
        test_descriptors.append((image_path, descriptor))

    # Stack all the descriptors vertically in a numpy array
    descriptors = test_descriptors[0][1]
    for image_path, descriptor in test_descriptors[0:]:
        descriptors = np.vstack((descriptors, descriptor))

    test_features = np.zeros((len(image_paths), k), "float32")
    for i in range(len(image_paths)):
        words, distance = vq(test_descriptors[i][1],voc)
        for w in words:
            test_features[i][w] += 1

    nbr_occurences = np.sum( (test_features > 0) * 1, axis = 0)
    idf = np.array(np.log((1.0*len(image_paths)+1) / (1.0*nbr_occurences + 1)), 'float32')

    test_features = stdSlr.transform(test_features)


    true_class =  [classes_names[i] for i in image_classes]
    predictions =  [classes_names[i] for i in clf.predict(test_features)]


    print ("true_class ="  + str(true_class))
    print ("prediction ="  + str(predictions))
    # needs to change to F1

    accuracy = accuracy_score(true_class, predictions)
    print ("accuracy = ", accuracy)
    cm = confusion_matrix(true_class, predictions)

    precision = (cm[0][0])/(cm[0][1]+cm[0][0])
    recall = (cm[0][0])/(cm[1][0]+cm[0][0])
    print("precision: ", precision)
    print("recall: ", recall)
    F1 = precision*recall
    aux = precision+recall
    F1 = F1 / aux
    print("F1 score: ",F1 )
    print(cm)
    showconfusionmatrix(cm)

def showconfusionmatrix(cm):
    pl.matshow(cm)
    pl.title('Confusion matrix')
    pl.colorbar()
    pl.show()
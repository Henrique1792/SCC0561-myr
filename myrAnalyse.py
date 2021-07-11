import cv2
import pickle
from scipy.spatial import distance as dist



from myrGendb import genHistogram, extractDescriptors
from myrPlot import showResults


# Chebyshev distance
def myrDistance(img1, img2):
    return dist.chebyshev(img1, img2)


def analyzeImg(imgName):
    # Load img input
    img = cv2.imread(imgName)

    # convert it to grayscale
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # generate SIFT extractor
    sift = cv2.xfeatures2d.SIFT_create()

    # generate img's globally keypoints
    keypoints, descriptors = sift.detectAndCompute(grayscale, None)

    # Draw each keypoint as circles at grayscale img
    out_img = cv2.drawKeypoints(grayscale, keypoints, img)

    #img2 = cv2.imread('pontos_chave_SIFT.jpg')
    cv2.imshow("Pontos-chave", out_img)
    k = cv2.waitKey(0)

    # Salva a img com os pontos-chave como 'pontos_chave_SIFT.jpg
    cv2.imwrite('pontos_chave_SIFT.jpg',out_img)


def compareBOVWDictHistograms(inputImg):
    dictHistograms = []
    #first, load dict
    with open("dict.pkl", "rb") as BOWD:
        bovw = pickle.load(BOWD)
        for content in bovw:
            dictHistograms.append(genHistogram(content))

    #Analyse img histogram
        _, inputImgD = extractDescriptors(inputImg)
        inputImgH = genHistogram(inputImgD)

        results = []
        for i in range(len(dictHistograms)):
            distance = myrDistance(inputImgH, dictHistograms[i])
            results.append([inputImgH, distance])
        showResults(inputImg, results)

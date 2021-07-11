import matplotlib.pyplot as plt
import cv2
import os


def showResults(imgName, results):
    fig = plt.figure("source: "+imgName)
    ax = fig.add_subplot(1,1,1)
    img = cv2.imread('db/'+imgName)
    ax.imshow(img)
    plt.axis("off")

    db_names = os.listdir("dict")

    # initialize the results figure
    fig = plt.figure("Results")
    fig.suptitle("Chebyshev distance", fontsize = 20)
    # loop over the results
    for (i, (k, v)) in (enumerate(results)):
        # show the result
        ax = fig.add_subplot(2, 5, i+1)
        ax.set_title("%d: %.2f" % (i, v))
        dct_img = cv2.imread('dict/'+db_names[i])
        dct_img = cv2.cvtColor(dct_img, cv2.COLOR_BGR2RGB)
        plt.imshow(dct_img)
        plt.axis("off")

    plt.show()

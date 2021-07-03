import cv2


def extractDescriptors(imgName):
    # Carrega a img de entrada
    img = cv2.imread('db/'+imgName)
    if img is None:
        print('db/'+imgName+'not Found!')
        return []

    # Converte a img para a escala de cinza
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ORB extrator
    orb = cv2.ORB_create()
    kp, des = orb.detectAndCompute(grayscale, None)

    return kp, des



def analyzeImg(imgName):
    # Carrega a img de entrada
    img = cv2.imread(imgName)

    # Converte a img para a escala de cinza
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Cria o extrator de caracteristicas SIFT
    sift = cv2.xfeatures2d.SIFT_create()

    # Detecta os pontos-chave da img globalmente
    keypoints, descriptors = sift.detectAndCompute(grayscale, None)

    # Desenha os pontos-chave como circulos na img 'grayscale' 
    out_img = cv2.drawKeypoints(grayscale, keypoints, img)

    #img2 = cv2.imread('pontos_chave_SIFT.jpg')
    cv2.imshow("Pontos-chave", out_img)
    k = cv2.waitKey(0)

    # Salva a img com os pontos-chave como 'pontos_chave_SIFT.jpg
    cv2.imwrite('pontos_chave_SIFT.jpg',out_img)


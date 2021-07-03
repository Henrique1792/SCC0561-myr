import cv2


def extractDescriptors():



def analyzeImg(imgName):
    # Carrega a imagem de entrada
    imagem = cv2.imread(imgName)

    # Converte a imagem para a escala de cinza
    escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Cria o extrator de caracteristicas SIFT
    sift = cv2.xfeatures2d.SIFT_create()

    # Detecta os pontos-chave da imagem globalmente
    keypoints, descritores = sift.detectAndCompute(escala_cinza, None)

    # Desenha os pontos-chave como circulos na imagem 'escala_cinza' 
    imagem_saida = cv2.drawKeypoints(escala_cinza, keypoints, imagem)

    #imagem2 = cv2.imread('pontos_chave_SIFT.jpg')
    cv2.imshow("Pontos-chave", imagem_saida)
    k = cv2.waitKey(0)

    # Salva a imagem com os pontos-chave como 'pontos_chave_SIFT.jpg
    cv2.imwrite('pontos_chave_SIFT.jpg',imagem_saida)


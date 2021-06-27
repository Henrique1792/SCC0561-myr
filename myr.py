import numpy as np
import cv2
import sys

#
# SCC0561 - MIR implementation
# author: Henrique F. M. Freitas
#


def generateDict():
        print("1")

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



def main():

    if len(sys.argv) < 2:
        print("insuficient nargs\n")
        print("usage: python3 myr.py <genDict||analysis> [tgtImg]")
        sys.exit()

    # defining which operation you're executing
    if sys.argv[1] == "genDict":
        generateDict()

    else:
        if sys.argv[1] == "analysis":
            analyzeImg(sys.argv[2])
        else:
            print("option not found")

main()

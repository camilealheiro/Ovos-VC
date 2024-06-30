import cv2
import numpy as np
import os

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480
framesize = IMAGE_WIDTH * IMAGE_HEIGHT

# Número do ovo
name = 533

# Número de elementos na pasta
for image in range(65):
    # Leitura da pasta desejada
    imagedata = cv2.imread(f'teste\ovo{name}.png', cv2.IMREAD_ANYDEPTH)
    
    #Normalização realizada
    norm = cv2.normalize(imagedata, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    norm *= 10000
    norm_final = norm.astype(np.uint16)

    #Escrita final das imagens
    cv2.imwrite(f"ovo{name}.png", norm_final)
    name += 1


### TESTE

# name = 1
# for image in range(14):
#     imagedata = cv2.imread(f'Imagens_16bits\Picture{name}_position1.png', cv2.IMREAD_ANYDEPTH)
    
#     norm = cv2.normalize(imagedata, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

#     norm *= 100000
#     norm_final = norm.astype(np.uint16)

#     cv2.imwrite(f"Imagens_16bits\Picture{name}_position1_norm.png", norm_final)
#     name += 1


# img = cv2.imread("Imagens_16bits/Picture1_position1_norm.png", cv2.IMREAD_ANYDEPTH)

# maximg = img.max()

# print(img[24])
# print(maximg)

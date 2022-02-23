#!/usr/bin/python3
# Programa para processamento de imagem
# no âmbito do trabalho de final de curso de João Bastos Pintor
# UTAD 2021-10-27

# Aceita com parametro o nome de um ficheiro CSV com o valor da distancia de cada pixel e
# reproduz numa imagem em tons de cinza a respetiva profundidade

import sys
import csv
import cv2
import numpy as np

def readtable(file): # lê ficeiro CSV com nome passado em file
    f = open(file)
    csvreader = csv.reader(f)
    t=[]
    for row in csvreader:
        t.append(row)
    f.close()
    return t

Icsv = readtable(sys.argv[1]);                      # lê o ficheiro CSV passado como primeiro argumento
I = list(map(lambda l: list(map(float, l)), Icsv))  # converte os valores lidos para float
I1 = np.array(I);                                   # converte a matriz lida num array 'numpy'
I1 = 255*(I1/I1.max());                             # normalia os valores no intervalo 0 a 255
I1 = I1.astype(np.uint8)                            # converte o array de float para uint8


cv2.imshow(sys.argv[1], I1)

cv2.waitKey()
cv2.destroyAllWindows()
quit



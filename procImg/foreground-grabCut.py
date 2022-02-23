#!/usr/bin/python3
# Programa para processamento de imagem
# no âmbito do trabalho de final de curso de João Bastos Pintor
# UTAD 2021-11-25

import csv
import cv2
import numpy as np

RGB_Dog = "./With Dog/RGB/RGB_";


for img in range(1, 2):
    RGB = cv2.imread(RGB_Dog + str(img) + ".jpg");
    RGBgb = cv2.GaussianBlur(RGB, (3, 3), 0)

    rect = (40,40,RGB.shape[1]-80, RGB.shape[0]-80)

    mask = np.zeros(RGB.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    cv2.grabCut(RGBgb,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    fo_mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    ba_mask = np.where((mask==2)|(mask==0),1,0).astype('uint8')
    forRGBm = RGB*fo_mask[:,:,np.newaxis]
    bacRGBm = RGB*ba_mask[:,:,np.newaxis]

    cv2.imshow("Original - " + RGB_Dog + str(img) + ".jpg", RGB)
    cv2.imshow("Foreground - "+ RGB_Dog + str(img) + ".jpg", forRGBm)
    cv2.imshow("Background - "+ RGB_Dog + str(img) + ".jpg", bacRGBm)
 
cv2.waitKey()
cv2.destroyAllWindows()



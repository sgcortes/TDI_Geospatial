# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 11:36:03 2018
Transferencia de colroes entre imagenes
conevrsion al espacio Lab, escalado por fraccion 
@author: sgcortes
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

def image_stats(image):
    '''
    Calculo media y desviacion de canales de imagen
    
    '''
    l, a, b = cv2.split(image)
    (lmean, lStd) = (l.mean(), l.std())
    (amean, aStd) = (a.mean(), a.std())
    (bmean, bStd) = (b.mean(), b.std())
    return (lmean, lStd, aMean, aStd, bMean, bStd)


# Leemos imágenes
source = cv2.imread('Kermit.jpeg')
target = cv2.imread('caramodelo.png')

plt.figure(figsize=(8,4))
plt.subplot(121)
plt.imshow(cv2.cvtColor(source,cv2.COLOR_BGR2RGB))
plt.subplot(122)
#plt.imshow(target)
plt.imshow(cv2.cvtColor(target,cv2.COLOR_BGR2RGB))













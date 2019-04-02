# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 00:56:11 2018

@author: Usuario
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

def image_stats(image):
	'''
    Calcula la media y desviacion estandar de cada canal de la imagen dada
    '''
	# compute the mean and standard deviation of each channel
	(l, a, b) = cv2.split(image)
	(lMean, lStd) = (l.mean(), l.std())
	(aMean, aStd) = (a.mean(), a.std())
	(bMean, bStd) = (b.mean(), b.std())

	# return the color statistics
	return (lMean, lStd, aMean, aStd, bMean, bStd)


source = cv2.imread('Kermit.jpeg')
cara = cv2.imread('caramodelo.png')

plt.figure(figsize=(8,4))
plt.subplot(121)
plt.imshow(source)
plt.subplot(122)
plt.imshow(cv2.cvtColor(cara, cv2.COLOR_BGR2RGB))

# source donde estan los colroes que queremos transferir
source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
# target la imagen a transformar sus colores
target = cv2.cvtColor(cara, cv2.COLOR_BGR2LAB).astype("float32")

# PASO 0: Calculamos las estadísticas de las imagenes
(lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
(lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)

# PASO 1: Sustraer las medias de la imagen objetivo
(l,a,b) = cv2.split(target)
l -= lMeanTar
a -= aMeanTar
b -= bMeanTar

# PAso 2: Escalar por las desviaciones estandar
l = (lStdSrc / lStdTar) * l
a = (aStdSrc / aStdTar) * a
b = (bStdSrc / bStdTar) * b

#l = (lStdTar / lStdSrc) * l
#a = (aStdTar / aStdSrc) * a
#b = (bStdTar / bStdSrc) * b

# Paso 4: Añadir la media de la fuente
l += lMeanSrc
a += aMeanSrc
b += bMeanSrc

# Ajustar la imagen al intervalo [0,255]
l_sc = np.clip(l, 0, 255)
a_sc = np.clip(a,0,255)
b_sc = np.clip(b,0,255)

# Apilar y cambiar de espacio de color
transfer = cv2.merge([l_sc,a_sc,b_sc])
transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)

# Mostrar la image con imshow OpenCV
cv2.imshow("RGB",transfer)

while True:
    k= cv2.waitKey(0) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
    



        







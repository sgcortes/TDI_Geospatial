# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 10:09:43 2018

@author: Usuario
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cambio modelo color OpenCV
road = cv2.imread('road.png')

road_hsv = cv2.cvtColor(road, cv2.COLOR_BGR2HSV)
plt.imshow(road)
plt.title('road_hsv')

# para mostrar la imagen correctamente podemos hacer
plt.imshow(cv2.cvtColor(road_hsv, cv2.COLOR_HSV2RGB))

plt.figure(figsize=(12,4))
plt.subplot(131)
plt.hist(road_hsv[:,:,0].ravel(),bins=256)
plt.title('Hue (tono)')
plt.subplot(132)
plt.hist(road_hsv[:,:,1].ravel(),bins=256)
plt.title('Saturation')
plt.subplot(133)
plt.hist(road_hsv[:,:,2].ravel(),bins=256)
plt.title('Value')

# Mostrando los flags de cvtColor
flags = [i for i in dir(cv2) if i.startswith('COLORMAP_')]
print(flags)

# Aplicar una mapa de color
colo = cv2.imread('../T2_HistogramaContraste/ColoradoLandsat8OLI541.tif')
color =cv2.applyColorMap(colo, cv2.COLORMAP_HOT)
cv2.imshow('Imagen color',color)
while True:
    k = cv2.waitKey(0)
    if k == 27: break
cv2.destroyAllWindows()



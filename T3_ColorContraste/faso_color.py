# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:38:25 2018

@author: Usuario
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lectura de imagen en OpenCV
road = cv2.imread('road.png')
plt.imshow(cv2.cvtColor(road, cv2.COLOR_BGR2RGB))

# Mostrar flags de espacios de color OpenCV
#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flags)

# CAmbio de color de imagen a HSV

road_hsv = cv2.cvtColor(road, cv2.COLOR_BGR2HSV)
plt.imshow(cv2.cvtColor(road_hsv, cv2.COLOR_HSV2RGB))
plt.title('HSV')
plt.axis('off')

plt.figure(figsize=(12,4))
plt.subplot(131)
plt.hist(road_hsv[:,:,0].ravel(),bins=256 )
plt.title('Hue')
plt.subplot(132)
plt.hist(road_hsv[:,:,1].ravel(),bins=256)
plt.title('Saturacion')
plt.subplot(133)
plt.hist(road_hsv[:,:,2].ravel(),bins=256)
plt.title('Value')

# Composiciones falso color
colo = cv2.imread('../T2_HistogramaContraste/ColoradoLandsat8OLI541.tif')
color = cv2.applyColorMap(colo, cv2.COLORMAP_HOT)
cv2.imshow('Imagen falso color',color)

while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()





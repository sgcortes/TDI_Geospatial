# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:42:19 2018

@author: Usuario
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

bgr_img = cv2.imread('san_francisco.jpg')
# Convertir color
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
# Escribir imagen
cv2.imwrite('san_francisco_grayscale.jpg', gray_img)

# Mostrar
plt.imshow(gray_img, cmap = plt.get_cmap('gray'))
plt.xticks([]), plt.yticks([]) # esconder ticks
plt.show()

# ORDEN BGR, RGB
# OpenCV ordena los píxeles BGR mientras que matplotlib lo hace
# como RGB

bgr_img = cv2.imread('san_francisco.jpg')

plt.imshow(bgr_img)
 # El resutlado al mostar con imshow es erróneo a causas del orden que 
 # emplea opencv para leer y almacenar la imagen en memoria
# si mostramos con matplotlib otendremos lo anterior

# Podemos corregirlo haciendo
 
b,g,r = cv2.split(bgr_img)
rgb_img = cv2.merge([r,g,b])
 
plt.imshow(rgb_img)
plt.xticks([]), plt.yticks([])
plt.show()
 
# Otro modo de evitar es mostrar desde opencv
print('_____________________________')
cv2.imshow("Result BGR", bgr_img)
# PEro se usa un visor externo con lo que es necesario
# disponer de un  método apra cerrar la ventana emergente
# el código es el que sigue para ello
while True:
    k = cv2.waitKey(0) & 0xFF    # 0xFF? To get the lowest byte.
    if k == 27: break            # Code for the ESC key 
cv2.destroyAllWindows()














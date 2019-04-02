# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:04:46 2018

@author: Usuario
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer imagen y mostrar Opencv
bgr_img = cv2.imread('san_francisco.jpg')

# Separar canales de la imagen
b, g, r = cv2.split(bgr_img)
# Apilar los canales en orden correcto
rgb_img = cv2.merge([r,g,b])
plt.imshow(rgb_img)

# Mostrar la image con imshow OpenCV
cv2.imshow("RGB",bgr_img)

while True:
    k= cv2.waitKey(0) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
    
    
    






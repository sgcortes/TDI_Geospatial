# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:40:13 2018

@author: Usuario
"""

from skimage import img_as_float, exposure, io
import numpy as np
import matplotlib.pyplot as plt

colo = io.imread('B8_colorado.tif')
colo = img_as_float(colo)
io.imshow(colo)
plt.axis('off')
# Ecualizacion del histograma
colo_equal = exposure.equalize_hist(colo,256)
plt.figure(figsize=(10,5))
plt.subplot(121)
io.imshow(colo)
plt.title('original')
plt.axis('off')
plt.subplot(122)
io.imshow(colo_equal)
plt.title('Ecualizada')
plt.axis('off')

plt.figure(figsize=(6,5))
plt.hist(colo.ravel(),bins=256)
plt.title('Original')

plt.figure(figsize=(6,6))
plt.hist(colo_equal.ravel(),bins=256)
plt.title('Ecualizada')

colo_equaladapt = exposure.equalize_adapthist(colo)
plt.figure(figsize=(6,6))
io.imshow(colo_equaladapt)
plt.figure(figsize=(6,6))
plt.hist(colo_equaladapt.ravel(),bins=256)
plt.title('Ecualizada adaptivamente')

















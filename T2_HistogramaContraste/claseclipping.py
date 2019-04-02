# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:31:31 2018

@author: Usuario
"""
from skimage import img_as_float, exposure, io
import numpy as np
import matplotlib.pyplot as plt

colo = io.imread('B8_colorado.tif')
colo = img_as_float(colo)
io.imshow(colo)
plt.axis('off')
print('Maximo ND= ', np.max(colo))
print('Minimo ND= ', np.min(colo))
plt.figure(figsize=(8,8))
plt.hist(np.ravel(colo), 256)
img_cdf, bin_center =exposure.cumulative_distribution(colo,256)
ax_cdf=plt.twinx()
ax_cdf.plot(bin_center,img_cdf,color='red')

# Expansión lineal del histograma
plt.figure(figsize=(10,5))
plt.subplot(121)
io.imshow(colo)
plt.axis('off')
plt.title('Original')
plt.subplot(122)
colo_rescaled = exposure.rescale_intensity(colo)
io.imshow(colo_rescaled)
plt.title('Expansión auttomática')
plt.axis('off')

plt.figure(figsize=(10,5))
plt.subplot(121)
io.imshow(colo)
plt.axis('off')
plt.title('Original')

plt.subplot(122)
pmin, pmax = np.percentile(colo,(2,98))
print('Percentiles (2%-98%)',pmin,pmax)
colo_clipped= exposure.rescale_intensity(colo, in_range=(pmin, pmax))
io.imshow(colo_clipped)
plt.axis('off')
plt.title('Clipped: [2%-98%]')










 


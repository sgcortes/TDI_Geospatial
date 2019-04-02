# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:32:45 2018

@author: Usuario
"""

from skimage import img_as_float, exposure, io
import numpy as np
import matplotlib.pyplot as plt

colo = io.imread('B8_colorado.tif')
colo = img_as_float(colo)
io.imshow(colo)
plt.axis('off')

# Imagen complemntaria
unos = np.ones(colo.shape)
comp = unos - colo
io.imshow(comp)




# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 00:54:24 2018

@author: Usuario
"""

import matplotlib.pyplot as plt # para visualizar imagenes e histogramas
import numpy as np # para manejar matrices
import skimage
from skimage import exposure # para modificar contraste
from skimage import data, img_as_float # para cargar imagenes y cambiar tipos datos

#%% 
# Cargar y visualizar
cam=data.camera()
print(cam.dtype)
print(skimage.dtype_limits(cam))
cam=img_as_float(cam)
print(skimage.dtype_limits(cam))
fg=skimage.io.imshow(cam)

# imagen complementaria
neg=np.ones(cam.shape)
neg=neg-cam
print(skimage.dtype_limits(neg))
skimage.io.imshow(neg)
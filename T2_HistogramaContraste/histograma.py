# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import skimage
import numpy as np # par manipular matrices (imagenes)
import matplotlib.pyplot as plt # para realizatr graficos

from skimage import exposure # para modificar contraste
from skimage import data, img_as_float 

# Carga de la imagen
cam = data.camera()
print(cam.dtype)
cam = img_as_float(cam)
# Visualizamos imagen
fg = plt.figure(figsize=(8,4))
ax_imagen = plt.subplot(1,2,1)
ax_imagen.imshow(cam, cmap= 'gray')
ax_imagen.axis('off')

# Histograma 
ax_hst = plt.subplot(122)
ax_hst.hist(cam.ravel(),bins=256,histtype='step',color='red')
ax_hst.set_ylim(0,6500)
# histograma acumulativo
ax_cdf = ax_hst.twinx()
img_cdf, bins = exposure.cumulative_distribution(cam,256)
ax_cdf.plot(bins, img_cdf )

fg.tight_layout()

# modificacion del contraste, funcion gamma
fig2= plt.figure(figsize=(15,8))
ax_img = plt.subplot(231)
ax_img.imshow(cam, cmap='gray')
ax_img.set_title('Original')
ax_img.axis('off')

ax_imgamma = plt.subplot(232)
cam_gamma = exposure.adjust_gamma(cam, 3)
ax_imgamma.imshow(cam_gamma,cmap='gray')
ax_imgamma.set_title('Gamma = 0.5')
ax_imgamma.axis('off')

# Grafico funcion transferencia
ax_transf = plt.subplot(233)
ax_transf.plot(cam.ravel(), cam_gamma.ravel(), color='green')
ax_transf.set_title('Función Gamma=0.5')


# Histogramas
ax_historig = plt.subplot(234)
ax_historig.hist(cam.ravel(),bins=256,histtype='step',color='green')
ax_historig.set_title('Hist. imagen original')
ax_histgam = plt.subplot(235)
ax_histgam.hist(cam_gamma.ravel(),bins=256,histtype='step',color='red')
ax_histgam.set_title('Hist. imagen Gamma=0.5')

































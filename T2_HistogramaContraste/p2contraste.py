# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:08:57 2018

@author: sgcortes@uniovi.es
"""
#%% 
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
# otro modo de visualizar con mas control sobre aspecto
# primero crear un objeto figura y uno ejes (matplotlib)
fig=plt.figure(figsize=(8,4))
ax_img=plt.subplot(121)
ax_img.axis('off')
ax_img.imshow(cam,cmap='gray')

# Histograma e histograma acumulativo
ax_hst=plt.subplot(122)
ax_hst.hist(cam.ravel(),bins=256,histtype='step',color='black')

# hist. acumulativo
img_cdf,bins=exposure.cumulative_distribution(cam,256)
ax_cdf=ax_hst.twinx()# segundo par de ejes x invisbles
ax_cdf.plot(bins, img_cdf)

# modificaicon del contraste mediante una gamma
fig2=plt.figure(figsize=(8,4))
cam_gamma=exposure.adjust_gamma(cam,0.5) # ecuacion: NDo=K I**g
ax_imgam=plt.subplot(121)
ax_imgam.imshow(cam_gamma,cmap='gray')
ax_hst=plt.subplot(122)
ax_hst.hist(cam_gamma.ravel(),bins=256,histtype='step',color='black')
img_cdf,bins=exposure.cumulative_distribution(cam_gamma,256)
ax_cdf=ax_hst.twinx()# segundo par de ejes x invisbles
ax_cdf.plot(bins, img_cdf)

#separar bien los bordes de la figura
fig2.tight_layout()

# funcion de trasnferencia entre la imagen original y la gamma
fig3=plt.figure(figsize=(8,4))
ax_transf=plt.subplot(121)
ax_transf.plot(cam.ravel(),cam_gamma.ravel(),color='green')
ax_transf.set_title('Gamma=0.5')

# ajuste del contraste con rescale_intensity(). clipping
'''
Este es un ajuste lineal de la intensidad opuesto al anterior
que sirve apra ampliar el rango de dinámico de la imagen

'''
#%% 

fig4=plt.figure(figsize=(8,4))
ax_imagen=plt.subplot(221)
ax_imagen.imshow(cam,cmap='gray')
ax_imagen2=plt.subplot(222)
vmin, vmax=np.percentile(cam, (0.5,97))
cam_rescaled=exposure.rescale_intensity(cam,in_range=(vmin,vmax))
ax_imagen2.imshow(cam_rescaled,cmap='gray')
ax_imagen.set_title('original')
ax_imagen2.set_title('reescalada intervalo completo')
ax_imagen.axis('off')
ax_imagen2.axis('off')

# histogramas
ax_historig=plt.subplot(223)
ax_historig.hist(cam.ravel(),bins=256,histtype='step',color='black')
ax_historig.set_title('reescalada intervalo completo')
ax_historig=plt.subplot(224)
ax_historig.hist(cam_rescaled.ravel(),bins=256,histtype='step',color='black')

# Ecualizacion histograma
fig5=plt.figure(figsize=(8,4))
ax_imagen=plt.subplot(221)
ax_imagen.imshow(cam,cmap='gray')
ax_imagen.set_title('original')
ax_imagen.axis('off')
ax_imagen2=plt.subplot(222)

cam_equal=exposure.equalize_hist(cam,256)
ax_imagen2.set_title('equalizada')
ax_imagen2.imshow(cam_equal,cmap='gray')
ax_imagen2.axis('off')

# histogramas
ax_historig=plt.subplot(223)
ax_historig.hist(cam.ravel(),bins=256,histtype='step',color='black')
ax_historig.set_title('reescalada intervalo completo')
ax_historig=plt.subplot(224)
ax_historig.hist(cam_equal.ravel(),bins=256,histtype='step',color='black')

#equalizacion adaptativa
fig6=plt.figure(figsize=(8,4))
ax_imagen=plt.subplot(221)
ax_imagen.imshow(cam,cmap='gray')
ax_imagen.set_title('original')
ax_imagen.axis('off')
ax_imagen2=plt.subplot(222)
cam_equal_adapt=exposure.equalize_adapthist(cam,256)
ax_imagen2.set_title('equalizada localmente')
ax_imagen2.imshow(cam_equal_adapt,cmap='gray')

# histogramas
ax_historig=plt.subplot(223)
ax_historig.hist(cam.ravel(),bins=256,histtype='step',color='black')
ax_historig.set_title('reescalada intervalo completo')
ax_historig=plt.subplot(224)
ax_historig.hist(cam_equal_adapt.ravel(),bins=256,histtype='step',color='black')






# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:44:33 2018

@author: Usuario
"""

import matplotlib.pyplot as plt # para visualizar imagenes e histogramas
import numpy as np # para manejar matrices
import skimage.io as io
from skimage import exposure # para modificar contraste
from skimage import data, img_as_float # para cargar imagenes

# Lectura de imagen RGB colorado
colo = io.imread('ColoradoLandsat8OLI541.tif')
colo = img_as_float(colo)
plt.figure(figsize=(8,8))
plt.imshow(colo)
plt.axis('off')
plt.title('Original')
# SEparar canales
R = colo[:,:,0]
G = colo[:,:,1]
B = colo[:,:,2]

#plt.figure(figsize=(12,4))
#ax_red=plt.subplot(131)
#ax_red.set_title('canal rojo')
#plt.hist(R.ravel(),bins=256)
#plt.subplot(132)
#plt.title('canal verde')
#plt.hist(G.ravel(),bins=256)
#plt.subplot(133)
#plt.title('canal azul')
#plt.hist(B.ravel(),bins=256)

# Clipping de los 3 canales al [2%-98%]
vmin, vmax=np.percentile(R, (2,98))
Rclip = exposure.rescale_intensity(R,in_range=(vmin,vmax))

vmin, vmax=np.percentile(G, (2,98))
Gclip = exposure.rescale_intensity(G,in_range=(vmin,vmax))

vmin, vmax=np.percentile(B, (2,98))
Bclip = exposure.rescale_intensity(B,in_range=(vmin,vmax))

def BCET(I,L,H,E):
   l=np.min(I)
   h=np.max(I)
   e=np.mean(I)
   s=np.cumsum(I**2)[-1]/np.size(I)
   bnum=(h**2)*(E-L)-s*(H-L)+(l**2)*(H-E)
   bden=2*(h*(E-L)-e*(H-L)+l*(H-E))
   b=bnum/bden
   a=(H-L)/((h-l)*(h+l-2*b))
   c=L-a*(l-b)**2
   Ibcet=a*(I-b)**2+c
   return Ibcet,a,b,c
   
# Probamos función
L=np.min(Bclip)
H=np.max(Bclip)
E=np.mean(Bclip)

Rbcet, a, b, c = BCET(Rclip, L, H, E)
Gbcet, a, b, c = BCET(Gclip, L, H, E)

# Apilamos los canales de la imagen
COLO = np.dstack((Rbcet,Gbcet,Bclip))
plt.figure(figsize=(8,8))
plt.imshow(COLO)


plt.figure(figsize=(12,4))
ax_red=plt.subplot(131)
ax_red.set_title('canal rojo')
plt.hist(R.ravel(),bins=256)
plt.subplot(132)
plt.title('canal verde')
plt.hist(G.ravel(),bins=256)
plt.subplot(133)
plt.title('canal azul')
plt.hist(B.ravel(),bins=256)

plt.figure(figsize=(12,4))
ax_red=plt.subplot(131)
ax_red.set_title('red BCET')
plt.hist(Rbcet.ravel(),bins=256)
plt.subplot(132)
plt.title('verde BCET')
plt.hist(Gbcet.ravel(),bins=256)
plt.subplot(133)
plt.title('azul BCET')
plt.hist(Bclip.ravel(),bins=256)






   







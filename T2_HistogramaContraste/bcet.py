# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 01:19:16 2018

@author: Usuario
"""
import matplotlib.pyplot as plt # para visualizar imagenes e histogramas
import numpy as np # para manejar matrices
import skimage.io as io
from skimage import exposure # para modificar contraste
from skimage import data, img_as_float # para cargar imagenes y cambiar tipos datos

# Lectura de imagen RGB colorado
colo= io.imread('ColoradoLandsat8OLI541.tif')
colo=img_as_float(colo)
plt.figure(figsize=(12,4))
plt.imshow(colo)
plt.axis('off')
plt.title('Original')

# Canal verde
R = colo[:,:,0]
G = colo[:,:,1]
B = colo[:,:,2]

plt.figure(figsize=(12,4))
plt.subplot(131)
plt.hist(R.ravel(),bins=256)
plt.subplot(132)
plt.hist(G.ravel(),bins=256)
plt.subplot(133)
plt.hist(B.ravel(),bins=256)

# Ajustemos el hsitograma del canal verde con unclipping del 2% en cada lado
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
    s=np.cumsum(I**2.)[-1]
    s=s/(np.size(I))

    bnum=(h**2.)*(E-L)-s*(H-L)+(l**2.)*(H-E)
    bden=2.*(h*(E-L)-e*(H-L)+l*(H-E))
    b=bnum/bden
    a=(H-L)/((h-l)*(h+l-2.*b))
    c=L-a*(l-b)**2.
    Ibcet=a*(I-b)**2.+c
    return Ibcet,a,b,c

# Guardemos el valor L, H y E del canal verde con clipping
L = np.min(Gclip)
H = np.max(Gclip)
E = np.mean(Gclip)

# calculemos los coeficientes de la trasnfomacion aprabólica a, b,c
# canal rojo: a,b,c # Aplicamos la transformacion al canal R
# y=a*(x-b)^2+c
Rbcet,a,b,c=BCET(Rclip,L,H,E)
Bbcet,a,b,c=BCET(Bclip,L,H,E)

#print('Valores máximo, mínimo, media, ROJO:',np.min(Rbcet), np.max(Rbcet), np.mean(Rbcet))
#Calculamos la trasnformacion del azulRBbcet,a,b,c=BCET(R,L,H,E)
#print('Valores máximo, mínimo, media, AZUL:',np.min(Bbcet), np.max(Bbcet), np.mean(Bbcet))
# Apilamos de nuevo la imagen
COLO = np.dstack((Rbcet, Gclip, Bbcet))
plt.figure(figsize=(8,4))
plt.imshow(COLO)
plt.title('COLORADO')

plt.figure(figsize=(12,4))
plt.subplot(131)
plt.hist(Rbcet.ravel(),bins=256)
plt.subplot(132)
plt.hist(Gclip.ravel(),bins=256)
plt.subplot(133)
plt.hist(Bbcet.ravel(),bins=256)












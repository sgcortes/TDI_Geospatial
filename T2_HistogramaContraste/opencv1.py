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

plt.imshow(bgr_img)

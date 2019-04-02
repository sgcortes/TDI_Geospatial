# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:05:05 2018

@author: Usuario
"""

import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
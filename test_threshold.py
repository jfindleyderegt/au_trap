import os, glob, cv2
import numpy as np
import pylab

im_simple = '/home/faedrus/Documents/au_trap/20141031/1414763725.88.png'
im_complex = '/home/faedrus/Documents/au_trap/20141031/1414769658.04.png'
img = cv2.imread(im_complex, 0)
(height, width)  = img.shape
ret,thresh1 = cv2.threshold(img, 127, 255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img, 127, 255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img, 127, 255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img, 127, 255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img, 127, 255,cv2.THRESH_TOZERO_INV)

cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.namedWindow('thresh_binary', cv2.WINDOW_NORMAL)
cv2.namedWindow('thresh_binary_inv', cv2.WINDOW_NORMAL)
cv2.namedWindow('thresh_trunc', cv2.WINDOW_NORMAL)
cv2.namedWindow('thresh_tozero', cv2.WINDOW_NORMAL)
cv2.namedWindow('thresh_tozero_inv', cv2.WINDOW_NORMAL)

cv2.imshow('original', img)
cv2.imshow('thresh_binary', thresh1)
cv2.imshow('thresh_binary_inv', thresh2)
cv2.imshow('thresh_trunc', thresh3)
cv2.imshow('thresh_tozero', thresh4)
cv2.imshow('thresh_tozero_inv', thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()

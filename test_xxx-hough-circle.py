import os, glob, cv2
import numpy as np
import pylab

im_simple = '/home/faedrus/Documents/au_trap/20141031/1414763725.88.png'
im_complex = '/home/faedrus/Documents/au_trap/20141031/1414769658.04.png'
img = cv2.imread(im_complex, 0)
(height, width)  = img.shape
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original', img)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    #outer circle
    cv2.circle (cimg, (i[0], i[1]), i[2], (0,255,0),2)
    #dot at center
    cv2.circle (cimg, (i[0], i[1]), 2   , (0,0,255),3)


cv2.namedWindow('hough', cv2.WINDOW_NORMAL)
cv2.imshow('hough', cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

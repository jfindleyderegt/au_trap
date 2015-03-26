import os, glob, cv2
import numpy as np
import pylab

im_simple = '/home/faedrus/Documents/au_trap/20141031/1414763725.88.png'
im_complex = '/home/faedrus/Documents/au_trap/20141031/1414769658.04.png'
img = cv2.imread(im_simple)
(height, width, depth)  = img.shape
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original', img)

#flatten to gray, convert to floating
harris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
harris = np.float32(harris)

#cornerHarris (image, blocksize, ksize, k)
dst = cv2.cornerHarris (harris, 2, 3, 0.04)
dst = cv2.dilate (dst, None)

#thresholding
#harris[dst > 0.99*dst.max()] = [0,0,255]


cv2.namedWindow('harris', cv2.WINDOW_NORMAL)
cv2.imshow('harris', harris)

cv2.waitKey(0)
cv2.destroyAllWindows()

import os, glob, cv2
import numpy as np
import pylab

im_simple = '/home/faedrus/Documents/au_trap/20141031/1414763725.88.png'
im_complex = '/home/faedrus/Documents/au_trap/20141031/1414769658.04.png'
img = cv2.imread(im_complex)
(height, width, depth)  = img.shape
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original', img)

#flatten to gray, convert to floating
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray = np.float32(gray)

sift = cv2.SIFT()
kp, des = sift.detectAndCompute(gray, None)
#print des

sifted = cv2.drawKeypoints (gray, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.namedWindow('sifted', cv2.WINDOW_NORMAL)
cv2.imshow('sifted', sifted)

cv2.waitKey(0)
cv2.destroyAllWindows()

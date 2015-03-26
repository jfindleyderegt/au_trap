import os, glob, cv2
import numpy as np
import pylab


im_simple = '/home/faedrus/Documents/au_trap/test/1414763725.88.png'
im_complex = '/home/faedrus/Documents/au_trap/test/1414769658.04.png'
img = cv2.imread(im_simple)
(height, width, depth)  = img.shape
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original', img)

#flatten to gray, convert to floating
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#initiate a FAST with defaults
fast = cv2.FastFeatureDetector()

# find and draw the keypoints
kp = fast.detect(img,None)
detect1 = cv2.drawKeypoints(img, kp, color=(255,0,0))

cv2.namedWindow('fast_defaults', cv2.WINDOW_NORMAL)
cv2.imshow('fast_defaults', detect1)

# get default params
thresh = fast.getInt('threshold')
sup = fast.getBool('nonmaxSuppression')
#neighborhood = fast.getInt('type')

#start playing with defaults
fast.setInt('threshold',20)
kp = fast.detect(img,None)
print len(kp)
detect2 = cv2.drawKeypoints(img, kp, color=(255,0,0))
cv2.namedWindow('thresh=small', cv2.WINDOW_NORMAL)
cv2.imshow('thresh=small', detect2)

#threshold over ~150 loses the particle, chooses noise
fast.setInt('threshold',165)
kp = fast.detect(img,None)
print len(kp)
detect3 = cv2.drawKeypoints(img, kp, color=(255,0,0))
cv2.namedWindow('thresh=large', cv2.WINDOW_NORMAL)
cv2.imshow('thresh=large', detect3)

cv2.waitKey(0)
cv2.destroyAllWindows()

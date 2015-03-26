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
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = img

surf = cv2.SURF()
#surf.upright = True should be faster, doesn't reckon orientation
#surf.upright = True
#surf.extended = True computes extra dimmensions of descriptors
#surf.extended = True
#hessian threshold, normally 300 - 500
hessian = 3000

kp, des = surf.detectAndCompute(gray, None)
print len(des)
print kp

while len(des) > 1:
    hessian += 100
    surf = cv2.SURF(hessian)
    kp, des = surf.detectAndCompute(gray, None)
print 'x: ' + str(kp[0].pt[0])
print 'y: ' + str(kp[0].pt[1])

surfed = cv2.drawKeypoints (gray, kp, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.namedWindow('surfed', cv2.WINDOW_NORMAL)
cv2.imshow('surfed', surfed)

cv2.waitKey(0)
cv2.destroyAllWindows()

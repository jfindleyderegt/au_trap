import os, glob, cv2
import numpy
import pylab

im_simple = '/home/faedrus/Documents/au_trap/20141031/1414763725.88.png'
im_complex = '/home/faedrus/Documents/au_trap/20141031/1414769658.04.png'
img = cv2.imread(im_simple)
(height, width, depth)  = img.shape
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original', img)

#flatten to gray, convert to floating
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Initiate STAR detector
# cv2.ORB([nFeatures[, scaleFactor[, nLevels[, edgeThreshold[, firstLevel[, WTA_K[, scoreType[, patchSize]]]]]]]])
# defs: cv2.ORB(500,   1.2,          8,        31,             0,           2,      ORB::HARRIS, 31)
orb = cv2.ORB(1)

# find the keypoints with ORB
# cv2.ORB.detect (image[, mask]) -> keypoints
kp = orb.detect(img,None)
# compute the descriptors with ORB
# cv2.ORB.compute (image, keypoints[, descriptors]) -> keypoints, descriptors
kp, des = orb.compute(img, kp)
#detected = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
#des.sort(axis=0)
n = 0
#for n in xrange(0,len(des)):
#    print des[n]
#    n += 1
#can also detect and compute at the same time: cv2.ORB.detectAndCompute(image, mask[, descriptors[, useProvidedKeypoints]]) -> keypoints, descriptors
# image should be 8-bit grayscale
# mask
# keypoints is a vector of points
# descriptors is an array
# useProvidedKeypoints is boolean, default false

#there are many defaults to play with:
#nFeatures is how many features to track, default 500
#scoreType is Harris or FAST, default Harris
#WTA_K is points per brief, default 2

#Dries' business:
positions=numpy.array([kpt.pt for kpt in kp])
# as there might be multiple keypoints per object, I have to somehow 
# find out which keypoints belong to the same object and then average
# over their positions.
positions.sort(axis=0) # sort the list according to the first column
# calculate distances in the x direction
distances=positions[1:,0]-positions[:-1,0]
# find the positions where the distance is >10
splits=numpy.where(distances>10)[0]
# split the positions array accordingly
split=numpy.split(positions,splits+1)
# now, average the subarrays
meanpositions=numpy.array([numpy.mean(pos,axis=0) for pos in split])
#print str(meanpositions[0,0]) + ", " + str(meanpositions[0,1])

image = cv2.drawKeypoints(gray, kp, color=(0,255,0),flags=0)

cv2.namedWindow('ORB', cv2.WINDOW_NORMAL)
cv2.imshow('ORB', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

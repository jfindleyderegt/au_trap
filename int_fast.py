import os, glob, cv2
import numpy as np
import pylab

def keypoints(im_file):
    #read image
    img = cv2.imread(im_file)
    (height, width, depth)  = img.shape
    #flatten to gray, convert to floating
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #initiate detector: default thresh=10, default suppress=true
    fast = cv2.FastFeatureDetector(10, True)
    # find and draw the keypoints
    kp = fast.detect(img,None)
    return kp

def file_mean(XXX_stuff_XXX):
    x = kp[0].pt[0]
    y = kp[0].pt[1]
    background = np.sum(img[(y-50):(y+50),(x-100):(x+100)])
    roi = np.sum(img[(y-50):(y+50),(x-50):(x+50)])
    intensity = 2*roi - background
    return intensity



path    = '/home/faedrus/Documents/au_trap/test/'
listing = os.listdir(path)
listing = sorted (listing)
amount = len(listing) / 10
found = 0
for im_file in listing:
    if len(keypoints(path+im_file)) < 1:
        print im_file
        found += 1

print 'found ' + str(found) + ' images without keypoints'

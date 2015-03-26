import os, glob, cv2
import numpy as np
import pylab

def file_mean(im_file):
    #read image
    img = cv2.imread(im_file)
    (height, width, depth)  = img.shape
    #flatten to gray, convert to floating
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Initiate STAR detector
    scale = 1.2
    levels = 8
    edgeThresh = 31
    orb = cv2.ORB (1, scale, levels, edgeThresh, 0, 2)
    kp = orb.detect(img,None)
    #initialize the summing
    background = 0
    roi = 0
    intensity = 0
    #check for keypoints
    if len(kp) == 1:
        x = kp[0].pt[0]
        y = kp[0].pt[1]
        background = np.sum(img[(y-50):(y+50),(x-100):(x+100)])
        roi = np.sum(img[(y-50):(y+50),(x-50):(x+50)])
        intensity = 2*roi - background
    return intensity


path    = '/home/faedrus/Documents/au_trap/20141119/'
listing = os.listdir(path)
listing = sorted (listing)
amount = len(listing) / 10


data = np.array ([file_mean (path+im_file) for im_file in listing]).reshape((amount,10))

mean=np.mean(data,axis=1)
std=np.std(data,axis=1)

pylab.figure(1)
pylab.hist(mean, 40)
pylab.xlabel('intensity (a.u.)')
pylab.ylabel('number of particles')
#pylab.yticks(range(0,5))

pylab.figure(2)
pylab.errorbar(range(len(mean)),mean,yerr=std)
pylab.axis([0,amount,0,3e5])
pylab.xlabel('particle number')
pylab.ylabel('intensity (a.u.)')

pylab.show()

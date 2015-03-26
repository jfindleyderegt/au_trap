import os, glob, cv2
import numpy as np
import pylab

def file_mean(im_file):
    #read image
    img = cv2.imread(im_file)
    (height, width, depth)  = img.shape
    #flatten to gray, convert to floating
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #find point of interest
    int_col = 0
    x = 0
    for i in range (0,width):
        if np.sum(img[:,i:i+1]) > int_col:
            x = i
            int_col = np.sum(img[:,i:i+1])

    int_col = 0
    y = 0
    for i in range (0,height):
        if np.sum(img[i:i+1,:]) > int_col:
            y = i
            int_col = np.sum(img[:,i:i+1])

    background = 0
    roi = 0
    intensity = 0

    background = np.sum(img[(y-50):(y+50),(x-100):(x+100)])
    roi = np.sum(img[(y-50):(y+50),(x-50):(x+50)])
    intensity = 2*roi - background
    return intensity

path    = '/home/faedrus/Documents/au_trap/test/'
listing = os.listdir(path)
listing = sorted (listing)
amount = len(listing) / 10

count = 0
for im_file in listing:
    print file_mean(path+im_file)

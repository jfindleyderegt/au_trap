import os, glob, cv2
import numpy as np
import pylab

def file_mean(im_file):
    img = cv2.imread(im_file)
    (height, width, depth)  = img.shape

    r_count = np.sum(img[:,width/4:3*width/4])
    r_background = np.sum(img[:,:width/4]) + np.sum(img[:,-width/4:])
    avg_count = r_count - r_background
    return avg_count

path    = '/home/faedrus/Documents/au_trap/20141113/'
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
pylab.axis([0,amount,0,5e4])
pylab.xlabel('particle number')
pylab.ylabel('intensity (a.u.)')

pylab.show()

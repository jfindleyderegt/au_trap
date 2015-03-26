import os, glob, cv2
import numpy
import pylab

path    = '/home/faedrus/Documents/au_trap/20141027/'
listing = os.listdir(path)
listing = sorted (listing)

count = 0
img = 0
amount = 0
for im_file in listing:
    new = cv2.imread(path+im_file)
    img = cv2.add(new, img)
    count += 1
    if count > 9:
        amount += 1
        cv2.imwrite('test/dump'+str(amount)+'.png', img)
        count = 0
        img = 0

test_list = sorted ( os.listdir( '/home/faedrus/Documents/au_trap/test/' ))
test_len = len(test_list)

print test_len

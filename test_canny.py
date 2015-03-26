import cv2
import numpy as np

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)

lowThreshold = 0
max_lowThreshold = 400
ratio = 7
kernel_size = 5

im_simple = '/home/faedrus/Documents/au_trap/20141031/1414763725.88.png'
im_complex = '/home/faedrus/Documents/au_trap/20141031/1414769658.04.png'
img = cv2.imread(im_complex)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('canny demo')

cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()


#(height, width, depth)  = img.shape
#
#r_count=np.sum(img[:,width/4:3*width/4,2])
#r_background=np.sum(img[:,:width/4,2])+np.sum(img[:,-width/4:,2])
#    
#avg_count = r_count - r_background
#return avg_count

#path    = '/home/faedrus/Documents/au_trap/20141013/'
#listing = os.listdir(path)
#listing = sorted (listing)
#print listing

#data=np.array([file_mean(path+im_file) for im_file in listing]).reshape((47,10))

#mean=np.mean(data,axis=1)
#std=np.std(data,axis=1)


#pylab.figure(1)
#pylab.hist(mean, 40)
#pylab.xlabel('intensity (a.u.)')
#pylab.ylabel('number of particles')

#pylab.figure(2)
#pylab.errorbar(range(len(mean)),mean,yerr=std)
#pylab.axis([0,50,0,6e5])
#pylab.xlabel('particle number')
#pylab.ylabel('intensity (a.u.)')
#fig1.show()
#pylab.show()
#print "Avg: " + str(r_count)


#r_min = np.array([0, 0, 0], np.uint8)
#r_max = np.array([100, 100, 255], np.uint8)

#dst = cv2.inRange(img, r_min, r_max)
#no_blue = cv2.countNonZero(dst)
#print('The number of blue pixels is: ' + str(no_blue))

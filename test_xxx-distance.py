import os, glob, cv2
import cv2.cv as cv
import numpy
import pylab

im_simple = '/home/faedrus/Documents/au_trap/20141031/1414763725.88.png'
im_complex = '/home/faedrus/Documents/au_trap/20141031/1414769658.04.png'

img = cv2.imread(im_simple)
(height, width, depth)  = img.shape
h = numpy.zeros((height, width, depth))

bins = numpy.arange(height).reshape(height,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]
for ch, col in enumerate(color):
    hist_item = cv2.calcHist([img],[ch],None,[height],[0,height])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
    hist=numpy.int32(numpy.around(hist_item))
    pts = numpy.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)
 
h=numpy.flipud(h)

cv2.imshow('colorhist',h)
cv2.waitKey(0)

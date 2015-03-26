import os
import time
import cv2

#cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture ('/home/faedrus/Desktop/VID_20150102_194520.mp4')
if not cam.isOpened():
    print "fuck-a you, dolphin!"


#cam.get(#) where:
#0 is current location in ms since video start
#3 is width
#4 is height
#10 is brightness
#11 is contrast
#12 is saturation
#13 is hue
frame = (int(cam.get(3)), int(cam.get(4)))
fps = 30

path = '/home/faedrus/Documents/test.avi'
#init cam

#define codec
fourcc = cv2.cv.CV_FOURCC(*'XVID')

#init vid writer - (filename, codec, fps, frame size(, color bool))
out = cv2.VideoWriter()
out.open(path, fourcc, fps, frame)
if not out.isOpened():
    print "fuck-a you, whale!"

#start cam
s,img=cam.read()
#init window
winName="blabla"
cv2.namedWindow(winName,cv2.CV_WINDOW_AUTOSIZE)
#the meat & potatoes
while s:
    s,img=cam.read()
    #convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #save frame
    out.write(gray)
    #show frame
    cv2.imshow(winName,gray)
    #watch for breakkey
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()

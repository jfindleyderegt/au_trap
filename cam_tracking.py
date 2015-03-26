import numpy
import cv2
import time

#initialize the cam
cam=cv2.VideoCapture(0)
#----------#

#start grabbing images
img = cam.read()

#init a window and some variables
winName="blabla"
cv2.namedWindow(winName,cv2.CV_WINDOW_AUTOSIZE)
record=False
rframes=0
runs=0
sift = cv2.SIFT()

#show the image
while True:

#    cv2.imshow(winName,img)
    img = numpy.array(cam.read())
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    keypoints = sift.detect(gray,None)
    if keypoints:
        positions=numpy.array([kpt.pt for kpt in keypoints])
        # as there might be multiple keypoints per object, I have to somehow 
        # find out which keypoints belong to the same object and then average
        # over their positions.
        positions.sort(axis=0) # sort the list according to the first column
        
        distances=positions[1:,0]-positions[:-1,0] # calculate distances in the x direction
        splits=numpy.where(distances>10)[0]	# find the positions where the distance is >10
        split=numpy.split(positions,splits+1)	# split the positions array accordingly
        meanpositions=[numpy.mean(pos,axis=0) for pos in split]	# now, average the subarrays
        for meanpos in meanpositions:
            cv2.line(img, (int(meanpos[0]),10), (int(meanpos[0]),20), (0,255,0))
            cv2.line(img, (int(meanpos[0]),85), (int(meanpos[0]),95), (0,255,0))

    image = cv2.drawKeypoints(gray, keypoints)

    cv2.imshow(winName,image)

    key=cv2.waitKey(10)

    if record is True:
        print "record frame",runs,rframes
        cv2.imwrite(str(time.time())+".png",img)
        rframes+=1            
    
    if rframes>=10:
        runs+=1
        record=False
        rframes=0

    if key== 27: # escape
        cv2.destroyWindow(winName)
        break;
    if key==10: # enter
        record=True


import flycapture2 as fc2
import numpy
import cv2
import time

#initialize the cams
cam0 = fc2.Context()
cam0.connect(*cam0.get_camera_from_index(0))

cam1 = fc2.Context()
cam1.connect(*cam1.get_camera_from_index(1))

#----------#

#grab an image
cam0.start_capture()
im0 = fc2.Image()

cam1.start_capture()
im1 = fc2.Image()

#init a window and some variables
winOne="First Window"
cv2.namedWindow(winOne,cv2.CV_WINDOW_AUTOSIZE)

winTwo="Second Window"
cv2.namedWindow(winTwo,cv2.CV_WINDOW_AUTOSIZE)

#show the image
while True:
    img0 = numpy.array(cam0.retrieve_buffer(im0))
    img1 = numpy.array(cam1.retrieve_buffer(im1))

    cv2.imshow(winOne,img0)
    cv2.imshow(winTwo,img1)

    key=cv2.waitKey(10)
    if key== 27: # escape
        cv2.destroyAllWindows()
        break;

#disconnect the camera
cam0.stop_capture()
cam0.disconnect()


import flycapture2 as fc2
import numpy
import cv2
import time

#initialize the cam
c = fc2.Context()
c.connect(*c.get_camera_from_index(0))
#----------#

#possible video modes
#fc2.VIDEOMODE_1280x960Y16
#fc2.VIDEOMODE_1280x960Y8
#fc2.VIDEOMODE_640x480Y16
#fc2.VIDEOMODE_640x480Y8
#possible frame rates
#only on 640x480: FC2_FRAMERATE_30
#FC2_FRAMERATE_15
#FC2_FRAMERATE_7_5
#FC2_FRAMERATE_3_75
#FC2_FRAMERATE_1_875
#c.set_video_mode_and_frame_rate(fc2.VIDEOMODE_1280x960Y16,fc2.FRAMERATE_7_5)
#m, f = c.get_video_mode_and_frame_rate()
#print m, f
#----------#

#possible settings
#not relevant to our camera
#fc2.BRIGHTNESS
#fc2.SHARPNESS
#fc2.WHITE_BALANCE
#fc2.HUE
#fc2.SATURATION
#fc2.FOCUS
#fc2.ZOOM
#unknown
#fc2.TRIGGER_MODE
#fc2.TRIGGER_DELAY

#relevant to our camera
#fc2.AUTO_EXPOSURE
#fc2.GAMMA
#fc2.PAN
#fc2.TILT
#fc2.SHUTTER
#fc2.GAIN
#fc2.FRAME_RATE
#fc2.TEMPERATURE

#get the relevant props
auto_exp = c.get_property (fc2.AUTO_EXPOSURE)
gamma = c.get_property (fc2.GAMMA)
pan = c.get_property (fc2.PAN)
tilt = c.get_property (fc2.TILT)
shut = c.get_property (fc2.SHUTTER)
gain = c.get_property (fc2.GAIN)
frame_rate = c.get_property (fc2.FRAME_RATE)
temp = c.get_property (fc2.TEMPERATURE)

#turn off all the auto stuff
auto_exp['on_off']=True
auto_exp['auto_manual_mode']=False
auto_exp['abs_value']=0
c.set_property(**auto_exp)

gamma['on_off']=False
gamma['auto_manual_mode']=False
c.set_property(**gamma)

pan['on_off']=False
pan['auto_manual_mode']=False
c.set_property(**pan)

tilt['on_off']=False
tilt['auto_manual_mode']=False
c.set_property(**tilt)

gain['on_off']=False
gain['auto_manual_mode']=False
gain['abs_value']=(0)
c.set_property(**gain)

frame_rate['on_off']=False
frame_rate['auto_manual_mode']=False
frame_rate['abs_value'] = 15
c.set_property(**frame_rate)

shut['on_off']=False
shut['auto_manual_mode']=False
shut['abs_value']=60
c.set_property(**shut)
#----------#

#start grabbing images
c.start_capture()
im = fc2.Image()

#init a window and some variables
winName="blabla"
cv2.namedWindow(winName,cv2.CV_WINDOW_AUTOSIZE)
record=False
rframes=0
runs=0
sift = cv2.SIFT()

#show the image
while True:
    img = numpy.array(c.retrieve_buffer(im))

    cv2.imshow(winName,img)
    key=cv2.waitKey(10)

    if record is True:
        print "record frame",runs,rframes
        cv2.imwrite(time.strftime("%Y%m%d") + "/" + str(time.time()) + ".png", img)
        #print time.strftime("%Y") + "/" + str(time.time()) + ".png"
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

c.stop_capture()
c.disconnect()


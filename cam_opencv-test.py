import time
import cv2
cam=cv2.VideoCapture(0)
#cam.set sets values
#3 - width:         640.0
#4 - height:        480.0
#10- brightness:    ~0.5            vary from 0.0 to 0.5
#11- contrast:      ~0.125          vary from 0.0 to 0.5
#12- saturation:    ~0.125          vary from 0.0 to 0.5
#14- gain:          0               0, 1, 10, 100, 1000 no visible change
#15- exposure:      0               cam claims unsupported


#cam.set(10,0.5)
#cam.set(11,0.125)
#cam.set(12,0.125)


s,img=cam.read()

winName="blabla"
cv2.namedWindow(winName,cv2.CV_WINDOW_AUTOSIZE)

record=False
rframes=0
runs=0

while s:
    cv2.imshow(winName,img)
    s,img=cam.read()
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

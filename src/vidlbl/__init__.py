import cv2
import numpy as np
import time

class label:
    def __init__(self,Range=(0,1),serial=True):
        '''
        Range:范围，默认(0,1)
        serial:是否连续，默认True
        '''
        self.Range=(0,1)
        self.serial=True
        self.out="time_start,time_end,value,min,max,serial\n"

    def label(self,value,time_start,time_end):
        if self.serial==True:
            self.out+="{},{},{},{},{},1\n".format(time_start,time_end,value,self.Range[0],self.Range[1])
        else:
            self.out+="{},{},{},{},{},0\n".format(time_start,time_end,value,self.Range[0],self.Range[1])

class video:
    def __init__(self,path):
        self.path=path

    def show(self,speed=1):
        cap = cv2.VideoCapture(self.path)
        FPS=cap.get(5)*speed
        n=0
        start_time=time.time()
        prev_time=time.time()-start_time
        while cap.isOpened():
            if n!=0:
                while curr_time>=n/FPS:
                    ret, img = cap.read()
                    n+=1
            else:
                while prev_time>=n/FPS:
                    ret, img = cap.read()
                    n+=1
                curr_time = time.time()-start_time
            if not ret:
                break
            if curr_time>=(n-1)/FPS and curr_time<=n/FPS:
                if img.shape[0]>720 or img.shape[1]>1280:
                    img = cv2.resize(img, None, fx=0.5, fy=0.5)
                curr_time = time.time()-start_time
                fps = 1/(curr_time-prev_time)
                prev_time = curr_time
                cv2.imshow('img',img)
            key = cv2.waitKey(1)
            print('\r'+str(curr_time*speed),end='')
            if key==27:
                break
        cap.release()
import cv2
import numpy as np
import time

class label:
    def __init__(self,Range=[0,1]):
        '''
        Range:范围，默认[0,1]
        '''
        self.Range=[0,1]
        self.out="values\n"
        for n,r in zip(range(len(Range)),Range):
            self.out+="{},{}\n".format(n,r)
        self.out+="labels\ntime_start,time_end,value\n"

    def label(self,value,time_start,time_end):
        '''
        添加标签
        '''
        self.out+="{},{},{}\n".format(time_start,time_end,value)

class video:
    def __init__(self,path):
        self.path=path

    def show(self,speed=1,start=0):
        cap = cv2.VideoCapture(self.path)
        n=0
        FPS=cap.get(5)
        start_time=time.time()
        prev_time=time.time()-start_time
        while cap.isOpened():
            if n!=0:
                while curr_time>=n/FPS/speed:
                    ret, img = cap.read()
                    if not ret:
                        break
                    n+=1
            else:
                while start*FPS>=n:
                    ret, img = cap.read()
                    if not ret:
                        break
                    while img.shape[0]>720 or img.shape[1]>1280:
                        img = cv2.resize(img, None, fx=0.5, fy=0.5)
                    cv2.imshow('img',img)
                    key = cv2.waitKey(1)
                    if key==27:
                        ret=False
                        break
                    print('\r'+str(int(n/FPS*100)/100)+"/"+str(start)+'\t',end='')
                    n+=1
                if start!=0:
                    start_time=time.time()-start/speed
                curr_time = time.time()-start_time
            if not ret:
                break
            if curr_time>=(n-1)/FPS/speed and curr_time<=n/FPS/speed:
                while img.shape[0]>720 or img.shape[1]>1280:
                    img = cv2.resize(img, None, fx=0.5, fy=0.5)
                cv2.imshow('img',img)
                curr_time = time.time()-start_time
                fps = 1/(curr_time-prev_time)
                prev_time = curr_time
                key = cv2.waitKey(1)
                if key==27:# esc 退出
                    break
                elif key==ord('w'):# w 2倍速
                    start_time+=curr_time*(1-speed/2)
                    prev_time=time.time()-start_time
                    speed=2
                    print('\n2x speed')
                    curr_time=time.time()-start_time
                elif key==ord('s'):# s 1倍速
                    start_time+=curr_time*(1-speed)
                    prev_time=time.time()-start_time
                    speed=1
                    print('\n1x speed')
                    curr_time=time.time()-start_time
                elif key==ord('x'):# x 0.5倍速
                    start_time+=curr_time*(1-speed*2)
                    prev_time=time.time()-start_time
                    speed=0.5
                    print('\n0.5x speed')
                    curr_time=time.time()-start_time
                elif key==32:# 空格暂停
                    cv2.waitKey(0)
                    start_time+=time.time()-start_time-curr_time
                print('\r'+str(int(curr_time*speed*100)/100)+'\t'+str(int(fps*10)/10)+'\t',end='')
        cap.release()
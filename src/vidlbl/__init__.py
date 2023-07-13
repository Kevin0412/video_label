import cv2
import numpy as np

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
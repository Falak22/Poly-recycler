# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:06:14 2021

@author: Falak Khan
"""

import serial
import time
ser = serial.Serial('COM8',9600, timeout=1)



    
while(True):
    #ser.write(str(chr(1)))
    #ser.write(str.encode('on'))
    x = ser.readline().strip()
    line = x.decode("utf-8")
    print(line)
    if( line == 'start'):
        print("image recognition is starting")
'''    time.sleep(0.4)
    ser.write(b'L')
    #ser.write(str.encode('0'))
    time.sleep(0.5)'''
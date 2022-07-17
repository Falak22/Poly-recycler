# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:20:00 2020

@author: Falak Khan
"""

import tensorflow.keras
#import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import cv2
from keras import models
import serial
import time
ser = serial.Serial('COM8',9600, timeout=1)

video = cv2.VideoCapture(0)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


x = ser.readline().strip()
line = x.decode("utf-8")
print(line)
while True:
    if(line == 'Start') :
        '''_,frame = video.read()
        image = Image.fromarray(frame, 'RGB')'''
        image = Image.open('can.jpg')
        image = image.resize((224,224))
        image_array= np.asarray(image)
    
        normalized_image_array = (image_array.astype(np.float32)/127.0)-1
        data[0] = normalized_image_array
        prediction = model.predict(data)
        print(prediction)
        if(prediction[0,0] >= 0.89 ):
            print("biodegradable")
      
        elif(prediction[0,1] >= 0.89 ):
            print("crushed bottles")
        elif(prediction[0,2] >= 0.89 ):
            print("cups")
        elif(prediction[0,3] >= 0.89 ):
            print("glass")
        elif(prediction[0,4] >=0.89) :
            ser.write(b'H')
            print("metal n stones")
        elif(prediction[0,5] >= 0.89):
            print("oil can")
        elif(prediction[0,6] >= 0.89):
            print("plastic")
        elif(prediction[0,7] >= 0.89):
            print("polyethene bags")
        elif(prediction[0,8] >= 0.89):
            print("sippers")
        elif(prediction[0,9] >= 0.89):
            print("soap")
            #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            #cv2.imshow("project", frame)
            key = cv2.waitKey(1)
    
        #if key == 'q':
            #break
video.release()
cv2.destroyAllWindows()
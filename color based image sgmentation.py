import cv2
import numpy as np


plant = cv2.imread('charlock.png') #input image
hsv = cv2.cvtColor(plant, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
# mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255)) #genral green mask
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

## slice the green
imask = mask>0 #pic all pixels>0
green = np.zeros_like(plant, np.uint8) #create an array of 0s same size as original image
green[imask] = plant[imask] # replace 0s with image mixels

## save 
cv2.imwrite("greenObject.png", green)
cv2.imshow('mask',green)
cv2.waitKey(0)
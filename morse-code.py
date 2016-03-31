#!/bin/python 

import RPi.GPIO as GPIO
import time
pinNum =14
GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(pinNum,GPIO.OUT) #replace pinNum with whatever pin you used, this sets up that pin as an output
while True:
  #GPIO.output(pinNum,GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(pinNum,GPIO.LOW)
  time.sleep(0.5)

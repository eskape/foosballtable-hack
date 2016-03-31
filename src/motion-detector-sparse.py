#!/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pir = 38
GPIO.setup(pir, GPIO.IN)
print "Waiting for sensor to settle"
time.sleep(2)
print "Detecting motion"
while True:
    if GPIO.input(pir) == 1:
        print "Motion Detected!"
        time.sleep(2)
    time.sleep(0.1)

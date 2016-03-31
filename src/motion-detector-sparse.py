#!/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
port_a = 40
port_b = 33
GPIO.setup(port_a, GPIO.IN)
GPIO.setup(port_b, GPIO.IN)
print "Waiting for sensor to settle"
time.sleep(2)
print "Detecting motion"
while True:
    i=GPIO.input(port_a)
    j=GPIO.input(port_b)
    if i+j > 0:
        if i == 1:
            print "A: Motion Detected! @ port %d" % port_a
        if j == 1:
            print "B: Motion Detected! @ port %d" % port_b

        time.sleep(2)
    time.sleep(0.1)

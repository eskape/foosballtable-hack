#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Setup Pins
pin_sensor = 31
GPIO.setup(pin_sensor, GPIO.IN)

curr=GPIO.input(pin_sensor)
prev=-1
while True:
    curr = GPIO.input(pin_sensor)
    if (curr == 0) and not curr is prev:
        print "Goal!"

    prev=curr

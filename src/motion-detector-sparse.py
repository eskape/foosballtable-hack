#!/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
port_a = 40
port_b = 37
GPIO.setup(port_a, GPIO.IN)
GPIO.setup(port_b, GPIO.IN)
print "Waiting for sensor to settle"
time.sleep(2)
print "Detecting motion"

def gimme_motion(channel):
  print "CH%d Motion Detected!" % channel

GPIO.add_event_detect(port_a, GPIO.RISING, callback=gimme_motion)
GPIO.add_event_detect(port_b, GPIO.RISING, callback=gimme_motion)

while True:
  time.sleep(30)

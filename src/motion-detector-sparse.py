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

GPIO.add_event_detect(port_a, GPIO.RISING, callback=gimme_motion)
GPIO.add_event_detect(port_b, GPIO.RISING, callback=gimme_motion)

def gimme_motion(channel, port):
  print "A: Motion Detected! @ channel %d" % channel

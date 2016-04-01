#!/bin/python

import RPi.GPIO as GPIO
import time
import signal 

timeout=5
GPIO.setmode(GPIO.BOARD)
port_a = 40
port_b = 37
GPIO.setup(port_a, GPIO.IN)
GPIO.setup(port_b, GPIO.IN)
print "Waiting for sensor to settle"
time.sleep(2)
print "Detecting motion"

ignoreEvent=False

def resetIgnoreEvent:
  ignoreEvent = False
  # reset timer
  signal.settimer(signal.ITIMER_REAL, 0)
  print "Events are recorded again!"

def gimme_motion(channel):
  if ignoreEvent:
    print "Currently ignoring events..."
    return

  ignoreEvent = True
  signal.setitimer(signal.ITIMER_REAL, timeout)
  print "CH%d Motion Detected!" % channel

GPIO.add_event_detect(port_a, GPIO.RISING, callback=gimme_motion)
GPIO.add_event_detect(port_b, GPIO.RISING, callback=gimme_motion)

signal.signal(signal.SIGALRM, resetIgnoreEvents)
while True:
  time.sleep(30)

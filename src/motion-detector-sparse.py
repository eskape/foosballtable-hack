#!/bin/python

import RPi.GPIO as GPIO
import time
import signal 

#global timeout
#global ignoreEvent
timeout = 5
ignoreEvent = False
score_TeamA = 0
score_TeamB = 0
port_a = 40
port_b = 37

score_mapping = { port_a: score_TeamA, port_b: score_TeamB }

def resetIgnoreEvent(signum, frame):
  global ignoreEvent
  ignoreEvent = False
  # reset timer
  signal.settimer(signal.ITIMER_REAL, 0)
  print "Events are recorded again!"

def gimme_motion(channel):
  if ignoreEvent:
    print "Currently ignoring events..."
    return

  global ignoreEvent
  global score_mapping
  ignoreEvent = True
  score_mapping[channel] += 1
  signal.setitimer(signal.ITIMER_REAL, timeout)
  print "CH%d Motion Detected!" % channel

GPIO.setmode(GPIO.BOARD)
GPIO.setup(port_a, GPIO.IN)
GPIO.setup(port_b, GPIO.IN)

print "Waiting for sensor to settle"
time.sleep(2)
print "Detecting motion"

GPIO.add_event_detect(port_a, GPIO.RISING, callback=gimme_motion)
GPIO.add_event_detect(port_b, GPIO.RISING, callback=gimme_motion)
signal.signal(signal.SIGALRM, resetIgnoreEvent)

while True:
  time.sleep(30)

#!/bin/python

import RPi.GPIO as GPIO
import time
import getopt
import sys

led_port=3
motion_port=11

try:
    opts, args = getopt.getopt(sys.argv[1:],"hl:m:",["--help","led-port=","motion-port="])
except getopt.GetoptError:
    print "Usage: --motion-port=<motion port|11> --led-port=<led port|3>%s " % sys.argv[0]
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h","--help"):
        print "Usage: --motion-port=<motion port|11> --led-port=<led port|3>%s " % sys.argv[0]
        quit()
    elif opt in ("-m", "--motion-port"):
        motion_port = int(arg)
    elif opt in ("-l", "--led-port"):
        led_port = int(arg)

print "Using motion port: %d" % motion_port
print "Using led port: %d" % led_port
quit()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motion_port, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(led_port, GPIO.OUT)         #LED output pin
while True:
    i=GPIO.input(motion_port)
    if i==0:
        #When output from motion sensor is LOW
        print "No intruders",i
        GPIO.output(led_port, 0)  #Turn OFF LED
        time.sleep(0.1)
  elif i==1:
        #When output from motion sensor is HIGH
        print "Intruder detected",i
        GPIO.output(led_port, 1)  #Turn ON LED
        time.sleep(0.1)

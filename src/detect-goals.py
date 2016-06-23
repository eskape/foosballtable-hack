#!/usr/bin/python

import time
from sensor import Sensor

#Setup Pins
pin_sensor1 = 31
pin_sensor2 = 29
events_stuff = Sensor(pin_sensor1,pin_sensor2)

while True:
  time.sleep(30)

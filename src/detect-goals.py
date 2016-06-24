#!/usr/bin/python

import time
import logging
from sensor import Sensor

#Setup Logging
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

#Setup Pins
pin_sensor1 = 31
pin_sensor2 = 29
events_stuff = Sensor(pin_sensor1,pin_sensor2)

while True:
  try:
    a=1
    time.sleep(0.125)
  except KeyboardInterrupt:
    logging.info("Keyboard interruption - detecting goals stopped")
    break

  
  

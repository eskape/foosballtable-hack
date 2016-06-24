import RPi.GPIO as GPIO

class Sensor:
  def __init__(self, *pins):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    self.__mappings = {}
    self.__setup(pins)
    
  def __setup(self, pins):
    self.__mappings = {}
    number = 0
    for pin in pins:
      number += 1
      GPIO.setup(pin, GPIO.IN)
      GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.__teamscores)
      self.__mappings[pin] = "Team %d" % number

  def __teamscores(self, channel):
    print "%s scored on channel %s" % (self.__mappings[channel], channel)

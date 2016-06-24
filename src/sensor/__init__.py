import RPi.GPIO as GPIO
import logging
import requests

class Sensor:
  def __init__(self, *channels):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    self.__mappings = {}
    self.__setup(channels)
    
  def __setup(self, channels):
    self.__mappings = {}
    number = 0
    for channel in channels:
      number += 1
      GPIO.setup(channel, GPIO.IN)
      GPIO.add_event_detect(channel, GPIO.FALLING, callback=self.__teamscores)
      self.__mappings[channel] = "Team %d" % number
      logging.info("Listening for events for %s on channel %s" % (self.__mappings[channel], channel))
  
  def __teamscores(self, channel):
    logging.info("Event detected for %s on channel %s" % (self.__mappings[channel], channel))
    response = requests.post("http://httpbin.org/post", data = {"Team": self.__mappings[channel]});

    if (response.status_code == 200):
      logging.info("Sent %s score successfully" % self.__mappings[channel])
    else:
      logging.info("Failed sending %s score" % self.__mappings[channel])
      logging.info("Status code %s" % response.status_code)
      logging.info(response.text)

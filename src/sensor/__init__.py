import RPi.GPIO as GPIO
import logging
import requests
import json

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
      self.__mappings[channel] = number
      logging.info("Listening for events for %s on channel %s" % (self.__mappings[channel], channel))
  
  def __teamscores(self, channel):
    logging.info("Event detected for %s on channel %s" % (self.__mappings[channel], channel))
    response = requests.post("http://foosballtable.mxapps.io/rest/event?Team=%s&Delta=1" % self.__mappings[channel]);
    try:
      response.raise_for_status()
      logging.info("Sent %s score successfully" % self.__mappings[channel])
    except Exception:
      logging.info("Failed sending %s score" % self.__mappings[channel])
      logging.info("Status code %s" % response.status_code)
      logging.info(response.text)

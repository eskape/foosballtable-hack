#!/bin/python

import RPi.GPIO as GPIO
import time
import signal 


class Sensor:
    """
        Detect motion on Raspberri Pi sensor to track scores.
        Have an idle timout of <self.timeout> on each channel after something is detected.

        add_listener(channel, name) - add a listener for teem <name> @ channel <channel>
        remove_listener(channel)    - remove the listener
        reset_score(channel)        - reset score to zero
        rename_team(channel, new_name)   - rename team to <new_name>
    """

    def __init__(self, idle_timeout = 5):
        GPIO.setmode(GPIO.BOARD)

        self.__max_channels = 40
        self.score = {}
        self.name = {}

        self.ignore_event = False
        self.__idle_timeout = idle_timeout
        self.timer = signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, self._reset_ignore_event)

    def add_listener(self, channel, name, score = 0):
        if not self.__is_channel_available(channel):
            print "Channel is already taken by team '%s'" % self.name[channel]
            return

        GPIO.setup(channel, GPIO.IN)
        self.score[channel] = score
        GPIO.add_event_detect(channel, GPIO.RISING, callback=self._handle_signal)
        print "Keeping track of score for team '%s' @ channel %d" % (name, channel)

    def remove_listener(self, channel):
        if self.__is_channel_available(channel):
            return

        GPIO.remove_event_detect(channel)
        GPIO.cleanup(channel)
        del self.name[channel]
        del self.score[channel]
        print "Cleared channel %d" % channel

    def reset_score(self, channel):
        if self.__is_channel_available(channel):
            print "Cannot reset score for unused channel"
            return

        self.score[channel] = 0
        print "Score for team '%s' reset to %d" % (self.name[channel], self.scores[channel])

    def rename_team(self, channel, new_name):
        if self.__is_channel_available(channel):
            print "Cannot rename unused channel"
            return

        old_name = self.name[channel]
        self.name[channel] = new_name
        print "Renamed '%s' -> '%s'" % (old_name, new_name)

    def _reset_ignore_event(self, signum, frame):
        self.ignore_event = False
        self.timer = signal.setitimer(signal.ITIMER_REAL, 0)

    def _handle_signal(self, channel):
        if self.ignore_event:
            return

        self.ignore_event= True
        self.score[channel] += 1
        self.timer = signal.setitimer(signal.ITIMER_REAL, self.__idle_timeout)

        print "GOOOAAAALL!!!, team %s scored" % self.name[channel]
        for key in self.name():
            print "%s%s: %d" % ("* " if key == channel else "  ", self.name[key], self.scores[key]

    def __is_channel_available(self, channel):
        if channel <= self.__max_channels and channel > 0 and not channel in self.scores:
            return True

        return False

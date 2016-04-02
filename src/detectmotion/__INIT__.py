#!/bin/python

import RPi.GPIO as GPIO
import time
import signal 


class MotionDetector:
    """
        Detect motion on Raspberri Pi sensor to track scores.
        Have an idle timout of <self.timeout> on each channel after something is detected.

        add_listener(channel, name) - add a listener for teem <name> @ channel <channel>
        remove_listener(channel)    - remove the listener
        reset_score(channel)        - reset score to zero
        rename(channel, new_name)   - rename team to <new_name>
    """

    def __init__(self, timeout = 5):
        GPIO.setmode(GPIO.BOARD)
        self.timeout = timeout
        self.__max_channels = 40
        self.timer = {}
        self.ignore_event = {}
        self.score = {}
        self.names = {}
        signal.signal(signal.SIGALRM, self._reset_ignore_event)

    def add_listener(self, channel, name, score = 0):
        if not self.__is_channel_available(channel):
            print "Channel is already taken by team '%s'" % self.names[channel]
            return

        GPIO.setup(channel, GPIO.IN)
        self.score[channel] = score
        self.ignore_event[channel] = False
        self.timer[channel] = signal.setitimer(signal.ITIMER_REAL, 0)
        GPIO.add_event_detect(channel, GPIO.RISING, callback=self._handle_signal)
        print "Keeping track of score @ channel %d" % channel

    def remove_listener(self, channel):
        if self.__is_channel_available(channel):
            return

        self.timer[channel] = signal.setitimer(signal.ITIMER_REAL, 0)
        GPIO.remove_event_detect(channel)
        GPIO.cleanup(channel)
        del self.names[channel]
        del self.score[channel]
        del self.timer[channel]
        del self.ignore_event[channel]
        print "Cleared channel %d" % channel

    def reset_score(self, channel):
        if self.__is_channel_available(channel):
            print "Cannot reset score for unused channel"
            return

        self.score[channel] = 0
        print "Score for team '%s' reset to %d" % (self.names[channel], self.scores[channel])

    def rename(self, channel, new_name):
        if self.__is_channel_available(channel):
            print "Cannot rename unused channel"
            return

        old_name = self.names[channel]
        self.names[channel] = new_name
        print "Renamed '%s' -> '%s'" % (old_name, new_name)


    def _reset_ignore_event(self, channel, frame):
        self.ignore_event[channel] = False
        self.timer[channel] = signal.setitimer(signal.ITIMER_REAL, 0)

    def _handle_signal(self, channel):
        if self.ignore_event[channel]:
            return

        self.ignore_event[channel] = True
        self.score[channel] += 1
        self.timers[channel] = signal.setitimer(signal.ITIMER_REAL, self.timeout)

        print "GOOOAAAALL!!!, team %s scored" % self.names[channel]
        for key in self.names():
            print "%s: %d" % (self.names[key], self.scores[key])

    def __is_channel_available(self, channel):
        if channel <= self.__max_channels and channel > 0 and not channel in self.scores:
            return True

        return False

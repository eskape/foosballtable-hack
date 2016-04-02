#!/bin/python

import time
import signal 
import random

global timeout
global ignoreEvent
port_a = 37
port_b = 40
timeout = 5
ignoreEvent = False
score_mapping = { port_a: 0, port_b: 0 }

def resetIgnoreEvent(signum, frame):
    global ignoreEvent
    ignoreEvent = False
    signal.setitimer(signal.ITIMER_REAL, 0)

def callback(channel, amount):
    global ignoreEvent

    if ignoreEvent:
        return

    global score_mapping
    ignoreEvent = True
    score_mapping[channel] += 1
    signal.setitimer(signal.ITIMER_REAL, timeout)

    print "GOOOAAAALL!!!"
    print "%d - %d" % (score_mapping[port_a], score_mapping[port_b])

signal.signal(signal.SIGALRM, resetIgnoreEvent)
i = 0
while True:
    time.sleep(.4)
    use_port = 37
    if random.random() > 0.5:
        use_port = 40

    i += 1

    callback(use_port, i)

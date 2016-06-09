import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Setup Pins
pin_sensor = 31
GPIO.setup(pin_sensor, GPIO.IN)

while True:
        i = GPIO.input(pin_sensor)
	if (i == 0):
		print "Goal!"
		time.sleep(1)	
	    

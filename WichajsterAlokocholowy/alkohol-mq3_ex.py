#!/bin/env/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)


while True:
    if (not GPIO.input(17)):
	print('Rock&roll!')
    time.sleep(0.500)


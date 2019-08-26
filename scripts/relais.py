#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys,os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#os.system("sudo echo "+str(sys.argv)+" > /home/openhabian/test")
if len(sys.argv) > 2:
    RELAIS_GPIO = int(sys.argv[1])# + int(sys.argv[2])
    GPIO.setup(RELAIS_GPIO, GPIO.OUT)
    #GPIO.output(RELAIS_GPIO, GPIO.LOW)
    if sys.argv[2] == "ON":
        GPIO.output(RELAIS_GPIO, GPIO.LOW)
    elif sys.argv[2] == "OFF":
        GPIO.output(RELAIS_GPIO, GPIO.HIGH) # an


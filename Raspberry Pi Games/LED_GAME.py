#STEFANO DANISI
#WHICH COLOUR LED TURNED ON


#
#
#RE-WRITE PROGRAM
#ALSO CLEAN UP PROGRAM
#
#

import RPi.GPIO as GPIO
import time
import random

#GPIO SETUP
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

y = 0

while True:
    if y == 0 or y == 10:
        ranLed = random.randint(1,2)
        if ranLed == 1:
            GPIO.output(7, True)
            time.sleep(.10)
            GPIO.output(7, False)
            x = input('Which LED was on (RED or GREEN)?: ')
            if x.lower() == 'red':
                y = 10
            else:
                y = 2
        else:
            GPIO.output(33, True)
            time.sleep(.10)
            GPIO.output(33, False)
            x = input('Which LED was on (RED or GREEN)?: ')
            if x.lower() == 'green':
                y = 10
            else:
                y = 2

    else:
        print("YOU LOST CHUMP!!!")
        break
    

#STEFANO DANISI
#WHICH COLOUR LED TURNED ON

#Change GPIO PIN NUMBERs to match your pin numbers

import RPi.GPIO as GPIO
import time
import random

ledRed = 7
ledGreen = 33
scoreRight = 0
scoreWrong = 0

#GPIO SETUP
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(ledRed, GPIO.OUT) #Game LED 1
GPIO.setup(ledGreen, GPIO.OUT) #Game LED 2


while True:
    userInput = input ("\nReady to play(Y/N)? ")
    if userInput.lower() == 'yes'  or userInput.lower() == 'y':
        ranLed = random.randint(1,2)
        if ranLed == 1:
            GPIO.output(ledRed, True)
            time.sleep(.10)
            GPIO.output(ledRed, False)
            x = input ("\nWhich LED was on (RED or GREEN)?: ")
            if x.lower() == 'red' or x.lower() == 'r':
                print ("\nCorrect!!")
                scoreRight += 1
            else:
                print ("\nIncorrect!!")
                scoreWrong += 1
        else:
            GPIO.output(ledGreen, True)
            time.sleep(.10)
            GPIO.output(ledGreen, False)
            x = input ("\nWhich LED was on (RED or GREEN)?: ")
            if x.lower() == 'green' or x.lower() == 'g':
                print ("\nCorrect!!")
                scoreRight += 1
            else:
                print ("\nIncorrect!!")
                scoreWrong += 1
    elif userInput.lower() == 'no' or userInput.lower() == 'n':
        print ("\nCorrect answers:", scoreRight)
        print ("\nIncorrect answers:", scoreWrong)
        print ("\nShutting Game Down")
        break
    else:
        print ("\nInvalid Input!!")
        pass

scoreRight = 0
scoreWrong = 0
GPIO.cleanup()

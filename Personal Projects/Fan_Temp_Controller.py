#Stefano Danisi
#Turn Fan 'ON' and 'OFF'
#depending on CPU temperatures


import RPi.GPIO as GPIO
import time
import subprocess

relay = 11 #GPIO Board pin number
relayStatus = True #Relay 'OFF'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)

programRunning = True #Keep program running


try:
    while programRunning:
        tempCmd = subprocess.check_output(['vcgencmd', 'measure_temp'])
        tempCmdConvert = str(tempCmd, 'utf-8') #Convert tempCmd to string format
        #Convert String to int
        tempNum = int(float(tempCmdConvert.replace("temp=", "").replace("'C\n","")))

        if tempNum >= 48 and relayStatus == True:
            print ("\nTurning Fan ON!")
            GPIO.output(relay, False)
            relayStatus = False
            for i in range(30): #Allows user to Keyboard Interrupt without waiting the entire sleep cycle
                time.sleep(1) #Sleep until next temp read.
        elif tempNum >= 48 and relayStatus == False:
            print("\nFan is already ON!")
            for i in range(30):
                time.sleep(1)
        elif tempNum < 55 and relayStatus == True:
            print("\nTemps haven't reached above 49'C")  
            for i in range(30):
                time.sleep(1)
        elif tempNum < 48 and relayStatus == False:
            print("\nTurning Fan OFF!")
            GPIO.output(relay, True)
            relayStatus = True
            for i in range(10):
                time.sleep(1)
        else:
            print("\nERROR! Resseting Program!") 
            GPIO.output(relay, True)
            relayStatus = True
            for i in range(3):
                time.sleep(1)
except KeyboardInterrupt:
    GPIO.output(relay, True)
    GPIO.cleanup()
    print ("CLEANED PINS AND TURNING RELAY OFF!")


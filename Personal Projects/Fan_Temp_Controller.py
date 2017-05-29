#Stefano Danisi
#Turn Fan 'ON' and 'OFF' depending on CPU temperatures

#
#Make sure to change GPIO PIN NUMBER to match your desired GPIO pin number 
#

import RPi.GPIO as GPIO
import time
import subprocess

relay = 11 #GPIO Board pin number
#To turn relay on set variable to 'False'
#To turn relay off set variable to 'True' 
relayStatus = True #Relay 'OFF'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay, GPIO.OUT)

programRunning = True #Keep program running


try:
    while programRunning:
        tempCmd = subprocess.check_output(['vcgencmd', 'measure_temp']) #Gets computer temperature
        tempCmdConvert = str(tempCmd, 'utf-8') #Convert tempCmd to string format
        #Convert String to int
        tempNum = int(float(tempCmdConvert.replace("temp=", "").replace("'C\n","")))
        
        #If the temperature is equal to or greater than desired temperature (55 degrees) the fan will turn on
        #Change temperature value to  when you want the fan to engage
        if tempNum >= 55 and relayStatus == True:
            print ("\nTurning Fan ON!")
            GPIO.output(relay, False)
            relayStatus = False
            for i in range(30): #Allows user to Keyboard Interrupt without waiting the entire sleep cycle
                time.sleep(1) #Sleep until next temp read.
        elif tempNum >= 55 and relayStatus == False:
            print("\nFan is already ON!")
            for i in range(30):
                time.sleep(1)
        elif tempNum < 55 and relayStatus == True:
            print("\nTemps haven't reached above 54'C")  
            for i in range(30):
                time.sleep(1)
        elif tempNum < 55 and relayStatus == False:
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


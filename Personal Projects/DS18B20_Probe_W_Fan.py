#This program is used with a DS18B20 temperature probe and a relay switch, which controls the fan
import os
import RPi.GPIO as GPIO
import glob
import time


# Data wire default GPIO 4
os.system('modprob w1-gpio')
os.system('modprob w1-therm')

GPIO.setmode(GPIO.BOARD)

#Relay   ADD GPIO PIN NUM
relayPin = 11
GPIO.setup(relayPin, GPIO.OUT)

#Relay in OFF position
relayStatus = True

therm_dir ='/sys/bus/w1/devices/'

therm_probe = glob.glob(therm_dir + '28*')[0]
device_file = therm_probe + '/w1_slave'

averageTemp = 0

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        #temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c#, temp_f


#RELAY and Fan Control
for i in range(0,30):
    print(read_temp(), "°C")
    time.sleep(2)

    #Gets the average temperature
    for x in range(0,3):
        averageTemp += read_temp()
        #Adjust sleep time to match desired interval temperature readings
        time.sleep(3)
        print('Average Temperature: ',averageTemp,'°C\n')

    averageTemp = averageTemp / 3
    
    #Fan will turn on 
    if averageTemp >= 21:
        GPIO.output(relayPin, False)
        time.sleep(5)
        #reset average 
        averageTemp = 0
    #Fan will turn off or do nothing    
    else:
        GPIO.output(relayPin, True)
        time.sleep(5)
        averageTemp = 0
        
averageTemp = 0     
GPIO.output(relayPin, True)
GPIO.cleanup()

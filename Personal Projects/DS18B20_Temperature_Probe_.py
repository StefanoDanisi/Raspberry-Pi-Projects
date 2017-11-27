#This code is created for a DS18B20 Temperature Probe

import sys
import time
import RPi.GPIO as GPIO
import glob
import os

#Change "path" variable to match where you want the output file to be saved
path = '/home/pi/Desktop/1_h_readout.txt'
txtWrite = open(path, 'a')

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

therm_dir ='/sys/bus/w1/devices/'

therm_probe = glob.glob(therm_dir + '28*')[0]
device_file = therm_probe + '/w1_slave'

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

for i in range (0,3):
    print("Pass ", i)
    txtWrite.write('{0:0.1f} °C \n'.format(read_temp()))
    time.sleep(30)

txtWrite.close()

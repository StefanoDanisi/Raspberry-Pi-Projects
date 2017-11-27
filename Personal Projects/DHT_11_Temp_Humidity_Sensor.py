import sys
import Adafruit_DHT
import time

#Average Humidity Reading
avrgHum = 0.0
avrgHumTwo = 0.0
avrgHumThree = 0.0
avrgHumFour = 0.0

avrgTemp = 0.0
avrTempTwo = 0.0
avrgTempThree = 0.0
avrgTempFour = 0.0

for i in range(0,10):
    #Adafruit_DHT.read_retry(Sensor_Ver., GPIO PIN NUMBER)
   humidity, temperature = Adafruit_DHT.read_retry(11, 4)
   time.sleep(6)
   humidityTwo, temperatureTwo = Adafruit_DHT.read_retry(11, 17)
   time.sleep(6)
   humidityThree, temperatureThree = Adafruit_DHT.read_retry(11, 26)
   time.sleep(6)
   humidityFour, temperatureFour = Adafruit_DHT.read_retry(11, 5)
   
   #Error handling for out of range humidity reading
   if (humidity >=100 or humidityTwo >=100 or humidityThree >=100 or humidityFour >=100):
      i -= 1
      time.sleep(10)
      
   elif (humidity <=5 or humidityTwo <=5 or humidityThree <=5 or humidityFour <= 5):
      i -= 1
      time.sleep(10)
   else:
      avrgHum += humidity
      avrgHumTwo += humidityTwo
      avrgHumThree += humidityThree
      avrgHumFour += humidityFour
      
      avrgTemp += temperature
      avrTempTwo += temperatureTwo
      avrgTempThree += temperatureThree
      avrgTempFour += temperatureFour
      
      print('\nPass: ', i+1)
      print ('Probe 1: Temp: {0:0.1f} C  Humidity: {1:0.1f}%'.format(temperature, humidity))
      print ('Probe 2: Temp: {0:0.1f} C  Humidity: {1:0.1f}%'.format(temperatureTwo, humidityTwo))
      print ('Probe 3: Temp: {0:0.1f} C  Humidity: {1:0.1f}%'.format(temperatureThree, humidityThree))
      print ('Probe 4: Temp: {0:0.1f} C  Humidity: {1:0.1f}%'.format(temperatureFour, humidityFour))
      time.sleep(10)
   
avrgHum = avrgHum / 10
avrgHumTwo = avrgHumTwo / 10
avrgHumThree = avrgHumThree / 10
avrgHumFour = avrgHumFour / 10

avrgTemp = avrgTemp / 10
avrgTempTwo = avrgTempTwo / 10
avrgTempThree = avrgTempThree / 10
avrgTemp = avrgTempFour / 10

print ('\nAverage Temperature Probe 1: {0:0.2f}%'.format(avrgTemp))
print ('Average Humidity Probe 1: {0:0.2f}%'.format(avrgHum))

print ('\nAverage Temperature Probe 2: {0:0.2f}%'.format(avrgTempTwo))
print ('Average Humidity Probe 2: {0:0.2f}%'.format(avrgHumTwo))

print ('\nAverage Temperature Probe 3: {0:0.2f}%'.format(avrgTempThree))
print ('Average Humidity Probe 3: {0:0.2f}%'.format(avrgHumThree))

print ('\nAverage Temperature Probe 4: {0:0.2f}%'.format(avrgTempFour))
print ('Average Humidity Probe 4: {0:0.2f}%'.format(avrgHumFour))

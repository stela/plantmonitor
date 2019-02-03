# home_temp_hum_display.py.py
#
# This is an project for using the Grove OLED Display and the Grove DHT Sensor from the GrovePi starter kit
# 
# In this project, the Temperature and humidity from the DHT sensor is printed on the DHT sensor

# from grovepi import *
from grove_oled import *
import time
import grovepi

# dht_sensor_port = 7		# Connect the DHt sensor to port 7

# Connect the Grove Moisture Sensor to analog port A0
# SIG,NC,VCC,GND
moisture_sensor = 0

# Connect the Grove Light Sensor to analog port A1
# SIG,NC,VCC,GND
light_sensor = 1

# Connect the Grove Temperature Sensor to analog port A2
temp_sensor = 2

# Connect the LED to digital port D4
# SIG,NC,VCC,GND
led = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 10

# TODO overlapping digital/analog pin numbers???
grovepi.pinMode(moisture_sensor, "INPUT")
grovepi.pinMode(light_sensor, "INPUT")
grovepi.pinMode(temp_sensor, "INPUT")
grovepi.pinMode(led, "OUTPUT")

# Start and initialize the OLED
oled_init()
oled_clearDisplay()
oled_setNormalDisplay()
oled_setVerticalMode()
time.sleep(.1)

while True:
	try:
		# Borrowed from http://www.seeedstudio.com/wiki/Grove_-_Light_Sensor#With_Raspberry_Pi
		light_raw = grovepi.analogRead(light_sensor)
		# Calculate resistance of sensor in K
		light_resistance = int(float(1023 - light_raw) * 10 / light_raw)

		hum = grovepi.analogRead(moisture_sensor)/10.0
		temp = grovepi.analogRead(temp_sensor)/25.0

		# if light_resistance > threshold:
		if hum < 75:
			grovepi.digitalWrite(led, 0)
			time.sleep(0.5)
			grovepi.digitalWrite(led, 1)
			time.sleep(0.5)
		if hum < 80:
			grovepi.digitalWrite(led, 1)
		else:
			grovepi.digitalWrite(led, 0)
		
		# No... don't have the combined temp + humidity sensor
		# [ temp,hum ] = dht(dht_sensor_port,1)		#Get the temperature and Humidity from the DHT sensor

		# print "temp =", temp, "C\thumidity =", hum,"%"
		t = str(temp)
		h = str(hum)
		
		oled_setTextXY(0, 1)			# Print at line 1
		oled_putString("Tomatoes!")
		
		oled_setTextXY(2, 0)			# Print "TEMP" and the temperature in line 3
		oled_putString("Temp :" + t)
		
		oled_setTextXY(3, 0)			# Print "HUM :" and the humidity in line 4
		oled_putString("Hum  :" + h+"%")

		oled_setTextXY(4, 0)
		oled_putString("Light:" + str(light_resistance) + "  ")

		time.sleep(1)
	except (IOError, TypeError) as e:
		print("Error")

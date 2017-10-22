#!/usr/bin/python
from time import sleep
import serial
import string
import math

# Establish the connection oln a specific port
ser = serial.Serial('/dev/ttyACM0', 115200)
#arduino =serial.Serial('/dev/ttyACM1',115200)
ser.write(b'setmapping2 YUYV 320 240 30.0 JeVois DemoArUco\r\n')
ser.write(b'setpar serout USB\r\n')
ser.write(b'setpar serstyle Normal\r\n')
ser.write(b'setpar markerlen 52\r\n')
ser.write(b'streamon\r\n')

x46 = 0
y46 = 0
x12 = 0
y12 = 0

x = 1 
while True:
	dirty = ser.readline() # Read the newest output
	clean=dirty.translate(None,'NU')
	clean = clean.lstrip()
	#clean = dirty2.lstrip()
	#clean1 = clean.strip('U')
	data = clean.split()
	iden = int(data[1])
	x1 = int(data[2])
	y = int(data[3])
	print "id = " , iden, "x=" , x1 ,"y=", y
	x += 1
	if iden  == 46:
		x46 = x1
		y46 = y
	else:
		x12 = x1
		y12 = y
	rad = math.atan2(y46-y12,x46-x12)
	print rad
	degree = rad + 3.14;
	value = degree*255
	final = value /(2*3.14)
	final = int(final)
	print "Angle = ", degree, "level = ", final
	#arduino.write(final)


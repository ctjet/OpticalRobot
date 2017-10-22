from time import sleep
import serial
#import string
#import math

# Establish the connection oln a specific port
ser = serial.Serial('/dev/ttyACM0', 115200)
#arduino =serial.Serial('/dev/ttyACM1',115200)
ser.write(b'setmapping2 YUYV 320 240 30.0 JeVois DemoArUco\r\n')
ser.write(b'setpar serout USB\r\n')
ser.write(b'setpar serstyle Normal\r\n')
ser.write(b'setpar markerlen 52\r\n')
ser.write(b'streamon\r\n')
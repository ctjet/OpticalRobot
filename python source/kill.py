from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM0', 115200)
ser.write(b'streamoff\r\n')
ser.write(b'restart\r\n')
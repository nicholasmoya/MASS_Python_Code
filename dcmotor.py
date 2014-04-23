#! /usr/bin/python	# used for voice commands
import serial	# library used to communicate with motor controller
import time    	# library used for delays
import sys     	# library used to access arguments

# sets speed and direction of the two motors
def setSpeed(ser, motor, direction, speed):
    if motor == 0 and direction == 0:
        sendByte = chr(0xC2)	# motor 1 goes forward    
    if motor == 1 and direction == 0:
        sendByte = chr(0xCA)  	# motor 2 goes forward
    if motor == 0 and direction == 1:
        sendByte = chr(0xC1)  	# motor 1 goes in reverse
    if motor == 1 and direction == 1:
        sendByte = chr(0xC9)  	# motor 2 goes in reverse
    ser.write(sendByte)  	# sends motor/direction data to motor controller
    ser.write(chr(speed))	#writes speed of motor controller

# used for serial communication
# ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)
ser = serial.Serial('/dev/ttyUSB0', 115200)

# go forward
if int(sys.argv[1]) == 1:
    setSpeed(ser, 0, 1, 127)
    setSpeed(ser, 1, 1, 127)
    time.sleep(float(sys.argv[2]))
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)

# go backward
if int(sys.argv[1]) == 2:
    setSpeed(ser, 0, 0, 127)
    setSpeed(ser, 1, 0, 127)
    time.sleep(float(sys.argv[2]))
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)

# turn right
if int(sys.argv[1]) == 3:
    setSpeed(ser, 0, 0, 127)
    setSpeed(ser, 1, 1, 127)
    time.sleep(float(sys.argv[2]))
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)

# turn left
if int(sys.argv[1]) == 4:
    setSpeed(ser, 0, 1, 127)
    setSpeed(ser, 1, 0, 127)
    time.sleep(float(sys.argv[2]))
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)

# stay still
if int(sys.argv[1]) == 5:
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)

# closes the serial port
ser.close()

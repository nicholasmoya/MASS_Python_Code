import serial   # library used to communicate with motor controller
import time     # library used for delays
import sys      # library used to access arguments

# sets speed and direction of the two motors
def setSpeed(ser, motor, direction, speed):
    if motor == 0 and direction == 0:
        sendByte = chr(0xC2)    # motor 1 goes forward    
    if motor == 1 and direction == 0:
        sendByte = chr(0xCA)    # motor 2 goes forward
    if motor == 0 and direction == 1:
        sendByte = chr(0xC1)    # motor 1 goes in reverse
    if motor == 1 and direction == 1:
        sendByte = chr(0xC9)    # motor 2 goes in reverse
    ser.write(sendByte)     # sends motor/direction data to motor controller
    ser.write(chr(speed))   #writes speed of motor controller

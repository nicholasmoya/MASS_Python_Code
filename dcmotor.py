#! /usr/bin/python
import serial
import time
import sys

def setSpeed(ser, motor, direction, speed):
    if motor == 0 and direction == 0:
        sendByte = chr(0xC2)
    if motor == 1 and direction == 0:
        sendByte = chr(0xCA)
    if motor == 0 and direction == 1:
        sendByte = chr(0xC1)
    if motor == 1 and direction == 1:
        sendByte = chr(0xC9)
    ser.write(sendByte)
    ser.write(chr(speed))

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)
if int(sys.argv[1]) == 1:
    setSpeed(ser, 0, 1, 127)
    setSpeed(ser, 1, 1, 127)
    time.sleep(float(sys.argv[2]))
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)
if int(sys.argv[1]) == 2:
    setSpeed(ser, 0, 0, 127)
    setSpeed(ser, 1, 0, 127)
    time.sleep(float(sys.argv[2]))
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)
if int(sys.argv[1]) == 3:
    setSpeed(ser, 0, 0, 127)
    setSpeed(ser, 1, 1, 127)
    time.sleep(float(sys.argv[2]))
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)
if int(sys.argv[1]) == 4:
    setSpeed(ser, 0, 1, 127)
    setSpeed(ser, 1, 0, 127)
    time.sleep(float(sys.argv[2]))
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)
if int(sys.argv[1]) == 5:
    setSpeed(ser, 0, 0, 0)
    setSpeed(ser, 1, 0, 0)
ser.close()

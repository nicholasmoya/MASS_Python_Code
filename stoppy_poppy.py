import serial
from setSpeed import setSpeed

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)

setSpeed(ser, 0, 0, 0)
setSpeed(ser, 1, 0, 0)

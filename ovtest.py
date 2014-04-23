from PIDFunction import PID_Algorithm as PID
import serial
import time
from setSpeed import setSpeed

# constant values
kp = 3.2
ki = 2
kd = 0.5
ideal_value = 0.1
LEFT_ADC_INPUT_1 = "P9_38"
LEFT_ADC_INPUT_2 = "P9_37"
RIGHT_ADC_INPUT_1 = "P9_35"
RIGHT_ADC_INPUT_2 = "P9_40"

# initial values
n = 1
uLeft = 0
uRight = 0
errorLeft = [0]*3
errorRight = [0]*3

# used for serial communication
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)

# loop PID control
while 1:
	# time.sleep(0.5)
	uLeft, errorLeft = PID(kp, ki, kd, n, uLeft, errorLeft, ideal_value, LEFT_ADC_INPUT_1, LEFT_ADC_INPUT_2) # left control
	uRight, errorRight = PID(kp, ki, kd, n, uRight, errorRight, ideal_value, RIGHT_ADC_INPUT_1, RIGHT_ADC_INPUT_2) # right control
        print ("uLeft: %f \n") % (uLeft)
        print ("uRight: %f \n") % (uRight)
        print ("errorLeft: %s \n") % (str(errorLeft))
        print ("errorRight: %s \n") % (str(errorRight))
        print ("n: %i \n") % (n)
        print "--------------------------\n"
	n = n + 1
	
	setSpeed(ser, 0, 1, int(uRight*127))
	setSpeed(ser, 1, 1, int(uLeft*127))


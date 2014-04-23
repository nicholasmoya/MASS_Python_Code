from PIDFunction import PID_Algorithm as PID
from front_sensor import front_sensor
import serial
import time
from setSpeed import setSpeed

# constant values
kp = 3.2
ki = 2
kd = 0.5
ideal_value = 0.1
obstructed_threshold = 25

# LEFT_ADC_INPUT_1 = "P9_38"
LEFT_ADC_INPUT = "P9_37"
# RIGHT_ADC_INPUT_1 = "P9_35"
RIGHT_ADC_INPUT = "P9_40"
FRONT_ADC_INPUT_1 = "P9_38"
FRONT_ADC_INPUT_2 = "P9_35"

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

        uLeft, errorLeft = PID(kp, ki, kd, n, uLeft, errorLeft, ideal_value, LEFT_ADC_INPUT) # left control
        uRight, errorRight = PID(kp, ki, kd, n, uRight, errorRight, ideal_value, RIGHT_ADC_INPUT) # right control
        print ("uLeft: %f \n") % (uLeft)
        print ("uRight: %f \n") % (uRight)
        print ("errorLeft: %s \n") % (str(errorLeft))
        print ("errorRight: %s \n") % (str(errorRight))
        print ("n: %i \n") % (n)
        print "--------------------------\n"
        n = n + 1

        front_obstructed = front_sensor(obstructed_threshold, FRONT_ADC_INPUT_1) + front_sensor(obstructed_threshold, FRONT_ADC_INPUT_2) 
        left_right_obstructed = ((uLeft == 0) and (uRight == 0))


        if((left_right_obstructed > 0) or (front_obstructed > 0)):
            setSpeed(ser, 0, 0, 127)
            setSpeed(ser, 1, 1, 127)
            front_obstructed = front_sensor(obstructed_threshold, FRONT_ADC_INPUT_1) + front_sensor(obstructed_threshold, FRONT_ADC_INPUT_2)
            left_right_obstructed = front_sensor(obstructed_threshold, RIGHT_ADC_INPUT) + front_sensor(obstructed_threshold, LEFT_ADC_INPUT) 
            # time.sleep(0.5)


        else:
            setSpeed(ser, 0, 1, int(uRight*127))
            setSpeed(ser, 1, 1, int(uLeft*127))

        """
        setSpeed(ser, 0, 1, int(uRight*127))
        setSpeed(ser, 1, 1, int(uLeft*127))
        """
        time.sleep(0.1)

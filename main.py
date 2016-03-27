import serial
import time
from PIDFunction import PID_Algorithm as PID
from setSpeed import setSpeed
from front_sensor import *
from motionDirection import *
from client_setup import *

obstructed_threshold = 25

FRONT_ADC_INPUT_1 = "P9_37"
RIGHT_ADC_INPUT = "P9_38"
LEFT_ADC_INPUT = "P9_39"
FRONT_ADC_INPUT_2 = "P9_40"

# initial values
n = 1
uLeft = 0
uRight = 0
errorLeft = [0]*3
errorRight = [0]*3

# Establish serial connection to motors
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)

# Establish bluetooth connection to remote machine
client_sock = client_setup()

while 1:

        #############
        # SCAN MODE #
        #############

        # bias = motionDirection()
        bias = 0

        if bias > 0:
            motion = "right"
            biasLeft = 1 
            biasRight = 1 - bias
        elif bias < 0:
            motion = "left"
            biasLeft = 1 - abs(bias)
            biasRight = 1
        elif bias == 0:
            motion = "about"
            biasLeft = 1
            biasRight = 1

        client_sock.send("I saw something moving %s. I'll check it out." % motion)

        ###############
        # FOLLOW MODE #
        ###############

        start = time.time()
        end = start

        while (end - start < 10):

            #######################
            # Partial Obstruction #
            #######################

            uLeft, errorLeft = PID(n, uLeft, errorLeft, LEFT_ADC_INPUT) # left control
            uRight, errorRight = PID(n, uRight, errorRight, RIGHT_ADC_INPUT) # right control

            print ("uLeft: %f \n") % (uLeft)
            print ("uRight: %f \n") % (uRight)
            print ("errorLeft: %s \n") % (str(errorLeft))
            print ("errorRight: %s \n") % (str(errorRight))
            print ("n: %i \n") % (n)
            print "--------------------------\n"

            n = n + 1

            ####################
            # Full Obstruction #
            ####################

            # Each front_sensor returns 1 if obstructed_threshold is surpassed
            # If either one returns 1, full obstruction
            front_obstructed = front_sensor(obstructed_threshold, FRONT_ADC_INPUT_1) + front_sensor(obstructed_threshold, FRONT_ADC_INPUT_2) 

            # If both motors have zero speed, full obstruction
            left_right_obstructed = ((uLeft == 0) and (uRight == 0))

            if((left_right_obstructed > 0) or (front_obstructed > 0)):
                # If fully obstructed, rotate in place
                client_sock.send("Something's in the way. I'm relocating.")
                setSpeed(ser, 0, 0, 127)
                setSpeed(ser, 1, 1, 127)
            else:
                # If not fully obstructed, proceed with PID control
                client_sock.send("Now tracking.")
                setSpeed(ser, 0, 1, int(uRight*127*biasRight))
                setSpeed(ser, 1, 1, int(uLeft*127*biasLeft))

            time.sleep(0.1)

            end = time.time()

        client_sock.send("I've been tracking for %s seconds now." % str(end - start))

        # Return to scan mode
        client_sock.send("Now scanning.")
        setSpeed(ser, 0, 1, 0)
        setSpeed(ser, 1, 1, 0)

client_sock.send("We're losing communication. Talk to you later.")
client_sock.close()

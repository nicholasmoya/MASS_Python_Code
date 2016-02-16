from PIDFunction1 import PID_Algorithm as PID
import time

# constant values
kp = 3.2
ki = 2
kd = 0.5
ideal_value = 0.1

# initial values
n = 1
uLeft = 0
uRight = 0
errorLeft = [0]*3
errorRight = [0]*3

# loop PID control
while 1:
	time.sleep(1)
	uLeft, errorLeft = PID(kp, ki, kd, n, uLeft, errorLeft, ideal_value, "P9_37") # left control
	uRight, errorRight = PID(kp, ki, kd, n, uRight, errorRight, ideal_value, "P9_40") # right control
        print ("uLeft: %f \n") % (uLeft)
        print ("uRight: %f \n") % (uRight)
        print ("errorLeft: %s \n") % (str(errorLeft))
        print ("errorRight: %s \n") % (str(errorRight))
        print ("n: %i \n") % (n)
        print "--------------------------\n"
	n = n + 1

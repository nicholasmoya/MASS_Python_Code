from PIDFunction import PID_Algorithm as PID
import time

# constant values
kp = 3.2
ki = 2
kd = 0.5
ideal_value = 0.1

# initial values
n = 1
u = 0

# loop PID control
while 1:
	time.sleep(1)
	u = PID(kp, ki, kd, n, u, ideal_value)
	n = n + 1

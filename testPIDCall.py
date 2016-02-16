from testPIDFunction import PID_Algorithm as PID
import time

print "--------------start--------------"

# constant values
kp = 3.2
ki = 2
kd = 0.5
ideal_value = 0.1

# initial values
n = 1
u = 0

# display values
print "OF n: ", n
print "kp: ", kp
print "ki: ", ki
print "kd: ", kd
print "u: ", u
print "ideal value: ", ideal_value

# loop PID control
while 1:
	time.sleep(1)
	u = PID(kp, ki, kd, n, u, ideal_value)
	n = n + 1
	print "---------------outside--------------"
	print "OF n: ", n
	print "OF u: ", u


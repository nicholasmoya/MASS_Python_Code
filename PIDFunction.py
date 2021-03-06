# allows value to be read from pin
import Adafruit_BBIO.ADC as ADC
ADC.setup()

kp = 3.2
ki = 2
kd = 0.5
ideal_value = 0.1

# begin PID algorithm
def PID_Algorithm(n, u, error, ADC_INPUT):
	
	# calculate k1, k2, k3
	k1 = kp + ki + kd
	k2 = -1*kp -2*kd
	k3 = kd

	# limits of control signal, u
	u_min = 0
	u_max = 1
	
	# read value from pin and display it
	measured_value = ADC.read(ADC_INPUT)
	
	# if first call
	if (n == 1):
		error[2] = 0
		error[1] = 0
		u1 = 0
	
	# if second call
	elif (n == 2):
		error[2] = 0 
		error[1] = error[0]
		u1 = u
	
	# if after second call
	else:
		error[2] = error[1]
		error[1] = error[0]
		u1 = u
	
	# calculate error and control signal, u
	error[0] = ideal_value - measured_value
	u = u1 + k1*error[0] + k2*error[1] + k3*error[2]
	
	# bound control signal, u
	if (u > u_max): u = u_max
	if (u < u_min): u = u_min
		
	# return control, u
	return u, error

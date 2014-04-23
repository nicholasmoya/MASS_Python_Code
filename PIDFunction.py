# THIS IS A VERSION OF THE PIDFUNCTION1.PY CODE THAT TAKES THE AVERAGE OF TWO SENSORS

# allows value to be read from pin
import Adafruit_BBIO.ADC as ADC
ADC.setup()

# begin PID algorithm
def PID_Algorithm(kp, ki, kd, n, u, error, ideal_value, ADC_INPUT_1, ADC_INPUT_2):
	
	# calculate k1, k2, k3
	k1 = kp + ki + kd
	k2 = -1*kp -2*kd
	k3 = kd

	# limits of control signal, u
	u_min = 0
	u_max = 1
	
	# read value from pin and display it
	measured_value_1 = ADC.read(ADC_INPUT_1)
	measured_value_2 = ADC.read(ADC_INPUT_2)
	measured_value = (measured_value_1 + measured_value_2)/2
	
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

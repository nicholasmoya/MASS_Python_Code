# allows value to be read from pin
import Adafruit_BBIO.ADC as ADC
import math

ADC.setup()

def front_sensor(front_threshold, ADC_INPUT):
	measured_value = ADC.read(ADC_INPUT)
        distance = 35*math.exp(-0.0006*measured_value*4000)
	
	if (distance <= front_threshold): return 1
	if (distance > front_threshold): return 0

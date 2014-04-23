#!/usr/bin/python

import time
import Adafruit_BBIO.ADC as ADC
ADC.setup()
RIGHT_ADC_INPUT = "P9_37"
FRONT_ADC_INPUT = "P9_39"
LEFT_ADC_INPUT = "P9_40"

while 1:
    time.sleep(0.1)
   
    right_value = ADC.read(RIGHT_ADC_INPUT)
    front_value = ADC.read(FRONT_ADC_INPUT)
    left_value = ADC.read(LEFT_ADC_INPUT)
    print "--------------------------------"
    print "right value:   ", right_value
    if (right_value >= 0.2): print "Object too close to right sensor!!!"
    print "front value:   ", front_value
    if (front_value >= 0.2): print "Object too close to front sensor!!!"
    print "left value:    ", left_value
    if (left_value >= 0.2): print "Object too close to left sensor!!!"

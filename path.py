#! /usr/bin/python
import math
import time
import os
import serial

ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
xpos_robot = int(raw_input("Robot X Position: "))
ypos_robot = int(raw_input("Robot Y Position: "))
xpos_goal = int(raw_input("Goal X Position: "))
ypos_goal = int(raw_input("Goal Y Position: "))

distance = math.sqrt((xpos_goal - xpos_robot)**2 + (ypos_goal - ypos_robot)**2)
angle = round(math.degrees(math.atan2((ypos_goal - ypos_robot), (xpos_goal - xpos_robot))))
if angle<0:
    angle += 360
print distance, angle
angle = (angle / 100)  # convert degress to time running
# Move angle first
os.system("python dcmotor.py 3 " + str(angle))
time.sleep(2)
# Now move distance
os.system("python dcmotor.py 1 " + str(distance))
# Go to while loop to stop if an object is encountered
while 1:
    x = ser.read(24)
    print (x)
    time.sleep(.1)
#! /usr/bin/python
import math
import time
import os
import serial

def calcDistance(xpos_goal, ypos_goal, xpos_robot, ypos_robot):
    distance = math.sqrt((xpos_goal - xpos_robot)**2 + (ypos_goal - ypos_robot)**2)
    return distance

def calcAngle(xpos_goal, ypos_goal, xpos_robot, ypos_robot):
    angle = round(math.degrees(math.atan2((ypos_goal - ypos_robot), (xpos_goal - xpos_robot))))
    if angle > 180:
        angle -= 360
    if angle < -180:
        angle += 360
    return angle

def moveRobot(distance, angle):
    angle = (angle / 95)  # convert degress to time running
    if angle > 0:
        os.system("python dcmotor.py 3 " + str(angle))
    else:
        angle = abs(angle)
        os.system("python dcmotor.py 4 " + str(angle))
    time.sleep(2)
    os.system("python dcmotor.py 1 " + str(distance) + "&")
    return

def findRange(x):
    pos1 = x.find("1=")
    pos2 = x.find("cm",pos1 + 2)
    if pos1 > 0 and pos2 > 0:
        range = int(x[pos1 + 2:pos2])
    else:
        range = 0
    return range

ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
xpos_robot = int(raw_input("Robot X Position: "))
ypos_robot = int(raw_input("Robot Y Position: "))
xpos_goal = int(raw_input("Goal X Position: "))
ypos_goal = int(raw_input("Goal Y Position: "))
angle = calcAngle(xpos_goal, ypos_goal, xpos_robot, ypos_robot)
distance = calcDistance(xpos_goal, ypos_goal, xpos_robot, ypos_robot)
print "Initial Angle", angle
print "Initial Distance", distance
moveRobot(distance, angle)
time_start = time.time()
while 1:
    x = ser.read(30)
    distanceBarrier = findRange(x)
    if distanceBarrier > 0 and distanceBarrier < 50:
        time_stop = time.time()
        os.system("python dcmotor.py 5")
        time_ran = time_stop - time_start
        print "Time Ran", time_ran
        xpos_robot = xpos_robot + time_ran * math.cos(math.radians(angle))
        print "Current Xpos", xpos_robot
        ypos_robot = ypos_robot + time_ran * math.sin(math.radians(angle))
        print "Current YPos", ypos_robot
        distance = 2
        angle = angle - 90
        if (angle < - 180):
            angle = angle + 360
        print "New Angle", angle
        moveRobot(distance, angle)
        time.sleep(5)
        while distanceBarrier < 100:
            x = ser.read(30)
            distanceBarrier = findRange(x)
            print "Distance ", distanceBarrier
            if distanceBarrier == 0:
                distanceBarrier = 101
        xpos_robot = xpos_robot + distance * math.cos(math.radians(angle))
        print "Current X", xpos_robot
        ypos_robot = ypos_robot + distance * math.sin(math.radians(angle))
        print "Current Y", ypos_robot
        if (angle > 0):
            angle = - angle
        else:
            angle = abs(angle)
        moveRobot(0, angle)
        time.sleep(5)
        angle = calcAngle(xpos_goal, ypos_goal, xpos_robot, ypos_robot)
        distance = calcDistance(xpos_goal, ypos_goal, xpos_robot, ypos_robot)
        print "Goal Distance", distance
        print "Goal Angle", angle
        moveRobot(distance, angle)
        xpos_robot = xpos_robot + distance * math.cos(math.radians(angle))
        print "Current X", xpos_robot
        ypos_robot = ypos_robot + distance * math.sin(math.radians(angle))
        print "Current Y", ypos_robot
        time_start = time.time()

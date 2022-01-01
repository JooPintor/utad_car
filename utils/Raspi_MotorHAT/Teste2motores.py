#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
    mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor1.setSpeed(150)
myMotor2.setSpeed(150)
#myMotor.run(Raspi_MotorHAT.FORWARD);
# turn on motor
#myMotor.run(Raspi_MotorHAT.RELEASE);
# turn off motor
i=1
while (i<5):
    print ("Forward! M1")
    myMotor1.run(Raspi_MotorHAT.FORWARD)

    print ("\tSpeed up...")
    for i in range(255):
        myMotor1.setSpeed(i)
        time.sleep(0.01)

    print ("\tSlow down...")
    for i in reversed(range(255)):
        myMotor1.setSpeed(i)
        time.sleep(0.01)

    print ("Backward! ")
    myMotor1.run(Raspi_MotorHAT.BACKWARD)

    print ("\tSpeed up...")
    for i in range(255):
        myMotor1.setSpeed(i)
        time.sleep(0.01)

    print ("\tSlow down...")
    for i in reversed(range(255)):
        myMotor1.setSpeed(i)
        time.sleep(0.01)

    print ("Release")
    myMotor1.run(Raspi_MotorHAT.RELEASE)
    time.sleep(1.0)

    print ("Forward! M2")
    myMotor2.run(Raspi_MotorHAT.FORWARD)

    print ("\tSpeed up...")
    for i in range(255):
        myMotor2.setSpeed(i)
        time.sleep(0.01)

    print ("\tSlow down...")
    for i in reversed(range(255)):
        myMotor2.setSpeed(i)
        time.sleep(0.01)

    print ("Backward! ")
    myMotor2.run(Raspi_MotorHAT.BACKWARD)

    print ("\tSpeed up...")
    for i in range(255):
        myMotor2.setSpeed(i)
        time.sleep(0.01)

    print ("\tSlow down...")
    for i in reversed(range(255)):
        myMotor2.setSpeed(i)
        time.sleep(0.01)

    print ("Release")
    myMotor2.run(Raspi_MotorHAT.RELEASE)
    time.sleep(1.0)

    myMotor2.run(Raspi_MotorHAT.RELEASE)
    
    i = i+1

    
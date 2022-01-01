#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor


# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

m=range(4)
for i in m:
    mh.getMotor(i+1).run(Raspi_MotorHAT.RELEASE)


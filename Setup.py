#MPU6050 Setup

import smbus
import math
from time import sleep


#Chip Setup
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H =0x47

bus = smbus.SMBus(1)
Device_Address = 0x68 #MPU6050 device address

def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    #Write Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    #Write to Configuration Register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    #ACcelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)

    #concatenate higher and lower value
    value = ((high << 8) | low)

    #to get signed value from mpu6050
    if(value> 32768):
        value = value - 65536
    return value

#def updateVariables():
#    
#    
#    Ax= Setup.read_raw_data(Setup.ACCEL_XOUT_H)/16384.0
#    Ay= Setup.read_raw_data(Setup.ACCEL_XOUT_H)/16384.0
#    Az= Setup.read_raw_data(Setup.ACCEL_XOUT_H)/16384.0
#
#    Gx= Setup.read_raw_data(Setup.GYRO_XOUT_H)/131.0
#    Gy= Setup.read_raw_data(Setup.GYRO_YOUT_H)/131.0
#    Gz= Setup.read_raw_data(Setup.GYRO_ZOUT_H)/131.0
#    
#    print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)     
#    sleep(1)

def initialize():
    MPU_Init()
    
def getGx():
    
    
    return read_raw_data(GYRO_XOUT_H)/131.0


def getGy():
    
    
    return read_raw_data(GYRO_YOUT_H)/131.0


def getGz():
    
   
    
    return read_raw_data(GYRO_ZOUT_H)/131.0

def getAx():
    
    
    return read_raw_data(ACCEL_XOUT_H)/16384.0

def getAy():
    
    
    return read_raw_data(ACCEL_YOUT_H)/16384.0

def getAz():
    
    
    return read_raw_data(ACCEL_ZOUT_H)/16384.0

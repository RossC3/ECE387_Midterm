import math
import Setup

import statistics

import os

os.system('python Setup.py')

Xrest = 0

Yrest = 0

#Zrest d

def initialize():
    Setup.initialize()
    

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def getYRotation():
    global Yrest
    rads = math.atan2(Setup.getAx(), dist(Setup.getAy(),Setup.getAz()))
    return - round(math.degrees(rads) + Yrest)


def getXRotation():
    global Xrest
    radians = math.atan2(Setup.getAy(), dist(Setup.getAx(),Setup.getAz()))
    return round(math.degrees(radians) - Xrest)

def getZRotation():
    radians = math.atan2(Setup.getAz(), dist(Setup.getAx(),Setup.getAy()))
    return round(math.degrees(radians))


def getXAcceleration():
    
    return Setup.getAx()*9.81
    
def getYAcceleration():
    
    return Setup.getAy()*9.81


def getZAcceleration():
    
    return Setup.getAz()*9.81
 
def calibrate():
    global Yrest
    global Xrest
    
    Xrest = calX()
    Yrest = calY()
    #Zrest = calZ()


def calY():
    
    sample = []
    i = 0
    while i < 100:
        sample.append(getYRotation())
        i += 1
        #print (Calculations.getYRotation())
    return statistics.mean(sample)

def calX():
    
    sample = []
    i = 0
    while i < 100:
        sample.append(getXRotation())
        i += 1
        #print (Calculations.getYRotation())
    return statistics.mean(sample)

initialize()
calibrate()


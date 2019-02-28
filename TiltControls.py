import Calculations

xOrientation = False
yOrientation = False

import os

Calculations.initialize()

os.system('python Calculations.py')
def setOrientation(a):
    os.system('python Calculations.py')
    global xOrientation
    global yOrientation
    if a == 0:
        xOrientation = True
    elif a == 1:
        yOrientation = True

def moveRight():
    global xOrientation
    global yOrientation
    if xOrientation:
        if(Calculations.getYRotation()> 1):
            return True
        
    elif yOrientation:
        if(Calculations.getXRotation()< -1):
            return True
    
    
    return False
    
    
def moveLeft():
    global xOrientation
    global yOrientation
    if xOrientation:
        if(Calculations.getYRotation() < -1):
            return True
        
    elif yOrientation:
        if(Calculations.getXRotation() > 1):
            return True
#    else:
#        
#        return True
    
    
    return False
    
def moveUp():
    global xOrientation
    global yOrientation
    if xOrientation:
        if(Calculations.getXRotation() < -1):
            return True
        
    elif yOrientation:
        if(Calculations.getYRotation() > 1):
            return True

    return False
    
def moveDown():
    global xOrientation
    global yOrientation
    if xOrientation:
        if(Calculations.getXRotation() > 1):
            return True
        
    elif yOrientation:
        if(Calculations.getYRotation()< -1):
            return True
    
    
    return False

#Tilt Controller Script MPU 6050

#imports and runs calculations script to get rotation
import Calculations

# Orientation of the Chip. Is the X-axis the horizontal axis or is the Y-axis
xOrientation = False
yOrientation = True

#degrees of sensitivity for tilt controller
hSense = 1
vSense = 1

# defines orientation, default is yOrientation
def setOrientation(a):
    
    global xOrientation
    global yOrientation
    if a == 0:
        yOrientation = True
        xOrientation = False
    elif a == 1:
        xOrientation = True
        yOrientation = False

#defines degree of sensitivity before notification of tilt default values are both 1
#increasing numbers decreases sensitivity
def setSensitivity(a, b):
    global hSense
    global vSense

    hSense = a + 1
    vSense = b + 1
    
#detects if the controller should move right or is past the Right degree sensitivity
def Right():
    global xOrientation
    global yOrientation
    global hSense
    

    if yOrientation:
        if(Calculations.getYRotation()> hSense):
            return True
        
    elif xOrientation:
        if(Calculations.getXRotation()> hSense):
            return True
    
    
    return False
    
#detects if the controller should move right or is past the left degree sensitivity
def Left():
    global xOrientation
    global yOrientation
    global hSense
    
    
    if yOrientation:
        if(Calculations.getYRotation() < -hSense):
            return True
        
    elif xOrientation:
        if(Calculations.getXRotation() < -hSense):
            return True

    
    
    return False
#detects if the controller should move right or is past the +vertical or forward degree sensitivity    
def Up():
    global xOrientation
    global yOrientation
    global vSense
    
    if yOrientation:
        if(Calculations.getXRotation() < -vSense):
            return True
        
    elif xOrientation:
        if(Calculations.getYRotation() > vSense):
            return True

    return False
#detects if the controller should move right or is past the -vertical or backward degree sensitivity    
def Down():
    global xOrientation
    global yOrientation
    global vSense
    
    if yOrientation:
        if(Calculations.getXRotation() > vSense):
            return True
        
    elif xOrientation:
        if(Calculations.getYRotation()< -vSense):
            return True
    
    
    return False



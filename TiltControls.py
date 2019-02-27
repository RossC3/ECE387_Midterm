import Calculations

xOrientiation = False
yOrientation = False


def moveRight():
    global xOrientation
    global yOrientation
    if xOrientation:
        if(Calculations.getYRotation()> 1):
            return True
        
    elif yOrientation:
        if(Calculations.getXRotation()> 1):
            return True
    else:
        
        return True
    
    
    return False
    
    
def moveLeft():
    global xOrientation
    global yOrientation
    if xOrientation:
        if(Calculations.getYRotation() < -1):
            return True
        
    elif yOrientation:
        if(Calculations.getXRotation()< -1):
            return True
#    else:
#        
#        return True
    
    
    return False
    
def moveUp():
    
    pass
    
def moveDown():
    pass
    
    
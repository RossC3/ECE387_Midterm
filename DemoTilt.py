import TiltControls



TiltControls.setOrientation(0)



def testSensitivity(a,b):

    TiltControls.setSensitivity(a,b)

    while True:
        
        if TiltControls.Right():

            print("You are leaning to far to the right!")
            break
        elif TiltControls.Left():

            print("You are leaning to far to the left!")
            break
        elif TiltControls.Up():

            print("You are leaning to far forward!")
            break
        elif TiltControls.Down():

            print("You are leaning to far back!")
            break

        print("You're Good!")



while True:

    x = input('Enter Horizontal Tilt: ')
    y = input('Enter Vertical Tilt: ')


    testSensitivity(int(x),int(y))

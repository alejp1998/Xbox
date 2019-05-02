from __future__ import print_function
import xbox

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")

# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)

# Instantiate the controller
joy = xbox.Joystick()
nwait = 0
# Show various axis and button states until Back button is pressed
print("Xbox controller printing in piTankEx")
while not joy.Back():

    #Control de los botones pulsados
    f1 = open("../piTankEx/xbox360-1.txt","w+")

    if nwait < 19 and nwait != 0 :
        nwait += 1
    elif joy.rightX() > 0.5:
        f1.write("R")
        nwait = 1
    elif joy.rightX() < -0.5:
        f1.write("L")
        nwait = 1
    elif joy.rightY() > 0.5:
        f1.write("U")
        nwait = 1
    elif joy.rightY() < -0.5:
        f1.write("D")
        nwait = 1
    elif joy.A(): 
        f1.write("A")
        nwait = 1
    elif joy.B(): 
        f1.write("B")
        nwait = 1
    elif joy.Y(): 
        f1.write("Y")
        nwait = 1
    elif joy.X(): 
        f1.write("X")
        nwait = 1
    else: 
        f1.write("N")
        nwait = 0    

    f1.close()

    #Control de joystick izquierdo para regulacion de velocidad de ruedas
    f2 = open("../piTankEx/xbox360-2.txt","w+")

    if joy.leftX() > 0.2 or joy.leftX() < -0.2: 
        f2.write("%1.3f" % joy.leftX())
    else: 
        f2.write("0.0")
    
    f2.close()

    f3 = open("../piTankEx/xbox360-3.txt","w+")

    if joy.leftY() > 0.2 or joy.leftY() < -0.2:
        f3.write("%1.3f" % joy.leftY())
    else:
        f3.write("0.0")
    
    f3.close()

# Close out when done
joy.close()

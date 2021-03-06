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

# Show various axis and button states until Back button is pressed
print("Xbox controller printing in piTankEx")
while not joy.Back():

    #Control de los botones pulsados
    if joy.dpadRight():
        str1 = "r"
    elif joy.dpadLeft():
        str1 = "l"
    elif joy.dpadUp():
        str1 = "u"
    elif joy.dpadDown():
        str1 = "d"
    elif joy.rightTrigger() > 0.5:
        str1 = "T"
    elif joy.Start():
        str1 = 'E'
    elif joy.A(): 
        str1 = "A"
    elif joy.B(): 
        str1 = "B"
    elif joy.Y(): 
        str1 = "Y"
    elif joy.X(): 
        str1 = "X"
    else: 
        str1 = "N"  

    #Control de joystick derecho como digital
    if joy.rightX() > 0.5:
        str2 = "R"
    elif joy.rightX() < -0.5:
        str2 = "L"
    elif joy.rightY() > 0.5:
        str2 = "U"
    elif joy.rightY() < -0.5:
        str2 = "D" 
    else: 
        str2 = "N" 

    #Control de joystick izquierdo para regulacion de velocidad de ruedas
    if joy.leftX() > 0.3 or joy.leftX() < -0.3: 
        str3 = "%1.3f" % joy.leftX()
    else: 
        str3 = "0.0"

    if joy.leftY() > 0.3 or joy.leftY() < -0.3:
        str4 = "%1.3f" % joy.leftY()
    else:
        str4 = "0.0"

    f1 = open("../piTankEx/xbox360.txt","w+")
    f1.write(str1 + " " + str2 + " " + str3 + " " + str4)
    f1.close()
# Close out when done
joy.close()

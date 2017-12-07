import xbox #wget https://raw.githubusercontent.com/FRC4564/Xbox/master/xbox.py

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

joy = xbox.Joystick()

print "Xbox controller sample: Press Back button to exit"
# Loop until back button is pressed
while not joy.Back():
    # Show connection status
    if joy.connected():
        print "Connected   ",
    else:
        print "Disconnected",

    # Left analog stick
    print "Lx,Ly ",fmtFloat(joy.leftX()),fmtFloat(joy.leftY()),
    # Right analog stick
    print "Rx,Ry ",fmtFloat(joy.rightX()),fmtFloat(joy.rightY()),
    # Right trigger
    print "rightTrigger ",fmtFloat(joy.rightTrigger()),
    # Right trigger
    print "leftTrigger ",fmtFloat(joy.leftTrigger()),

    # A/B/X/Y buttons
    print "Buttons ",
    if joy.A():
        print "A",
    else:
        print " ",
    if joy.B():
        print "B",
    else:
        print " ",
    if joy.X():
        print "X",
    else:
        print " ",
    if joy.Y():
        print "Y",
    else:
        print " ",
    # Dpad U/D/L/R
    print "Dpad ",
    if joy.dpadUp():
        print "U",
    else:
        print " ",
    if joy.dpadDown():
        print "D",
    else:
        print " ",
    if joy.dpadLeft():
        print "L",
    else:
        print " ",
    if joy.dpadRight():
        print "R",
    else:
        print " ",

    # Move cursor back to start of line
    print chr(50),
# Close out when done
joy.close()

import xbox #wget https://raw.githubusercontent.com/FRC4564/Xbox/master/xbox.py
import RPi.GPIO as GPIO
#from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 23
Motor1B = 24
Motor1E = 12
Motor2A = 17
Motor2B = 27
Motor2E = 13

GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

joy = xbox.Joystick()

flag = 1
ljoy = 0
rjoy = 0

print "Xbox controller sample: Press Back button to exit"
# Loop until back button is pressed
while not joy.Back():
    ljoy = joy.leftY()
    rjoy = joy.rightY()
    # Show connection status
    if joy.connected():
        print "Connected   ",
    else:
        print "Disconnected",
    #Left Motor , motor number 1
    if ljoy > 0:
        if flag:
            GPIO.output(Motor1A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
            pwm1 = GPIO.PWM(Motor1E,1000)
            pwm1.start(90)
            flag = 0;
        pwm1.ChangeDutyCycle(abs(ljoy * 100))
    elif ljoy < 0:
        if not flag:
            flag = 1
            GPIO.output(Motor1A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.HIGH)
            pwm1.start(0)
        pwm1.ChangeDutyCycle(abs(ljoy * 100))
    # Left analog stick
    print "Ly ",ljoy,

    #Right Motor , motor number 2


    # Right analog stick
    print "Ry ",rjoy,

    # Move cursor back to start of line
    print chr(13),

print "Stopping motor"

GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2A,GPIO.LOW)

GPIO.cleanup()

# Close out when done
joy.close()


# while(key != "q"):
#         if(key == "w"):
#             print "Forward"
            # GPIO.output(Motor1A,GPIO.HIGH)
            # GPIO.output(Motor1B,GPIO.LOW)
            # GPIO.output(Motor2A,GPIO.HIGH)
            # GPIO.output(Motor2B,GPIO.LOW)
            # pwm1 = GPIO.PWM(Motor1E,1000)
            # pwm2 = GPIO.PWM(Motor2E,1000)
            # //pwm1.start(90)
#             //pwm2.start(30)
#             key = raw_input()
#         elif(key == "s"):
#                 print "Backward"
#                 GPIO.output(Motor1B,GPIO.HIGH)
#                 GPIO.output(Motor1A,GPIO.LOW)
#                 GPIO.output(Motor2B,GPIO.HIGH)
#                 GPIO.output(Motor2A,GPIO.LOW)
#                 key = raw_input()
#         elif(key == "d"):
#                 print "Right"
#                 GPIO.output(Motor1B,GPIO.HIGH)
#                 GPIO.output(Motor1A,GPIO.LOW)
#                 GPIO.output(Motor2B,GPIO.LOW)
#                 GPIO.output(Motor2A,GPIO.HIGH)
#                 key = raw_input()
#         elif(key == "a"):
#                 print "Left"
#                 GPIO.output(Motor1B,GPIO.LOW)
#                 GPIO.output(Motor1A,GPIO.HIGH)
#                 GPIO.output(Motor2B,GPIO.HIGH)
#                 GPIO.output(Motor2A,GPIO.LOW)
#                 key = raw_input()
#         elif(key == "e"):
#                 GPIO.output(Motor1B,GPIO.LOW)
#                 GPIO.output(Motor1A,GPIO.LOW)
#                 GPIO.output(Motor2B,GPIO.LOW)
#                 GPIO.output(Motor2A,GPIO.LOW)

import RPi.GPIO as GPIO
from time import sleep

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


print " w\na d\n s"

key = raw_input()

while(key != "q"):
        if(key == "w"):
            print "Forward"
            GPIO.output(Motor1A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
            GPIO.output(Motor2A,GPIO.HIGH)
            GPIO.output(Motor2B,GPIO.LOW)
            pwm1 = GPIO.PWM(Motor1E,1000)
            pwm2 = GPIO.PWM(Motor2E,1000)
            pwm1.start(90)
            key = raw_input()
        elif(key == "s"):
                print "Backward"
                GPIO.output(Motor1B,GPIO.HIGH)
                GPIO.output(Motor1A,GPIO.LOW)
                GPIO.output(Motor2B,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.LOW)
                key = raw_input()
        elif(key == "d"):
                print "Right"
                GPIO.output(Motor1B,GPIO.HIGH)
                GPIO.output(Motor1A,GPIO.LOW)
                GPIO.output(Motor2B,GPIO.LOW)
                GPIO.output(Motor2A,GPIO.HIGH)
                key = raw_input()
        elif(key == "a"):
                print "Left"
                GPIO.output(Motor1B,GPIO.LOW)
                GPIO.output(Motor1A,GPIO.HIGH)
                GPIO.output(Motor2B,GPIO.HIGH)
                GPIO.output(Motor2A,GPIO.LOW)
                key = raw_input()
        elif(key == "e"):
                GPIO.output(Motor1B,GPIO.LOW)
                GPIO.output(Motor1A,GPIO.LOW)
                GPIO.output(Motor2B,GPIO.LOW)
                GPIO.output(Motor2A,GPIO.LOW)
                key = raw_input()
        else:
                key = raw_input()
print "Stopping motor"

GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2A,GPIO.LOW)

GPIO.cleanup()

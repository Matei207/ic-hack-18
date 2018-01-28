import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
 
beltMotor1 = 16
beltMotor2 = 18
beltMotor3 = 22

#Get integer input from Alexa
#Select motor depending on input

#GPIO.setup(MotorRIGHT, GPIO.OUT)
#GPIO.setup(MotorLeft, GPIO.OUT)

GPIO.setup(beltMotor1,GPIO.OUT)
GPIO.setup(beltMotor2,GPIO.OUT)
GPIO.setup(beltMotor3,GPIO.OUT)
	
print "Going forwards"
GPIO.output(beltMotor1,GPIO.HIGH)
GPIO.output(beltMotor2,GPIO.LOW)
GPIO.output(beltMotor3,GPIO.HIGH)
sleep(2)

print "Going backwards"
GPIO.output(beltMotor1, GPIO.LOW)
GPIO.output(beltMotor2, GPIO.HIGH)
GPIO.output(beltMotor3, GPIO.HIGH)
sleep(2)

GPIO.output(beltMotor3,GPIO.LOW)
GPIO.cleanup()

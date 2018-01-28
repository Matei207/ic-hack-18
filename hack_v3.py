from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
from time import sleep

print "Started service"
app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

shelf1Full = False
shelf2Full = False
beltMotorFwd = 16
beltMotorBck = 18
beltMotorEn  = 22
leftMotorFwd = 11
leftMotorBck = 13
leftMotorEn  = 15
rightMotorFwd = 29
rightMotorBck = 31
rightMotorEn  = 36

def setupGPIO():
        GPIO.setmode(GPIO.BOARD)
	GPIO.setup(beltMotorFwd, GPIO.OUT)
	GPIO.setup(beltMotorBck, GPIO.OUT)
	GPIO.setup(beltMotorEn, GPIO.OUT)
	GPIO.setup(leftMotorFwd, GPIO.OUT)
	GPIO.setup(leftMotorBck, GPIO.OUT)
	GPIO.setup(leftMotorEn, GPIO.OUT)
	GPIO.setup(rightMotorFwd, GPIO.OUT)
	GPIO.setup(rightMotorBck, GPIO.OUT)
	GPIO.setup(rightMotorEn, GPIO.OUT)

def beltmovefwd():
        GPIO.output(beltMotorFwd,GPIO.HIGH)
        GPIO.output(beltMotorBck,GPIO.LOW)
        GPIO.output(beltMotorEn,GPIO.HIGH)
        sleep(2)

def beltmovebck():
        GPIO.output(beltMotorFwd,GPIO.LOW)
        GPIO.output(beltMotorBck,GPIO.HIGH)
        GPIO.output(beltMotorEn,GPIO.HIGH)
        sleep(2)

def leftmovefwd():
        GPIO.output(leftMotorFwd,GPIO.HIGH)
        GPIO.output(leftMotorBck,GPIO.LOW)
        GPIO.output(leftMotorEn,GPIO.HIGH)
        sleep(2) 

def leftmovebck():
        GPIO.output(leftMotorFwd,GPIO.LOW)
        GPIO.output(leftMotorBck,GPIO.HIGH)
        GPIO.output(leftMotorEn,GPIO.HIGH)
        sleep(2)

def rightmovefwd():
        GPIO.output(rightMotorFwd,GPIO.HIGH)
        GPIO.output(rightMotorBck,GPIO.LOW)
        GPIO.output(rightMotorEn,GPIO.HIGH)
        sleep(2)

def rightmovebck():
        GPIO.output(rightMotorFwd,GPIO.LOW)
        GPIO.output(rightMotorBck,GPIO.HIGH)
        GPIO.output(rightMotorEn,GPIO.HIGH)
        sleep(2)

def withdraw(shelf):
        if shelf == 1 and shelf1Full == True:
		return statement('Shelf 1 chosen')
                leftmovefwd()
                leftmovebck()
                beltmovefwd()

        elif shelf == 2 and shelf2Full == True:
		return statement('Shelf 2 chosen')
                rightmovefwd()
                rightmovebck()
                beltmovefwd()
	else:
		return statement('Invalid shelf selected')

def deposit(shelf):
        if shelf == 1 and shelf1Full == False:
		return statement('Putting back item into shelf 1')
                leftmovefwd()
                beltmovebck()
                leftmovebck()
        elif shelf == 2 and shelf2Full == False:
		return statement('Putting back item into shelf 2')
                rightmovefwd()
                beltmovebck()
                rightmovebck()

setupGPIO()
@ask.intent('GPIOControlIntent')
def gpio_control(shelf):

   try:
       shelfNum = int(shelf)
   except Exception as e:
       return statement('Invalid request')

   withdraw(shelfNum)

#init  main
GPIO.cleanup()
if __name__== '__main__':
        port = 5000
        app.run(host='0.0.0.0',port=port,debug=True)

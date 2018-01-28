def setupGPIO():
	global beltMotorFwd = 16
	global beltMotorBck = 18
	global beltMotorEn  = 22
	global leftMotorFwd = 11
	global leftMotorBck = 13
	global leftMotorEn  = 15
	global rightMotorFwd = 29
	global rightMotorBck = 31
	global rightMotorEn  = 36
	GPIO.setmode(GPIO.BOARD)
	return


def beltmovefwd():
	GPIO.output(beltMotorFwd,GPIO.HIGH)
	GPIO.output(beltMotorBck,GPIO.LOW)
	GPIO.output(beltMotorEn,GPIO.HIGH)
	sleep(2)
	return

def beltmovebck():
	GPIO.output(beltMotorFwd,GPIO.LOW)
	GPIO.output(beltMotorBck,GPIO.HIGH)
	GPIO.output(beltMotorEn,GPIO.HIGH)
	sleep(2)
	return

def leftmovefwd():
	GPIO.output(leftMotorFwd,GPIO.HIGH)
	GPIO.output(leftMotorBck,GPIO.LOW)
	GPIO.output(leftMotorEn,GPIO.HIGH)
	sleep(2)
	return

def leftmovebck():
        GPIO.output(leftMotorFwd,GPIO.LOW)
        GPIO.output(leftMotorBck,GPIO.HIGH)
        GPIO.output(leftMotorEn,GPIO.HIGH)
        sleep(2)
        return

def rightmovefwd():
        GPIO.output(rightMotorFwd,GPIO.HIGH)
        GPIO.output(rightMotorBck,GPIO.LOW)
        GPIO.output(rightMotorEn,GPIO.HIGH)
        sleep(2)
        return

def rightmovebck():
        GPIO.output(rightMotorFwd,GPIO.LOW)
        GPIO.output(rightMotorBck,GPIO.HIGH)
        GPIO.output(rightMotorEn,GPIO.HIGH)
        sleep(2)
        return

def withdraw(shelf):
	if shelf == "1":
		leftmovefwd()
		leftmovebck()
		beltmovefwd()
	else:
		rightmovefwd()
		rightmovebck()
		beltmovefwd()
	return

def deposit(shelf):
        if shelf == "1":
                leftmovefwd()
		beltmovebck()
                leftmovebck()
        else:
                rightmovefwd()
                beltmovebck()
                rightmovebck()
        return


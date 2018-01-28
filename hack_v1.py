import serial, time

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
time.sleep(1)

while True:
	voice_input = raw_input("Input phrase: ")
	voice_input.lower()

	if voice_input.find("shelf one") != -1:
		print("Shelf #1 selected")
		arduinoSerialData.write('3')
		
	elif voice_input.find("shelf two") != -1:
		print("Shelf #2 selected")
		arduinoSerialData.write('6')
		
	elif voice_input.find("shelf three") != -1:
		print("Shelf #3 selected")
		arduinoSerialData.write('8')
		
	else:
		print("Voice input not valid!")
		break

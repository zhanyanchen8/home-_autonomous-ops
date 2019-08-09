#!/usr/bin/python2

def toArduino(destination, data):
	
	import R2Protocol as r2p

	import serial
	ser = serial.Serial('/dev/ttyACM0', 9600)

	distanceIDstart = "0" #drivetrain
	degreesIDstart = "1" #turntable

	cnt = 0

	source = "JETSON"
	ID = "12"
	
	# keep track to see if destination ID is to motor controlling drivetrain or turntables
	"""
	for i in range(0, len(destination)):
		num = r2p.encode(source, destination[i], ID, data[i])
		ser.write(num)
		
		confirmation = ser.read()
		# confirmation that command has been sent and run - CONFIRMATION CONSTANT = 1
		if (confirmation != 1):
			print ("system error")
			return 0
	"""
	
	num = r2p.encode(source, destination, ID, data)
	print (num)
	ser.write(num)
		
	confirmation = ser.read()
	
	print (confirmation)
	
	"""
	# confirmation that command has been sent and run - CONFIRMATION CONSTANT = 1
	if (confirmation != 10):
		print ("system error")
		return 0
	"""
	
	return 1
	

def test():
	
	import serial
	ser = serial.Serial('/dev/ttyACM0', 9600)
	
	# read from Arduino
	inputIn = ser.read()
	print ("Read input " + inputIn.decode("utf-8") + " from Arduino.")

	# write something back
	ser.write(b'A')

	# read response back from Arduino
	for i in range (0, 255):
		inputIn = ser.read()
		input_number = ord(inputIn)
		print ("Read input back: " + str(input_number))

test()

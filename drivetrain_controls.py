class DriveTrainControls:
	
	#######################
	# 
	# INSTANCES:
	#	sensorPairA, sensorPairB (corners) - FUTURE ITERATION 
	#	wheelPairA,  wheelPairB	 (corners) - Arduinos controlling motors across from each other (List)
	#	turntable (?)
	#
	# ASSUMMPTIONS:
	#	obstacles are not considered in this algorithm iteration
	#	turntable not a factor at the moment
	#######################
	
	def driveToLocation (direction):
		
		print ("in driveToLocation, driving " + direction.direct + ".")
		
		# direct drivetrain to the left
		if (direction.direct == "LEFT"):
			wheelPairA.driveLeft(direction)
			wheelPairB.driveLeft(direction)
				
		# direct drivetrain to the right
		elif (direction.direct == "RIGHT"):
			wheelPairA.driveRight(direction)
			wheelPairB.driveRight(direction)
	
	# USE MOTOR SPECS TO DETERMINE ANGLES OF ROTATION
	
	
	def rotateToLocation (direction):
		
		# direct drivetrain to rotate in certain direction
		if (direction.rotate == "LEFT"):
			turntable.turnLeft(direction)
		elif (direction.rotate == "RIGHT"):
			turntable.turnRight(direction)
	
		

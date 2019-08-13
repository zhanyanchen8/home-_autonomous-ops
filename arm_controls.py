class ArmControls:
	
	#######################
	#
	# INSTANCES
	#	arm - object modelling the arm
	#	
	#
	#######################
	
	# tell arm to reposition itself so the claw is parallel to ground
	# WHILE still maintaining its horizontal center
	def levelClaw():
		angle = 15 # get claw angle from gyroscope (in degrees) - CHECK SPECS
		
		while (angle >= -2 and angle <= 2): # in degrees
			arm.adjustAngle(angle)
			# bend the arm so claw is within the bounds but still pointing at object (2nd iteration), then check
			angle = 30 # get claw angle from gyroscope (in degrees)
			
			
	#centering to the Y position center
	def moveToLocation(direction):
		arm.reposition(direction)
		levelClaw()
		
		### coordinate values as parameters inside each function to determine how much time/how much to move
		### maybe use another class to manage this like moving drivetrain

"""
14 away, 9 vertical
12 away, 8 vertical
10 away, 7 vertical
8 away, 6 vertical
"""

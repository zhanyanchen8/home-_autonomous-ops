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
		angle = # get claw angle from gyroscope (in radians) - CHECK SPECS
		
		while (angle >= -0.10 and angle <= 0.10):
			arm.adjustAngle(angle)
			# bend the arm so claw is within the bounds but still pointing at object (2nd iteration), then check
			angle = # get claw angle from gyroscope (in radians)
			
			
	#centering to the Y position center
	def moveToLocation(direction):
		arm.reposition(direction)
		levelClaw()
		
		### coordinate values as parameters inside each function to determine how much time/how much to move
		### maybe use another class to manage this like moving drivetrain


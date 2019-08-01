class Directions:
	
	#######################
	#
	# INSTANCES:
	#	String direct
	#	String rotate
	#	float milliseconds
	# 
	# SPECIFICALLY FOR THE DRIVETRAIN
	#
	#######################
	
	def __init__ (d, r, px):
		self.direct = d
		self.rotate = r
		self.milliseconds = linearTime(px)
	
	#function to calculate number of milliseconds to travel in given num Pixels in desired direction (x/y) 
	#BEWARE OF DATA LOSS
	def linearTime(px):
		distanceAway = # get distance sensor data from camera, convert to inches as necessary
		pixelsPerInch = ((float)(640))/distanceAway
		distanceToMove = px/pixelsPerInch
		
		# grab motor spec to determine speed of motors (rotation)
		
		
		time = # final calculations here
		return time
		
	
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
		
		# direct drivetrain to the left
		if (direction.direct == "LEFT"):
			wheelPairA.driveLeft(direction)
			wheelPairB.driveLeft(direction)
				
		# direct drivetrain to the right
		elif (direction.direct == "RIGHT"):
			wheelPairA.driveRight(direction)
			wheelPairB.driveRight(direction)
	
	"""	USE MOTOR SPECS TO DETERMINE ANGLES OF ROTATION
	
	def rotateToLocation (direction):
		
		# direct drivetrain to rotate in certain direction
		while (
		if (direction.rotate == "LEFT"):
			turntable.turnLeft(direction)
		elif (direction.rotate == "RIGHT"):
			turntable.turnRight(direction);
		#fill in the blank with command
		
	"""
		
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
			# bend the arm so claw is within the bounds, then check
			angle = # get claw angle from gyroscope (in radians)
			
	
	#centering to the Y position center
	def moveToCenter():
		
		boundingCenter = # extract bounding box center, y coordinate here
		screenCenterY = (float)(480)/2;
		difference = boundingCenter - screenCenterY
		while (abs(difference) >= 10):
			if (difference > 0):
				arm.moveUp(difference)
			else:
				arm.moveDown(difference)
		
		### coordinate values as parameters inside each function to determine how much time/how much to move
		### maybe use another class to manage this like moving drivetrain


def main():
	

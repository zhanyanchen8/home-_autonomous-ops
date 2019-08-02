class Directions:
	
	#######################
	#
	# INSTANCES:
	#	String direct - direction to linearly move drivetrain in
	#	String rotate - direction to rotate in
	#	float degrees - number of degrees for the motor to turn
	# 
	# SPECIFICALLY FOR THE DRIVETRAIN
	#
	#######################
	
	def __init__ (d, r, px):
		self.direct = d
		self.rotate = r
		self.degrees = getDegrees(px)
	
	#function to calculate number of milliseconds to travel in given num Pixels in desired direction (x/y) 
	#BEWARE OF DATA LOSS
	def getDegrees(px):
		distanceAway = # get distance sensor data from camera, convert to inches as necessary
		pixelsPerInch = ((float)(640))/distanceAway
		distanceToMove = px/pixelsPerInch
		
		# grab motor spec information to determine how many degrees to approach (rotation)
		
		
		degrees = 
		return degrees
		


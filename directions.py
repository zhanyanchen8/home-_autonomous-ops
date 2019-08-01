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
		


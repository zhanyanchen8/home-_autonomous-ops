class Directions:
	
	#######################
	#
	# INSTANCES:
	#	String direct - direction to linearly move drivetrain in
	#	String rotate - direction to rotate in
	#	float distance - distance to travel
	#	float degrees - degrees to rotate
	# 
	# SPECIFICALLY FOR THE DRIVETRAIN
	#
	#######################
	
	#function to calculate number of inches to travel in given num Pixels in desired direction (x/y) 
	#BEWARE OF DATA LOSS
	def getDistance(self, px):
		distanceAway = 5 # get distance sensor data from camera, convert to inches as necessary
		pixelsPerInch = ((float)(640))/distanceAway
		distanceToMove = px/pixelsPerInch
		
		return distanceToMove
		
	def __init__ (self, d, r, px, deg):
		self.direct = d
		self.rotate = r
		self.distance = self.getDistance(px)
		self.degrees = 0
		if (deg > 15 and deg < 240):
			self.degrees = deg
	
	
		


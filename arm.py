class Arm:
	
	#######################
	#
	# INSTANCES:
	#	String direct
	#	String rotate
	#	float degrees # representative of the number of degrees motor needs to turn to achieve distance
	# 
	# SPECIFICALLY FOR THE ARM
	#
	#######################
	
	def __init__(d, r, px):
		self.direct = d
		self.rotate = r
		self.degrees = getDegrees(px)
	
	def getDegrees (px):
		distanceAway = # get distance sensor data from camera, convert to inches as necessary
		
		# translating pixel value to height to travel value
		
	# ...
	
	def reposition():
		
	

	

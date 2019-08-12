import communications

class Turntable:
	
	#######################
	#
	# INSTANCES:
	#	String id3 (id for motor controlling turntable)
	# 	float tableRadius
	#
	#######################
	
	def __init__(identification, r):
		self.id3 = identification
		self.tableRadius = r
	
	def turnLeft(direction):
		
		print ("turning left")
		#to do here: send serial commands to id3-listed motor
		
	def turnRight(direction):
		
		print ("turning right")
		
		#to do here: send serial commands to id3-listed motor
		

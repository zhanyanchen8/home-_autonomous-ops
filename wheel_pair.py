import math
import directions
import communications

class wheel_pair:
	
	#######################
	#
	# INSTANCES:
	#	String id1, id2 (ids for motors connecting to the wheels)
	# 	float wheelRadius
	#	float circumference
	#
	#######################
	
	def __init__(self, identification1, identification2, radius):
		id1 = identification1
		id2 = identification2
		wheelRadius = radius
		self.circumference = 2 * radius * math.pi
		
		
	def driveLeft(self, direction):
		cnt = -1 * self.getCnt(direction)
		
		print ("driving left, cnt = " + str(cnt) + ".")
		
		#right here - send data to the arduino to execute the action
		# to id1 and id2 wheel identification
		
		
	def driveRight(self, direction):
		cnt = self.getCnt(direction)
		
		print ("driving right, cnt = " + str(cnt) + ".")
		#right here - send data to the arduino to execute the action
		# to id1 and id2 wheel identification
	
	
	def getCnt(self, direction):
		cpr = 2994.6
		return (direction.distance/self.circumference) * cpr
		
		
		
		

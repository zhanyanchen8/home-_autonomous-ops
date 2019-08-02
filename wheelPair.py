import math
import directions

class wheelPair:
	
	#######################
	#
	# INSTANCES:
	#	String id1, id2 (ids for motors connecting to the wheels)
	# 	float wheelRadius
	#	float circumference
	#
	#######################
	
	def __init__(identification1, identification2, radius):
		self.id1 = identification1
		self.id2 = identification2
		self.wheelRadius = radius
		self.circumference = 2 * radius * math.pi
		
		
	def driveLeft(direction):
		cnt = -1 * getCnt(direction)
		
		#right here - send data to the arduino to execute the action
		# to id1 and id2 wheel identification
		
		
	def driveRight(direction):
		cnt = getCnt(direction)
		
		#right here - send data to the arduino to execute the action
		# to id1 and id2 wheel identification
	
	
	def getCnt(direction):
		cpr = 2994.6
		return (direction.distance/circumference) * cpr
		
		
		
		

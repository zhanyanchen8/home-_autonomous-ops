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
	
	def __init__(identification1, identification2, radius):
		id1 = identification1
		id2 = identification2
		wheelRadius = radius
		circumference = 2 * radius * math.pi
		
		
	def driveLeft(direction):
		cnt = -1 * getCnt(direction)
		
		print ("driving left, cnt = " + str(cnt) + ".")
		
		#right here - send data to the arduino to execute the action
		# to id1 and id2 wheel identification
		
		
	def driveRight(direction):
		cnt = getCnt(direction)
		
		print ("driving right, cnt = " + str(cnt) + ".")
		#right here - send data to the arduino to execute the action
		# to id1 and id2 wheel identification
	
	
	def getCnt(direction):
		cpr = 2994.6
		return (direction.distance/circumference) * cpr
		
		
		
		

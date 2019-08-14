import directions
import drivetrain_controls
import arm_controls
import wheel_pair
import turntable
# import communications

import sys
sys.path.append("/home/arl/Documents/homeplus_autonomous-ops/jetson/python/examples")
import detection_camera

import thread

print ("imports complete")

global objectPickedUp
objectPickedUp = False

# HERE - use list of motors to begin instantiating objects (wheelPairs, turntable, arm, etc.)
wp1 = wheel_pair.wheel_pair(1, 3, 2)
wp2 = wheel_pair.wheel_pair(2, 4, 2)

def grabObject():
	return objectPickedUp

def calculateRotationAngle(distInches, turntable):
	return (float)(distInches)/(turntable.tableRadius) * 360

def getDistance(px):
	distanceAway = 5 # get distance sensor data from camera, convert to inches as necessary
	pixelsPerInch = ((float)(640))/distanceAway
	distanceToMove = px/pixelsPerInch
		
	return distanceToMove
				
def main():
	
	objectPickedUp = False

	while (not objectPickedUp):
		toMove = detection_camera.main()
		
		#toMove = (100, -52)
		
		if (toMove == None):
			print ("error - check detection_camera.py program")
			break
			
		else:
			
			# horizontal movement using the drivetrain
			horizontalDirection = ""
			rotateDirection = ""
			if (toMove[0] < 0):
				horizontalDirection = "LEFT"
				rotateDirection = "LEFT"
			else:
				horizontalDirection = "RIGHT"
				rotateDirection = "RIGHT"
			
			pixelsHorizontal = abs(toMove[0])
			#rotateAmt = calculateRotationAngle(getDistance(pixelsHorizontal)) # fill in the blank here for calculations of degrees to rotate
			#error in line above calling method in different class
			
			rotateAmt = 0
			direction1 = directions.Directions(horizontalDirection, rotateDirection, pixelsHorizontal, rotateAmt)
			
			drivetrain_controls.driveToLocation(wp1, wp2, direction1)
			
			"""
			# integrate movements together through concurrency
			# manipulate arm
			verticalDirection = ""
			if (toMove[1] < 0):
				verticalDirection = "UP"
			else:
				verticalDirection = "DOWN"
			
			pixelsVertical = abs(toMove[1])
			
			directions2 = directions(verticalDirection, rotate, pixelsVertical)
			
			arm_controls.levelClaw()
			arm_controls.moveToCenter(directions2)
			"""
			
		objectPickedUp = grabObject()

main()

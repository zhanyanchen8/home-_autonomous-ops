import directions
import drivetrain_controls
import arm_controls
from jetson-inference.python.examples import detection_camera

print ("imports complete")

objectPickedUp = False

while (not objectPickedUp):
	toMove = detection_camera.main()
	
	if (toMove == None):
		print ("error - check detection_camera.py program")
		break
		
	else:
		
		# horizontal movement using the drivetrain
		horizontalDirection = ""
		if (toMove[0] < 0):
			horizontalDirection = "LEFT"
		else:
			horizontalDirection = "RIGHT"
		
		rotate = None
		# fill in the blank of rotate here
		
		pixelsHorizontal = abs(toMove[0])
		
		direction1 = directions(horizontalDirection, rotate, pixelsHorizontal)
		
		drivetrain_controls.driveToLocation(direction1)
		
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
		
	objectPickedUp = grabObject()

	
		
		

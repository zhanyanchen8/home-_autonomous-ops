#!/usr/bin/python
#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
# https://rawgit.com/dusty-nv/jetson-inference/python/docs/html/python/jetson.inference.html

import jetson.inference
import jetson.utils
import argparse
import directions
import drivetrain_controls
import arm_controls
import wheel_pair
import turntable
import time

"""
import sys
sys.path.append("/home/arl/Documents/homeplus_autonomous-ops/")
import controls
"""

"""
from threading import Event
import threading
event = threading.Event()
"""

"""
global lockReleased
lockReleased = False
#lockReleased = True
"""

def calcMvt (detection, screen_center):
	move_x = detection.Center[0] - screen_center[0]
	move_y = detection.Center[1] - screen_center[1]
	
	return (move_x, move_y)

###################################################
"""
import sys
sys.path.append("/home/arl/Documents/homeplus_autonomous-ops/jetson/python/examples")
import detection_camera
"""

from threading import Thread, RLock, Event
import threading
print ("imports complete")

global objectPickedUp
objectPickedUp = False

cameraEvent = threading.Event()
cameraEvent.clear()

controlsEvent = threading.Event()
controlsEvent.clear()

global toMove
toMove = (0,0)

# HERE - use list of motors to begin instantiating objects (wheelPairs, turntable, arm, etc.)
wp1 = wheel_pair.wheel_pair(1, 3, 2)
wp2 = wheel_pair.wheel_pair(2, 4, 2)
###################################################


def camera_detection():
	
	while (not controlsEvent.isSet()):
		# set event such that this event is the only one that can run		
		print ("EVENT ABOUT TO BE SET BY CAMERA")
		cameraEvent.set()
		print ("EVENT SET BY CAMERA")
			
		print ("in detection_camera")
		
		# parse the command line
		parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
								   formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage())

		parser.add_argument("--network", type=str, default="ssd-mobilenet-v1", help="pre-trained model to load, see below for options")
		parser.add_argument("--threshold", type=float, default=0.6, help="minimum detection threshold to use")
		parser.add_argument("--camera", type=str, default="/dev/video0", help="index of the MIPI CSI camera to use (NULL for CSI camera 0)\nor for VL42 cameras the /dev/video node to use.\nby default, MIPI CSI camera 0 will be used.")
		parser.add_argument("--width", type=int, default=640, help="desired width of camera stream (default is 640 pixels)")
		parser.add_argument("--height", type=int, default=480, help="desired height of camera stream (default is 480 pixels)")

		opt, argv = parser.parse_known_args()

		# load the object detection network
		net = jetson.inference.detectNet(opt.network, argv, opt.threshold)

		# create the camera and display
		camera = jetson.utils.gstCamera(opt.width, opt.height, opt.camera)
		display = jetson.utils.glDisplay()

		# process frames until user exits
		while display.IsOpen() and not controlsEvent.isSet() and cameraEvent.isSet():
			
			# capture the image
			img, width, height = camera.CaptureRGBA()

			# detect objects in the image (with overlay)
			detections = net.Detect(img, width, height)

			# print the detections
			print("detected {:d} objects in image".format(len(detections)))
			
			for detection in detections:
				print(detection)
				print(net.GetClassDesc(detection.ClassID))
				
				print(detection.Center)
				screen_center = (640/2, 480/2)
				
				if (detection.ClassID == 44):
					global toMove
					toMove = (detection.Center[0] - screen_center[0], detection.Center[1] - screen_center[1])
			
					# prevent this event  from running
					cameraEvent.clear()
					print (cameraEvent.isSet())
					controlsEvent.set()
					print ("EVENT CLEARED BY DETECTION_CAMERA")
					display.closeDisplay()
					return
					
			# render the image
			display.RenderOnce(img, width, height)

			# update the title bar
			display.SetTitle("{:s} | Network {:.0f} FPS".format(opt.network, 1000.0 / net.GetNetworkTime()))

			# synchronize with the GPU
			if len(detections) > 0:
				jetson.utils.cudaDeviceSynchronize()

			# print out performance info
			# net.PrintProfilerTimes()

def calculateRotationAngle(distInches, turntable):
	return (float)(distInches)/(turntable.tableRadius) * 360

def getDistance(px):
	distanceAway = 5 # get distance sensor data from camera, convert to inches as necessary
	pixelsPerInch = ((float)(640))/distanceAway
	distanceToMove = px/pixelsPerInch
		
	return distanceToMove
				
def main():
	
	objectPickedUp = False
	global toMove
	
	while (True):
		
		print (controlsEvent.isSet())
		
		cameraEvent.set()
		while (cameraEvent.isSet()):
			camera_detection()
		
		while (controlsEvent.isSet()):
			
			controlsEvent.set()
			print ("EVENT NOW IN CONTROLS")
			
			if (toMove == None):                                                             
				print ("error - check detection_camera.py program")
				break
			
			else: 
				print ("------------------------------------------------ ABOUT TO SET VARIABLES ------------------------------------------------")
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
				#rotateAmt = calculateRota/home/arl/Downloads/homeplus_autonomous-ops/turntable.pyionAngle(getDistance(pixelsHorizontal)) # fill in the blank here for calculations of degrees to rotate
				#error in line above calling method in different class
				
				rotateAmt = 0
				direction1 = directions.Directions(horizontalDirection, rotateDirection, pixelsHorizontal, rotateAmt)
				print ("directions created")
				
				drivetrain_controls.driveToLocation(wp1, wp2, direction1)
				print ("drivetrain control done")
				
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
				
				objectPickedUp = False
				
				print ("------------------------------------------------ END OF CONTROLS LOOP ------------------------------------------------")
			
			controlsEvent.clear()
			print ("EVENT CLOSED IN CONTROLS")
				
		#t1.join()
	
	print ("END. fin")

main()

# /home/arl/Documents/homeplus_autonomous-ops/jetson/utils/display - change the method in here OR attempt to utilize the display method


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
import time

import sys
sys.path.append("/home/arl/Documents/homeplus_autonomous-ops/")
import directions

#import Set

global toMove
toMove = (0,0)

"""
STARTS UP OBJECT DETECTOIN MODULE FROM THE JETSON

Take in an <i>object</i> set and uses camera_detection to determine
if a particular objects has been found or not

More Information/Cloning GitHub Repository: https://github.com/dusty-nv/jetson-inference
"""
def camera_detection(objects):	
		
	# parse the command line
	parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
							   formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage())

	parser.add_argument("--network", type=str, default="ssd-mobilenet-v1", help="pre-trained model to load, see below for options")
	parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")
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
	
	while display.IsOpen():
		
		# capture the image
		img, width, height = camera.CaptureRGBA()

		# detect objects in the image (with overlay)
		detections = net.Detect(img, width, height)
		
		for detection in detections:
			#print(detection)
			print(net.GetClassDesc(detection.ClassID))
			print(detection.Center)
			screen_center = (640/2, 480/2)
			
			# determine and change toMove value if bottle (ClassID 44) is found
			if (net.GetClassDesc(detection.ClassID) in objects and detection.Confidence > 0.8):
				global toMove
				toMove = (detection.Center[0] - screen_center[0], detection.Center[1] - screen_center[1])
				return net.GetClassDesc(detection.ClassID)
				
		# render the image
		display.RenderOnce(img, width, height)

		# update the title bar
		display.SetTitle("{:s} | Network {:.0f} FPS".format(opt.network, 1000.0 / net.GetNetworkTime()))

		# synchronize with the GPU
		if len(detections) > 0:
			jetson.utils.cudaDeviceSynchronize()

"""
MAIN METHOD USED TO OPERATE THE CONTROLS OF THE ROBOT

takes in string of objects to find from Arduino via Serial and 
returns...
"""
def main():
	
	# setting up new variables
	#import serial
	#ser = serial.Serial('/dev/ttyACM0', 9600)
	objectFound = False
			
	global toMove	
	if (toMove == None):                                                             
		print ("toMove issue")
		return
	
	# parse through string detailing objects to find, saving each in a set	
	toFind = set()
	#objects = ser.read()
	objects = "bottle,cup,"
	i = 0
	
	while (not (i == len(objects) - 1)):
		endIndex = objects.find(",", i)
		if (endIndex == -1):
			break
		print (objects[i:endIndex])
		toFind.add(objects[i:endIndex])
		i = endIndex + 1;	
	
	print ("end parsing, about to find")
	verified = camera_detection(toFind)
	
	print (verified)
	print (toMove)

main()

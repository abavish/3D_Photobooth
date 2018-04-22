# Code reference: Alexander Baran-Harper 
# https://www.youtube.com/watch?v=1eAYxnSU2aw

from time import sleep
from datetime import datetime
from sh import gphoto2 as gp
import signal, os, subprocess

# kill gphoto process that starts whenever 
# we connect the camera

#gphoto2 --set-config capturetarget=1 
#above command is to set default storage on camera


def killPTPcameraProcessLeft() :
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()

	# Search for the line which has the process we have to kill
	for line in out.splitlines():
		if b'PTPCamera' in line:
			#Kill the process
			#get the PID which is the first column
			pid = int(line.split(None,1) [0])
			os.kill(pid, signal.SIGKILL)

#shot_date = datetime.now().strftime("%Y-%m-%d")
#shot_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#picID = "PyBooth"

#clear existing photos on the left camera and then proceed
#modified code to add in port as a parameter
clearCommandLeft = ["--port=usb:020,004", "--folder", "/store_00020001/DCIM/100EOS7D", \
				"-R", "--delete-all-files"]
triggerCommandLeft = ["--port=usb:020,004", "--trigger-capture"]
downloadCommandLeft = ["--port=usb:020,004", "--get-all-files"]
folderNameLeft = "Left"
saveLocationLeft = "/Users/Vishal/Downloads/Canon/" + folderNameLeft


def createSaveFolderLeft():
	try:
		os.makedirs(saveLocationLeft)
	except:
		print("Failed to create the new repository")
	os.chdir(saveLocationLeft)  


#function to capture the image from both cameras
def captureImageLeft():
	gp(triggerCommandLeft)
	sleep(1)
	gp(downloadCommandLeft)
	gp(clearCommandLeft)


#does not overwirite, hence we need to clear the repository first.
# before clearing repository first copy to another folder
def renameFilesLeft():
	for filename in os.listdir("."):
		if len(filename) < 13:
			if filename.endswith(".JPG"):
				os.rename(filename, ("Left.JPG"))#ID is the parameter of the function
				#print("Renamed the JPG")
			
killPTPcameraProcessLeft()
gp(clearCommandLeft)
createSaveFolderLeft()
captureImageLeft()
renameFilesLeft()



import subprocess
from time import sleep

def runLeftCapture():
	cmd1 = 'python3 imageCaptureLeft.py'
	test = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
	output, err = test.communicate()

def runRightCapture():
	cmd2 = 'python3 imageCaptureRight.py'
	anaglyphFile = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)
	out, err = anaglyphFile.communicate()

def runAnaglyph():
	cmd3 = 'python Anaglyph_image.py'
	anaglyphFile = subprocess.Popen(cmd3, stdout=subprocess.PIPE, shell=True)
	out, err = anaglyphFile.communicate()

#sleep(5)
runLeftCapture()
runRightCapture()
runAnaglyph()
import os
import librosa
import numpy as np
import os, sys
import time
import logging

def printh(strInput):
	print "\n" , strInput , "<br>"
	time.sleep(.1)

def main(args):
	# script setup and housekeeping
	#
	logging.basicConfig(
		filename = "Log.txt",
		level = logging.DEBUG, 
		format = '[Python Web Backend] %(levelname)-7.7s %(message)s'
	)
	
	logging.info("MMDP Web Service - *Started* @ %s" % time.ctime())
	
	printh("System Arguments:")
	printh("---------------------------")
	printh(args)
	printh("")
	
	printh("Python - Live Output Test:")
	printh("---------------------------")
	
	for x in range(5):
		printh("Round: " + str(x + 1))
		printh("Done In:  " + str(5-x))
		printh("")
		time.sleep(.5)
		
	printh("Goodbye, from PYTHON")
	printh("**DONE**")
	logging.info("MMDP Web Service - *Finished* @ %s" % time.ctime())

if __name__ == '__main__':
    main(sys.argv)
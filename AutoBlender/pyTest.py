import os
import librosa
import numpy as np
import os, sys
import time
import logging

def printh(strInput):
	return strInput

def main(args):
	# script setup and housekeeping
	#
	logging.basicConfig(
		filename = "Out.txt",
		level = logging.DEBUG, 
		format = '[webPy]: %(message)s'
	)
	
	logging.info("Python Web Service Test - *Started* @ %s" % time.ctime())
	
	logging.info(printh("System Arguments:"))
	logging.info(printh("---------------------------"))
	logging.info(args)
	logging.info(printh(""))
	
	logging.info(printh("Python - Live Output Test:"))
	logging.info(printh("---------------------------"))
	
	for x in range(5):
		logging.info(printh("Round: " + str(x + 1)))
		logging.info(printh("Done In:  " + str(5-x)))
		logging.info(printh(""))
		time.sleep(2)
		
	logging.info(printh("Goodbye, from PYTHON"))
	logging.info(printh("**DONE**"))
	logging.info("Python Web Service Test - *Finished* @ %s" % time.ctime())

if __name__ == '__main__':
    main(sys.argv)
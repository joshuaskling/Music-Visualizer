import os
import logging
import time
import sys

logging.basicConfig(
	filename = "Log.txt",
	level = logging.DEBUG, 
	format = '[Python Web Backend] %(levelname)-7.7s %(message)s'
)

logging.info("MMDP Web Service Initialized at: %s" % time.ctime())
print("<br>")
for x in range(5):
	print("Round: " + str(x))
	print("\n<br>")
	print("Waiting: " + str(5-x))
	print("<br>")
	print("<br>")
	time.sleep(1)
print("Goodbye, from PYTHON")
print("^^ BYE!!! ^^")

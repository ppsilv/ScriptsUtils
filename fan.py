#Version : 0.0.1 - Initial version.
#Version : 0.0.2 - Fixed bug, app was writting several times fan on or fan off into syslog.


from gpiozero import CPUTemperature
from time import sleep
import logging
import logging.handlers

version = "1.0.1"
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

my_logger.addHandler(handler)

try:
	import RPi.GPIO as gpio
except RuntimeError:
	my_logger.critical("Error: Impossible to import GPIO")

#gpio.setmode(gpio.BOARD)
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#cpuTempMax=55.0
#cpuTempWork=45.0
cpuTempMax=60.0
cpuTempWork=50.0



gpio.setup(17, gpio.OUT)
my_logger.debug("fan: running ...")
fanRunning = False
while True:
	cpuTemp = CPUTemperature()
	if cpuTemp.temperature >= cpuTempMax:
            if fanRunning == False:
               gpio.output(17, 1)		
               my_logger.debug("fan: on ...")
               fanRunning =True
	if cpuTemp.temperature <= ( cpuTempWork ):
            if fanRunning == True:
               gpio.output(17, 0)
               my_logger.debug("fan: off ...")
               fanRunning = False
	sleep(5)

try:
        import RPi.GPIO as gpio
except RuntimeError:
        print("Error: Impossible to import GPIO")
import os
import subprocess
import time

def current_milli_time():
  return round(time.time() * 1000)

import logging
import logging.handlers

version = "1.0.1"
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

my_logger.addHandler(handler)


#gpio.setmode(gpio.BOARD)
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

led = 18
pinShutdown = 15
gpio.setup(led, gpio.OUT)
gpio.setup(pinShutdown, gpio.IN)

ledAceso = 0.5
ledApagado = 1.5
ledStatus = False
ledLastTime = current_milli_time()

millisecond = 0

my_logger.debug("pisca2: *******************************************************************************************...")
my_logger.debug("pisca2:                            System pisca initialing...")

def readbutton():
    status = gpio.input(pinShutdown)
    if status == 0:
        print("shuting system down: status=", status)
        my_logger.debug("pisca2: *******************************************************************************************...")
        my_logger.debug("pisca2:                         shuting system down...")
        with open(os.devnull, "wb") as limbo:
          ret=subprocess.Popen(["shutdown", "-h", "now"],stdout=limbo, stderr=limbo).wait()

while True:
    gpio.output(led, 0)
    time.sleep(ledAceso)
    
    readbutton()

    gpio.output(led, 1)
    time.sleep(ledApagado)

    readbutton()

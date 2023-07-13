try:
        import RPi.GPIO as gpio
except RuntimeError:
        print("Error: Impossible to import GPIO")
import os
import subprocess
import time
import threading

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
aceso = 1000
apagado = 1000



millisecond = 0

my_logger.debug("pisca2: *******************************************************************************************...")
my_logger.debug("pisca2:                            System pisca initializing...")

def readbutton():
    status = gpio.input(pinShutdown)
    if status == 0:
        print("shuting system down: status=", status)
        my_logger.debug("pisca2: *******************************************************************************************...")
        my_logger.debug("pisca2:                         shuting system down...")
        with open(os.devnull, "wb") as limbo:
          ret=subprocess.Popen(["shutdown", "-h", "now"],stdout=limbo, stderr=limbo).wait()

def piscaLed(var):
  global led, ledApagado, LedAceso  
  while True:
    gpio.output(led, 0)
    time.sleep(ledApagado)
    
    gpio.output(led, 1)
    time.sleep(ledAceso)



def piscaLed2():
  global led, ledStatus, ledLastTime, apagado, aceso  
  while True:  
    if ledStatus == False:
        if ( ledLastTime + apagado ) < current_milli_time():
            ledLastTime = current_milli_time()
            ledStatus = True
            gpio.output(led, 0)
    else:
        if ( ledLastTime + aceso ) < current_milli_time():
            ledLastTime = current_milli_time()
            ledStatus = False
            gpio.output(led, 1)
    readbutton()

ledLastTime = current_milli_time()
print("ledLastTime ",ledLastTime)
time.sleep(1)
ledLastTime = current_milli_time()
print("ledLastTime ",ledLastTime)

x = threading.Thread(target=piscaLed, args=(1,))
x.start()

while True:
    readbutton()
    time.sleep(0.1)


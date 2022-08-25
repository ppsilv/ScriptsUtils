try:
	import RPi.GPIO as gpio
except RuntimeError:
	print("Error: Impossible to import GPIO")

#gpio.setmode(gpio.BOARD)
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(17, gpio.OUT)

gpio.output(17, 1)


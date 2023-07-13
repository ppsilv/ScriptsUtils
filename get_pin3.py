try:
        import RPi.GPIO as gpio
except RuntimeError:
        print("Error: Impossible to import GPIO")

import time

#gpio.setmode(gpio.BOARD)
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

porta = 3
gpio.setup(3, gpio.IN)


while True:
  status = gpio.input(3)
  print("Valor do status")
  print(status)
  time.sleep(1)


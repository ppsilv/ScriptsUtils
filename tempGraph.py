from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

cpu = CPUTemperature()

tempAnterior=cpu.temperature

plt.ion()
x = []
y = []

def write_temp(temp):
    with open("/home/pi/cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()

while True:
    temp = cpu.temperature
    if (temp - tempAnterior) > 5 or (tempAnterior - temp) > 5:
        write_temp(temp)
#    graph(temp)
    plt.pause(1)



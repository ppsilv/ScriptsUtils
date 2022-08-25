from ina219 import INA219
from ina219 import DeviceRangeError
import logging
import logging.handlers
import time
import os

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

my_logger.addHandler(handler)

my_logger.debug('Voltage verification...')
#_logger.critical('this is critical')



SHUNT_OHMS = 0.05


def read():
    """Define method to read information from coulometer."""
    ina = INA219(SHUNT_OHMS)
    ina.configure()
    my_logger.debug("Bus Voltage: %.3f V" % ina.voltage())
    try:
        my_logger.debug("Bus Current: %.3f mA" % ina.current())
        my_logger.debug("Power: %.3f mW" % ina.power())
        my_logger.debug("Shunt voltage: %.3f mV" % ina.shunt_voltage())
    except DeviceRangeError as e:
        my_logger.debug(e)

if __name__ == "__main__":

    while True:    
        read()
        stream = os.popen('vcgencmd measure_temp')
        output = stream.read()
        my_logger.debug(output)
        time.sleep(60)


import logging
from x10.controllers.cm11 import CM11
if __name__ == "__main__":
    logger = logging.getLogger()
    hdlr = logging.StreamHandler() # Console
    formatter = logging.Formatter('%(module)s - %(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.DEBUG)
    
    dev = CM11('/dev/ttyUSB0')
    dev.open()
    test = dev.actuator('A3')
    test.on()

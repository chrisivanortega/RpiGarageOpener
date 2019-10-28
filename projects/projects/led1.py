
import requests
import time
from gpiozero import LED
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LedOnOff:


    def __init__(self):
        self.api = "http://api.x10host.com/garage"
        self.led = 17
        

    def exe(self):
        led = LED(self.led)
        state = self.getState()
        logger.info('Start reading database')
        if not state[0]:
            records = {'state': state[1], 'error': "reading state"}
            logger.debug('Records: %s', records)

            return
        else:
            state = state[1]
        while(True):
            newstate = self.getState()
            if newstate[0] == True:
                if newstate[1] in ['0','1']:
                    newstate = newstate[1]
                else:
                    logging.info("state error")
                    time.sleep(1)
                    continue
            else:
                continue
            if newstate != state:
                logger.info('state change go an open the door. turning on led: ' + str(self.led))
                # here we are going to ligth up a gpio
                led.on()
                time.sleep(1)
                led.off()

                logger.info('state change go an open the door. turning off led: ' + str(self.led))

                state = newstate
            time.sleep(1)


    def setState(self):
        try:
            r = requests.get(self.api + "/index.php/garage/state/set")
            if r.status_code ==  200:
                return True
            else:
                return False
        except:
            return False
        
    def getState(self):
        try:
            r = requests.get(self.api + "/index.php/garage/state/get")
            if r.status_code ==  200:
                res = r.json()
                return True,res['records']['state']
            else:
                return False,r
        except Exception as e:
            return False,e


if "__main__":
    led = LedOnOff()
    led.exe()

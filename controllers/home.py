from flask import Flask, render_template,jsonify
import time
from gpiozero import LED

class HomeController:
    def __init__(self):
        self.gpio = 17
        self.led = LED(self.gpio)

    def home(self):
        return render_template('button.html')

    def readState(self):
        state = self.led.value
        return jsonify({"state":state,"gpio":self.gpio})

    def toggleGPIO(self):
        self.led.on()
        time.sleep(1)
        self.led.off()
        return jsonify({"action":"finished"})
  
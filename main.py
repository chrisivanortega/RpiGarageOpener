from flask import Flask, render_template,jsonify
from controllers.home import HomeController
hc = HomeController()

app = Flask(__name__)


@app.route('/')
def home():
   return hc.home()

@app.route('/readState')
def readState():
   return hc.readState()

@app.route('/toggleGPIO')
def toggleGPIO():
   return hc.toggleGPIO()


if __name__ == '__main__':
   app.run(host = '0.0.0.0',port = 81)

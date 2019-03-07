from flask import Flask
from flask import render_template
from flask import request
import models
import controllers

app = Flask(__name__)

# Route kodları burda bulunuyor

@app.route("/")
def operation_calendar():
    return controllers.get_operation()

@app.route("/shiftcalendar")
def shift_calendar():
    return controllers.get_shift()

@app.route("/addshift", methods=['GET'])
def getaddshift():
    return controllers.get_addshift()

@app.route("/addshift", methods=['POST'])
def postaddshift():
    return controllers.post_addshift()

@app.route("/addoperation", methods=['GET'])
def getaddoperation():
    return controllers.get_addoperation()

@app.route("/addoperation", methods=['POST'])
def postaddoperation():
    return controllers.post_addoperation()

if __name__ == "__main__":
    app.run(port=8080)
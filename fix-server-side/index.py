from flask import Flask, jsonify, request
from simplefix import FixMessage

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/api/logon")
def simplefix_init():
    msg = FixMessage()
    msg.append_string("8=FIX.4.2")
    msg.append_pair("9", "")
    return 'p', 204
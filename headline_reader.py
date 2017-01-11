from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/headline_reader")

def get_headlines():
    pass

@app.route("/")
def homepage():
    return "Welcome to the homepage!"

@ask.launch
def launch_program():
    open_message = "Hello! Want to hear the news headlines?"
    return question(open_message)

if __name__ == '__main__':
    app.run(debug = True)
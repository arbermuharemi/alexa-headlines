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

@ask.intent("Continue")
def speak_headlines():
    news_headlines = get_headlines()
    news_msg = "These are the top news stories: {}".fromat(news_headlines)
    return statement(news_msg)

@ask.intent("Stop")
def exit_program():
    exit_message = "Okay, thanks for stopping by. See you soon!"
    return statement(exit_message)

if __name__ == '__main__':
    app.run(debug = True)
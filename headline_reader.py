from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/headline_reader")

def get_headlines():
    user_info = {"username":"<INSERT USERNAME HERE>",
                 "password":"<INSERT PASSWORD HERE>",
                 "api_type":"json"}
    session = requests.Session()
    session.headers.update({"User-Agent": "Alexa Headline Reader"})
    reddit_url = "https://reddit.com/"
    session.post(reddit_url + "api/login", data = user_info)
    time.sleep(1)
    html = session.get(reddit_url + "r/worldnews/.json?limit=10")
    data = json.loads(html.content.decode("utf-8"))
    headlines = [unidecode.unidecode(listing["data"]["title"]) for listing in data["data"]["children"]]
    headlines = '...'.join([i for i in headlines])
    return headlines


# for testing purposes
# headlines = get_headlines()
# print(headlines)


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
    news_msg = "These are the top news stories: {}".format(news_headlines)
    return statement(news_msg)

@ask.intent("Stop")
def exit_program():
    exit_message = "Okay, thanks for stopping by. See you soon!"
    return statement(exit_message)

if __name__ == '__main__':
    app.run(debug=True)
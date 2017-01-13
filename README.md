# alexa-headlines
A script that can be used on an Alexa-enabled device that will read the top news headlines from Reddit's r/worldnews

## How to use
* Download or clone the repo
* Open the headline_reader.py in a text editor and insert your reddit username and password
* Run headline_reader.py in command prompt/terminal
* Execute ngrok.exe
* In command prompt/terminal, type ngrok http 5000
* Navigate to the [Amazon Developer Website](https://goo.gl/hl4kwD)
* Follow setup procedures (ensuring to sign up with the Amazon account that is linked to your Alexa device)
* Navigate to Alexa > Alexa Skills Kit > Add a New Skill
* Choose any name and invocation name
* Copy and paste the following intent schema:

```json
{
    "intents": [{
        "intent": "Continue"
    },
                
    {
        "intent": "Stop"
    }]
}
```
* Use any desired utterances. This is the list I used
```
Continue sure
Continue go ahead
Continue yes
Continue okay

Stop no
Stop no thanks
Stop stop
Stop leave
```
* On the next screen, you will need to open the terminal that has the ngrok server information. Copy the https address and append to the end: "/headline_reader"
* Proceed and select the "My development endpoint is a sub-domain ..."
* Now you can use the program! If you don't own an Alexa device, you can test it on [Echoism](https://goo.gl/qePSpx)

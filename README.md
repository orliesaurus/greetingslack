#Greetings Slackers
This simple script written in bad Python will allow you to hook into the real time API of Slack and perform a greeting to every new joiner!
Usually this is used to tell new joiners about the network, the guidelines, rules, useful links etc etc

#Requirements
Python 2.7+
Edit `bot.py` on lines 7-8 to customise with your greeting and token

#Installation
```bash
git clone <thisgitrepo>
cd <thisgitrepo>
virtualenv greetingslack
. greetingslack/bin/activate
pip install requests
pip install websocket-client
python bot.py &
```

#Heroku
Deploy with a click supported now
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)


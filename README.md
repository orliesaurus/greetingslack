#Greetings Slackers
This simple script written in bad Python will allow you to hook into the real time API of Slack and perform a greeting to every new joiner!
Usually this is used to tell new joiners about the network, the guidelines, rules, useful links etc etc

If you like this project and you use it for your community or anything else, please hit the STAR button ⭐️ on the top right side so I know you dig it! It makes me feel appreciated and it's free.

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

Don't forget to scale your worker to 1 as below (notice the one? hit the edit button on the right to scale it to 1)
![Scale](https://dl.dropbox.com/s/stpnk04pi3l5cj4/Screenshot%202015-06-16%2011.35.25.png?dl=0)


# Greetings Slackers
This simple script written in basic Python will allow you to hook into the real time API of Slack and perform a direct message greeting to every new joiner!
Usually this is used to tell new joiners about the network, the guidelines, rules, useful links etc etc

New to programming or don't know how to get started just yet? Don't fret! @izzydoesizzy wrote an amazing step by step, [tutorial with screenshot](https://medium.com/@izzydoesizzy/create-a-slack-bot-that-privately-greets-new-users-in-5-easy-steps-a38eabeabcb5)

If you like this project and you use it for your community or anything else, please hit the STAR button ⭐️ on the top right side so I know you dig it! It makes me feel appreciated and it's free.

If you have questions open an `Issue` (preferred) or reply to the tutorial article

# Requirements
Python 2.7+
Edit `bot.py` on lines 7-8 to customise with your greeting and token

# Installation
```bash
git clone <thisgitrepo>
cd <thisgitrepo>
virtualenv greetingslack
. greetingslack/bin/activate
pip install requests
pip install websocket-client
python bot.py &
```

# Heroku
Deploy with a click supported now

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

🔥 **DONT FORGET TO SCALE YOUR FREE DYNO**

# Q&A

## Q1. How do you change the welcome message?

## A1.
To change the welcome message, edit your Heroku variables:
Go to Heroku's Settings, then  where it says `Config Variables` click `Reveal Config Vars` and it will reveal your message and other fields.  This will restart your Heroku instance pretty quickly and apply the changes for you

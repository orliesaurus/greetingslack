# Rebuilding from 

 https://github.com/slackapi/python-slackclient/blob/master/tutorial/01-creating-the-slack-app.md
 
 :wrench::wrench::wrench::wrench::wrench::wrench:

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
A1.
To change the welcome message, edit your Heroku variables:
Go to Heroku's Settings, then  where it says `Config Variables` click `Reveal Config Vars` and it will reveal your message and other fields.  This will restart your Heroku instance pretty quickly and apply the changes for you

## Q2. How do I know if it worked?
A2.
After setting up the bot, your welcome message will be displayed to every new user, as soon as a they join your Slack network - as a direct message.
Check the example below:

![Example](https://i.snag.gy/YyOLfb.jpg)

## Q3. How do I enable the debug channel?
A3.
In the environment variables set DEBUG_CHANNEL_ID to be the ID of your chosen debug channel. That's usually achieved by using `export DEBUG_CHANNEL_ID=<YOUR SLACK CHANNEL ID>` in your CLI. We suggest to make this channel private so not just anyone can join it.


## Q4. How do I enabled the bot to forward messages sent to it? 
A4. You can tell your greeting bot to forward messages that users send to it to another channel. 

1. [Generate an API Token](https://api.slack.com/custom-integrations/legacy-tokens) for you slack workspace. Set the `SLACK_TOKEN` environment variable to the token. 

  ```
  export SLACK_TOKEN=<WORKSPACE API TOKEN>
  ```
  **Note:** This is a different token then the one needed to configure the bot
2. Create a channel for the bot to post and add the bot to the channel
3. Get the channel id for the channel. Set the `RESPONSE_CHANNEL` environment variable to this. 

  ```
  export RESPONSE_CHANNEL=<channel id>
  ```
  
After setting these variables, the bot will forward messages sent to it by copying the users `real_name` and message content and posting in the `RESPONSE_CHANNEL`. 

**Note:** the `real_name` is used since it is the only name field that always contains a name.


![](https://i.imgur.com/24TzT9a.png)

![](https://i.imgur.com/SH7Fnyv.png)

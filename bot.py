import websocket
import json
import requests
import urllib
import os
import sys
import logging


logging.basicConfig(level=logging.DEBUG,
        stream=sys.stdout)

# Suppress InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

###VARIABLES THAT YOU NEED TO SET MANUALLY IF NOT ON HEROKU#####
try:
        MESSAGE = os.environ['WELCOME_MESSAGE']
        TOKEN = os.environ['SLACK_TOKEN']
        UNFURL = os.environ['UNFURL_LINKS']
        DEBUG_CHANNEL_ID = os.environ.get('DEBUG_CHANNEL_ID', False)
except:
        MESSAGE = 'Manually set the Message if youre not running through heroku or have not set vars in ENV'
        TOKEN = 'Manually set the API Token if youre not running through heroku or have not set vars in ENV'
        UNFURL = 'FALSE'
###############################################################

def is_team_join(msg):
    return msg['type'] == "team_join"

def is_debug_channel_join(msg):
    return msg['type'] == "member_joined_channel" and msg['channel'] == DEBUG_CHANNEL_ID and msg['channel_type'] == 'C'

def parse_join(message):
    m = json.loads(message)
    if is_team_join(m) or is_debug_channel_join(m):
        user_id = m["user"]["id"] if is_team_join(m) else m["user"]
        logging.debug(m)
        x = requests.get("https://slack.com/api/im.open?token="+TOKEN+"&user="+user_id)
        x = x.json()
        x = x["channel"]["id"]
        logging.debug(x)

        data = {
                'token': TOKEN,
                'channel': x,
                'text': MESSAGE,
                'parse': 'full',
                'as_user': 'true',
                }

        logging.debug(data)

        if (UNFURL.lower() == "false"):
          data = data.update({'unfurl_link': 'false'})

        xx = requests.post("https://slack.com/api/chat.postMessage", data=data)
        logging.debug('\033[91m' + "HELLO SENT TO " + m["user"]["id"] + '\033[0m')

#Connects to Slacks and initiates socket handshake
def start_rtm():
    r = requests.get("https://slack.com/api/rtm.start?token="+TOKEN, verify=False)
    r = r.json()
    logging.info(r)
    r = r["url"]
    return r

def on_message(ws, message):
    parse_join(message)

def on_error(ws, error):
    logging.error("SOME ERROR HAS HAPPENED: " + error)

def on_close(ws):
    logging.info('\033[91m'+"Connection Closed"+'\033[0m')

def on_open(ws):
    logging.info("Connection Started - Auto Greeting new joiners to the network")


if __name__ == "__main__":
    r = start_rtm()
    ws = websocket.WebSocketApp(r, on_message = on_message, on_error = on_error, on_close = on_close)
    #ws.on_open
    ws.run_forever()


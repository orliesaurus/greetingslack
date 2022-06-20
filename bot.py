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
        MESSAGE = os.environ.get('WELCOME_MESSAGE')
        TOKEN = os.environ.get('SLACK_TOKEN')
        CHANNEL_TOKEN = os.environ.get('CHANNEL_TOKEN')
        UNFURL = os.environ.get('UNFURL_LINKS')
        RESPONSE_CHANNEL = os.environ.get('RESPONSE_CHANNEL')
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

def is_direct_message(msg):
    print(msg)
    is_bot = False
    if 'bot_id' in msg:
        is_bot = True
    return msg['type'] == "message" and msg['channel'][0] == 'D' and not is_bot

def get_display_name(user_id):
    logging.debug('FINDING USER WITH ID'+user_id)
    users = requests.get("https://slack.com/api/users.list?token="+TOKEN)
    users = users.json()

    for item in users['members']:
        if user_id == item['id']:
            return item['real_name']

def parse_join(message):
    m = json.loads(message)
    if is_team_join(m) or is_debug_channel_join(m):
        user_id = m["user"]["id"] if is_team_join(m) else m["user"]
        logging.debug(m)
        conversation = requests.post("https://slack.com/api/conversations.open?token=" + TOKEN + "&users=" + user_id,
                          data=None).json()
        conversation_channel = conversation["channel"]["id"]
        logging.debug(conversation_channel)

        data = {
                'token': TOKEN,
                'channel': conversation_channel,
                'text': MESSAGE,
                'parse': 'full',
                'as_user': 'true',
                }

        logging.debug(data)

        if (UNFURL.lower() == "false"):
          data.update({'unfurl_link': 'false'})

        post_message_response = requests.post("https://slack.com/api/chat.postMessage", data=data)
        logging.debug('\033[91m' + "HELLO SENT TO " + m["user"]["id"] + '\033[0m')

    if is_direct_message(m):
        logging.debug('DM RECEIVED')
        user_id = m["user"]
        user_message = m['text']
        user_message = urllib.quote(user_message)

        # Need to get the display name from the user_id
        real_name = get_display_name(user_id)

        #logging.DEBUG('SENDING MESSAGE: '+user_message+' TO USER '+real_name)
        # Need to send a message to a channel
        requests.get("https://slack.com/api/chat.postMessage?token="+CHANNEL_TOKEN+"&channel="+RESPONSE_CHANNEL+"&text="+user_message+"&as_user=false&username="+real_name)

#Connects to Slacks and initiates socket handshake
def start_rtm():

    r = requests.get("https://slack.com/api/rtm.connect?token="+TOKEN, verify=False)
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

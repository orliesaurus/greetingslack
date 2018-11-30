import websocket
import json
import requests
import urllib
import os
import sys
import logging


users = requests.get("https://slack.com/api/users.list?token=xoxp-22100655441-397633544705-471849303060-f6c3c8b32309a1a364e317e2b9b4cd3a")
users = users.json()

#for item in users['members']['profile']:
#  print item

userId = 'UDS50FRNU'

for item in users['members']:
  if userId == item['id']:
    print item['real_name']+'wants to kill you\n> fuck off'
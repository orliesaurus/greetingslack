import websocket
import json
import requests
import urllib
import os
import sys
import logging

#for item in users['members']['profile']:
#  print item

def get_display_name(user_id):
  print user_id
  users = requests.get("https://slack.com/api/users.list?token="+TOKEN)
  users = users.json()

  for item in users['members']:
    print item['id']
    if item['id'] == user_id:
      return item['real_name']


uid = 'UEHT0GL14'
print get_display_name(uid)
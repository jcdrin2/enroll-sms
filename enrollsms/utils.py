import os
import re
from models import *
from message_data import message_data
from flask import request, render_template, redirect
from twilio.rest import TwilioRestClient

#utils
def handle_global_response(response):
  return response

def normalize_response(response):
  r = response.strip().lower()
  r = re.sub(r'\W+', '', r)

  #yes/no response for health insurance question
  if r[0] == 'y':
    return 1
  elif r[0] == 'n':
    return -1

  #full name responses for coverage type question
  elif r in ['private', 'kaiser', 'bluecross', 'blueshield', 'blue']:
    return 1
  elif r == 'medical':
    return 2
  elif r == 'sfpath' or r == 'path':
    return 3
  elif r == 'healthysf' or r == 'healthy':
    return 4
  
  #integer responses for coverage type question
  elif r.isdigit() and r in range(1, 5):
    return int(r)

  #invalid response
  else:
    return False

def user_valid_response(u, n_response):
  return True

def get_or_create_user(phone_number):
  u = User.query.filter(User.phone_number == phone_number).first()
  u = u if u else User(phone_number = phone_number)
  db.session.add(u)
  return u

def send_message_to_user(u, key, clarification=False):
  #send msg
  text = render_template(key + '.html')
  send_sms(u.phone_number, text)
  
  #set state
  next_message = message_data[key]['next_message']
  u.state = 'AWAITING-RESPONSE' if next_message else 'DONE'

  #save
  u.last_message = key
  db.session.add(u)
  return text

def send_sms(phone_number, body):
  account_sid = os.environ['ACCOUNT_SID']
  auth_token = os.environ['AUTH_TOKEN']
  from_number = os.environ['TWIL_NUMBER']
  client = TwilioRestClient(account_sid, auth_token)
  client.sms.messages.create(to=phone_number,
                              from_=from_number,
                              body=body)
import os
from models import *
from message_data import message_data
from flask import request, render_template, redirect
from twilio.rest import TwilioRestClient

#utils
def handle_global_response(response):
  return response

def normalize_response(response):
  return int(response)

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
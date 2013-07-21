from enrollsms import app
from models import *
from utils import *
from message_data import message_data
from flask import request

@app.teardown_request
def shutdown_session(exception=None):
	try:
		db.session.commit()
		db.session.remove()
	except:
		db.session.rollback()

@app.route('/')
def index():
  return 'enroll-sms home'

@app.route('/sms')
def sms():
  response = handle_global_response(request.values.get('Body'))
  u = get_or_create_user(request.values.get('From'))

  while True:
    if u.state == 'READY':
      return send_message_to_user(u, 'q-health-insurance')
    
    elif u.state == 'AWAITING-RESPONSE':
      n_response = normalize_response(response)

      #valid msg > send next one
      if user_valid_response(u, n_response):
        next_message = message_data[u.last_message]['next_message'][n_response]
      #invalid msg > resend last one
      else:
        next_message = u.last_message
      return send_message_to_user(u, next_message)

    elif u.state == 'DONE':
      # for now keep looping finished users
      u.state = 'READY'
      db.session.add(u)
      break

  return 'unrecognized state'

@app.route('/users')
def users():
  u = User.query.first()
  return str(u.phone_number)
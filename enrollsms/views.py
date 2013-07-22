from enrollsms import app
import time
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
  return render_template('index.html')

@app.route('/sms')
def sms():
  response = request.values.get('Body')
  u = get_or_create_user(request.values.get('From'))

  while True:
    if u.state == 'READY':
      send_sms(u.phone_number, render_template('welcome.html'))
      time.sleep(3)
      return send_message_to_user(u, 'q-health-insurance')
    
    elif u.state == 'AWAITING-RESPONSE':
      n_response = normalize_response(response)

      #valid msg > send next one
      if n_response:
        return send_message_to_user(u, message_data[u.last_message]['next_message'][n_response])
      #invalid msg > resend last one
      else:
        return send_message_to_user(u, u.last_message, clarification=True)

    elif u.state == 'DONE':
      # for now keep looping finished users
      u.state = 'READY'
      db.session.add(u)

  return 'unrecognized state'

@app.route('/users')
def users():
  u = User.query.first()
  return str(u.phone_number)
from enrollsms import app
import twilio.twiml
import os
from models import *
from flask import request, render_template, redirect
from twilio.rest import TwilioRestClient

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
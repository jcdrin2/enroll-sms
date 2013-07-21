import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['DEBUG'] = os.environ['DEBUG']
db = SQLAlchemy(app)

import enrollsms.views
import enrollsms.models

if os.environ['ENV'] == 'dev':
  db.drop_all()
  db.create_all()
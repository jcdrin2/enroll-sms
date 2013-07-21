from enrollsms import db
from sqlalchemy import Column, Integer, String, Text

class User(db.Model):
  id = Column(Integer, primary_key=True)
  phone_number = Column(String(200), unique=True)
  state = Column(String(100))
  last_message = Column(String(100))
  answers = Column(Text)

  def __init__(self, phone_number):
    self.phone_number = phone_number
    self.state = 'READY'
    self.last_message = None
    self.answers = None

  def get_answers_as_dict(self):
    pass

  def save_answers_from_dict(self):
    pass
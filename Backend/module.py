from Backend import app, db
from datetime import datetime

class Messages(db.Model):
    index = db.Column('index', db.Integer, primary_key=True)
    id = db.Column('id', db.Integer)
    sender = db.Column('sender', db.String(50))
    receiver = db.Column('receiver', db.String(50))
    message = db.Column('message ', db.String)
    subject = db.Column('subject  ', db.String)
    creation_date = db.Column('creation_date ', db.Date)
    reading = db.Column('reading', db.Boolean, default=False)

    def __init__(self,id , sender, receiver, message, subject, creation_date, reading):
        self.id = id
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.subject = subject
        self.creation_date = creation_date
        self.reading = reading

with app.app_context():
    db.create_all()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



######################
### Defaine the app ##
######################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///API.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


######################
### Defaine the DB ###
######################
from Backend.module import Messages
with app.app_context():
    db.create_all()

# from datetime import datetime
# one_massage = Messages(id=1, sender='lidor', receiver='test', message='Hello,World', subject='sport', reading=False)
# with app.app_context():
#     db.session.add(one_massage)
#     db.session.commit()

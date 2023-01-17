
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS


######################
### Defaine the app ##
######################

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///API.sqlite3'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)
CORS(app)

######################
### Defaine the DB ###
######################
from Backend.module import Messages
with app.app_context():
    db.create_all()

"""Import all moudle im need use in program"""
from datetime import datetime
from flask import request
from Backend.module import app, Messages, db


@app.route('/AllMessage/<id>', methods=['GET'])
def show_all_msg(id_user=-1):
    """ Show all the message from user """
    message = []
    for msg in Messages.query.filter_by(id=int(id_user)):
        message.append({"id": msg.id,
        "sender": msg.sender,
        "receiver": msg.receiver,
        "message": msg.message,
        "subject": msg.subject,
        "creation_date": msg.creation_date,
        "reading": msg.reading,
        "index": msg.index})
    return message

@app.route('/NewMessage/',methods=['POST'])
def add_new_message():
    """Create new message """
    if request.method == 'POST':
        get_json = request.json
        new_message = Messages(id=get_json['id'],
        sender=get_json['sender'],
        receiver=get_json['receiver'],
        message=get_json['message'], subject=get_json['subject'],
        creation_date=datetime.utcnow().date(),
        reading=get_json['reading'])
        db.session.add(new_message)
        db.session.commit()
        return 'Adding new message'
    return 'Please change methods to POST'


@app.route('/UnReadMessage/<id>',methods=['GET'])
def unread_message(id_user=-1):
    """Return all message unread from user"""
    unread= []
    for msg in Messages.query.filter_by(id = int(id_user),  reading = False):
        unread.append({"id":msg.id,
        "sender":msg.sender,
        "receiver":msg.receiver,
        "message":msg.message, "subject":msg.subject,
        " creation_date":msg.creation_date,
        "reading":msg.reading})
    return unread

@app.route('/OneMessage/<id>/<index>',methods=['GET'])
def return_one_message(id_user=-1, index_msg=-1):
    """ Return only one massge from user , You need choos your id and index message """
    message = []
    for msg in Messages.query.filter_by(id = int(id_user),  index = int(index_msg)):
        message.append({"id":msg.id,
        "sender":msg.sender,
        "receiver":msg.receiver,
        "message":msg.message,
        "subject":msg.subject,
        "creation_date":msg.creation_date,
        "reading":msg.reading})
    return message

@app.route('/DelMessage/<id>/<index>',methods=['DELETE', 'GET'])
def delete_message(id_user=-1, index_msg=-1):
    """Delete one message , You need choose your id and index message you eant to delete"""
    for msg in Messages.query.filter_by(id = int(id_user), index = int(index_msg)):
        db.session.delete(msg)
        db.session.commit()
    return 'The messgae is deleted'

from Backend.module import app, Messages, db
from flask import request
from datetime import datetime


@app.route('/AllMessage/<id>',methods=['GET'])
def Show_all_Msg(id=-1):
    message = []
    for msg in Messages.query.filter_by(id = int(id)):
        message.append({"id":msg.id, "sender":msg.sender, "receiver":msg.receiver, "message":msg.message, "subject":msg.subject, " creation_date":msg.creation_date, "reading":msg.reading, "index":msg.index})
    return message

@app.route('/NewMessage/',methods=['GET','POST'])
def Add_new_message():
    if request.method == 'POST':
        DATA = request.json
        New_message = Messages(id=DATA['id'], sender=DATA['sender'], receiver=DATA['receiver'], message=DATA['message'], subject=DATA['subject'], creation_date=datetime.utcnow().date(), reading=DATA['reading'])
        db.session.add(New_message)
        db.session.commit()
        return 'Adding new message'
    return 'Please change methods to POST'

@app.route('/UnReadMessage/<id>',methods=['GET'])
def UnReadMessage(id=-1):
    unread= []
    for msg in Messages.query.filter_by(id = int(id),  reading = False):
        unread.append({"id":msg.id, "sender":msg.sender, "receiver":msg.receiver, "message":msg.message, "subject":msg.subject, " creation_date":msg.creation_date, "reading":msg.reading})
    return unread

@app.route('/OneMessage/<id>/<index>',methods=['GET'])
def Return_one_message(id=-1, index=-1):
    message = []
    for msg in Messages.query.filter_by(id = int(id),  index = int(index)):
        message.append({"id":msg.id, "sender":msg.sender, "receiver":msg.receiver, "message":msg.message, "subject":msg.subject, " creation_date":msg.creation_date, "reading":msg.reading})
    return message

@app.route('/DelMessage/<id>/<index>',methods=['DELETE', 'GET'])
def Delete_message(id=-1, index=-1):
    for msg in Messages.query.filter_by(id = int(id), index = int(index)):
        db.session.delete(msg)
        db.session.commit()
    return 'The messgae is deleted'


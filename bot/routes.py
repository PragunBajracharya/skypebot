from bot import app
import os
import json
from dotenv import load_dotenv
from skpy import Skype
from flask import Flask, request, jsonify

load_dotenv()

sk = Skype(os.getenv('email'), os.getenv('password'))


@app.route("/sendMessage", methods=['GET', 'POST'])
def sendMessage():
    if request.method == 'GET':
        return {'status': 'error', 'message': 'Bad Request'}
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return {'status': 'error', 'message': 'Content-Type not supported!'}
        data = json.loads(request.data)
        if 'username' in data.keys() and 'message' in data.keys():
            username = data['username']
            message = data['message']
            try:
                ch = sk.contacts[username].chat
                ch.sendMsg(message)
                return {'status': 'success', 'message': 'Message sent successfully.'}
            except:
                return {'status': 'error', 'message': 'Message not sent.'}
        return {'status': 'error', 'message': 'Missing parameter.'}

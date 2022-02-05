# This file is using python 3.9.8

from flask_cors import CORS
from flask import Flask, request, jsonify

import os
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
CORS(app)

# Create chatbot
chatbot = ChatBot("chatbot",
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3')
# train
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('./data/train_data.txt')


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/messages/send', methods=['POST'])
def sendmessage():
    message = request.json['message']
    response_message = chatbot.get_response(message)
    print("response_message", response_message)
    return jsonify({"success": True, "response_message": str(response_message)})


if __name__ == '__main__':
    app.run(debug=True)

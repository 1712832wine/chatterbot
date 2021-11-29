import os
import chatterbot
from flask import Flask, request, jsonify

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import jsonify, make_response
import json
# text
app = Flask(__name__)

'''bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)'''
bot = ChatBot(
    "English Bot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch",
    ],
    database_uri='sqlite:///database.sqlite3'
)
trainer = ChatterBotCorpusTrainer(bot)
path = './content/english'
for file in os.listdir(path):
    file_path = './content/english/' + file
    trainer.train(file_path)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/messages/send', methods=['POST'])
def sendmessage():
    message = request.json['message']
    response_message = bot.get_response(message)
    return jsonify({"success": True,
                    "response_message": str(response_message)})


if __name__ == '__main__':
    app.run(debug=True)

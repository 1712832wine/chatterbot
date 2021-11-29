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

# The following loop will execute each time the user enters input
# incoming_msg = request.values.get('message').lower()
#     print("incoming_msg", incoming_msg)
#
#     resp_msg = resp.text
#     json_resp = {"success": true, "response_message": resp_msg}
#     return jsonify({'task': task}), 201


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/message/send', methods=['POST'])
def sendmessage():
    message = request.json['message']
    response_message = bot.get_response(message)
    print("response_message", response_message)
    # return make_response(jsonify({'success': True,
    #                               'response_message': response_message}), 200)
    # return json.dumps({'success': True,
    #                    'response_message': response_message})


if __name__ == '__main__':
    app.run(debug=True)

import os
import chatterbot
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
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

print('Type something to begin...')

# The following loop will execute each time the user enters input


@app.route('/api/message/send', methods=['POST'])
def bot():
    incoming_msg = request.values.get('message').lower()
    resp = bot.get_response(incoming_msg)
    resp_msg = resp.text
    json_resp = {"success": true, "response_message": resp_msg}
    return json.dumps(json_resp)


if __name__ == '__main__':
    app.run()

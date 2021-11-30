from flask_cors import CORS
from flask import Flask, request, jsonify

import os
import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# text
app = Flask(__name__)
CORS(app)

bot = ChatBot(
    "English Bot",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.BestMatch",
    ],
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
